
def adjMatToLst(G):
    n = len(G)
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                adj_list[i].append(j)

    return adj_list

def adjLstToMat(L):
    n = len(L)
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in L[i]:
            G[i][j] = 1

        
    return G

class queue :
    def __init__ ( self ):
        self.l = []
        self.h = 0
    def isEmpty ( self ):
        # your code here
        # must have constant complexity !
        return self.h == len(self.l)
    def push ( self , x ):
        self.l.append(x)
    def pop ( self ):
        # your code here
        # must have constant complexity !
        self.h += 1
        return self.l[self.h-1]
    def compress ( self ):
        # your code here
        # must be in place and have linear complexity !
        for i in range(len(self.l) - self.h - 1, -1 , -1):
            self.l[i] = self.l[i+self.h]
        for i in range(self.h):
            self.l.pop()
        self.h = 0

class uf :
    def __init__ ( self , n ):
        self . l = list ( range ( n ))
        self . d = [0] * n
    
    def find ( self , a ):
        # additional optimisation: path compression
        if self.l[a] != a:
            self.l[a] = self.find(self.l[a])
            return self.l[a]
        else:
            return a
    
    def union ( self , a , b ):
        a = self.find(a)
        b = self.find(b)
        if (self.l[a] <= self.l[b]): a , b = b , a

        self.d[a] += self.d[b]
        self.l[b] = a

    def toList ( self ):
        n = len ( self . l )
        t = []
        for i in range ( n ):
            t . append ([])
        for a in range ( n ):
            t [ self . find ( a )]. append ( a )
        r = []
        for i in range ( n ):
            if t [ i ] != []:
                r . append ( t [ i ])
        return r
    
