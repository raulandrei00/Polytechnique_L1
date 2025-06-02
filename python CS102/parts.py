
import sys
from functools import cache

def parts_lex (n):
    
    def find_index (arr):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != 1:
                return i
        return -1
    
    crt = [n]

    if n == 0:
        yield []
        return

    yield crt.copy()
    while True:
        i = find_index(crt)
        if i == -1:
            break
        else:
            crt = crt[:i] + ((n - sum(crt[:i])) // (crt[i]-1)) * [crt[i] - 1] + [(n - sum(crt[:i])) % (crt[i]-1)]
            if crt[-1] == 0:
                crt = crt[:-1]
            yield crt.copy()

@cache
def parts_cnt(n , k=None):
    
    if k is None:
        sum = 0
        for k in range(n+1):
            sum += parts_cnt(n, k)
        return sum
    if (n == 0) and (k == 0):
        return 1
    elif k == 0: return 0
    elif k > n: return 0
    else: return parts_cnt(n-1 , k-1) + parts_cnt(n-k, k)

def parts_rec(n, k=None):

    gen = parts_lex(n)

    while (exists := next(gen, None)) is not None:
        if k is None:
            yield exists
        elif len(exists) == k:
            yield exists


import random

class RandPartsGen:

    

    def rand_gen(self , n):
        '''Random generator of partitions of integers n <= maxn.'''
        while True:
            ret = []
            if self.k is None: self.k = random.choices(range(1 , n+1) , [parts_cnt(n , k) / parts_cnt(n) for k in range(1 , n+1)])[0]
                
            if n == 0:
                yield ret
            while (len(ret) < self.k):
                path = random.choices([1 , 2] , [parts_cnt(n-1 , self.k-1) / parts_cnt(n , self.k) , 1-parts_cnt(n-1 , self.k-1) / parts_cnt(n , self.k)])
                if path[0] == 2:
                    ret = [x + 1 for x in next(self.generators[n-self.k])]
                else:
                    self.k -= 1
                    ret = next(self.generators[n-1]) + [1]
                    self.k += 1

            ret.sort(reverse=True)
            yield ret


    def __init__(self, maxn):
        '''Initialize a random generator of partitions of integers n <= maxn.'''
        self.generators = [self.rand_gen(n) for n in range(maxn+1)]
        self.k = None

    def randpart(self, n, k=None):
        '''Assuming 0 <= n <= self.maxn, returns a uniformly random partition of n with k parts.
        If there is no such partition, returns None.'''
        if k is not None and k > n:
            return None 
        self.k = k
        return next(self.generators[n])
        
rx = RandPartsGen(1000)
for i in range(10):
    print(rx.randpart(10))