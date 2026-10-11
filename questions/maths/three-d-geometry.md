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

