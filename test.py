from pythagon import *
from sympy.geometry import *

def test_triangle():
    O = Point(0,0)
    b,c = 1,1
    alpha = pi/2

    print(triangle(O,b,alpha,c))

print(triangle(O,b,alpha,c))

def main():
    test_triangle()
