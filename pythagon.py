from sympy.geometry import *
from sympy import acos, cos, pi, sin, sqrt

def expi(angle):
    return Point(cos(angle), sin(angle))

def triangle(O, b, alpha, c):

    # SAS
    a = sqrt(b*b+c*c-2*b*c*cos(alpha))
    R = a/(2*sin(alpha))
    beta1 = acos((c*c+a*a-b*b)/(2*c*a))
    gamma1 = pi - alpha - beta1

    A = O + Point(1,0) * Point(0,R)
    B = O + expi(alpha) * Point(0,-R)
    C = O + expi(-alpha) * Point(0,-R)

    return [A,B,C]
