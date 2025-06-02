
def repeat (x):
    while True:
        yield x

def cross (n , x , g):
    cnt = 1
    while cnt:
        if cnt % n == 0:
            next(g)
            yield x
        else:
            yield next(g)
        cnt += 1

def sieve ():
    yield False
    ciur = repeat (True)
    n = 1
    while True:
        n += 1
        crt = next(ciur)
        if (crt == True):
            ciur = cross (n , False , ciur)
        yield crt

def prime_pi(n):
    primes = sieve()
    pi = 0
    for i in range (1 , n+1):
        if (next(primes) == True):
            pi += 1

    return pi