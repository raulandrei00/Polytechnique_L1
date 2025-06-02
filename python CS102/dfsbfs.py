def revert_edges (AG):
    rev_adj_list = {nod : [] for nod in AG}
    for nod in AG:
        for to in AG[nod]:
            rev_adj_list[to].append(nod)
    return rev_adj_list


def required_list(G, c):
    visited = []
    stiva = [c]
    rasp = []
    while (len(stiva)):
        nod = stiva[-1]
        rasp.append(nod)
        stiva.pop()
        for to in G[nod]:
            if to in visited: continue
            stiva.append(to)
            visited.append(to)

    return rasp


def required(G, c):
    return len(required_list(G , c))

def needed_for (G , c):
    radj = revert_edges(G)
    return len(required_list(radj , c))

def dfs (G , start , viz):
    stiva = [start]
    while (len(stiva)):
        nod = stiva[-1]
        viz.append(nod)
        for to in G[nod]:
            if to not in viz:
                stiva.append(to)


def cyclic_dependence(G):
    pass

from collections import deque
from math import inf as INF


def vector_sum (v1 , v2):
    return (v1[0] + v2[0] , v1[1] + v2[1])


def shortest_escape(maze, start, finish):
    
    dist = {start : 0}
    directions = [(1 , 0) , (0 , 1) , (0 , -1) , (-1 , 0)]
    
    q = deque()
    q.append(start)
    while (len(q)):
        nod = q[0]
        q.popleft()
        for dir in directions:
            to = vector_sum(nod , dir)
            if (to[0] >= len(maze) or to[0] < 0 or to[1] < 0 or to[1] >= len(maze[0]) or maze[to[0]][to[1]] == 0): continue
            if to not in dist:
                dist[to] = dist[nod]+1
                q.append(to)

    def next_node (nod):
        for dir in directions:
            to = vector_sum(nod , dir)
            if (to in dist and dist[to] < dist[nod]): return to

    if (finish not in dist): return None
    else:
        nod = finish
        ret = [finish]
        while nod != start:
            nod = next_node(nod)
            ret.append(nod)
        ret.reverse()
        return ret
    

def shortest_escape_len(maze, start, finish):
    ret = shortest_escape(maze , start , finish)
    if ret is None: return INF
    else: return len(ret) - 1

