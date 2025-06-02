def slice_dice(n, s, dice):
    return [dice[i * s:i * s + s] for i in range(n)]


def win_probability(D1, D2):
    win_cases = 0
    total_cases = len(D1) * len(D2)
    for d1 in D1:
        for d2 in D2:
            if (d1 > d2):
                win_cases += 1
    return win_cases / total_cases

def beats(D1, D2):
    return win_probability(D1 , D2) > 0.5


def check_list (s , dices):
    
    for i in range (len(dices)):
        if (i % s != 0 and dices[i] < dices[i-1]): return 0
    return 1

def get_dice(n, s, dice):
    # print(dice)
    if not check_list(s , dice): return
    if (len(dice) == n * s):
        dices = slice_dice(n , s , dice)
        ok = 1
        for i in range(n):
            if (not beats(dices[i] , dices[(i+1)%n])): ok = 0
        if ok:
            yield dice
        
    else:
        for new_add in range (0 , n * s):
            
            if new_add in dice: continue
            yield from get_dice(n , s , dice + [new_add])


# gen = get_dice(3, 4, [0])

# for i in range(18):
#     print(next(gen))