def rev1_checked(xs):
    xs_input = xs[:]  # we copy the original input list to be able to refer to it in the invariant
    n = len(xs)
    for k in range(n//2):
        t = xs[k]
        xs[k] = xs[n-1-k]
        xs[n-1-k] = t
        assert xs[:k+1] == xs_input[-1:-2-k:-1] and xs_input[:k+1] == xs[-1:-2-k:-1]
        # the check for k == n//2 - 1 is equivalent to xs[:] == xs_input[::-1]


def improved_check_rev(revfn, xs):
    n = len(xs)
    xs_copy = xs[:]
    try:
        revfn(xs_copy)
    except Exception as e:
        return False
    return all (xs_copy[i] == xs[n-1-i] for i in range(n))


def rev2_buggy(xs):
    n = len(xs)
    for m in range(n,1,-1):
        for i in range(m-1):
            t = xs[i]
            xs[i] = xs[i+1]
            xs[i+1] = t

# xs = [1,2,3,4,5,6,7,8]
# rev2_buggy(xs)
# print(xs)

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Node{(self.value, self.left, self.right)}' if self.left or self.right \
            else f'Node({self.value})'
    def __eq__(self, other):
        try:
            return other is not None and \
                self.value == other.value and \
                self.left == other.left and self.right == other.right
        except:
            return False
        
    def copy(self):
        left  = self.left.copy() if self.left else None
        right = self.right.copy() if self.right else None
        return Node(self.value, left, right)

def bst_remove2(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = bst_remove2(node.left, x)
    elif x > node.value:
        node.right = bst_remove2(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.left
        while current.right is not None:
            parent, current = current, current.right
        if parent is node:
            parent.left = current.left
        else:
            parent.right  = current.left
        node.value = current.value
  
    return node

def bst_remove1(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = bst_remove1(node.left, x)
    elif x > node.value:
        node.right = bst_remove1(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.left
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 

def check_bst_remove (delfn , node , x):

    _node = node.copy()

    # print(_node , x)
    def inorder (tree):
        ret = []
        if tree is None: return ret
        ret += inorder(tree.left)
        ret += [tree.value]
        ret += inorder(tree.right)
        
        return ret
    
    lst = inorder(_node)
    try:
        new_tree = delfn(_node , x)
    except:
        return False
    lst_new = inorder(new_tree)

    # print(new_tree)

    try: lst.remove(x)
    except: pass

    return lst_new == lst

def all_bst_gen_rec (l , r):
    
    if (l == r): 
        yield None
        return

    for i in range (l , r):
        gen_left = all_bst_gen_rec(l , i)
        
        while (found_left := next(gen_left , -1)) != -1:
            gen_right = all_bst_gen_rec(i+1 , r)
        
            while (found_right := next(gen_right , -1)) != -1:
                # print(Node(i , found_left, found_right))
                yield Node(i , found_left, found_right)

def all_bst_gen (n):
    gen_rec = all_bst_gen_rec(0,n)
    
    while found := next(gen_rec , False):
        yield found

# generator = all_bst_gen(3)

def test_bst_remove(delfn, maxn):
    for n in range (2 , maxn):
        gen_n = all_bst_gen(n)

        while (tree := next(gen_n , False)) != False:
            # print(tree)
            for x in range(0, n+1):
                try:
                    # print(check_bst_remove(delfn , tree , x))
                    if check_bst_remove(delfn , tree , x) == False:
                        return tree , x
                except:
                    return tree , x , "exception"
    return None


import buggy
print(test_bst_remove(buggy.del5 , 6))

assert check_bst_remove(buggy.del0, Node(0), 0) == False
#(Node(0), 2, 'exception') -> exception error
assert check_bst_remove(buggy.del1, Node(0), 2) == False
assert check_bst_remove(buggy.del2 , Node(1, Node(0), Node(2)), 1) == False
assert check_bst_remove(buggy.del3 , Node(2, Node(0, None, Node(1)), Node(3)), 2) == False
assert check_bst_remove(buggy.del4 , Node(1, Node(0), Node(3, Node(2), None)), 1) == False
assert check_bst_remove(buggy.del4 , Node(0, None, Node(2, Node(1), Node(4, Node(3), None))), 2) == False
