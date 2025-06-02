from math import sqrt
from functools import cache, lru_cache

class Complex:
    def __init__(self, re, im):
        """Define a complex number with real part re and imaginary part im."""
        self.re = re
        self.im = im
    def __repr__(self):
        return f'Complex({self.re},{self.im})'

    def __add__(self, x):
        """Given a complex number x, return a complex number representing self + x."""
        return Complex(self.re+x.re , self.im + x.im)
    def __mul__(self, x):
        """Given a complex number x, return a complex number representing self * x."""
        return Complex(self.re * x.re - self.im * x.im , self.re * x.im + self.im * x.re)
    def __pow__(self, n):
        """Given a non-negative integer n, return a complex number representing self ** n."""
        x = Complex(self.re , self.im)
        ret = Complex(1 , 0)
        while (n):
            if (n % 2):
                ret = ret * x
            x = x*x
            n //= 2
        return ret

    def __abs__(self):
        """Return the absolute value of a complex number."""
        return sqrt(self.re ** 2 + self.im ** 2)
    
@cache
def z_fun (c , n):
    if (n == 0):
        return Complex(0,0)
    else:
        return z_fun(c , n-1) ** 2 + c
    
def z_gen(c):
    z = Complex(0,0)
    while True:
        yield z
        z = z ** 2 + c

def in_mset(c, timeout=16):
    z = Complex(0,0)
    for i in range(16):
        if abs(z) > 2:
            return False
        z = z ** 2 + c

    return True

def escape_time(c, bound=2, timeout=16):
    z = Complex(0,0)
    for i in range(16):
        if abs(z) > 2:
            return i
        z = z ** 2 + c
    
    return 16

def csector(density, xmin, xmax, ymin, ymax):
    xn = int((xmax-xmin) * density)
    yn = int((ymax-ymin) * density)
    xaxis = [xmin + i / density  for i in range(xn)]
    yaxis = [ymin + i / density  for i in range(yn)]
    return [Complex(a,b) for a in xaxis for b in yaxis]

import matplotlib.pyplot as plt

def visualize_mset(density=100, xmin=-2, xmax=0.5, ymin=-1.5, ymax=1.5):
    mset = [c for c in csector(density, xmin, xmax, ymin, ymax) if in_mset(c)]
    plt.scatter([c.re for c in mset], [c.im for c in mset], color="black", marker=",", s=1)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.show()

def visualize_mset_escape(density=100, xmin=-2, xmax=0.5, ymin=-1.5, ymax=1.5):
    def to_color(t):
        return '#00ff00' if t >= 16 else '#{0:06x}'.format(t * 0x111111)
    cs = csector(density, xmin, xmax, ymin, ymax)
    plt.scatter([c.re for c in cs], [c.im for c in cs], c=[to_color(escape_time(c)) for c in cs], marker=",", s=1)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.show()

visualize_mset_escape()
