def read_positive_integer(text, position):
    if not position < len(text) or not text[position].isdigit():
        return ("" , position)
    else:
        ret = read_positive_integer(text , position+1)
        
        return (str(text[position]) + ret[0] , ret[1])


# def check_par (exp , left , right):
#     while exp[left] != '(':
#         if exp[left] == ')':
#             return (False , left)
#         if left == right:
#             return (True , len(exp))
#         left += 1
#     while exp[right] != ')':
#         if exp[right] == '(':
#             return (False , right)
#         right -= 1

#     return check_par(exp , left+1 , right-1)

def is_balanced(expression, position):
    
    # print(expression , position)

    if position >= len(expression):
        return (True , position)
    elif expression[position] == '(':
        balance = 1
        close = -1
        for i in range (position+1 , len(expression)):
            if expression[i] == '(':
                balance += 1
            elif expression[i] == ')':
                balance -= 1
            if balance == 0:
                close = i
                break
        if close == -1:
            return (False , position)
        else:
            ret = is_balanced(expression[position+1:close] , 0)
            if ret[0] == True:
                return is_balanced(expression , close+1)
            else:
                return ret
    elif expression[position] == ')':
        return (False , position)
    else:
        return is_balanced(expression , position+1)

# print(is_balanced("()",0) , is_balanced("((abc)(eee))(123))",0) , is_balanced("abc)",0))

opening = ['(', '[', '{', '<' ]
closing = [')', ']', '}', '>' ]



def is_totally_balanced(expression, position, balance = []):
    if position >= len(expression):
        return (balance == [] , position)
    
    for ch in opening:
        if expression[position] == ch:
            balance.append(ch)
    
    for i , ch in enumerate(closing):
        if expression[position] == ch:
            if len(balance) > 0 and balance[-1] == opening[i]:
                balance.pop()
            else:
                return (False , position)
            
    

    return is_totally_balanced(expression , position+1 , balance)

# print(is_totally_balanced('({((()))[]<>}', 0))

def evaluate (expression , position):
    t1 , t2 = -1 , -1
    # print("rec")
    if expression[position] == '(':
        t1 , position = evaluate(expression , position+1)
    else:
        t1 , position = read_positive_integer(expression , position)
        if t1 == '':
            return (-1 , None)
        else:
            t1 = int(t1)


    # print(t1 , position)

    if position == None:
        return (-1 , None)
    if (position >= len(expression) or expression[position] == ')'):
        return (t1 , position)
    oper = expression[position]

    position += 1

    if expression[position] == '(':
        t2 , position = evaluate(expression , position+1)
    else:
        t2 , position = read_positive_integer(expression , position)
        if t2 == '':
            return (-1 , None)
        else:
            t2 = int(t2)
    if position == None:
        return (-1 , None)
    
    # print(" " , t2 , position)

    if oper == '+':
        return (t1+t2 , position+1)
    elif oper == '-':
        return (t1-t2 , position+1)
    elif oper == '*':
        return (t1*t2 , position+1)
    else:
        return (-1 , None)
    

def check_and_evaluate(expression):
    if is_balanced(expression , 0)[0]:
        ret = evaluate(expression , 0)
        if ret[1] == None:
            return None
        else:
            return ret[0]
    else:
        return None

s = 'one'.join('two')
print(s)