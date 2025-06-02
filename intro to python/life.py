class Point:


    def __init__(self , x , y):
        self.x = x
        self.y = y

    def __leq__(self , other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def get_directions():
        return [Point(0,1), Point(0,-1), Point(1,0), Point(-1,0), Point(1,1), Point(1,-1), Point(-1,1), Point(-1,-1)]
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self , other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return 100000 * self.x + self.y

    def __add__(self , other):
        return Point(self.x + other.x , self.y + other.y)

    def get_neighbors(self):
        return {self + dir for dir in Point.get_directions()}
    


class Board:

    def __init__(self, x_size, y_size, points):
        self.alive_points = points
        self.x_size = x_size
        self.y_size = y_size

    def copy(self):
        new_board = Board(self.x_size, self.y_size, self.alive_points)
        return new_board

    def is_legal(self, point):
        return point.x < self.x_size and point.x >= 0 and point.y < self.y_size and point.y >= 0

    def number_live_neighbors(self, p):
        return sum([(pt in self.alive_points) for pt in p.get_neighbors()])

    def next_step(self):
        new_alive = set()
        for pt in self.alive_points:
            if (self.number_live_neighbors(pt) == 2):
                new_alive.add(pt)

        for x in range(self.x_size):
            for y in range(self.y_size):
                if (self.number_live_neighbors(Point(x,y)) == 3):
                    new_alive.add(Point(x,y))

        self.alive_points = new_alive
    
    def toggle_point(self, x, y):
        try:
             self.alive_points.remove(Point(x,y))
        except:
            self.alive_points.add(Point(x,y))


def load_from_file(filename):
    with open(filename , 'r') as file:
        x = int(file.readline())
        y = int(file.readline())

        alive = set()

        for line in file.readlines():
            (xi,yi) = line.split(',')
            
            xi = int(xi)
            yi = int(yi)
            alive.add(Point(xi,yi))

        return Board(x,y,alive)

def is_periodic(board):
    board_copy = board.copy()
    states = [(board.alive_points , 0)]
    min_ind = 1001
    for rep in range(1000):
        board_copy.next_step()
        if (board_copy.alive_points == board.alive_points):
            return (True, 0)

        for state in states:
            
            if (state[0] == board_copy.alive_points):
                min_ind = min(min_ind , state[1])
        
        states.append((board_copy.alive_points , rep+1))
    return (False , min_ind)

# b = Board(5, 5, {Point(2,2)})
# b.next_step()

# b = load_from_file("/users/eleves-a/2024/raul-andrei.pop/Desktop/python101/mock.txt")
# print(b.number_live_neighbors(Point(6,6)))
# print(is_periodic(b))