import math
from copy import copy

def gcd (x , y):
    if (x == 0 or y == 0):
        return max(x , y)
    else:
        return gcd(max(x , y) % min(x , y) , min(x , y))
    
def is_palindrome (s):
    if (len(s) == 0):
        return True
    return s[0] == s[len(s)-1] and is_palindrome(s[1:len(s)-1])



def rec_pow (a , b):
    
    """Compute a**b recursively"""
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return rec_pow(a , b/2) ** 2
    else:
        return a * rec_pow(a , (b-1)/2) ** 2
    # your code here

def binary_search(sorted_list, lower, upper, element):
    mid = math.floor((lower + upper) / 2)
    
    if (sorted_list[mid] == element):
        return mid
    elif (mid == lower): 
        return -1
    elif sorted_list[mid] < element:
        return binary_search(sorted_list , mid , upper , element)
    else:
        return binary_search(sorted_list , lower , mid , element)
    
def find_subsets(s):
    """Return a list of all the sub sets of set `s`
    (in any order)
    """
    if len(s) == 0:
        return [set()]
    # to use `copy` function, add `from copy import copy` at the beginning of your file
    s_copy = copy(s)
    elem = s_copy.pop()
    result = find_subsets(s_copy)
    ret = copy(result)
    for subset in result:
        sbs = copy(subset)
        sbs.add(elem)
        ret.append(sbs)

   # print(ret)
    return ret
    
# s = ['b', 'c', 'd', 'f', 'g', 'h']
# print( binary_search(['b', 'c', 'd', 'f', 'g', 'h'], 0, 6, 'd') )

# print (find_subsets({4, 5, 6}))

def find_permutations(arr):
    if (len(arr) == 0):
        return [[]]
    prev = find_permutations(arr[0:len(arr)-1])
    # print(prev)
    # print(arr)
    ret = []
    for ar in prev:
        for pos in range(len(ar)+1):
            new_perm = copy(ar)
            new_perm.insert(pos , arr[len(ar)])
            ret.append(new_perm)

    return ret

def load_dictionary(filename):
    with open(filename, 'r') as f:
        words = [line.strip() for line in f]
        return words
    
def find_acronyms(phrase, word_list):
    """Find each word in word_list that can be constructed
    by taking one letter from each word in phrase, in order.
    """
    return find_acronyms_rec(phrase.split(), '', word_list)

def find_acronyms_rec(phrase_words, prefix, word_list):

    ret = set()
    if len(phrase_words) == 0:
      #  print(prefix)
        if (prefix in word_list):
            ret.add(prefix)
    else:
            
        for ch in phrase_words[0]:
            ret = ret.union(find_acronyms_rec(phrase_words[1::] , prefix + ch , word_list))

    return ret

# words = load_dictionary("/users/eleves-a/2024/raul-andrei.pop/Desktop/python101/wordlist.txt")
# print( find_acronyms('how are you', words) )
