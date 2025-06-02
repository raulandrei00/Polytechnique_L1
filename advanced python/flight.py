example_flight = [0,1,1,-1]
example_fruits = [{}, {-1,0},{-1,1,2},{-3,2},{-2,1,4}]


def flights_list(n):
    if n == 0:
       return [[]]
    return [[i] + w for w in flights_list(n-1) for i in [-1,0,1]]

def flights_gen(n):
    if n == 0:
       return ([])
    return ([i] + w for w in flights_list(n-1) for i in [-1,0,1])

def flight_value(fruits, flight):
    ret = 0
    x , y = 0,0
    if 0 in fruits[0]:
        ret += 1
    for move in flight:
        x += 1
        y += move
        if y in fruits[x]:
            ret += 1
    return ret

def optimal_brute(fruits):
    maxx = 0
    for flight in flights_gen(len(fruits)-1):
        maxx = max(maxx , flight_value(fruits , flight))

    return maxx

def optimal_rec(fruits, x=0, y=0):
    if x == len(fruits)-1:
        return int(y in fruits[x])
    else:
        v = 0
        for d in [-1 , 0 , 1]:
            v = max(v , optimal_rec(fruits , x+1 , y+d))
        v += int(y in fruits[x])
        return v
    
from functools import cache

def optimal_td (fruits , x=0 , y=0, memo=None):
    if memo is None:
        memo = {}
    elif (x,y) in memo:
        return memo[x,y]

    if x == len(fruits)-1:
        return int(y in fruits[x])
    else:
        v = 0
        for d in [-1 , 0 , 1]:
            v = max(v , optimal_td(fruits , x+1 , y+d, memo))
        v += int(y in fruits[x])
        memo[x,y] = v
        return v
    
def optimal_bu(fruits):
    dp = {}
    for i in range(len(fruits)-1 , -1 , -1):
        
        new_dp = {}
        for j in range(-i , i+1):
            new_dp[j] = 0
            for d in [-1 , 0 , 1]:
                if j+d in dp:
                    new_dp[j] = max(new_dp[j] , dp[j+d])
            new_dp[j] += int(j in fruits[i])
        dp = new_dp
    return dp[0]


def optimal_path(fruits):
    dp = {}
    for i in range(len(fruits)-1 , -1 , -1):
        
        
        for j in range(-i , i+1):
            dp[i , j] = 0,0
            for d in [-1 , 0 , 1]:
                if (i+1 , j+d) in dp:
                    dp[i , j] = max(dp[i , j] , (dp[i+1 , j+d][0] , d))
            dp[i , j] = dp[i,j][0] + int(j in fruits[i]) , dp[i,j][1]
    
    i , j = 0,0
    ret = []
    while i < len(fruits)-1:
        ret.append(dp[i,j][1])
        j += dp[i,j][1]
        i += 1

    return ret
    
def optimal_paths(fruits):
    dp = {}
    go = {}
    for i in range(len(fruits)-1 , -1 , -1):
        
        for j in range(-i , i+1):
            dp[i , j] = 0
            go[i,j] = []
            for d in [-1 , 0 , 1]:
                if (i+1 , j+d) in dp:
                    dp[i , j] = max(dp[i , j] , dp[i+1 , j+d])

            for d in [-1 , 0 , 1]:
                if (i+1 , j+d) in dp and (dp[i+1 , j+d] == dp[i,j]):
                    go[i,j].append(d)
            dp[i , j] = dp[i,j] + int(j in fruits[i])
    
    choice = [0] * (len(fruits)-1)
    while True:
        ret = []
        j = 0
        for i in range(len(fruits)-1):
            ret.append(go[i,j])

# print(optimal_path(example_fruits))