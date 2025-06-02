class Leaf:
    def __init__(self, value: int):
        self.value = value
    def __repr__(self):
        return f'Leaf({self.value})'

class Node:
    def __init__(self, left: 'Tree', right: 'Tree'):
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Node({self.left}, {self.right})'

Tree = Leaf | Node
# remove "type" from the previous line for Python 3.11, i.e., replace by
# Tree = Leaf | Node

import asyncio, time



async def f(x):
    await asyncio.sleep(2*x)
    return 2*x

async def g(x):
    await asyncio.sleep(3*x)
    return 3*x
    
async def h(x):
    vf, vg = await asyncio.gather(f(x), g(x))
    await asyncio.sleep(x)
    return vf + vg

if __name__ == "__main__":
    x = time.time()
    print(asyncio.run(h(1)))
    print(time.time() - x)