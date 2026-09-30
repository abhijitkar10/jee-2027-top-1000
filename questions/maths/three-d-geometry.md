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

### M-TDG-06 — JEE Main 2024 · 29 Jan Shift 2 · Q90 · Numerical

Let $O$ be the origin, and $M$ and $N$ points on the lines $\dfrac{x-5}4=\dfrac{y-4}1=\dfrac{z-5}3$ and $\dfrac{x+8}{12}=\dfrac{y+2}5=\dfrac{z+11}9$ respectively, such that $MN$ is the shortest distance between the given lines. Then $\overrightarrow{OM}\cdot\overrightarrow{ON}$ is equal to ______.

**Answer: 9** · key ✔

**Solution.** $\vec d_1\times\vec d_2=(4,1,3)\times(12,5,9)=(-6,0,8)$, so $\overrightarrow{MN}\parallel(-3,0,4)$. With $M=(5+4s,4+s,5+3s)$ and $N=(-8+12t,-2+5t,-11+9t)$, the $y$-component of $\overrightarrow{MN}$ is zero: $5t-s=6\Rightarrow s=5t-6$. Then $\overrightarrow{MN}=(11-8t,\,0,\,2-6t)\parallel(-3,0,4)\Rightarrow4(11-8t)=-3(2-6t)\Rightarrow t=1,\ s=-1$. So $M=(1,3,2)$, $N=(4,3,-2)$ and $\overrightarrow{OM}\cdot\overrightarrow{ON}=4+9-4=9$.

### M-TDG-07 — JEE Main 2024 · 30 Jan Shift 1 · Q79 · MCQ

Let $(\alpha,\beta,\gamma)$ be the foot of the perpendicular from the point $(1,2,3)$ on the line $\dfrac{x+3}5=\dfrac{y-1}2=\dfrac{z+4}3$. Then $19(\alpha+\beta+\gamma)$ is equal to

(1) 102  (2) 101  (3) 99  (4) 100

**Answer: (2)** · key ✔

**Solution.** A point on the line: $(-3+5t,\,1+2t,\,-4+3t)$. The vector from $(1,2,3)$ is $(5t-4,\,2t-1,\,3t-7)$; perpendicular to $(5,2,3)$: $25t-20+4t-2+9t-21=0\Rightarrow t=\tfrac{43}{38}$. Foot $=\left(\tfrac{101}{38},\tfrac{124}{38},-\tfrac{23}{38}\right)$, with coordinate sum $\dfrac{202}{38}$. So $19(\alpha+\beta+\gamma)=101$.

### M-TDG-08 — JEE Main 2024 · 30 Jan Shift 2 · Q79 · MCQ

Let $L_1:\vec r=(\hat i-\hat j+2\hat k)+\lambda(\hat i-\hat j+2\hat k)$, $L_2:\vec r=(\hat j-\hat k)+\mu(3\hat i+\hat j+p\hat k)$ and $L_3:\vec r=\delta(l\hat i+m\hat j+n\hat k)$ be three lines such that $L_1\perp L_2$ and $L_3$ is perpendicular to both $L_1$ and $L_2$. Then a point which lies on $L_3$ is

(1) $(-1,7,4)$  (2) $(-1,-7,4)$  (3) $(1,7,-4)$  (4) $(1,-7,4)$

**Answer: (1)** · key ✔

**Solution.** $L_1\perp L_2$: $(1,-1,2)\cdot(3,1,p)=3-1+2p=0\Rightarrow p=-1$. $L_3$ has direction $(1,-1,2)\times(3,1,-1)=\left((-1)(-1)-2(1),\ 2(3)-(1)(-1),\ 1(1)-(-1)(3)\right)=(-1,7,4)$. $L_3$ passes through the origin, so $\delta(-1,7,4)$ lies on it; at $\delta=1$ the point is $(-1,7,4)$.

### M-TDG-09 — JEE Main 2024 · 31 Jan Shift 1 · Q78 · MCQ

The distance of the point $Q(0,2,-2)$ from the line passing through $P(5,-4,3)$ and perpendicular to the lines $\vec r=-3\hat i+2\hat k+\lambda(2\hat i+3\hat j+5\hat k)$ and $\vec r=\hat i-2\hat j+\hat k+\mu(-\hat i+3\hat j+2\hat k)$ is

(1) $\sqrt{86}$  (2) $\sqrt{20}$  (3) $\sqrt{54}$  (4) $\sqrt{74}$

**Answer: (4)** · key ✔

**Solution.** The direction is $(2,3,5)\times(-1,3,2)=(-9,-9,9)\parallel(1,1,-1)$. $\overrightarrow{PQ}=(-5,6,-5)$ and $\overrightarrow{PQ}\times(1,1,-1)=(-1,-10,-11)$ with squared magnitude $222$; $|\vec d|^2=3$. Distance$^2=\dfrac{222}3=74$.

### M-TDG-10 — JEE Main 2024 · 31 Jan Shift 2 · Q78 · MCQ

Let $(\alpha,\beta,\gamma)$ be the mirror image of the point $(2,3,5)$ in the line $\dfrac{x-1}2=\dfrac{y-2}3=\dfrac{z-3}4$. Then $2\alpha+3\beta+4\gamma$ is equal to

(1) 32  (2) 33  (3) 31  (4) 34

**Answer: (2)** · key ✔

**Solution.** A point on the line: $(1+2t,2+3t,3+4t)$. Perpendicular from $(2,3,5)$: $(2t-1)2+(3t-1)3+(4t-2)4=0\Rightarrow29t=13$. Foot $=\left(\tfrac{55}{29},\tfrac{97}{29},\tfrac{139}{29}\right)$. Image $=2\cdot\text{foot}-(2,3,5)=\left(\tfrac{52}{29},\tfrac{107}{29},\tfrac{133}{29}\right)$. $2\alpha+3\beta+4\gamma=\dfrac{104+321+532}{29}=\dfrac{957}{29}=33$.

### M-TDG-11 — JEE Main 2024 · 31 Jan Shift 2 · Q90 · Numerical

A line passes through $A(4,-6,-2)$ and $B(16,-2,4)$. The point $P(a,b,c)$, where $a,b,c$ are non-negative integers, on the line $AB$ lies at a distance of $21$ units from the point $A$. The distance between the points $P(a,b,c)$ and $Q(4,-12,3)$ is equal to ______.

**Answer: 22** · key ✔

**Solution.** $\overrightarrow{AB}=(12,4,6)\parallel(6,2,3)$ with length $7$, so unit direction $\pm\tfrac17(6,2,3)$. At distance $21$: $P=A\pm3(6,2,3)$. $A+3(6,2,3)=(22,0,7)$ has non-negative integer coordinates, whereas $A-3(6,2,3)=(-14,-12,-11)$ does not. $PQ=\sqrt{18^2+12^2+4^2}=\sqrt{484}=22$.

