# 3D Geometry

> Theory: [../../theory/maths/three-d-geometry.md](../../theory/maths/three-d-geometry.md)

### M-TDG-01 — JEE Main 2024 · 27 Jan Shift 1 · Q79 · MCQ

The distance of the point $(7,-2,11)$ from the line $\dfrac{x-6}1=\dfrac{y-4}0=\dfrac{z-8}3$, measured along the line $\dfrac{x-5}2=\dfrac{y-1}{-3}=\dfrac{z-5}6$, is

(1) 12  (2) 14  (3) 18  (4) 21

**Answer: (2)** · key ✔

**Solution.** From the point, move along $(2,-3,6)$: $(7+2t,\,-2-3t,\,11+6t)$. It meets the first line when $y=4\Rightarrow t=-2$, giving $(3,4,-1)$, which satisfies $\tfrac{x-6}1=-3=\tfrac{z-8}3$. Distance $=|t|\,\|(2,-3,6)\|=2\cdot7=14$.

### M-TDG-02 — JEE Main 2024 · 27 Jan Shift 1 · Q80 · MCQ

If the shortest distance between the lines $\dfrac{x-4}1=\dfrac{y+1}2=\dfrac z{-3}$ and $\dfrac{x-\lambda}2=\dfrac{y+1}4=\dfrac{z-2}{-5}$ is $\dfrac6{\sqrt5}$, then the sum of all possible values of $\lambda$ is

(1) 5  (2) 8  (3) 7  (4) 10

**Answer: (2)** · key ✔

**Solution.** $\vec d_1\times\vec d_2=(1,2,-3)\times(2,4,-5)=(2,-1,0)$ with magnitude $\sqrt5$. The join of the given points is $(\lambda-4,0,2)$, and $\left|(\lambda-4,0,2)\cdot(2,-1,0)\right|=2|\lambda-4|$. So $\dfrac{2|\lambda-4|}{\sqrt5}=\dfrac6{\sqrt5}\Rightarrow\lambda=1$ or $7$; the sum is $8$.

### M-TDG-03 — JEE Main 2024 · 27 Jan Shift 2 · Q90 · Numerical

The lines $\dfrac{x-2}2=\dfrac y{-2}=\dfrac{z-7}{16}$ and $\dfrac{x+3}4=\dfrac{y+2}3=\dfrac{z+2}1$ intersect at the point $P$. If the distance of $P$ from the line $\dfrac{x+1}2=\dfrac{y-1}3=\dfrac{z-1}1$ is $l$, then $14l^2$ is equal to ______.

**Answer: 108** · key ✔

**Solution.** Points: $(2+2s,-2s,7+16s)=(-3+4t,-2+3t,-2+t)$. From $y$: $s=1-\tfrac32t$; from $x$: $4-3t=-3+4t\Rightarrow t=1,\ s=-\tfrac12$. Check $z$: $7-8=-1=-2+1$ ✓. So $P=(1,1,-1)$. Take $Q(-1,1,1)$ on the third line with direction $\vec d=(2,3,1)$, $\vec{QP}=(2,0,-2)$. $\vec{QP}\times\vec d=(6,-6,6)$, so $l^2=\dfrac{108}{14}$ and $14l^2=108$.

### M-TDG-04 — JEE Main 2024 · 29 Jan Shift 1 · Q79 · MCQ

Let $PQR$ be a triangle with $R(-1,4,2)$. Suppose $M(2,1,2)$ is the midpoint of $PQ$. The distance of the centroid of $\triangle PQR$ from the point of intersection of the lines $\dfrac{x-2}0=\dfrac y2=\dfrac{z+3}{-1}$ and $\dfrac{x-1}1=\dfrac{y+3}{-3}=\dfrac{z+1}1$ is

(1) 69  (2) 9  (3) $\sqrt{69}$  (4) $\sqrt{99}$

**Answer: (3)** · key ✔

**Solution.** Lines: $(2,2s,-3-s)$ and $(1+t,-3-3t,-1+t)$. From $x$: $t=1$; from $y$: $2s=-6\Rightarrow s=-3$; check $z$: $-3+3=0=-1+1$ ✓. Intersection $(2,-6,0)$. The centroid divides median $RM$ in $2:1$ from $R$: $G=R+\tfrac23(M-R)=(1,2,2)$. Distance $=\sqrt{1+64+4}=\sqrt{69}$.

### M-TDG-05 — JEE Main 2024 · 29 Jan Shift 1 · Q90 · Numerical

A line with direction ratios $2,1,2$ meets the lines $x=y+2=z$ and $x+2=2y=2z$ at the points $P$ and $Q$ respectively. If the length of the perpendicular from the point $(1,2,12)$ to the line $PQ$ is $l$, then $l^2$ is ______.

**Answer: 65** · key ✔

**Solution.** $P=(t,t-2,t)$ and $Q=(u-2,\tfrac u2,\tfrac u2)$. $\overrightarrow{PQ}=k(2,1,2)$: from $y,z$ components: $\tfrac u2-t+2=k$ and $\tfrac u2-t=2k$, so $k=-2$ and $\tfrac u2-t=-4$. From $x$: $u-2-t=-4\Rightarrow u-t=-2$. Solving gives $u=4,\ t=6$: $P(6,4,6)$. For the point $(1,2,12)$: $\vec w=(-5,-2,6)$, $\vec d=(2,1,2)$. $\vec w\times\vec d=(-10,22,-1)$, $|\vec w\times\vec d|^2=585$, $|\vec d|^2=9$, so $l^2=65$.

