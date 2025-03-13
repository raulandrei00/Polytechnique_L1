
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

q = queue ()
for i in range (6):
    q . push ( i )
for i in range (5):
    print ( q . pop () , end = " " )
print ()
print ( q .l , q . h )
l = q . l
q . compress ()
print (l , q . h )