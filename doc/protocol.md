 Every geometry drawing is a special case. Therefore, geometric construction involve 3 parts:

1. Semantics:  All this part provides is the raw instructions.
1. Numerics: An average example of the drawing.
1. Style: How to draw it. What colors, linestyles, decorations, etc... you should use.
1. Control: specifies how a GUI program handle user interactions

## Semantics

```Python
A=(1,3) # Point definition
A=(theta) 
A=(3; theta)
A*B # All points are complex numbers
A,B,C = (4,0),O,(0,3) # Triangle ABC. Points are comma separated
A_1,A_2,...,A_n # Every polygon is an array
line=A,B # line definition
```

### Circles

```python
(O) # Last constructed circle with radius O
O(r) # circle centered at O with radius r.
O(P) # Circle Centered at O passing through P
Circle(A,B,theta) # Circle passing through A,B with angle theta
Circle(A,B, 180) # diameter A,B
```

### Bisection

```python
bis(A,B,C) # Angle bisector
bis(P1,P2) # perpendicular bisector
bis(l,m) # Angle bisector
```

### Reflection

```python
ref(A, l)
ref(A, B)
ref(A, c) # Inversion
ref(l, l)
ref(l, c)
```

### Perpendicular and Orthogonal

```python
Ortho(P, c) # Orthogonal circle passing through P, 
Ortho(P, l) # Perpendicular line on l passing through P
Ortho(A,B,C) # Foot of A over line B,C
```

### Feet

```python
foot(A,B,C)
foot(A,B,C, .5) # median
foot([A,B,C])[2]
foot(A,B,C, anglebisector)
```



### Truth check

```python
arePar
areOrtho
areCyclic
areConcur
```

#### Dual function of points and lines

```python
l=A,B # line AB
A=l,m # intersection l,m


K=l,c[0] # First intersection of line l, c

l=A,m # Line through A parallel to line m
l=A,c # Line through A parallel to circle c
```

# Draft

Every output in geometry is either C,L, or P. So functions can be like:

```python
P(l, l) # intersection
P(P, P) # midpoint
P(l, C) # ...
L(L,L) # Angle bisector
L(P,P,L) # idk
P(L, L, P)

P:= A #(definition copy)
P = B #(Static copy)
P = (32,1); #(adding semicolon does not draw the point)
```

## Defaults

```python
# unless one of A,B,C is defined, the following takes place by default
""" Numerics """
O=(0,0)
A=(110)
B=(210)
C=(330)
""" Semantics """
I=Incenter(A,B,C)=Center(A,B,C,1)
H=Ortho(A,B,C)=Center(A,B,C,4)
G=Centroid(A,B,C)=Center(A,B,C,3)
X_n=Center(A,B,C,n)
cyclic(H_{defTri.A})

```

## Transformations

```python
# Which is better? Poland postfix notation?
H Ref B,C; B,C Circle
# or
Circle(Ref(B,C), B, C) # I prefer #2
```

## Settings

* Counterclockwise ordering
* setDefault(X,Y,Z): Rename the default triangle
