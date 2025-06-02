import random
from math import sqrt
from math import pi
import math


def torus_volume_cuboid(R, r, N=100_000):
    inside = 0
    for i in range(N):
        x = random.uniform(-(R+r) , R+r)
        y = random.uniform(-(R+r) , R+r)
        z = random.uniform(-r , r)
        if ((sqrt(x**2 + y**2) - R) ** 2 + z ** 2 <= r ** 2):
            inside += 1
    return inside / N * (2 * (R+r)) ** 2 * 2*r

def torus_volume_cylinder(R, r, N=100_000):
    inside = 0
    for i in range(N):
        theta = random.uniform(0 , 2*pi)
        x = random.uniform(0,1)
        h = random.uniform(-r,r)

        x,y,z = (R+r) * sqrt(x)*math.cos(theta) , (R+r) * sqrt(x) * math.sin(theta) , h

        if ((sqrt(x**2 + y**2) - R) ** 2 + z ** 2 <= r ** 2):
            inside += 1

    return inside / N * pi * ((R+r)**2) * 2*r

def torus_volume_pipe(R, r, N=100_000):
    inside = 0
    for i in range(N):
        theta = random.uniform(0 , 2*pi)
        x = random.uniform((R-r) / (R+r),1)
        h = random.uniform(-r,r)

        x,y,z = (R+r) * sqrt(x)*math.cos(theta) , (R+r) * sqrt(x) * math.sin(theta) , h

        if ((sqrt(x**2 + y**2) - R) ** 2 + z ** 2 <= r ** 2):
            inside += 1

    return inside / N * pi * ((R+r)**2 - (R-r)**2) * 2*r

from sys import maxsize

def pi_coprimality(N=100_000):
    good = 0
    for i in range (N):
        a = random.randint(0 , maxsize)
        b = random.randint(0 , maxsize)
        if (math.gcd(a , b) == 1):
            good += 1

    # good / N == 6 / pi^2

    return sqrt(N / good * 6)

def pi_evenness(N=100_000):
    good = 0
    for i in range(N):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (round(x / y) % 2 == 0):
            good += 1
    
    return 5 - good / N * 4

def pi_chords(N=100_000):
    sum = 0
    for i in range(N):
        r = 1
        theta = random.uniform(0,2*pi)
        x1 , y1 = sqrt(r) * math.cos(theta) , sqrt(r) * math.sin(theta)
        
        r = 1
        theta = random.uniform(0,2*pi)
        x2 , y2 = sqrt(r) * math.cos(theta) , sqrt(r) * math.sin(theta)
        
        
        sum += sqrt((x1 - x2) ** 2 + (y1-y2)**2)

    avg = sum / N
    # avg == 4/pi =>

    return 4 / avg

def dist (p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1-y2)**2)

# this function is copied from the website geeks for geeks
def areaTriangle(a, b, c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def area3 (p1 , p2 , p3):
    a , b , c = dist(p1 , p2) , dist(p2 , p3) , dist(p3 , p1)
    return areaTriangle(a , b, c)

def bounding_rect(p1, p2, p3):
    low = min(p1[0] , p2[0] , p3[0]) , min(p1[1] , p2[1] , p3[1])
    high = max(p1[0] , p2[0] , p3[0]) , max(p1[1] , p2[1] , p3[1])
    return low,high

def inside (p , p1 , p2 , p3) :
    return math.isclose(area3(p,p1,p2) + area3(p,p2,p3) + area3(p,p1,p3) , area3(p1,p2,p3))


def rejection_sample3(p1, p2, p3):
    
    bound = bounding_rect(p1,p2,p3)
    
    while True :
        x = random.uniform(bound[0][0], bound[1][0])
        y = random.uniform(bound[0][1], bound[1][1])
        if (inside ((x,y) , p1,p2,p3)):
            return x,y


def add (p1 , p2):
    return p1[0]+p2[0] , p1[1]+p2[1]

def subtract (p1 , p2):
    return p1[0]-p2[0] , p1[1]-p2[1]

def scalar_mult (alpha , p):
    return alpha * p[0] , alpha * p[1]

def quick_sample3(p1, p2, p3):
    a = subtract(p2 , p1)
    b = subtract(p3 , p1)

    alpha = random.random()
    beta = random.random() * (1 - alpha)

    rand_point = add( scalar_mult(alpha , a) , scalar_mult(beta , b))

    return add (rand_point , p1)
