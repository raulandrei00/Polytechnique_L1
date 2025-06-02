import random 
import typing 

def generate_walks (n):
    if (n == 0): yield []
    else:
        pref = generate_walks(n-1)
        
        for crt in pref:
            yield crt + [-1]
            yield crt + [1]

for w in generate_walks(5):
    if sum(w) == 3:
        print(w)

def generate_meanders(n,k):
    if (n == 0 and k == 0):
        yield []
    if (n == 0 or k < 0 or abs(k) > n): return
    
    up = generate_meanders(n-1,k+1)
    down = generate_meanders(n-1,k-1)

    for crt in up:
        yield crt + [-1]
    for crt in down:
        yield crt + [1]


for m in generate_meanders(5,3):
    print(m)

cache_mem = {}
def count_meanders(n,k):
    if (n == 0 and k == 0): return 1
    if (n == 0 or k < 0 or abs(k) > n): return 0
    
    if (n,k) in cache_mem: return cache_mem[(n,k)]
    cache_mem[(n,k)] = count_meanders(n-1,k+1) + count_meanders(n-1,k-1)

    return count_meanders(n-1,k+1) + count_meanders(n-1,k-1)

print(count_meanders(10,2))


class RandMeanderGen:
    def __init__(self, maxn):
        '''Initialize a random generator of meanders of length n <= maxn.'''
        self.maxn = maxn
        pass

    def random_meander(self, n, k):
        '''Assuming 0 <= n <= self.maxn, returns a uniformly random meander of length n with final height k.
        If there is no such meander, returns None.'''
        pass

def heappush (heap : list[tuple[str , int]], a : str , w : int):
    heap.append((a , w))
    crt_pos = len(heap) - 1
    while (crt_pos > 0):
        parent_pos = (crt_pos - 1) // 2
        if heap[parent_pos][1] <= w: break
        heap[crt_pos] , heap[parent_pos] = heap[parent_pos] , heap[crt_pos]
        crt_pos = parent_pos

def heappop (heap : list[tuple[str , int]]) -> tuple[str , int]:
    if len(heap) == 0: raise Exception('IndexError')
    ret = heap[0]
    last_ind = len(heap) - 1
    heap[0] = heap[last_ind]
    heap.pop()
    crt_pos = 0
    while (crt_pos < len(heap)):
        left_child = 2 * crt_pos + 1
        right_child = 2 * crt_pos + 2
        if left_child >= len(heap): break
        elif right_child >= len(heap):
            if heap[crt_pos][1] > heap[left_child][1]:
                heap[crt_pos], heap[left_child] = heap[left_child], heap[crt_pos]
            break
        elif heap[crt_pos][1] <= heap[left_child][1] and heap[crt_pos][1] <= heap[right_child][1]:
            break
        elif heap[left_child][1] < heap[right_child][1]:
            heap[crt_pos], heap[left_child] = heap[left_child], heap[crt_pos]
            crt_pos = left_child
        else:
            heap[crt_pos], heap[right_child] = heap[right_child], heap[crt_pos]
            crt_pos = right_child
