import sympy
from sympy import acos, cos, pi, sin, sqrt
from sympy.geometry import *

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
