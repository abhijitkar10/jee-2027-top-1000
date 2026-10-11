# 3D Geometry

> Theory: [../../theory/maths/three-d-geometry.md](../../theory/maths/three-d-geometry.md)

### M-TDG-01 — JEE Main 2024 · 27 Jan Shift 1 · Q80 · MCQ

If the shortest distance between the lines $\dfrac{x-4}1=\dfrac{y+1}2=\dfrac z{-3}$ and $\dfrac{x-\lambda}2=\dfrac{y+1}4=\dfrac{z-2}{-5}$ is $\dfrac6{\sqrt5}$, then the sum of all possible values of $\lambda$ is

(1) 5  (2) 8  (3) 7  (4) 10

**Answer: (2)** · key ✔

**Solution.** $\vec d_1\times\vec d_2=(1,2,-3)\times(2,4,-5)=(2,-1,0)$ with magnitude $\sqrt5$. The join of the given points is $(\lambda-4,0,2)$, and $\left|(\lambda-4,0,2)\cdot(2,-1,0)\right|=2|\lambda-4|$. So $\dfrac{2|\lambda-4|}{\sqrt5}=\dfrac6{\sqrt5}\Rightarrow\lambda=1$ or $7$; the sum is $8$.

### M-TDG-02 — JEE Main 2024 · 27 Jan Shift 2 · Q90 · Numerical

The lines $\dfrac{x-2}2=\dfrac y{-2}=\dfrac{z-7}{16}$ and $\dfrac{x+3}4=\dfrac{y+2}3=\dfrac{z+2}1$ intersect at the point $P$. If the distance of $P$ from the line $\dfrac{x+1}2=\dfrac{y-1}3=\dfrac{z-1}1$ is $l$, then $14l^2$ is equal to ______.

**Answer: 108** · key ✔

**Solution.** Points: $(2+2s,-2s,7+16s)=(-3+4t,-2+3t,-2+t)$. From $y$: $s=1-\tfrac32t$; from $x$: $4-3t=-3+4t\Rightarrow t=1,\ s=-\tfrac12$. Check $z$: $7-8=-1=-2+1$ ✓. So $P=(1,1,-1)$. Take $Q(-1,1,1)$ on the third line with direction $\vec d=(2,3,1)$, $\vec{QP}=(2,0,-2)$. $\vec{QP}\times\vec d=(6,-6,6)$, so $l^2=\dfrac{108}{14}$ and $14l^2=108$.

### M-TDG-03 — JEE Main 2024 · 29 Jan Shift 1 · Q79 · MCQ

Let $PQR$ be a triangle with $R(-1,4,2)$. Suppose $M(2,1,2)$ is the midpoint of $PQ$. The distance of the centroid of $\triangle PQR$ from the point of intersection of the lines $\dfrac{x-2}0=\dfrac y2=\dfrac{z+3}{-1}$ and $\dfrac{x-1}1=\dfrac{y+3}{-3}=\dfrac{z+1}1$ is

(1) 69  (2) 9  (3) $\sqrt{69}$  (4) $\sqrt{99}$

**Answer: (3)** · key ✔

**Solution.** Lines: $(2,2s,-3-s)$ and $(1+t,-3-3t,-1+t)$. From $x$: $t=1$; from $y$: $2s=-6\Rightarrow s=-3$; check $z$: $-3+3=0=-1+1$ ✓. Intersection $(2,-6,0)$. The centroid divides median $RM$ in $2:1$ from $R$: $G=R+\tfrac23(M-R)=(1,2,2)$. Distance $=\sqrt{1+64+4}=\sqrt{69}$.

### M-TDG-04 — JEE Main 2024 · 29 Jan Shift 1 · Q90 · Numerical

A line with direction ratios $2,1,2$ meets the lines $x=y+2=z$ and $x+2=2y=2z$ at the points $P$ and $Q$ respectively. If the length of the perpendicular from the point $(1,2,12)$ to the line $PQ$ is $l$, then $l^2$ is ______.

**Answer: 65** · key ✔

**Solution.** $P=(t,t-2,t)$ and $Q=(u-2,\tfrac u2,\tfrac u2)$. $\overrightarrow{PQ}=k(2,1,2)$: from $y,z$ components: $\tfrac u2-t+2=k$ and $\tfrac u2-t=2k$, so $k=-2$ and $\tfrac u2-t=-4$. From $x$: $u-2-t=-4\Rightarrow u-t=-2$. Solving gives $u=4,\ t=6$: $P(6,4,6)$. For the point $(1,2,12)$: $\vec w=(-5,-2,6)$, $\vec d=(2,1,2)$. $\vec w\times\vec d=(-10,22,-1)$, $|\vec w\times\vec d|^2=585$, $|\vec d|^2=9$, so $l^2=65$.

### M-TDG-05 — JEE Main 2024 · 29 Jan Shift 2 · Q90 · Numerical

Let $O$ be the origin, and $M$ and $N$ points on the lines $\dfrac{x-5}4=\dfrac{y-4}1=\dfrac{z-5}3$ and $\dfrac{x+8}{12}=\dfrac{y+2}5=\dfrac{z+11}9$ respectively, such that $MN$ is the shortest distance between the given lines. Then $\overrightarrow{OM}\cdot\overrightarrow{ON}$ is equal to ______.

**Answer: 9** · key ✔

**Solution.** $\vec d_1\times\vec d_2=(4,1,3)\times(12,5,9)=(-6,0,8)$, so $\overrightarrow{MN}\parallel(-3,0,4)$. With $M=(5+4s,4+s,5+3s)$ and $N=(-8+12t,-2+5t,-11+9t)$, the $y$-component of $\overrightarrow{MN}$ is zero: $5t-s=6\Rightarrow s=5t-6$. Then $\overrightarrow{MN}=(11-8t,\,0,\,2-6t)\parallel(-3,0,4)\Rightarrow4(11-8t)=-3(2-6t)\Rightarrow t=1,\ s=-1$. So $M=(1,3,2)$, $N=(4,3,-2)$ and $\overrightarrow{OM}\cdot\overrightarrow{ON}=4+9-4=9$.

### M-TDG-06 — JEE Main 2024 · 30 Jan Shift 1 · Q79 · MCQ

Let $(\alpha,\beta,\gamma)$ be the foot of the perpendicular from the point $(1,2,3)$ on the line $\dfrac{x+3}5=\dfrac{y-1}2=\dfrac{z+4}3$. Then $19(\alpha+\beta+\gamma)$ is equal to

(1) 102  (2) 101  (3) 99  (4) 100

**Answer: (2)** · key ✔

**Solution.** A point on the line: $(-3+5t,\,1+2t,\,-4+3t)$. The vector from $(1,2,3)$ is $(5t-4,\,2t-1,\,3t-7)$; perpendicular to $(5,2,3)$: $25t-20+4t-2+9t-21=0\Rightarrow t=\tfrac{43}{38}$. Foot $=\left(\tfrac{101}{38},\tfrac{124}{38},-\tfrac{23}{38}\right)$, with coordinate sum $\dfrac{202}{38}$. So $19(\alpha+\beta+\gamma)=101$.

### M-TDG-07 — JEE Main 2024 · 30 Jan Shift 2 · Q79 · MCQ

Let $L_1:\vec r=(\hat i-\hat j+2\hat k)+\lambda(\hat i-\hat j+2\hat k)$, $L_2:\vec r=(\hat j-\hat k)+\mu(3\hat i+\hat j+p\hat k)$ and $L_3:\vec r=\delta(l\hat i+m\hat j+n\hat k)$ be three lines such that $L_1\perp L_2$ and $L_3$ is perpendicular to both $L_1$ and $L_2$. Then a point which lies on $L_3$ is

(1) $(-1,7,4)$  (2) $(-1,-7,4)$  (3) $(1,7,-4)$  (4) $(1,-7,4)$

**Answer: (1)** · key ✔

**Solution.** $L_1\perp L_2$: $(1,-1,2)\cdot(3,1,p)=3-1+2p=0\Rightarrow p=-1$. $L_3$ has direction $(1,-1,2)\times(3,1,-1)=\left((-1)(-1)-2(1),\ 2(3)-(1)(-1),\ 1(1)-(-1)(3)\right)=(-1,7,4)$. $L_3$ passes through the origin, so $\delta(-1,7,4)$ lies on it; at $\delta=1$ the point is $(-1,7,4)$.

### M-TDG-08 — JEE Main 2024 · 31 Jan Shift 1 · Q78 · MCQ

The distance of the point $Q(0,2,-2)$ from the line passing through $P(5,-4,3)$ and perpendicular to the lines $\vec r=-3\hat i+2\hat k+\lambda(2\hat i+3\hat j+5\hat k)$ and $\vec r=\hat i-2\hat j+\hat k+\mu(-\hat i+3\hat j+2\hat k)$ is

(1) $\sqrt{86}$  (2) $\sqrt{20}$  (3) $\sqrt{54}$  (4) $\sqrt{74}$

**Answer: (4)** · key ✔

**Solution.** The direction is $(2,3,5)\times(-1,3,2)=(-9,-9,9)\parallel(1,1,-1)$. $\overrightarrow{PQ}=(-5,6,-5)$ and $\overrightarrow{PQ}\times(1,1,-1)=(-1,-10,-11)$ with squared magnitude $222$; $|\vec d|^2=3$. Distance$^2=\dfrac{222}3=74$.

### M-TDG-09 — JEE Main 2024 · 31 Jan Shift 2 · Q78 · MCQ

Let $(\alpha,\beta,\gamma)$ be the mirror image of the point $(2,3,5)$ in the line $\dfrac{x-1}2=\dfrac{y-2}3=\dfrac{z-3}4$. Then $2\alpha+3\beta+4\gamma$ is equal to

(1) 32  (2) 33  (3) 31  (4) 34

**Answer: (2)** · key ✔

**Solution.** A point on the line: $(1+2t,2+3t,3+4t)$. Perpendicular from $(2,3,5)$: $(2t-1)2+(3t-1)3+(4t-2)4=0\Rightarrow29t=13$. Foot $=\left(\tfrac{55}{29},\tfrac{97}{29},\tfrac{139}{29}\right)$. Image $=2\cdot\text{foot}-(2,3,5)=\left(\tfrac{52}{29},\tfrac{107}{29},\tfrac{133}{29}\right)$. $2\alpha+3\beta+4\gamma=\dfrac{104+321+532}{29}=\dfrac{957}{29}=33$.

### M-TDG-10 — JEE Main 2024 · 31 Jan Shift 2 · Q90 · Numerical

A line passes through $A(4,-6,-2)$ and $B(16,-2,4)$. The point $P(a,b,c)$, where $a,b,c$ are non-negative integers, on the line $AB$ lies at a distance of $21$ units from the point $A$. The distance between the points $P(a,b,c)$ and $Q(4,-12,3)$ is equal to ______.

**Answer: 22** · key ✔

**Solution.** $\overrightarrow{AB}=(12,4,6)\parallel(6,2,3)$ with length $7$, so unit direction $\pm\tfrac17(6,2,3)$. At distance $21$: $P=A\pm3(6,2,3)$. $A+3(6,2,3)=(22,0,7)$ has non-negative integer coordinates, whereas $A-3(6,2,3)=(-14,-12,-11)$ does not. $PQ=\sqrt{18^2+12^2+4^2}=\sqrt{484}=22$.

### M-TDG-11 — JEE Advanced 2025 · Paper 1 · Q5 · Multiple correct

$L_1$ is the line of intersection of the planes $2x+3y+z=4$ and $x+2y+z=5$. $L_2$ passes through $P(2,-1,3)$ and is parallel to $L_1$. $M$ is the plane $2x+y-2z=6$; $L_2$ meets $M$ at $Q$ and $R$ is the foot of the perpendicular from $P$ to $M$. Which are TRUE?

(A) $PQ=9\sqrt3$  (B) $QR=15$  (C) the area of $\triangle PQR$ is $\tfrac32\sqrt{234}$  (D) the acute angle between $PQ$ and $PR$ is $\cos^{-1}\!\left(\tfrac1{2\sqrt3}\right)$

**Answer: (A), (C)** · official key ✔ (re-derived)

**Solution.** Direction of $L_1$: $(2,3,1)\times(1,2,1)=(1,-1,1)$. Points of $L_2$: $(2+t,-1-t,3+t)$. On $M$: $2(2+t)+(-1-t)-2(3+t)=6\Rightarrow-3-t=6\Rightarrow t=-9$, so $Q=(-7,8,-6)$ and $PQ=9\sqrt3$ (A true). The unit normal is $\tfrac13(2,1,-2)$; $P$ is at signed distance $\tfrac{6-(-3)}3=3$ from $M$, so $R=P+(2,1,-2)=(4,0,1)$, $PR=3$. $QR=\sqrt{11^2+8^2+7^2}=\sqrt{234}\ne15$ (B false). $PR\perp M$ so $\triangle PQR$ is right-angled at $R$: area $=\tfrac12\cdot3\cdot\sqrt{234}=\tfrac32\sqrt{234}$ (C true). $\cos\angle P=\dfrac{PR}{PQ}=\dfrac{3}{9\sqrt3}=\dfrac1{3\sqrt3}\ne\dfrac1{2\sqrt3}$ (D false).

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let the line $L$ pass through the point $(-3,5,2)$ and make equal angles with the positive coordinate axes. If the distance of $L$ from the point $(-2,r,1)$ is $\sqrt{\dfrac{14}3}$, then the sum of all possible values of $r$ is:

(1) 10  (2) 6  (3) 12  (4) 16

**Answer: (1)** · key (compiled)

**Solution.** Equal angles with the axes means direction $\vec d=(1,1,1)$. With $\vec{PQ}=(1,r-5,-1)$: $\vec{PQ}\times\vec d=(r-4,-2,6-r)$, so $|\vec{PQ}\times\vec d|^2=(r-4)^2+4+(6-r)^2=2r^2-20r+56$. Distance$^2=\dfrac{2r^2-20r+56}3=\dfrac{14}3\Rightarrow r^2-10r+21=0\Rightarrow r=3,7$. Sum $=10$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q2 · MCQ

Let the line $L_1$ be parallel to the vector $-3\hat i+2\hat j+4\hat k$ and pass through the point $(2,6,7)$, and the line $L_2$ be parallel to the vector $2\hat i+\hat j+3\hat k$ and pass through the point $(4,3,5)$. If the line $L_3$ is parallel to the vector $-3\hat i+5\hat j+16\hat k$ and intersects the lines $L_1$ and $L_2$ at the points $C$ and $D$, respectively, then $|\overrightarrow{CD}|^2$ is equal to:

(1) 89  (2) 312  (3) 171  (4) 290

**Answer: (4)** · key (compiled)

**Solution.** $C=(2-3\lambda_1,\ 6+2\lambda_1,\ 7+4\lambda_1)$ and $D=(4+2\lambda_2,\ 3+\lambda_2,\ 5+3\lambda_2)$. $\overrightarrow{CD}=(2+2\lambda_2+3\lambda_1,\ -3+\lambda_2-2\lambda_1,\ -2+3\lambda_2-4\lambda_1)\parallel(-3,5,16)$. The first two ratios give $13\lambda_2+9\lambda_1=-1$ and the last two give $\lambda_2-12\lambda_1=38$. Solving: $\lambda_1=-3$, $\lambda_2=2$, so $C=(11,0,-5)$, $D=(8,5,11)$ and $\overrightarrow{CD}=(-3,5,16)$. $|CD|^2=9+25+256=290$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q3 · MCQ

Let the direction cosines of two lines satisfy the equations $4l+m-n=0$ and $2mn+10nl+3lm=0$. Then the cosine of the acute angle between these lines is:

(1) $\dfrac{20}{3\sqrt{38}}$  (2) $\dfrac{10}{3\sqrt{38}}$  (3) $\dfrac{10}{7\sqrt{38}}$  (4) $\dfrac{10}{\sqrt{38}}$

**Answer: (2)** · key (compiled)

**Solution.** Substitute $n=4l+m$: $2m(4l+m)+10l(4l+m)+3lm=0\Rightarrow40l^2+21lm+2m^2=0$. With $t=l/m$: $40t^2+21t+2=0\Rightarrow t=-\tfrac18$ or $-\tfrac25$. $t=-\tfrac18$: $(l,m,n)\propto(-1,8,4)$; $t=-\tfrac25$: $(l,m,n)\propto(-2,5,-3)$. $\cos\theta=\dfrac{|2+40-12|}{\sqrt{81}\sqrt{38}}=\dfrac{30}{9\sqrt{38}}=\dfrac{10}{3\sqrt{38}}$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q4 · MCQ

The vertices $B$ and $C$ of a triangle $ABC$ lie on the line $\dfrac x1=\dfrac{1-y}{-2}=\dfrac{z-2}3$. The coordinates of $A$ and $B$ are $(1,6,3)$ and $(4,9,\alpha)$ respectively and $C$ is at a distance of 10 units from $B$. The area (in sq. units) of $\triangle ABC$ is:

(1) $20\sqrt{13}$  (2) $5\sqrt{13}$  (3) $15\sqrt{13}$  (4) $10\sqrt{13}$

**Answer: (2)** · key (compiled)

**Solution.** The line is $x=\dfrac{y-1}2=\dfrac{z-2}3$: through $(0,1,2)$ with direction $(1,2,3)$ ($|d|=\sqrt{14}$). $BC=10$ lies along it. Distance of $A(1,6,3)$ from the line: $\vec{v}=(1,5,1)$, $\vec v\times(1,2,3)=(13,-2,-3)$ with magnitude $\sqrt{182}$, so the distance is $\sqrt{182/14}=\sqrt{13}$. Area $=\tfrac12\cdot10\cdot\sqrt{13}=5\sqrt{13}$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q5 · MCQ

Let $Q(a,b,c)$ be the image of the point $P(3,2,1)$ in the line $\dfrac{x-1}1=\dfrac y2=\dfrac{z-1}1$. Then the distance of $Q$ from the line $\dfrac{x-9}3=\dfrac{y-9}2=\dfrac{z-5}{-2}$ is:

(1) 8  (2) 5  (3) 7  (4) 6

**Answer: (3)** · key (compiled)

**Solution.** Foot of the perpendicular from $P$: $M=(1+t,2t,1+t)$ with $(t-2,2t-2,t)\cdot(1,2,1)=6t-6=0\Rightarrow t=1$, $M=(2,2,2)$. $Q=2M-P=(1,2,3)$. Distance of $Q$ from the second line (through $(9,9,5)$, direction $(3,2,-2)$, $|d|=\sqrt{17}$): $\vec v=(-8,-7,-2)$, $\vec v\times(3,2,-2)=(18,-22,5)$ with magnitude $\sqrt{833}=7\sqrt{17}$. Distance $=\dfrac{7\sqrt{17}}{\sqrt{17}}=7$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q6 · Numerical

If the distance of the point $P(43,\alpha,\beta)$, $\beta<0$, from the line $\vec r=4\hat i-\hat k+\mu(2\hat i+3\hat k)$, $\mu\in\mathbb R$ along a line with direction ratios $3,-1,0$ is $13\sqrt{10}$, then $\alpha^2+\beta^2$ is equal to ______.

**Answer: 170** · key (compiled)

**Solution.** Moving from $P$ along $(3,-1,0)$ by parameter $s$: $(43+3s,\ \alpha-s,\ \beta)$. To reach the line (which has $y=0$) we need $s=\alpha$, and the distance is $|\alpha|\sqrt{10}=13\sqrt{10}\Rightarrow|\alpha|=13$. The point reached is $(43+3\alpha,0,\beta)=(4+2\mu,0,-1+3\mu)$. For $\alpha=13$: $\mu=39$, $\beta=116>0$ (rejected). For $\alpha=-13$: $\mu=0$, $\beta=-1<0$ ✓. $\alpha^2+\beta^2=169+1=170$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q7 · MCQ

The sum of all values of $\alpha$, for which the shortest distance between the lines $\dfrac{x+1}\alpha=\dfrac{y-2}{-1}=\dfrac{z-4}{-\alpha}$ and $\dfrac x\alpha=\dfrac{y-1}2=\dfrac{z-1}{2\alpha}$ is $\sqrt2$, is:

(1) 6  (2) 8  (3) $-8$  (4) $-6$

**Answer: (4)** · key (compiled)

**Solution.** $\vec a_1=(-1,2,4)$, $\vec b_1=(\alpha,-1,-\alpha)$; $\vec a_2=(0,1,1)$, $\vec b_2=(\alpha,2,2\alpha)$. $\vec b_1\times\vec b_2=(0,-3\alpha^2,3\alpha)$ with magnitude $3|\alpha|\sqrt{\alpha^2+1}$. $(\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)=(1,-1,-3)\cdot(0,-3\alpha^2,3\alpha)=3\alpha^2-9\alpha$. Shortest distance $=\dfrac{|3\alpha^2-9\alpha|}{3|\alpha|\sqrt{\alpha^2+1}}=\dfrac{|\alpha-3|}{\sqrt{\alpha^2+1}}=\sqrt2\Rightarrow(\alpha-3)^2=2(\alpha^2+1)\Rightarrow\alpha^2+6\alpha-7=0\Rightarrow\alpha=1,-7$. Sum $=-6$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q8 · MCQ

Let $L$ be the line $\dfrac{x+1}2=\dfrac{y+1}3=\dfrac{z+3}6$ and let $S$ be the set of all points $(a,b,c)$ on $L$, whose distance from the line $\dfrac{x+1}2=\dfrac{y+1}3=\dfrac{z-9}0$ along the line $L$ is 7. Then $\sum_{(a,b,c)\in S}(a+b+c)$ is equal to:

(1) 6  (2) 34  (3) 40  (4) 28

**Answer: (2)** · key (compiled)

**Solution.** Points of $L$: $(2k-1,3k-1,6k-3)$. The second line lies in the plane $z=9$, so $L$ meets it where $6k-3=9$, i.e. $k=2$: $M=(3,5,9)$ (and $x$, $y$ agree with the second line, $\lambda=2$). The direction $(2,3,6)$ has length 7, so a point of $L$ at distance 7 from $M$ along $L$ is $k=2\pm1$: $(1,2,3)$ and $(5,8,15)$. Sum of coordinates: $6+28=34$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q9 · MCQ

If the image of the point $P(1,2,a)$ in the line $\dfrac{x-6}3=\dfrac{y-7}2=\dfrac{7-z}2$ is $Q(5,b,c)$, then $a^2+b^2+c^2$ is equal to:

(1) 298  (2) 293  (3) 264  (4) 283

**Answer: (1)** · key (compiled)

**Solution.** The line passes through $(6,7,7)$ with direction $(3,2,-2)$. Foot $M=(6+3t,7+2t,7-2t)$; $\vec{PM}\cdot(3,2,-2)=0\Rightarrow3(5+3t)+2(5+2t)-2(7-2t-a)=0\Rightarrow17t+11+2a=0$. $Q=2M-P=(11+6t,\ 12+4t,\ 14-4t-a)$. $Q_x=5\Rightarrow t=-1$, so $a=3$, $b=8$, $c=14+4-3=15$. $a^2+b^2+c^2=9+64+225=298$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q10 · MCQ

Let $P(\alpha,\beta,\gamma)$ be the point on the line $\dfrac{x-1}2=\dfrac{y+1}{-3}=z$ at a distance $4\sqrt{14}$ from the point $(1,-1,0)$ and nearer to the origin. Then the shortest distance between the lines $\dfrac{x-\alpha}1=\dfrac{y-\beta}2=\dfrac{z-\gamma}3$ and $\dfrac{x+5}2=\dfrac{y-10}1=\dfrac{z-3}1$ is equal to:

(1) $4\sqrt{\dfrac75}$  (2) $2\sqrt{\dfrac74}$  (3) $7\sqrt{\dfrac54}$  (4) $4\sqrt{\dfrac57}$

**Answer: (1)** · key (compiled)

**Solution.** $P=(2\lambda+1,-3\lambda-1,\lambda)$ with $|\lambda|\sqrt{14}=4\sqrt{14}\Rightarrow\lambda=\pm4$. The point nearer to the origin is $\lambda=-4$: $P=(-7,11,-4)$ ($|OP|^2=186$ vs $266$). Now $\vec b_1\times\vec b_2=(1,2,3)\times(2,1,1)=(-1,5,-3)$ with magnitude $\sqrt{35}$, and $\vec a_2-\vec a_1=(-5,10,3)-(-7,11,-4)=(2,-1,7)$. Distance $=\dfrac{|-2-5-21|}{\sqrt{35}}=\dfrac{28}{\sqrt{35}}=\dfrac{4\sqrt{35}}5=4\sqrt{\dfrac75}$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q11 · Numerical

If the image of the point $P(a,2,a)$ in the line $\dfrac x2=\dfrac{y+a}1=\dfrac z1$ is $Q$ and the image of $Q$ in the line $\dfrac{x-2b}2=\dfrac{y-a}1=\dfrac{z+2b}{-5}$ is $P$, then $a+b$ is equal to ______.

**Answer: 3** · key (compiled)

**Solution.** The midpoint $M$ of $PQ$ lies on both lines, and $PQ$ is perpendicular to both directions, i.e. parallel to $(2,1,1)\times(2,1,-5)=(-6,12,0)\propto(1,-2,0)$. Take $M=(2\lambda,\lambda-a,\lambda)$ on the first line. $\vec{PM}=(2\lambda-a,\ \lambda-a-2,\ \lambda-a)\parallel(1,-2,0)$ forces $\lambda=a$, then $\vec{PM}=(a,-2,0)$, so $a=1$ and $M=(2,0,1)$. $M$ on the second line: $(2b+2\mu,\ 1+\mu,\ -2b-5\mu)=(2,0,1)\Rightarrow\mu=-1$, $b=2$ (check: $-4+5=1$ ✓). $a+b=3$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q12 · MCQ

Let $(\alpha,\beta,\gamma)$ be the co-ordinates of the foot of the perpendicular drawn from the point $(5,4,2)$ on the line $\vec r=(-\hat i+3\hat j+\hat k)+\lambda(2\hat i+3\hat j-\hat k)$. Then the length of the projection of the vector $\alpha\hat i+\beta\hat j+\gamma\hat k$ on the vector $6\hat i+2\hat j+3\hat k$ is:

(1) $\dfrac{15}7$  (2) 4  (3) $\dfrac{18}7$  (4) 3

**Answer: (3)** · key (compiled)

**Solution.** A point of the line is $Q=(-1+2\lambda,3+3\lambda,1-\lambda)$ and $\vec{PQ}=(-6+2\lambda,-1+3\lambda,-1-\lambda)$. $\vec{PQ}\cdot(2,3,-1)=14\lambda-14=0\Rightarrow\lambda=1$: foot $(1,6,0)$. Projection of $(1,6,0)$ on $(6,2,3)$: $\dfrac{6+12+0}{\sqrt{36+4+9}}=\dfrac{18}7$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q13 · MCQ

If the distances of the point $(1,2,a)$ from the line $\dfrac{x-1}1=\dfrac y2=\dfrac{z-1}1$ along the lines $L_1:\dfrac{x-1}3=\dfrac{y-2}4=\dfrac{z-a}b$ and $L_2:\dfrac{x-1}1=\dfrac{y-2}4=\dfrac{z-a}c$ are equal, then $a+b+c$ is equal to:

(1) 5  (2) 7  (3) 4  (4) 6

**Answer: (2)** · key (compiled)

**Solution.** Both $L_1$ and $L_2$ pass through $A(1,2,a)$. Points of the given line: $(1+s,2s,1+s)$. $L_1$: $A+\lambda(3,4,b)$ meets it when $3\lambda=s$ and $2+4\lambda=2s=6\lambda\Rightarrow\lambda=1$, $s=3$, and $a+b=1+s=4$ (point $(4,6,4)$). $L_2$: $A+\mu(1,4,c)$: $s=\mu$ and $2+4\mu=2\mu\Rightarrow\mu=-1$, $s=-1$, and $a-c=1+s=0$, so $c=a$ (point $(0,-2,0)$). Equal distances: $|\lambda|\sqrt{25+b^2}=|\mu|\sqrt{17+c^2}\Rightarrow25+b^2=17+c^2$. With $c=a=4-b$: $(4-b)^2-b^2=8\Rightarrow b=1$, $a=c=3$. $a+b+c=7$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q14 · MCQ

Let the lines $L_1:\vec r=\hat i+2\hat j+3\hat k+\lambda(2\hat i+3\hat j+4\hat k)$, $\lambda\in\mathbb R$ and $L_2:\vec r=(4\hat i+\hat j)+\mu(5\hat i+2\hat j+\hat k)$, $\mu\in\mathbb R$, intersect at the point $R$. Let $P$ and $Q$ be the points lying on lines $L_1$ and $L_2$, respectively, such that $|\overrightarrow{PR}|=\sqrt{29}$ and $|\overrightarrow{PQ}|=\sqrt{\dfrac{47}3}$. If the point $P$ lies in the first octant, then $27(QR)^2$ is equal to:

(1) 348  (2) 340  (3) 320  (4) 360

**Answer: (4)** · key (compiled)

**Solution.** Equate the lines: $1+2\lambda=4+5\mu$, $2+3\lambda=1+2\mu$, $3+4\lambda=\mu$ give $\lambda=\mu=-1$, so $R=(-1,-1,-1)$. $P=(1+2\lambda,2+3\lambda,3+4\lambda)$ has $\overrightarrow{PR}=(\lambda+1)(2,3,4)$ and $|PR|^2=29(\lambda+1)^2=29\Rightarrow\lambda=0$ (first octant) or $-2$ (not): $P=(1,2,3)$, $\overrightarrow{RP}=(2,3,4)$. Let $Q=R+s(5,2,1)$. $|PQ|^2=|(2,3,4)-s(5,2,1)|^2=29-40s+30s^2=\tfrac{47}3\Rightarrow9s^2-12s+4=0\Rightarrow s=\tfrac23$. $QR^2=30s^2=\tfrac{40}3$ and $27\,QR^2=360$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q15 · Numerical

Let a line $L$ passing through the point $P(1,1,1)$ be perpendicular to the lines $\dfrac{x-4}4=\dfrac{y-1}1=\dfrac{z-1}1$ and $\dfrac{x-17}1=\dfrac{y-71}1=\dfrac z0$. Let the line $L$ intersect the $yz$-plane at the point $Q$. Another line parallel to $L$ and passing through the point $S(1,0,-1)$ intersects the $yz$-plane at the point $R$. Then the square of the area of the parallelogram $PQRS$ is equal to ______.

**Answer: 6** · key (compiled)

**Solution.** Direction of $L$: $(4,1,1)\times(1,1,0)=(-1,1,3)$. $L:(1-t,1+t,1+3t)$ meets $x=0$ at $t=1$: $Q=(0,2,4)$. The parallel line through $S$: $(1-u,u,-1+3u)$ meets $x=0$ at $u=1$: $R=(0,1,2)$. In parallelogram $PQRS$, $\vec{PQ}=(-1,1,3)$ and $\vec{PS}=(0,-1,-2)$. $\vec{PQ}\times\vec{PS}=(1,-2,1)$, so the area is $\sqrt6$ and its square is $6$.

### § — JEE Main 2025 · Jan session · set Q2 · MCQ

The distance of the line $\dfrac{x-2}2=\dfrac{y-6}3=\dfrac{z-3}4$ from the point $(1,4,0)$ along the line $\dfrac x1=\dfrac{y-2}2=\dfrac{z+3}3$ is:

(1) $\sqrt{17}$  (2) $\sqrt{15}$  (3) $\sqrt{14}$  (4) $\sqrt{13}$

**Answer: (3)** · key (compiled)

**Solution.** Move from $(1,4,0)$ along the direction $(1,2,3)$: $(1+t,\,4+2t,\,3t)$. This lies on the first line when $\dfrac{t-1}2=\dfrac{2t-2}3=\dfrac{3t-3}4$, which holds only for $t=1$ (all three equal 0). The point is $(2,6,3)$ and the distance is $t\,|(1,2,3)|=\sqrt{14}$.

### § — JEE Main 2025 · Jan session · set Q3 · MCQ

If the square of the shortest distance between the lines $\dfrac{x-2}1=\dfrac{y-1}2=\dfrac{z+3}{-3}$ and $\dfrac{x+1}2=\dfrac{y+3}4=\dfrac{z+5}{-5}$ is $\dfrac mn$, where $m,n$ are coprime, then $m+n$ is equal to:

(1) 21  (2) 9  (3) 14  (4) 6

**Answer: (2)** · key (compiled)

**Solution.** $\vec d_1\times\vec d_2=(1,2,-3)\times(2,4,-5)=(2,-1,0)$. The vector between the points $(2,1,-3)$ and $(-1,-3,-5)$ is $(-3,-4,-2)$, whose dot product with the cross product is $-6+4=-2$. $d^2=\dfrac{4}{|(2,-1,0)|^2}=\dfrac45$, so $m+n=9$.

### § — JEE Main 2025 · Jan session · set Q4 · MCQ

If the image of the point $(4,4,3)$ in the line $\dfrac{x-1}2=\dfrac{y-2}1=\dfrac{z-1}3$ is $(\alpha,\beta,\gamma)$, then $\alpha+\beta+\gamma$ is equal to:

(1) 9  (2) 12  (3) 7  (4) 8

**Answer: (1)** · key (compiled)

**Solution.** A point of the line is $(1+2k,2+k,1+3k)$. Perpendicularity of the join to $(4,4,3)$ with the direction $(2,1,3)$: $2(2k-3)+(k-2)+3(3k-2)=0\Rightarrow14k=14$, $k=1$, so the foot is $(3,3,4)$. The image is $2(3,3,4)-(4,4,3)=(2,2,5)$, so $\alpha+\beta+\gamma=9$.

### § — JEE Main 2025 · Jan session · set Q6 · MCQ

Let a straight line $L$ pass through the point $P(2,-1,3)$ and be perpendicular to the lines $\dfrac{x-1}2=\dfrac{y+1}1=\dfrac{z-3}{-2}$ and $\dfrac{x-3}1=\dfrac{y-2}3=\dfrac{z+2}4$. If the line $L$ intersects the $yz$-plane at the point $Q$, then the distance between the points $P$ and $Q$ is:

(1) $\sqrt{10}$  (2) $2\sqrt3$  (3) 2  (4) 3

**Answer: (4)** · key (compiled)

**Solution.** The direction of $L$ is $(2,1,-2)\times(1,3,4)=(10,-10,5)\parallel(2,-2,1)$. Points of $L$: $(2+2s,-1-2s,3+s)$. On the $yz$-plane $x=0\Rightarrow s=-1$, so $Q=(0,1,2)$ and $PQ=\sqrt{4+4+1}=3$.

### § — JEE Main 2025 · Jan session · set Q7 · MCQ

Let $A(x,y,z)$ be a point in the $xy$-plane which is equidistant from the three points $(0,3,2)$, $(2,0,3)$ and $(0,0,1)$. Let $B=(1,4,-1)$ and $C=(2,0,-2)$. Then among the statements (S1): $\triangle ABC$ is an isosceles right-angled triangle, and (S2): the area of $\triangle ABC$ is $\dfrac{9\sqrt2}2$:

(1) both are true  (2) only (S2) is true  (3) only (S1) is true  (4) both are false

**Answer: (3)** · key (compiled)

**Solution.** $A=(x,y,0)$ with equal distances: $x^2+(y-3)^2+4=x^2+y^2+1\Rightarrow y=2$, and $(x-2)^2+y^2+9=x^2+y^2+1\Rightarrow x=3$. $A=(3,2,0)$, $\vec{AB}=(-2,2,-1)$, $\vec{AC}=(-1,-2,-2)$, both of length 3 and $\vec{AB}\cdot\vec{AC}=2-4+2=0$: an isosceles right triangle (S1 true). Its area is $\tfrac12\cdot3\cdot3=\tfrac92$, not $\tfrac{9\sqrt2}2$ (S2 false).

### § — JEE Main 2025 · Jan session · set Q8 · MCQ

Let $L_1:\dfrac{x-1}2=\dfrac{y-2}3=\dfrac{z-3}4$ and $L_2:\dfrac{x-2}3=\dfrac{y-4}4=\dfrac{z-5}5$ be two lines. Then which of the following points lies on the line of the shortest distance between $L_1$ and $L_2$?

(1) $\left(\tfrac{14}3,-3,\tfrac{22}3\right)$  (2) $\left(-\tfrac53,-7,1\right)$  (3) $\left(2,3,\tfrac13\right)$  (4) $\left(\tfrac83,-1,\tfrac13\right)$

**Answer: (1)** · key (compiled)

**Solution.** $\vec d_1\times\vec d_2=(-1,2,-1)$. Let the common perpendicular meet $L_1$ at $(1+2s,2+3s,3+4s)$ and $L_2$ at $(2+3t,4+4t,5+5t)$; their difference must be parallel to $(1,-2,1)$. Solving gives $s=\tfrac13$, $t=-\tfrac16$, so the foot on $L_1$ is $\left(\tfrac53,3,\tfrac{13}3\right)$ and the line of shortest distance is $\left(\tfrac53+u,\,3-2u,\,\tfrac{13}3+u\right)$. For $u=3$ this is $\left(\tfrac{14}3,-3,\tfrac{22}3\right)$.

### § — JEE Main 2025 · Jan session · set Q9 · MCQ

Let a line pass through two distinct points $P(-2,-1,3)$ and $Q$, and be parallel to the vector $3\hat i+2\hat j+2\hat k$. If the distance of the point $Q$ from the point $R(1,3,3)$ is 5, then the square of the area of $\triangle PQR$ is equal to:

(1) 148  (2) 136  (3) 144  (4) 140

**Answer: (2)** · key (compiled)

**Solution.** $Q=P+s(3,2,2)$ and $|QR|^2=(3-3s)^2+(4-2s)^2+(2s)^2=25\Rightarrow17s^2-34s=0$, so $s=2$ ($Q\ne P$) and $Q=(4,3,7)$. $\vec{PQ}=(6,4,4)$, $\vec{PR}=(3,4,0)$, $\vec{PQ}\times\vec{PR}=(-16,12,12)$, whose squared length is 544. (Area)$^2=\dfrac{544}4=136$.

### § — JEE Main 2025 · Jan session · set Q10 · MCQ

The perpendicular distance of the line $\dfrac{x-1}2=\dfrac{y+2}{-1}=\dfrac{z+3}2$ from the point $P(2,-10,1)$ is:

(1) 6  (2) $5\sqrt2$  (3) $4\sqrt3$  (4) $3\sqrt5$

**Answer: (4)** · key (compiled)

**Solution.** Take $A(1,-2,-3)$ on the line, $\vec d=(2,-1,2)$ with $|\vec d|=3$, and $\vec{AP}=(1,-8,4)$. $\vec{AP}\times\vec d=(-12,6,15)$, of magnitude $\sqrt{405}=9\sqrt5$. Distance $=\dfrac{9\sqrt5}3=3\sqrt5$.

### § — JEE Main 2025 · Jan session · set Q14 · MCQ

Let the line passing through the point $(-1,2,1)$ and parallel to the line $\dfrac{x-1}2=\dfrac{y+1}3=\dfrac z4$ intersect the line $\dfrac{x+2}3=\dfrac{y-3}2=\dfrac{z-4}1$ at the point $P$. Then the distance of $P$ from the point $Q(4,-5,1)$ is:

(1) 5  (2) $5\sqrt5$  (3) $5\sqrt6$  (4) 10

**Answer: (2)** · key (compiled)

**Solution.** Equate $(-1+2a,2+3a,1+4a)=(-2+3b,3+2b,4+b)$: $2a-3b=-1$ and $3a-2b=1$ give $a=b=1$; $P=(1,5,5)$ (the third coordinates agree: $5=5$). $PQ=\sqrt{9+100+16}=5\sqrt5$.

### § — JEE Main 2025 · Jan session · set Q17 · MCQ

Let $\vec a=\hat i+2\hat j+\hat k$ and $\vec b=2\hat i+7\hat j+3\hat k$. Let $L_1:\vec r=(-\hat i+2\hat j+\hat k)+\lambda\vec a$ and $L_2:\vec r=(\hat j+\hat k)+\mu\vec b$ be two lines. If the line $L_3$ passes through the point of intersection of $L_1$ and $L_2$ and is parallel to $\vec a+\vec b$, then $L_3$ passes through the point:

(1) $(5,17,4)$  (2) $(2,8,5)$  (3) $(8,26,12)$  (4) $(-1,-1,1)$

**Answer: (3)** · key (compiled)

**Solution.** Equating coordinates: $-1+\lambda=2\mu$, $2+2\lambda=1+7\mu$, $1+\lambda=1+3\mu$. From the first and third, $\lambda=3\mu$ and $\mu=1$, $\lambda=3$ (the second equation holds: $8=8$). The intersection point is $(2,8,4)$. $\vec a+\vec b=(3,9,4)$, so $L_3$: $(2+3t,8+9t,4+4t)$, which at $t=2$ gives $(8,26,12)$.

### § — JEE Main 2025 · Jan session · set Q19 · MCQ

Let $P$ be the foot of the perpendicular from the point $(1,2,2)$ on the line $L:\dfrac{x-1}1=\dfrac{y+1}{-1}=\dfrac{z-2}2$. Let the line $\vec r=(-\hat i+\hat j-2\hat k)+\lambda(\hat i-\hat j+\hat k)$, $\lambda\in\mathbb R$, intersect the line $L$ at $Q$. Then $2(PQ)^2$ is equal to:

(1) 25  (2) 19  (3) 29  (4) 27

**Answer: (4)** · key (compiled)

**Solution.** Points of $L$: $(1+m,-1-m,2+2m)$. For the foot: $(m,-3-m,2m)\cdot(1,-1,2)=6m+3=0\Rightarrow m=-\tfrac12$, $P=\left(\tfrac12,-\tfrac12,1\right)$. Intersection with the second line: $-1+\lambda=1+m$, $-2+\lambda=2+2m$ give $m=-2$, $\lambda=0$, so $Q=(-1,1,-2)$ (the second coordinate also matches). $\vec{PQ}=\left(-\tfrac32,\tfrac32,-3\right)$ and $PQ^2=\tfrac{27}2$, so $2PQ^2=27$.

### § — JEE Main 2025 · Apr session · set Q2 · MCQ

The line $L_1$ is parallel to the vector $\vec a=-3\hat i+2\hat j+4\hat k$ and passes through the point $(7,6,2)$, and the line $L_2$ is parallel to the vector $\vec b=2\hat i+\hat j+3\hat k$ and passes through the point $(5,3,4)$. The shortest distance between the lines $L_1$ and $L_2$ is:

(1) $\dfrac{23}{\sqrt{38}}$  (2) $\dfrac{21}{\sqrt{57}}$  (3) $\dfrac{23}{\sqrt{57}}$  (4) $\dfrac{21}{\sqrt{38}}$

**Answer: (1)** · key (compiled)

**Solution.** $\vec a\times\vec b=(2\cdot3-4\cdot1,\ 4\cdot2-(-3)\cdot3,\ -3\cdot1-2\cdot2)=(2,17,-7)$, of magnitude $\sqrt{342}=3\sqrt{38}$. The vector between the given points is $(-2,-3,2)$ and its dot product with the cross product is $-4-51-14=-69$. Distance $=\dfrac{69}{3\sqrt{38}}=\dfrac{23}{\sqrt{38}}$.

### § — JEE Main 2025 · Apr session · set Q3 · MCQ

Let the shortest distance between the lines $\dfrac{x-3}3=\dfrac{y-\alpha}{-1}=\dfrac{z-3}1$ and $\dfrac{x+3}{-3}=\dfrac{y+7}2=\dfrac{z-\beta}4$ be $3\sqrt{30}$. Then the positive value of $5\alpha+\beta$ is:

(1) 42  (2) 46  (3) 48  (4) 40

**Answer: (2)** · key (compiled)

**Solution.** $\vec d_1\times\vec d_2=(3,-1,1)\times(-3,2,4)=(-6,-15,3)$, of magnitude $3\sqrt{30}$. The vector between the points $(3,\alpha,3)$ and $(-3,-7,\beta)$ is $(-6,-7-\alpha,\beta-3)$, and its dot product with the cross product is $36+15(7+\alpha)+3\beta-9=132+15\alpha+3\beta$. Setting the distance $=3\sqrt{30}$: $|132+15\alpha+3\beta|=270$, so $15\alpha+3\beta=138$ or $-402$, i.e. $5\alpha+\beta=46$ or $-134$. The positive value is 46.

### § — JEE Main 2025 · Apr session · set Q6 · MCQ

If the image of the point $P(1,0,3)$ in the line joining the points $A(4,7,1)$ and $B(3,5,3)$ is $Q(\alpha,\beta,\gamma)$, then $\alpha+\beta+\gamma$ is equal to:

(1) $\tfrac{47}3$  (2) $\tfrac{46}3$  (3) 18  (4) 13

**Answer: (2)** · key (compiled)

**Solution.** Direction $\vec{AB}=(-1,-2,2)$; a point of the line is $(4-k,7-2k,1+2k)$. Perpendicularity: $(3-k,7-2k,-2+2k)\cdot(-1,-2,2)=9k-21=0\Rightarrow k=\tfrac73$, so the foot is $\left(\tfrac53,\tfrac73,\tfrac{17}3\right)$. The image is $2\cdot\text{foot}-P=\left(\tfrac73,\tfrac{14}3,\tfrac{25}3\right)$ with sum $\tfrac{46}3$.

### § — JEE Main 2025 · Apr session · set Q9 · MCQ

The distance of the point $(7,10,11)$ from the line $\dfrac{x-4}1=\dfrac{y-4}0=\dfrac{z-2}3$ along the line $\dfrac{x-9}2=\dfrac{y-13}3=\dfrac{z-17}6$ is:

(1) 18  (2) 14  (3) 12  (4) 16

**Answer: (2)** · key (compiled)

**Solution.** Along the direction $(2,3,6)$ (length 7): $(7+2t,10+3t,11+6t)$. It lies on the given line when $y=4$, i.e. $t=-2$, giving $(3,4,-1)$ (check: $x-4=-1$, $(z-2)/3=-1$). The distance is $|t|\cdot7=14$.

### § — JEE Main 2025 · Apr session · set Q10 · MCQ

Let $A$ and $B$ be two distinct points on the line $L:\dfrac{x-6}3=\dfrac{y-7}2=\dfrac{z-7}{-2}$. Both $A$ and $B$ are at a distance $2\sqrt{17}$ from the foot of the perpendicular drawn from the point $(1,2,3)$ on the line $L$. If $O$ is the origin, then $\vec{OA}\cdot\vec{OB}$ is equal to:

(1) 49  (2) 47  (3) 21  (4) 62

**Answer: (2)** · key (compiled)

**Solution.** Foot: $(6+3k,7+2k,7-2k)$ with $(5+3k,5+2k,4-2k)\cdot(3,2,-2)=17+17k=0$, $k=-1$, so $F=(3,5,9)$. Since $|\vec d|=\sqrt{17}$, $A$ and $B$ correspond to $k=-1\pm2$: $A=(9,9,5)$ and $B=(-3,1,13)$. $\vec{OA}\cdot\vec{OB}=-27+9+65=47$.

### § — JEE Main 2025 · Apr session · set Q13 · MCQ

Let the line $L$ pass through $(1,1,1)$ and intersect the lines $\dfrac{x-1}2=\dfrac{y+1}3=\dfrac{z-1}4$ and $\dfrac{x-3}1=\dfrac{y-4}2=\dfrac z1$. Then which of the following points lies on the line $L$?

(1) $(4,22,7)$  (2) $(5,4,3)$  (3) $(10,-29,-50)$  (4) $(7,15,13)$

**Answer: (4)** · key (compiled)

**Solution.** The plane through $(1,1,1)$ and the first line contains $(1,-1,1)$ and has direction $(2,3,4)$; its equation is $z=2x-1$. The second line $(3+t,4+2t,t)$ meets it when $t=5+2t$, i.e. $t=-5$: the point $(-2,-6,-5)$. $L$ joins $(1,1,1)$ and $(-2,-6,-5)$: direction $(3,7,6)$, and $(1,1,1)+2(3,7,6)=(7,15,13)$.

### § — JEE Main 2025 · Apr session · set Q14 · MCQ

Consider the lines $L_1:x-1=y-2=z$ and $L_2:x-2=y=z-1$. Let the feet of the perpendiculars from the point $P(5,1,-3)$ on the lines $L_1$ and $L_2$ be $Q$ and $R$ respectively. If the area of the triangle $PQR$ is $A$, then $4A^2$ is equal to:

(1) 139  (2) 147  (3) 151  (4) 143

**Answer: (2)** · key (compiled)

**Solution.** Both lines have direction $(1,1,1)$. On $L_1$: $(4-k,-1-k,-3-k)\cdot(1,1,1)=-3k=0$, so $Q=(1,2,0)$. On $L_2$: $(3-m,1-m,-4-m)\cdot(1,1,1)=-3m=0$, so $R=(2,0,1)$. $\vec{PQ}=(-4,1,3)$, $\vec{PR}=(-3,-1,4)$, cross product $(7,7,7)$ with squared length 147. $A=\tfrac12\sqrt{147}$, so $4A^2=147$.

### § — JEE Main 2025 · Apr session · set Q15 · MCQ

Let the values of $\lambda$ for which the shortest distance between the lines $\dfrac{x-1}2=\dfrac{y-2}3=\dfrac{z-3}4$ and $\dfrac{x-\lambda}3=\dfrac{y-4}4=\dfrac{z-5}5$ is $\dfrac1{\sqrt6}$ be $\lambda_1$ and $\lambda_2$. Then the radius of the circle passing through the points $(0,0)$, $(\lambda_1,\lambda_2)$ and $(\lambda_2,\lambda_1)$ is:

(1) $\dfrac{5\sqrt2}3$  (2) 4  (3) $\dfrac{\sqrt2}3$  (4) 3

**Answer: (1)** · key (compiled)

**Solution.** $\vec d_1\times\vec d_2=(-1,2,-1)$, magnitude $\sqrt6$; the vector between points is $(\lambda-1,2,2)$ and its dot product with the cross product is $3-\lambda$. $\dfrac{|3-\lambda|}{\sqrt6}=\dfrac1{\sqrt6}\Rightarrow\lambda=2$ or $4$. For the circle through $(0,0)$, $(2,4)$, $(4,2)$ with centre $(h,k)$: $2h+4k=10$ and $4h+2k=10$, so the centre is $\left(\tfrac53,\tfrac53\right)$ and the radius is $\sqrt2\cdot\tfrac53=\dfrac{5\sqrt2}3$.

