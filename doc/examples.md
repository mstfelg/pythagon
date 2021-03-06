## [1](https://artofproblemsolving.com/community/c4h2442556_some_nice_geo_i_made)

Let $I$ be the incenter of $\triangle ABC$, and let the circumcircle of $\triangle BIC$ intersect lines $AB$ and $AC$ at $D$ and $E$, respectively. Let $DE$ intersect the circumcircle of $\triangle ABC$ at $X$ and $Y$. Given that $AB=5,\,BC=7,\,AC=8$, find the area of $\triangle AXY$.

---

```python
a,b,c=7,8,5
t=triangle(7,8,5)
---
I;
k=Circle(B,I,C)
---
D=[A,B],k[0]
E=[A,C],k[0]
# or
cyclic([A,B],k[0])
# or
D,E=[A,[for B,C]],k[0]
---
X,Y=[D,E],k
area([A,X,Y])?
```

## [2](https://artofproblemsolving.com/community/c6h2351758_intersecting_lines)

Let $ABC$ be a triangle. Let $A_1$, $B_1$ and $C_1$ be the centers of $BC$, $AC$ and $AB$ respectively and $A_2$, $B_2$, $C_2$ be the centers of the heights from $A$, $B$ and $C$ respectively. Show that $A_1A_2$, $B_1B_2$ and $C_1C_2$ intersect.

---

```python
cyclic(A_1=Center(B,C))
#or
A_1...=Center(B,C)
---
A_2...=Center(Foot(A,B,C))
areConcur(cyclic(A_1,A_2))
```

## [3](https://artofproblemsolving.com/community/c6t48f6h420437_prove_that_oa_and_ra_are_perpendicular)

Acute triangle $ABC$ is inscribed in circle $\omega$. Let $H$ and $O$ denote its orthocenter and circumcenter, respectively. Let $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Rays $MH$ and $NH$ meet $\omega$ at $P$ and $Q$, respectively. Lines $MN$ and $PQ$ meet at $R$. Prove that $OA\perp RA$.

```python
Cyclic(M=Center(A,B))
Cyclic(P=MH, Circle(A,B,C))
R=[M,N],[P,Q]
isPerp([O,A],[R,A])
```

