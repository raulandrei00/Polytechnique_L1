
def comb_print(n, comb):
    def occupied(i,j):
        return i<len(comb) and comb[i] == j

    print(' '*3*n + '__')
    for line in range(n):
        print(' '*(n-line-1)*3 + '__/', end='')
        for cell in range(line+1):
            i = n-1-line+cell
            j = cell
            s = '@@' if occupied(i,j) else '  '
            print(s + '\\__' + ('/' if cell<line else ''), end='')
        print()
    for line in range(n,2*n):
        print(' '*(line-n)*3 + '  \\__/', end='')
        for cell in range(2*n-1-line):
            i = cell
            j = cell+line-n+1
            s = '@@' if occupied(i,j) else '  '
            print(s + '\\__/', end='')
        print()
    print()

def invalid_offset(k, comb, j):
    return j in comb or ((j + k) in [i + comb[i] for i in range(k)])

def queen_bees(n, k, comb):
    if (len(comb) == n):
        yield comb
    for j in range (n):
        if not invalid_offset(k , comb , j):
            yield from queen_bees(n , k+1 , comb + [j])

def show_combs(n):
   for comb in queen_bees(n, 0, []):
        comb_print(n, comb)

def count_combs(n):
    cnt = 0
    for comb in queen_bees(n , 0 , []):
        cnt += 1
    return cnt

def board_print(n, black, white):
    def square(i,j):
        if (i,j) in black:
            return 'B'
        elif (i,j) in white:
            return 'W'
        return '.'

    print('+' + '-' * (2*n+1) + '+')
    for i in range(n):
        print('|', end = '')
        for j in range(n):
            print(' ' + square(i,j), end = '')
        print(' |')
    print('+' + '-' * (2*n+1) + '+')

def peaceable_queens(n, m):
    pass

def solve_peace(n, m, black,  white, bmoves, wmoves):
    pass


def attacking (queens , pos):
    for queen in queens:
        if pos[0] == queen[0] or pos[1] == queen[1] or pos[1]+pos[0] == queen[1]+queen[0] or pos[0]-pos[1] == queen[0]-queen[1]:
            return 1
    return 0    


import random

def vegas_queens(n):

    queen_list = []
    for i in range (n):
        possible_col = []
        for j in range(n):
            if not attacking(queen_list , (i , j)):
                possible_col.append(j)
        
        if (possible_col == []) :
            return vegas_queens(n)
        else:
            queen_list.append(i , possible_col[random.randint(0,len(possible_col)-1)])

    return queen_list

