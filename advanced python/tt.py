
def fib_dp (n , mem = dict()):
    if (n == 1 or n == 2):
        return 1
    else:
        if n in mem:
            return mem[n]
        else:
            mem[n] = fib_dp(n-1) + fib_dp(n-2)
            return mem[n]
        

print(fib_dp(4))