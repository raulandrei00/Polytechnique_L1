import random

COLORS = ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']

def input_color(color):
    
    return color in COLORS


def create_code ():
    arr = []
    for i in range(4):
        arr.append(random.choice(COLORS))
    return arr

def black_pins(guess , code):
    ret = 0

    for i in range(4):
        if (guess[i] == code[i]):
            ret += 1
    
    return ret

def score_guess(guess , code):
    actual_code = code.copy()
    actual_guess = guess.copy()
    black = black_pins(guess , code)
    white = 0
    i , j = 0,0
    actual_guess.sort()
    actual_code.sort()
    while i < 4 and j < 4:
        if actual_guess[i] == actual_code[j]:
            white += 1
            i += 1
            j += 1
        elif actual_guess[i] < actual_code[j]:
            i += 1
        else:
            j += 1
    white -= black
    
    return black , white

#print(score_guess(['RED', 'RED', 'RED', 'YELLOW'], ['RED', 'YELLOW', 'BROWN', 'RED']))

def input_guess():
    ret = []
    numerals = ['1st' , '2nd' , '3rd' , '4th']
    guess = 0
    while guess < 4:
        print(numerals[guess] , " color:")
        add = input()
        print("\n")
        if (add not in COLORS):
            print("Please input a color from the list ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']")
        else:
            guess += 1
            ret.append(add)
    return ret

#print(input_guess())

def one_round (code):
    if len(code) != 4:
        return None
    for i in range(4):
        if (not input_color(code[i])):
            return None
    
    guess = input_guess()
    black , white = score_guess(guess , code)
    print(black , " black, " , 1 , " white")
    if (black == 4):
        return True
    else:
        return False

def play_mastermind(code):
    
    round_number = 1
    while True:
        print("Round " , round_number)
        if one_round(code):
            break

    print("You win!")