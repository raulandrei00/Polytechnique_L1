
import random

dir = [(1,0),(0,1),(0,-1),(-1,0)]

def vect(pos , add):
    return (pos[0] + add[0] , pos[1] + add[1])

def print_coord(x , y):
    return f"({x},{y})"

class Player:
    """
    Encapsulates players and their properties
    
    Data Attributes:
    name         -- the name of the player
    position     -- the current position of the player on the board
    role         -- the role of the player, detective or criminal
    coins        -- number of coins for tickets
    """

    def __init__(self, name, posx, posy, role, coins):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.position = (posx,posy)
        self.coins = coins
        self.role = role
        

    def __str__(self):
        return f"Player {self.name} is a {self.role} in position {print_coord(self.position[0] , self.position[1])} with {self.coins} coins"

    def bus_move(self, nextx, nexty):
        return abs(nextx - self.position[0]) + abs(nexty - self.position[1]) == 1


    def can_move(self, nextx, nexty):
        return self.bus_move(nextx,nexty) and self.coins > 0 or self.coins > 1


    def move(self, nextx, nexty):
        if (self.bus_move(nextx , nexty)):
            self.coins -= 1
            if (self.role != "criminal"):
                print(f"Player {self.name} took the bus to position {print_coord(nextx,nexty)}")
            else:
                print(f"Player {self.name} took the bus to a secret position")
        else:
            self.coins -= 2
            if (self.role != "criminal"):
                print(f"Player {self.name} took the metro to position {print_coord(nextx,nexty)}")
            else:
                print(f"Player {self.name} took the metro to a secret position")
        
        self.posx = nextx
        self.posy = nexty
        self.position = (nextx , nexty)
        



class MetroStation:
    """
    Data Attributes:
    position -- own position of the station
    next_stations -- a set of coordinates for the subsequent stations on the line
    """

    def __init__(self, x, y):
        self.position = (x,y)
        self.next_stations = set()

    def __str__(self):
        if (len(self.next_stations) != 0):
            return f"Metro station at position {self.position} with next stations {self.next_stations}"
        else:
            return f"Metro station at position {self.position} with next stations {{}}"

    def add_next_station(self, position):
        self.next_stations.add(position)



class Board:
    """
    A gameboard for our version of Scotland Yard
    
    Data Attributes:
    xsize          -- the number of squares in x direction
    ysize          -- the number of squares in y direction
    metro_stations -- a dictionary with the metro stations on the board
    gameboard      -- a two-dimensional list as the map of the board
    """
 
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.metro_stations = dict()
        self.create_gameboard()

    def inside (self , pos):
        return pos[0] > 0 and pos[0] <= self.xsize and pos[1] > 0 and pos[1] <= self.ysize

    def __str__(self):
        outstr = f'Board of size {self.xsize}x{self.ysize}'
        for p,m in self.metro_stations.items():
            outstr += '\n'
            outstr += f'{m}'
        return outstr

    def create_gameboard(self):
        """
    Method to represent the board in its current state
    """
        self.gameboard = [['-'] * (self.ysize+1) for i in range(self.xsize+1)]
        for j in range(len(self.gameboard[0])):
            self.gameboard[0][j] = ""
        for i in range(len(self.gameboard)):
            self.gameboard[i][0] = ""

    def draw_board(self):
        """
        Method to draw the board in the console
        """
        outstr = f'Board of size {self.xsize}x{self.ysize}'
        for i in range(len(self.gameboard)):
            outstr+="\n"
            for j in range(len(self.gameboard[i])):
                outstr+=(self.gameboard[i][j])
        print(outstr)
    
    def has_metro_station(self, pos):
        return pos in self.metro_stations
            

    def create_metro_station(self, x, y):
        """Set metro station at (x,y) and return the metro station object"""
        self.gameboard[x][y] = 'M'
        self.metro_stations[(x,y)] = MetroStation(x,y)
        return MetroStation(x,y)


    def get_distance(self, pos1, pos2):
        return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2


    def is_free(self, pos):
        """
        This method uses the board_game in order to check if a square is already occupied by a detective
        """
        x = pos[0]
        y = pos[1]
        return (self.gameboard[x][y]!='P')

    def clean_position(self, pos):
        """
        Remove player symbol P from board and redraw M or -
        """
        x = pos[0]
        y = pos[1]
        if(self.has_metro_station(pos)):
           self.gameboard[x][y]='M'
        else:
           self.gameboard[x][y]='-'


    def draw_player(self, player):
        """
        Gets a player object and draws it on the gamebord
        """
        x = player.position[0]
        y = player.position[1]
        if(player.role == "detective"):
            self.gameboard[x][y]='P'
        if(player.role == "criminal"):
            self.gameboard[x][y]='X'


    def add_metro_lines(self,pos):
        """
        Creates the connections between metro stations.
        Calculate the 2 nearest neighboring metro stations on the board
        and add them to next_stations.
        The input argument is the position of the current metro station which has been created before
        using create_metro_station.
        """
        mpos = list(self.metro_stations.keys())
        mpos.remove(pos)
        """The following sort function sorts the metro stations by distance from the current one"""
        mpos.sort(key = lambda x : self.get_distance(x, pos))
        if(len(mpos)>0):
            self.metro_stations[pos].add_next_station(mpos[0])
        if(len(mpos)>1):
            self.metro_stations[pos].add_next_station(mpos[1])


    def get_rand_pos (self):
        ret = (random.randint(1,self.xsize) , random.randint(1,self.ysize))
        while not self.is_free(ret):
            ret = (random.randint(1,self.xsize) , random.randint(1,self.ysize))
        return ret

    def get_next_pos(self, player_pos):
        """
        Get next position a player can move to.
        Use the method is_free() to check if the possible next position is still free
        """
        ret = [vect(player_pos , d) for d in dir if self.inside( vect(player_pos,d) ) and self.is_free(vect(player_pos,d))]
        if player_pos in self.metro_stations:
            for station_pos in self.metro_stations[player_pos].next_stations:
                ret.append(station_pos)
        return ret





class Game:
    """
    A game of Scotland Yard.

    Data Attributes:
    board      -- the board of the game
    players    -- a list of Player objects with the last one playing Mr. X
    turn       -- the number of the current turn
    last_x_pos -- the position the criminal has been seen last 
    """ 
    
    def __init__(self, board, player_names):
        self.turn = 0
        self.board = board
        self.players = []
        
        for i in range (len(player_names)):
            if (i != len(player_names)-1):
                pos = board.get_rand_pos()
                self.players.append(Player(player_names[i] , pos[0] , pos[1] , 'detective' , 2*(board.xsize+board.ysize)//len(player_names)))
            else:
                pos = board.get_rand_pos()
                self.last_x_pos = pos
                self.players.append(Player(player_names[i] , pos[0] , pos[1] , 'criminal' , 2*(board.xsize+board.ysize)//len(player_names)))
            
    def print_game_state(self):
        """Print state of game after every turn."""
        print('-------------game state-------------')
        for player in self.players:
            print(player)
        print('-------------game state-------------\n')

    

    def change_turn(self):
        self.turn += 1
        if (self.turn % 5 == 0):
            self.board.clean_position(last_x_pos)
            last_x_pos = ( self.players[len(self.players)-1].position[0] , self.players[len(self.players)-1].position[1] )
            self.board.draw_player(self.players[len(self.players)-1])


    def move_player(self, curr_player):
        player_pos = (curr_player.position[0] , curr_player.position[1])
        possible = self.board.get_next_pos(player_pos)
        if (curr_player.coins == 1):
            possible = [pos for pos in possible if curr_player.bus_move(pos[0] . pos[1])]
        elif curr_player.coins == 0:
            possible = []

        if (len(possible) == 0):
            return player_pos
        elif curr_player.role == 'criminal':
            ret_pos = random.choice(possible)
            curr_player.move(ret_pos[0] , ret_pos[1])
            return ret_pos
        else:
            ret_pos = possible[0]
            for pos in possible:
                if (self.board.get_distance(pos , self.last_x_pos) < self.board.get_distance(ret_pos , self.last_x_pos)):
                    ret_pos = pos

            self.board.clean_position(player_pos)
            curr_player.move(ret_pos[0] , ret_pos[1])
            self.board.draw_player(curr_player)

            return ret_pos


    def play(self):
        can_move = 1
        while (can_move):
            can_move = 0
            self.board.draw_board()
            self.change_turn()
            for player in self.players:
                old_pos = player.position
                move_player(player)
                if old_pos != player.position:
                    can_move = 1
            for i in range(len(self.players)-1):
                if self.players[i].position == self.players[len(self.players)-1].position:
                    return 1
        return 0


def load_from_file(filename):
    with open (filename , 'r') as in_file:
        board_size = in_file.readline().split(' ')
        player_names = [name.split('\n')[0] for name in in_file.readline().split(' ')]
        stations = in_file.readlines()

        board = Board(int(board_size[0]) , int(board_size[1]))
        for coord in stations:
            actual = coord.split(',')
            board.create_metro_station(int(actual[0]) , int(actual[1]))

        for coord in stations:
            actual = coord.split(',')
            board.add_metro_lines((int(actual[0]) , int(actual[1])))

        
        game = Game(board , player_names)
        return game
