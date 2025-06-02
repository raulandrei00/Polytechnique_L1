import random


def is_prime (n , k=32):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    
    var = n-1
    r = 0
    while var % 2 == 0:
        r += 1
        var //= 2
    d = var

    for i in range(k):
        a = random.randint(2,n-2)
        x = pow(a,d,n)
        if x == 1 or x == n-1:
            continue
        continue_loop = 0
        for j in range(r-1):
            x = pow(x , 2 , n)
            if (x == 1):
                return False
            elif(x == n-1):
                continue_loop = 1
                break
        if (continue_loop):
            continue
        return False

    return True

def generate (x , y):
    while True:
        yield random.randint(x , y)

def random_prime (n):
    gen = generate(n , 2*n-1)
    while True:
        cand = next(gen)
        if (is_prime(cand)):
            return cand
        
