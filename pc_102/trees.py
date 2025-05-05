
from math import inf

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def calc_size (self):
        pass

def size (root):
    if (root is None): return 0
    ret = 1
    # if (root.left is not None):
    ret += size (root.left)
    # if (root.right is not None):
    ret += size (root.right)
        
    return ret

def sum_values (root):
    if (root is None): return 0
    ret = root.value
    # if (root.left is not None):
    ret += sum_values (root.left)
    # if (root.right is not None):
    ret += sum_values (root.right)
    return ret

def mirrored(lroot, rroot):
    if lroot is None and rroot is not None or lroot is not None and rroot is None:
        return False
    elif lroot is None and rroot is None:
        return True
    elif lroot.value != rroot.value:
        return False
    else: return mirrored(lroot.right , rroot.left) and mirrored(lroot.left , rroot.right)

def check_symmetry(root):
    if root is None: return True
    return mirrored (root.left , root.right)


def bst_rec (root):
    if (root is None): return (True ,  0, 0)
    possible , minv , maxv = True , root.value , root.value

    if (root.left is not None):
        (bst_left , min_val , max_val) = bst_rec(root.left)
        minv = min(minv , min_val)
        if (max_val <= root.value):
            possible = possible and bst_left
        else:
            possible = 0
    if (root.right is not None):
        (bst_right , min_val , max_val) = bst_rec(root.right)
        maxv = max(maxv , max_val)
        if (min_val >= root.value):
            possible = possible and bst_right
        else:
            possible = 0
        

    return (possible , minv , maxv)

def check_BST (root):
    return bst_rec(root)[0]

def min_BST(root):
    if root is None: return inf
    while (root.left is not None):
        root = root.left
    return root.value

crt_val = 69696969696

def min_diff_rec (root):
    global crt_val
    ret = inf
    if root is None: return ret

    if (root.left is not None):
        ret = min(ret , min_diff_rec(root.left))
    # print(f"  {root.value} , {crt_val}")

    if crt_val is not None:
        ret = min(ret , abs(root.value - crt_val))
    crt_val = root.value

    if (root.right is not None):
        ret = min(min_diff_rec(root.right) , ret)
    return ret

def min_diff (root):
    global crt_val
    crt_val = None
    return min_diff_rec(root)

# print(min_diff(Node(-949, Node(-985, None, None), None)))

def check_val (root):
    return crt_val != root.value

def count_distinct_rec (root):
    global crt_val
    ret = 0
    if root is None: return ret

    if (root.left is not None):
        ret += count_distinct_rec(root.left)
    # print(f"  {root.value} , {crt_val}")

    if not check_val(root):
        ret += 1
    crt_val = root.value
    

    if (root.right is not None):
        ret += count_distinct_rec(root.right)

    return ret

def count_distinct (root):
    global crt_val
    crt_val = 69696969696969
    ans = size(root)
    ans -= count_distinct_rec(root)
    return ans

def bst_search(node, x):
    if node is None:
        return False
    elif node.value == x:
        return True
    elif x < node.value:
        return bst_search(node.left, x)
    else:
        return bst_search(node.right, x)
    
def bst_insert(node, x):
    if node is None:
        return Node(x)
    elif x <= node.value:
        node.left = bst_insert(node.left, x)
    else:
        node.right = bst_insert(node.right, x)
    return node

def bst_remove (root , x):
    virtual_root = Node(None , root , None)
    
    par = virtual_root
    dir = "left"
    while root is not None and root.value != x:
        if (root.value < x): 
            par = root
            root = root.right
            dir = "right"
        elif (root.value > x): 
            par = root
            root = root.left
            dir = "left"
    if (root is None): return virtual_root.left
    if (root.left is None):
        if dir == 'left':
            par.left = root.right
        elif dir == "right":
            par.right = root.right
        root = None
         
    elif (root.right is None):
        if dir == 'left':
            par.left = root.left
        elif dir == "right":
            par.right = root.left
        root = None
    else:
        to_rem = root.right
        parent = root
        while to_rem.left is not None:
            parent = to_rem
            to_rem = to_rem.left
        if parent == root:
            parent.right = to_rem.right
        else: parent.left = to_rem.right
        
        root.value = to_rem.value
    return virtual_root.left

root = None

level = ""

def print_bst (root):
    global level
    level = level + " "
    if root is None:
        level = level[:-1]
        return
    print_bst(root.left)
    print(level + str(root.value))
    print_bst(root.right)
    level = level[:-1]

root = bst_insert(root , 9)
root = bst_insert(root , 6)
root = bst_insert(root , 7)
root = bst_insert(root , 3)
root = bst_insert(root , 0)
root = bst_insert(root , 2)
root = bst_insert(root , 4)
root = bst_insert(root , 8)
root = bst_insert(root , 5)
root = bst_insert(root , 1)

root = bst_remove(root , 8)
root = bst_remove(root , 0)
root = bst_remove(root , 3)
print_bst(root)
root = bst_remove(root , 2)
root = bst_remove(root , 7)

    
