
import random


class Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self , suit , rank):
        self.suit = suit
        self.rank = rank
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def __gt__(self , other):
        if (self.rank > other.rank):
            return 1
        elif (self.rank == other.rank and self.suit > other.suit): 
            return 1
        else:
            return 0

class Deck:
    def __init__(self, minrank):
        self.cards = []
        
        for suit in range(len(Card.suit_names)):
            for rk in range(minrank , len(Card.rank_names)):
                self.cards.append(Card(suit, rk))
    def __str__(self):
        return ', '.join([str(i) for i in self.cards])

    def pop(self):
        ret = self.cards[-1]
        del self.cards[-1]
        return ret

    def add_card (self , card):
        self.cards.insert(0, card)

    def len(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Deck(len(Card.rank_names))
    
    def __str__(self):
        ret = f"Player {self.name} has"
        if (len(self.hand.cards) == 0):
            ret += " no cards"
        else:
            ret += f": {str(self.hand)}"
        return ret

    def add_card (self , card):
        self.hand.add_card(card)
    
    def num_cards(self):
        return self.hand.len()

    def remove_card(self):
        ret = self.hand.cards[-1]
        del self.hand.cards[-1]
        return ret
'''
p = Player(" lu octav")
print(p)

p.hand = Deck(11)
print(p)'''

class CardGame:
    def __init__(self, player_arr, minrank):
        self.deck = Deck(minrank)
        self.players = []
        for name in player_arr:
            self.players.append(Player(name))
        self.num_cards = self.deck.len()

    def __str__(self):
        ret = '\n'.join([str(i) for i in self.players])

        return ret

    def burn_cards(self , cards):
        for card in cards:
            try:
                self.deck.cards.remove(card)
            except:
                pass
        self.num_cards = self.deck.len()

    def shuffle_deck(self):
        self.deck.shuffle()

    def deal_cards(self):
        for i in range(self.num_cards):
            self.players[i%len(self.players)].add_card(self.deck.cards[-1])
            del self.deck.cards[-1]

    def simple_turn(self):
        card_list = []
        highest = Card(0,0)
        winner = self.players[0]
        for player in self.players:
            try:
                crt_card = player.remove_card()
                print(f"Player {player.name}: {crt_card}")
                card_list.append(crt_card)
                if (crt_card > highest):
                    winner = player
                    highest = crt_card
            except:
                pass

        return (winner.name , card_list)

    def play_simple(self):
        while (len(self.players) > 1):
            for player in self.players:
                if player.hand.len() == 0:
                    self.players.remove(player)
            (winner_name , card_list) = self.simple_turn()
            random.shuffle(card_list)
            for player in self.players:
                if player.name == winner_name:
                    for card in card_list:
                        player.add_card(card)
        return self.players[0].name
            
        
#g = CardGame(['Grace', 'Emmy', 'Sofia'], 11)
#print(g)
