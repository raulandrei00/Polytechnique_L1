import random
import os

COLORS = ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']
CODE_LENGTH = 4

def input_color(color):
    
    return color in COLORS


def create_code ():
    arr = []
    for i in range(CODE_LENGTH):
        arr.append(random.choice(COLORS))
    return arr

def black_pins(guess , code):
    ret = 0

    for i in range(CODE_LENGTH):
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
    while i < CODE_LENGTH and j < CODE_LENGTH:
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
    while guess < CODE_LENGTH:
        print(guess, " color:")
        add = input()
        print("\n")

        status = 0
        actual = str()
        for color in COLORS:
            if color.startswith(add):
                if (status == 0):
                    status = 1
                    actual = color
                elif status == 1:
                    status = -1
                    actual = ""

        if (status < 1):
            print("Please input an unambiguous prefix of a color from the list ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']")
        else:
            guess += 1
            ret.append(actual)
    return ret

#print(input_guess())

def one_round (code):
    if len(code) != CODE_LENGTH:
        return None
    for i in range(CODE_LENGTH):
        if (not input_color(code[i])):
            return None
    
    guess = input_guess()
    black , white = score_guess(guess , code)
    print(black , " black, " , white , " white")
    if (black == CODE_LENGTH):
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

#print(input_guess())