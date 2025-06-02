
import random


class Ship:
    """A ship that can be placed on the grid."""

    def __repr__(self):
        return f"Ship('{self.name}', {self.positions})"

    def __str__(self):
        return f'{repr(self)} with hits {self.hits}'

    def __init__(self, name, positions):
        self.name = name
        self.positions = positions
        self.hits = set()

    def __eq__(self , other):
        return self.name == other.name and self.positions == other.positions and self.hits == other.hits
    def is_afloat (self):
        return len(self.hits) < len(self.positions)

    def take_shot(self , shot):
        if (shot in self.positions and shot in self.hits or shot not in self.positions):
            return 'MISS'
        elif (shot in self.positions):
            self.hits.add(shot)
            if (len(self.hits) == len(self.positions)):
                return 'DESTROYED'
            else:
                return 'HIT'
ship_types = [('Battleship',4),('Carrier',5),('Cruiser',3),('Destroyer',2),('Submarine',3)]

class Grid:
    """Encodes the grid on which the Ships are placed.
    Also remembers the shots fired that missed all of the Ships.
    """
    
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.ships = list()
        self.misses = set()

    def add_ship(self, ship):
        for _ship in self.ships:
            if len(ship.positions.intersection(_ship.positions)) > 0:
                return
        self.ships.append(ship)

    def shoot (self , shot):
        for ship in self.ships:
            outcome = ship.take_shot(shot)
            if outcome == 'HIT':
                return ('HIT' , None)
            elif outcome == 'DESTROYED':
                return ("DESTROYED" , ship)
        self.misses.add (shot)
        return ('MISS' , None)

    def random_ship(self):
        if (random.randint(0,1)):
            (name , sz) = ship_types[random.randint(0,4)]
            posUp = (random.randint(1,self.x_size-1) , random.randint(1,(self.y_size-sz-1)))
            poslist = set()
            for i in range(sz):
                poslist.add((posUp[0] , posUp[1]+i))
        else:
            (name , sz) = ship_types[random.randint(0,4)]
            posUp = (random.randint(1,self.x_size-sz-1) , random.randint(1,self.y_size-1))
            poslist = set()
            for i in range(sz):
                poslist.add((posUp[0]+i , posUp[1]))

        return Ship(name , poslist)

    def create_random(self , n):
        while(len(self.ships) < n):
            self.add_ship(self.random_ship())
            
    

def create_ship_from_line(line):
    line = line.split(" ")
    return Ship (line[0] , { (int(i.split(':')[0]) , int(i.split(':')[1])) for i in line[1:]})


def load_grid_from_file(filename):
    with open (filename) as infile:
        lines = infile.readlines()
        
        returnGrid = Grid(int(lines[0].split(":")[0]) , int(lines[0].split(":")[1]))
        for line in lines[1:]:
            returnGrid.add_ship(create_ship_from_line(line))

        return returnGrid

class BlindGrid:

    def __init__(self , grid):
        self.x_size = grid.x_size
        self.y_size = grid.y_size
        self.misses = grid.misses
        self.hits = set()
        self.sunken_ships = []
        for ship in grid.ships:
            if (not ship.is_afloat()):
                self.sunken_ships.append(ship)
            for hit in ship.hits:
                self.hits.add(hit)
        

#print(load_grid_from_file('/users/eleves-a/2024/raul-andrei.pop/Desktop/python101/grid.txt').y_size)