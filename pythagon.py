from sympy.geometry import *
from sympy import acos, cos, pi, sin, sqrt

def expi(angle):
    return Point(cos(angle), sin(angle))

def triangle(b, alpha, c, O=Point(0,0)):

    # SAS
    a = sqrt(b*b+c*c-2*b*c*cos(alpha))
    R = a/(2*sin(alpha))
    beta1 = acos((c*c+a*a-b*b)/(2*c*a))
    gamma1 = pi - alpha - beta1

    A = O + Point(1,0) * Point(0,R)
    B = O + expi(alpha) * Point(0,-R)
    C = O + expi(-alpha) * Point(0,-R)

    return [A,B,C]

def circumradius(a, b, c):
	return a*b*c/sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c));

def angles_sss(a, b, c):
	alpha = acos((b*b+c*c-a*a)/(2*b*c));
	beta = acos((c*c+a*a-b*b)/(2*c*a));
	gamma = pi-alpha-beta;
	return [alpha, beta, gamma];

'''
    SSS Construction
'''
def triangle_sss(a, b, c, O=Point(0,0)):
    angles = angles_sss(a,b,c);

    alpha = angles[0];
    beta = angles[1];
    gamma = angles[2];
    R = circumradius(a,b,c);

    A = O + expi(beta-gamma)*(0,R);
    B = O + expi(-pi+beta+gamma)*(0,-R);
    C = O + expi(pi-beta-gamma)*(0,-R);
    return [A, B, C]
