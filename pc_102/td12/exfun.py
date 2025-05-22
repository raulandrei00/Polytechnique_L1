class InvalidInput(Exception):
    pass

def sum_of_input() -> int:
    sum = 0
    while True:
        try:
            user_input = input()
            x = int()
            try: x = int(user_input)
            except: raise(InvalidInput)
            sum += x
        except EOFError:
            return sum

import time
from typing import Callable

def timed[S,T](f: Callable[[S],T], x: S) -> tuple[T, float]:
    start = time.time()
    out = f(x)
    end = time.time()
    return (out, end-start)

def timed_ex[S,T](f: Callable[[S],T], x: S) -> tuple[T | Exception, float]:
    start = time.time()
    ret = tuple()

    try:
        out = f(x)
        ret = (out, time.time()-start)
    except Exception as e:
        ret = (e, time.time()-start)
    finally:
        return ret


from trees import Leaf, Node, Tree

def cbt(n: int, x:int = 0) -> Tree:
    if n == 0: return Leaf(x)
    else:      return Node(cbt(n-1, x), cbt(n-1, x + 2**(n-1)))

def count_nodes(t: Tree) -> int:
    match t:
        case Leaf(): return 0
        case Node(): return count_nodes(t.left) + count_nodes(t.right) + 1
        case _: raise TypeError(f"Invalid type {type(t)}")

example1 : Tree = Node(Leaf(0), Node(Leaf(1), Leaf(2)))
example2 : Tree = Node(Node(Leaf(0), Leaf(1)), Leaf(2))
example3 : Tree = Node(Node(Leaf(0), Node(Leaf(1), Leaf(2))), Node(Leaf(3), Leaf(4)))

print(count_nodes(example3))

def sum_leaves(t: Tree) -> int:
    match t:
        case Leaf(): return t.value
        case Node(): return sum_leaves(t.left) + sum_leaves(t.right)
        case _: raise TypeError(f"Invalid type {type(t)}")

def leaves(t: Tree) -> list[int]:
    match t:
        case Leaf(): return [t.value]
        case Node(): return leaves(t.left) + leaves(t.right)
        case _: raise TypeError(f"Invalid type {type(t)}")

def mirror(t: Tree) -> Tree:
    match t:
        case Leaf(): return t
        case Node(): return Node(mirror(t.right), mirror(t.left))
        case _: raise TypeError(f"Invalid type {type(t)}")

def fold_tree[S,T,L] (t: Tree, f_leaf: Callable[[S],T], f_node: Callable[[T,T],L]) -> L:
    match t:
        case Leaf(): return f_leaf(t.value)
        case Node(): return f_node(fold_tree(t.left, f_leaf, f_node), fold_tree(t.right, f_leaf, f_node))
        case _: raise TypeError(f"Invalid type {type(t)}")

def count_nodes_as_fold(t : Tree) -> int:
    return fold_tree(t, lambda x:0, lambda l, r: l + r + 1)


def sum_leaves_as_fold(t : Tree) -> int:
    return fold_tree(t, lambda x:x, lambda l, r: l + r)

def leaves_as_fold(t : Tree) -> list[int]:
    return fold_tree(t, lambda x:[x], lambda l, r: l + r)
# print(leaves_as_fold(example3))

def mirror_as_fold(t : Tree) -> Tree:
    return fold_tree(t, lambda x:Leaf(x), lambda l, r: Node(r, l))

def eq_tree(t: Tree, u: Tree) -> bool:
    return t == u
    
ex4 = Node(Leaf(0), Node (Leaf(1), Leaf(2)))
print(example1 , ex4)
print(eq_tree(example1, ex4))