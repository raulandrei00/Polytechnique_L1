import random 

def streak (n , k):
    streak = 0
    found = 0
    for i in range(n):
        # Do three coin tosses, and count the number of
        # times it lands "Heads".
        # Here, we use True for "Heads" and False for "Tails"
        if random.choice([True, False]):
            streak += 1
        else:
            streak = 0
        if (streak == k):
            
            found = 1
    return found

def experiment (n , k):
    target_outcome = 0
    for i in range(int(1e5)):
        target_outcome += int(streak(n,k))

    return target_outcome / 1e5


# print(experiment(100 , 5)) #0.81135
# for (100 , 30) the chance is 0 (there is almost no chance of 30 consecutive heads)



def generate_coinflip () :
    while True:
        if (random.choice([True , False])):
            yield 'h'
        else:
            yield 't'


def exp_2 () : 
    p1 = ['h','h','t'] 
    p2 = ['t','h','h']

    coinflip = generate_coinflip()

    coin_stack = []

    while True :
        coin_stack.append(next(coinflip))
        if (coin_stack[-3::] == p1):
            return 1
        elif coin_stack[-3::] == p2:
            return 0
        

    

def penney ():
    first_wins = 0
    for i in range (int(1e5)):
        first_wins += exp_2()
    return first_wins / 1e5

# print(penney())
#it looks like 1st player's chjance to win is about 25%


def roll (D):
    seed = random.uniform(0,1)
    sum = 0
    side = 0
    while (sum < seed):
        sum += D[side]
        side += 1
    return side

def rolls (D , N):
    ret = [0] * len(D)
    for i in range(N):
        ret[roll(D)-1] += 1
    return ret

import matplotlib.pyplot as plt

def plot(ns):
    N  = sum(ns)
    ns = [float(x) / N for x in ns]
    plt.bar(range(len(ns)), height=ns)
    plt.xticks(range(len(ns)), [str(i+1) for i in range(len(ns))])
    plt.ylabel('Probability')
    plt.title('Biased die sampling')
    plt.show()
