import random
from collections import deque

def eulerian (n , k):
    
    if (n == k+1 or k == 0): return 1
    ank = (n-k) * eulerian(n-1,k-1) + (k+1) * eulerian(n-1,k)
    return ank


def eulerian_dp (n , k, a = -1):
    if (a == -1): a = dict()
    if (n == k+1 or k == 0): a[n,k] = 1
    elif ((n,k) not in a): a[n,k] = (n-k) * eulerian_dp(n-1,k-1,a) + (k+1) * eulerian_dp(n-1,k,a)
    return a[n,k]


def count_ascents (p):
    ret = 0
    for i in range (len(p)-1):
        if (p[i] < p[i+1]): ret += 1
    
    return ret

def ascent_probabilities (n , repeats):
    ret = [0 for _ in range(n)]
    xs = [i for i in range(n)]
    
    for i in range (repeats):
        random.shuffle(xs)
        ret[count_ascents(xs)] += 1
    for i in range(n):
        ret[i] /= repeats

    return ret

# print(ascent_probabilities(7 , 10000))

def add_edge (G , n):
    i , j = -1,-1
    while (i == j or j in G[i]):
        i = random.randrange(n) 
        j = random.randrange(n)
        

    G[i].append(j)
    G[j].append(i)


def average_degree_test(n, m, trials=1000):
    degree = 0
    for _ in range(trials):
        G = random_network(n,m)
        i = random.randrange(n)
        degree += len(G[i])
    return degree/trials

def random_network (n , m):
    G = [[] for _ in range(n)]
    
    for i in range (m):
        add_edge(G , n)

    

    return G

def suggest_friends(G,u,k):
    n = len(G)
    q = deque()
    q.append(u)
    dist = [-1 for _ in range(n)]
    dist[u] = 0
    while (len(q)):
        nod = q[0]
        q.popleft()
        for to in G[nod]:
            if dist[to] == -1:
                dist[to] = dist[nod] + 1
                q.append(to)

    ret = [u for u in range(n) if dist[u] == k]
    return ret

def fdk_test(n, m, k, trials=1000):
    fdk = 0
    for _ in range(trials):
        G = random_network(n,m)
        i = random.randrange(n)
        fdk += len(suggest_friends(G,i,k))
    return fdk/trials

def next_space(m, n, grid):
    for i in range (m):
        for j in range (n):
            if (grid[i][j] == 0): return i , j

    return None

def solve_tatami (m , n):
    grid = [[0 for _ in range(n)] for _ in range(m)]
    gen = tatami_rec(m , n , grid)
    
    
    while (found:= next(gen , -1)) != -1:
        yield found

def tatami_rec (m , n , grid , crt_num= 1):

    ok = 1
    for i in range(m-1):
        for j in range (n-1):
            s = set()
            s.add(grid[i][j])
            s.add(grid[i+1][j])
            s.add(grid[i][j+1])
            s.add(grid[i+1][j+1])
            if len(s) == 4: ok = 0

    if ok == 0: return

    if next_space(m , n , grid) == None:
        yield grid
        return
    
    i , j = next_space(m , n , grid)
    if (i < m-1 and grid[i+1][j] == 0):
        grid[i][j] = crt_num
        grid[i+1][j] = crt_num
        gen = tatami_rec(m , n , grid , crt_num+1)
        while (found:= next(gen , -1)) != -1:
            yield found
        grid[i][j] = 0
        grid[i+1][j] = 0
    
    if (j < n-1 and grid[i][j+1] == 0):
        grid[i][j] = crt_num
        grid[i][j+1] = crt_num
        gen = tatami_rec(m , n , grid , crt_num+1)
        while (found:= next(gen , -1)) != -1:
            yield found
        grid[i][j] = 0
        grid[i][j+1] = 0

def print_tatami(grid):
    for row in grid:
        for n in row:
            print(f'{n:2}', end=' ')
        print()
    print()

def test_tatami(m, n):
    for grid in solve_tatami(m, n):
        
        print_tatami(grid)


# test_tatami(5 , 6)
# print([sum(1 for _ in solve_tatami(5, 2*n)) for n in range(1,10)])