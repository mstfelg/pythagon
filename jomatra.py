import sympy
from sympy.geometry import *
from sympy import pi, sqrt, cos, sin, acos

class Point(sympy.Point2D):
    def __mul__(self, point):
        x,y = self.args[0], self.args[1]
        a,b = point.args[0], point.args[1]
        return Point(a*y+b*x, a*x-b*y)

def expi(angle):
    return Point(cos(angle), sin(angle))

def triangle(O, b, A, c):
    
    # SAS
    a = sqrt(b*b+c*c-2*b*c*cos(A))
    R = a/(2*sin(A))
    beta1 = acos((c*c+a*a-b*b)/(2*c*a))
    gamma1 = pi - A - beta1

    A = O + Point(1,0)*Point(0,R)
    B = O + expi(A)*Point(0,-R)
    C = O + expi(-A)*Point(0,-R)
    return [A,B,C]

O = Point(0,0)
b,c = 1,1
alpha = pi/2

print(triangle(O,b,alpha,c))
