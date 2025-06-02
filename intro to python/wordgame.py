
def is_in_dictionary (word , dictionary):
    return word in dictionary

def read_dictionary (filename):
    with open (filename , 'r') as file:
        
        ret = file.read()
      #  print(type(ret))
        ret = ret.split(' ')

        dic = []
        
        for x in ret:
            x = x.split('\n')
            for y in x:
                if y != '':
                    dic.append(y)
                
        
        
    return dic



def is_constructable (target , source):
    ok = True
    for let in target:
        if source.count(let) < target.count(let):
            ok = False
    return ok

def one_round(mainword, found, dictionary):
    print (f"Please construct a new word from the letters of the word {mainword}:")
    resp = input()
    if (resp == '!'):
        return -1
    elif (resp == mainword):
        print("Let's try something more interesting!")
        return 0
    elif (not resp in dictionary):
        print("I do not know this word!")
        return 0
    elif (resp in found):
        print("You have already found this word!")
        return 0
    elif (not is_constructable(resp , mainword)):
        print("Not enough letters!")
        return 0
    else:
        found.append(resp)
        print(f"Good job, you have earned {len(resp)} points")
        return len(resp)

def play_game(mainword, dictionary):
    found = []
    s = one_round(mainword, found, dictionary)
    sum = 0
    while (s != -1):
        sum += s
        s = one_round(mainword, found, dictionary)
    print_words = ''

    for word in found:
        print_words += word + ','

    print_words = print_words[:len(print_words)-1:]

    print (f"You have constructed: {print_words}\nTotal score: {sum}")
    

def superplayer(mainword, dictionary):
    word_list = []
    score = 0
    
    for word in dictionary:
        if (is_constructable(word , mainword)):
            score += len(word)
            word_list.append(word)
    return (word_list , score)
    

def cringe (let):
    if let == 'q':
        return 'Q'
    if let == 'w':
        return 'W'
    if let == 'e':
        return 'E'
    if let == 'r':
        return 'R'
    if let == 't':
        return 'T'
    if let == 'y':
        return 'Y'
    if let == 'u':
        return 'U'
    if let == 'i':
        return 'I'
    if let == 'o':
        return 'O'
    if let == 'p':
        return 'P'
    if let == 'a':
        return 'A'
    if let == 's':
        return 'S'
    if let == 'd':
        return 'D'
    if let == 'f':
        return 'F'
    if let == 'g':
        return 'G'
    if let == 'h':
        return 'H'
    if let == 'j':
        return 'J'
    if let == 'k':
        return 'K'
    if let == 'l':
        return 'L'
    if let == 'z':
        return 'Z'
    if let == 'x':
        return 'X'
    if let == 'c':
        return 'C'
    if let == 'v':
        return 'V'
    if let == 'b':
        return 'B'
    if let == 'n':
        return 'N'
    if let == 'm':
        return 'M'


def is_constructable2(target, source):
    need = dict()
    if (not is_constructable(target , source)):
        return None
    else:
        for let in target:
            need[let] = 0
        for let in source:
            need[let] = 0
        for let in target:
            need[let] = need[let] + 1
        ret = str()
        for let in source:
            if need[let] > 0:
                ret += cringe(let)
                need[let] = need[let] - 1
            else:
                ret += let
        return ret