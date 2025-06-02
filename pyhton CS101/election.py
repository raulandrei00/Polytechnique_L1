
def quote (s):
    return "'" + s + "'"

class Vote:
    def __init__(self, preference_list):
        self.preference_list = preference_list
    
    def __str__(self):
        if (len(self.preference_list) == 0):
            return 'Blank'
        else:
            return " > ".join(self.preference_list)
        
    def __repr__(self):
        return 'Vote([' + ', '.join([quote(s) for s in self.preference_list]) + "])"
    
    def first_preference(self):
        if (len(self.preference_list) == 0):
            return None
        else:
            return self.preference_list[0]
        
    def preference (self , names):
        for name in self.preference_list:
            if (name in names) :
                return name
            
        return None
        

class Election:
    """A basic election class.
    
    Data attributes:
    - parties: a list of party names
    - blank: a list of blank votes
    - piles: a dictionary with party names for keys
      and lists of votes (allocated to the parties) for values
    """
    
    def __init__(self, parties):
        self.parties = parties
        self.blank = []
        self.piles = {name: [] for name in self.parties}
        #self.count_votes = {name : 0 for name in self.parties}

    def add_vote(self , vote):
        if len(vote.preference_list) == 0:
            self.blank.append(vote)
        else:
            self.piles[vote.first_preference()].append(vote)
        #    self.count_votes[vote.first_preference()] = len(self.piles[vote.first_preference()])

    def status (self):
        count_votes = {name : 0 for name in self.parties}
        for name in self.piles:
            count_votes[name] = len(self.piles[name])
        return count_votes
    
    def add_votes_from_file (self , filename):
        with open(filename , 'r') as infile:
            for line in infile.readlines():
                
                
                    line = line.strip('\n')
                #    print( [name for name in line.split(" ") if len(name) > 1])
                    name_arr = [name for name in line.split(" ") if len(name) > 1]
                    self.add_vote(Vote(name_arr))
    

class FirstPastThePostElection(Election):
    def winner(self):
        winner = None
        votes = 0
        for name in self.parties:
            if (len (self.piles[name]) > votes):
                votes = len(self.piles[name])
                winner = name
            elif (len (self.piles[name]) == votes):
                winner = None
        return winner


class WeightedElection(Election):
    def status(self):
        weighted_votes = {name : 0 for name in self.parties}
        for name in self.piles:
            for vote in self.piles[name]:
                for i in range(min(5 , len(vote.preference_list))):
                    weighted_votes[vote.preference_list[i]] += 5-i

        return weighted_votes
    
    def winner(self):
        winner = None
        votes = -1
        self.parties.sort()
        for name in self.parties:
            if self.status()[name] > votes:
                votes = self.status()[name]
                winner = name
        return winner

class PreferentialElection(Election):
    """
    Simple preferential/instant-runoff elections.
    """

    def __init__(self, parties):
        super().__init__(parties)  # Initialize as for Elections
        self.dead = []
    def eliminate(self, party):
        self.parties.remove(party)
        for vote in self.piles[party]:
            if (vote.preference(self.parties) != None):
                self.piles[vote.preference(self.parties)].append(vote)
            else:
                self.dead.append(vote)
        del self.piles[party]

    def tie_break(self , name1 , name2):
        x1 = 0
        x2 = 0
        for vote in self.piles[name1]:
            if vote.preference_list[0] == name1:
                x1 += 1

        for vote in self.piles[name2]:
            if vote.preference_list[0] == name2:
                x2 += 1
        
        if (x1 < x2):
            return name1
        elif (x2 < x1):
            return name2
        elif (name1 < name2):
            return name1
        else:
            return name2


    def round_loser(self):
        loser = "?"
        
        for name in self.parties:
            if name in self.piles:
                loser = name
        
        votes = len(self.piles[loser])
        for name in self.piles:
            if (len(self.piles[name]) < votes):
                votes = len(self.piles[name])
                loser = name
                #print(votes , name)
            elif len(self.piles[name]) == votes:
                loser = self.tie_break(loser , name)
            
        return loser

    def winner(self):
        while len(self.piles) > 1:
            self.eliminate(self.round_loser())

        for name in self.piles:
            return name
        

# e = PreferentialElection(['BLUE', 'GREEN', 'PURPLE', 'RED', 'WHITE'])
# e.add_votes_from_file("/users/eleves-a/2024/raul-andrei.pop/Desktop/python101/votes.txt")
# print(e.status())
# print(e.round_loser())
# e.eliminate(e.round_loser())
# print(e.round_loser())
# e.eliminate(e.round_loser())
# print(e.round_loser())
# print(e.status())
# e.eliminate(e.round_loser())
# print(e.round_loser())