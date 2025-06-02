
example_maze = [ [1 , 0 , 0 , 1 , 0 , 0] ,
                 [1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 0 , 1 , 0 , 1 , 1] ,
                 [1 , 1 , 1 , 1 , 1 , 0] ,
                 [1 , 0 , 0 , 1 , 0 , 0] ,
                 [1 , 0 , 1 , 1 , 1 , 1] ]

dir = [(1,0),(0,1),(-1,0),(0,-1)]

def vector_sum (p1 , p2):
    return (p1[0] + p2[0] , p1[1] + p2[1])

def escape_bt(n, M, p):

    if p[-1] == (n-1 , n-1):
        return p

    for d in dir:
        rez = vector_sum(d , p[-1])
        if rez not in p and rez[0] >= 0 and rez[0] < n and rez[1] < n and rez[1] >= 0 and M[rez[0]][rez[1]] == 1:

            path = escape_bt(n, M, p + [rez])
            if path is not None:
                return path
    return None

def escape(n , M):
    return escape_bt(n , M , [(0,0)])

print(escape(len(example_maze) , example_maze))
