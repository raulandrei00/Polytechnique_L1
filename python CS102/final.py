import random
from typing import Callable, Iterable, Iterator

# Q1
def throw(n: int, p: int, g: int, ts: list[int]) -> list[list[int]]:
    bins = [[0 for _ in range(2)] for __ in range(n)]
    for i , b in enumerate(ts):
        if (i < p):
            bins[b][0] += 1
        else:
            bins[b][1] += 1
    return bins

#----------------------------------------------------------------------

# Q2
A = []
def countA(n: int, p: int) -> int:
    global A
    A = [[0 for _ in range(p+1)] for __ in range(n+1)]
    
    A[0][0] = 1;
    
    for i in range(1 , n+1):
        for j in range (0 , p+1):
            for b in range(0 , j+1):
                A[i][j] += A[i-1][j-b]
          #  print(i , j , A[i][j])
        
    
    return A[n][p]

#----------------------------------------------------------------------

def dist(sample_fn: Callable[[int,int],list[int]], n: int, p: int, samples: int = 10000) -> list[tuple[list[int], float]]:
    counts : dict[Iterable[int], float] = dict()
    for _ in range(samples):
        u = sample_fn(n,p)
        counts[tuple(u)] = counts.get(tuple(u), 0) + 1
    return [(list(u), v / samples) for (u,v) in counts.items()]

# Q3
def sample_naive(n: int, p: int) -> list[int]:
    bins = [0 for _ in range(n)]
    for _ in range(p):
        b = random.randrange(0, n)
        bins[b] += 1
    return bins

# Q4
def sample_best_of_k(n: int, p: int, k: int) -> list[int]:
    bins = [0 for _ in range(n)]
    for _ in range(p):
        selector = [i for i in range(n)]
        random.shuffle(selector)
        minn = (p+1 , 0)
        for i , b in enumerate(selector):
            if i == k: break
            if bins[b] < minn[0]: minn = (bins[b] , b)
        bins[minn[1]] += 1
    
    return bins

# Q5
def sample_uniform(n: int, p: int) -> list[int]:
    countA(n, p)
    # assigning bins from right to left
    bins = [0 for i in range(n)]
    balls_left = p
    for i in range(n-1 , -1 , -1):
        b = random.choices(range(balls_left+1) , A[i][balls_left::-1])
        
        balls_left -= b[0]
        bins[i] = b[0]
        
    return bins

#----------------------------------------------------------------------

class Bin:
    def __init__(self, label: str) -> None:
        self.label = label

class Move:
    def __init__(self, label: str, incoming: list[Bin], outgoing: list[Bin]) -> None:
        self.label = label
        self.incoming = incoming
        self.outgoing = outgoing

(A, B, C, D, E, F)    = (Bin('A'), Bin('B'), Bin('C'), Bin('D'), Bin('E'), Bin('F'))
(g, h, i, j, k, l, m) = (Move('g', [A], [B]), Move('h', [B], [C,E]), Move('i', [B], [C]),
                         Move('j', [C], [D]), Move('k', [D,E], [F]), Move('l', [E], [A,F]),
                         Move('m', [C], []))

init = {'A':1,'B':0,'C':0,'D':0,'E':0,'F':0}
goal = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':1}

# Q6




def winning(bins: list[Bin], moves: list[Move], state: dict[str, int], goal: dict[str, int], timeout: int) -> Iterator[list[str]]:
    # iterate through possible moves and yield it and generator
    # of (bin , move, modified_state, goal, timeout-1)
    
    current_state = state.copy()
    
        
    # !! base case
    if (current_state == goal): 
        yield []
        
    elif (timeout == 0): return
    
    for node in moves:
        
        # check
        if not all(current_state[frm.label] > 0 for frm in node.incoming): continue
    
        for frm in node.incoming:
            current_state[frm.label] -= 1
            
        for to in node.outgoing:
            current_state[to.label] += 1
            
        for cont in winning(bins , moves , current_state , goal , timeout-1):
            yield [node.label] + cont
        # revert state
        for frm in node.incoming:
            current_state[frm.label] += 1
            
        for to in node.outgoing:
            current_state[to.label] -= 1
    
        































