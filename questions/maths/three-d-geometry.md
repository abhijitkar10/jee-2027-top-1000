# 3D Geometry

> Theory: [../../theory/maths/three-d-geometry.md](../../theory/maths/three-d-geometry.md)

### M-TDG-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let the line $L$ pass through the point $(-3,5,2)$ and make equal angles with the positive coordinate axes. If the distance of $L$ from the point $(-2,r,1)$ is $\sqrt{\dfrac{14}3}$, then the sum of all possible values of $r$ is:

(1) 10  (2) 6  (3) 12  (4) 16

**Answer: (1)** · key (compiled)

**Solution.** Equal angles with the axes means direction $\vec d=(1,1,1)$. With $\vec{PQ}=(1,r-5,-1)$: $\vec{PQ}\times\vec d=(r-4,-2,6-r)$, so $|\vec{PQ}\times\vec d|^2=(r-4)^2+4+(6-r)^2=2r^2-20r+56$. Distance$^2=\dfrac{2r^2-20r+56}3=\dfrac{14}3\Rightarrow r^2-10r+21=0\Rightarrow r=3,7$. Sum $=10$.

### M-TDG-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q3 · MCQ

Let the direction cosines of two lines satisfy the equations $4l+m-n=0$ and $2mn+10nl+3lm=0$. Then the cosine of the acute angle between these lines is:

(1) $\dfrac{20}{3\sqrt{38}}$  (2) $\dfrac{10}{3\sqrt{38}}$  (3) $\dfrac{10}{7\sqrt{38}}$  (4) $\dfrac{10}{\sqrt{38}}$

**Answer: (2)** · key (compiled)

**Solution.** Substitute $n=4l+m$: $2m(4l+m)+10l(4l+m)+3lm=0\Rightarrow40l^2+21lm+2m^2=0$. With $t=l/m$: $40t^2+21t+2=0\Rightarrow t=-\tfrac18$ or $-\tfrac25$. $t=-\tfrac18$: $(l,m,n)\propto(-1,8,4)$; $t=-\tfrac25$: $(l,m,n)\propto(-2,5,-3)$. $\cos\theta=\dfrac{|2+40-12|}{\sqrt{81}\sqrt{38}}=\dfrac{30}{9\sqrt{38}}=\dfrac{10}{3\sqrt{38}}$.

### M-TDG-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q5 · MCQ

Let $Q(a,b,c)$ be the image of the point $P(3,2,1)$ in the line $\dfrac{x-1}1=\dfrac y2=\dfrac{z-1}1$. Then the distance of $Q$ from the line $\dfrac{x-9}3=\dfrac{y-9}2=\dfrac{z-5}{-2}$ is:

(1) 8  (2) 5  (3) 7  (4) 6

**Answer: (3)** · key (compiled)

**Solution.** Foot of the perpendicular from $P$: $M=(1+t,2t,1+t)$ with $(t-2,2t-2,t)\cdot(1,2,1)=6t-6=0\Rightarrow t=1$, $M=(2,2,2)$. $Q=2M-P=(1,2,3)$. Distance of $Q$ from the second line (through $(9,9,5)$, direction $(3,2,-2)$, $|d|=\sqrt{17}$): $\vec v=(-8,-7,-2)$, $\vec v\times(3,2,-2)=(18,-22,5)$ with magnitude $\sqrt{833}=7\sqrt{17}$. Distance $=\dfrac{7\sqrt{17}}{\sqrt{17}}=7$.

### M-TDG-04 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q7 · MCQ

The sum of all values of $\alpha$, for which the shortest distance between the lines $\dfrac{x+1}\alpha=\dfrac{y-2}{-1}=\dfrac{z-4}{-\alpha}$ and $\dfrac x\alpha=\dfrac{y-1}2=\dfrac{z-1}{2\alpha}$ is $\sqrt2$, is:

(1) 6  (2) 8  (3) $-8$  (4) $-6$

**Answer: (4)** · key (compiled)

**Solution.** $\vec a_1=(-1,2,4)$, $\vec b_1=(\alpha,-1,-\alpha)$; $\vec a_2=(0,1,1)$, $\vec b_2=(\alpha,2,2\alpha)$. $\vec b_1\times\vec b_2=(0,-3\alpha^2,3\alpha)$ with magnitude $3|\alpha|\sqrt{\alpha^2+1}$. $(\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)=(1,-1,-3)\cdot(0,-3\alpha^2,3\alpha)=3\alpha^2-9\alpha$. Shortest distance $=\dfrac{|3\alpha^2-9\alpha|}{3|\alpha|\sqrt{\alpha^2+1}}=\dfrac{|\alpha-3|}{\sqrt{\alpha^2+1}}=\sqrt2\Rightarrow(\alpha-3)^2=2(\alpha^2+1)\Rightarrow\alpha^2+6\alpha-7=0\Rightarrow\alpha=1,-7$. Sum $=-6$.

### M-TDG-05 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q8 · MCQ

Let $L$ be the line $\dfrac{x+1}2=\dfrac{y+1}3=\dfrac{z+3}6$ and let $S$ be the set of all points $(a,b,c)$ on $L$, whose distance from the line $\dfrac{x+1}2=\dfrac{y+1}3=\dfrac{z-9}0$ along the line $L$ is 7. Then $\sum_{(a,b,c)\in S}(a+b+c)$ is equal to:

(1) 6  (2) 34  (3) 40  (4) 28

**Answer: (2)** · key (compiled)

**Solution.** Points of $L$: $(2k-1,3k-1,6k-3)$. The second line lies in the plane $z=9$, so $L$ meets it where $6k-3=9$, i.e. $k=2$: $M=(3,5,9)$ (and $x$, $y$ agree with the second line, $\lambda=2$). The direction $(2,3,6)$ has length 7, so a point of $L$ at distance 7 from $M$ along $L$ is $k=2\pm1$: $(1,2,3)$ and $(5,8,15)$. Sum of coordinates: $6+28=34$.

### M-TDG-06 · A — JEE Main 2026 · 22 Jan Shift 1 · set Q9 · MCQ

If the image of the point $P(1,2,a)$ in the line $\dfrac{x-6}3=\dfrac{y-7}2=\dfrac{7-z}2$ is $Q(5,b,c)$, then $a^2+b^2+c^2$ is equal to:

(1) 298  (2) 293  (3) 264  (4) 283

**Answer: (1)** · key (compiled)

**Solution.** The line passes through $(6,7,7)$ with direction $(3,2,-2)$. Foot $M=(6+3t,7+2t,7-2t)$; $\vec{PM}\cdot(3,2,-2)=0\Rightarrow3(5+3t)+2(5+2t)-2(7-2t-a)=0\Rightarrow17t+11+2a=0$. $Q=2M-P=(11+6t,\ 12+4t,\ 14-4t-a)$. $Q_x=5\Rightarrow t=-1$, so $a=3$, $b=8$, $c=14+4-3=15$. $a^2+b^2+c^2=9+64+225=298$.

### M-TDG-07 · A — JEE Main 2026 · 23 Jan Shift 2 · set Q11 · Numerical

If the image of the point $P(a,2,a)$ in the line $\dfrac x2=\dfrac{y+a}1=\dfrac z1$ is $Q$ and the image of $Q$ in the line $\dfrac{x-2b}2=\dfrac{y-a}1=\dfrac{z+2b}{-5}$ is $P$, then $a+b$ is equal to ______.

**Answer: 3** · key (compiled)

**Solution.** The midpoint $M$ of $PQ$ lies on both lines, and $PQ$ is perpendicular to both directions, i.e. parallel to $(2,1,1)\times(2,1,-5)=(-6,12,0)\propto(1,-2,0)$. Take $M=(2\lambda,\lambda-a,\lambda)$ on the first line. $\vec{PM}=(2\lambda-a,\ \lambda-a-2,\ \lambda-a)\parallel(1,-2,0)$ forces $\lambda=a$, then $\vec{PM}=(a,-2,0)$, so $a=1$ and $M=(2,0,1)$. $M$ on the second line: $(2b+2\mu,\ 1+\mu,\ -2b-5\mu)=(2,0,1)\Rightarrow\mu=-1$, $b=2$ (check: $-4+5=1$ ✓). $a+b=3$.

### M-TDG-08 · A — JEE Main 2026 · 21 Jan Shift 1 · set Q12 · MCQ

Let $(\alpha,\beta,\gamma)$ be the co-ordinates of the foot of the perpendicular drawn from the point $(5,4,2)$ on the line $\vec r=(-\hat i+3\hat j+\hat k)+\lambda(2\hat i+3\hat j-\hat k)$. Then the length of the projection of the vector $\alpha\hat i+\beta\hat j+\gamma\hat k$ on the vector $6\hat i+2\hat j+3\hat k$ is:

(1) $\dfrac{15}7$  (2) 4  (3) $\dfrac{18}7$  (4) 3

**Answer: (3)** · key (compiled)

**Solution.** A point of the line is $Q=(-1+2\lambda,3+3\lambda,1-\lambda)$ and $\vec{PQ}=(-6+2\lambda,-1+3\lambda,-1-\lambda)$. $\vec{PQ}\cdot(2,3,-1)=14\lambda-14=0\Rightarrow\lambda=1$: foot $(1,6,0)$. Projection of $(1,6,0)$ on $(6,2,3)$: $\dfrac{6+12+0}{\sqrt{36+4+9}}=\dfrac{18}7$.

### M-TDG-09 · A — JEE Main 2026 · 24 Jan Shift 1 · set Q14 · MCQ

Let the lines $L_1:\vec r=\hat i+2\hat j+3\hat k+\lambda(2\hat i+3\hat j+4\hat k)$, $\lambda\in\mathbb R$ and $L_2:\vec r=(4\hat i+\hat j)+\mu(5\hat i+2\hat j+\hat k)$, $\mu\in\mathbb R$, intersect at the point $R$. Let $P$ and $Q$ be the points lying on lines $L_1$ and $L_2$, respectively, such that $|\overrightarrow{PR}|=\sqrt{29}$ and $|\overrightarrow{PQ}|=\sqrt{\dfrac{47}3}$. If the point $P$ lies in the first octant, then $27(QR)^2$ is equal to:

(1) 348  (2) 340  (3) 320  (4) 360

**Answer: (4)** · key (compiled)

**Solution.** Equate the lines: $1+2\lambda=4+5\mu$, $2+3\lambda=1+2\mu$, $3+4\lambda=\mu$ give $\lambda=\mu=-1$, so $R=(-1,-1,-1)$. $P=(1+2\lambda,2+3\lambda,3+4\lambda)$ has $\overrightarrow{PR}=(\lambda+1)(2,3,4)$ and $|PR|^2=29(\lambda+1)^2=29\Rightarrow\lambda=0$ (first octant) or $-2$ (not): $P=(1,2,3)$, $\overrightarrow{RP}=(2,3,4)$. Let $Q=R+s(5,2,1)$. $|PQ|^2=|(2,3,4)-s(5,2,1)|^2=29-40s+30s^2=\tfrac{47}3\Rightarrow9s^2-12s+4=0\Rightarrow s=\tfrac23$. $QR^2=30s^2=\tfrac{40}3$ and $27\,QR^2=360$.

### M-TDG-10 · A — JEE Advanced 2025 · Paper 1 · Q5 · Multiple correct

$L_1$ is the line of intersection of the planes $2x+3y+z=4$ and $x+2y+z=5$. $L_2$ passes through $P(2,-1,3)$ and is parallel to $L_1$. $M$ is the plane $2x+y-2z=6$; $L_2$ meets $M$ at $Q$ and $R$ is the foot of the perpendicular from $P$ to $M$. Which are TRUE?

(A) $PQ=9\sqrt3$  (B) $QR=15$  (C) the area of $\triangle PQR$ is $\tfrac32\sqrt{234}$  (D) the acute angle between $PQ$ and $PR$ is $\cos^{-1}\!\left(\tfrac1{2\sqrt3}\right)$

**Answer: (A), (C)** · official key ✔ (re-derived)

**Solution.** Direction of $L_1$: $(2,3,1)\times(1,2,1)=(1,-1,1)$. Points of $L_2$: $(2+t,-1-t,3+t)$. On $M$: $2(2+t)+(-1-t)-2(3+t)=6\Rightarrow-3-t=6\Rightarrow t=-9$, so $Q=(-7,8,-6)$ and $PQ=9\sqrt3$ (A true). The unit normal is $\tfrac13(2,1,-2)$; $P$ is at signed distance $\tfrac{6-(-3)}3=3$ from $M$, so $R=P+(2,1,-2)=(4,0,1)$, $PR=3$. $QR=\sqrt{11^2+8^2+7^2}=\sqrt{234}\ne15$ (B false). $PR\perp M$ so $\triangle PQR$ is right-angled at $R$: area $=\tfrac12\cdot3\cdot\sqrt{234}=\tfrac32\sqrt{234}$ (C true). $\cos\angle P=\dfrac{PR}{PQ}=\dfrac{3}{9\sqrt3}=\dfrac1{3\sqrt3}\ne\dfrac1{2\sqrt3}$ (D false).

### M-TDG-11 · A — JEE Main 2025 · Jan session · set Q2 · MCQ

The distance of the line $\dfrac{x-2}2=\dfrac{y-6}3=\dfrac{z-3}4$ from the point $(1,4,0)$ along the line $\dfrac x1=\dfrac{y-2}2=\dfrac{z+3}3$ is:

(1) $\sqrt{17}$  (2) $\sqrt{15}$  (3) $\sqrt{14}$  (4) $\sqrt{13}$

**Answer: (3)** · key (compiled)

**Solution.** Move from $(1,4,0)$ along the direction $(1,2,3)$: $(1+t,\,4+2t,\,3t)$. This lies on the first line when $\dfrac{t-1}2=\dfrac{2t-2}3=\dfrac{3t-3}4$, which holds only for $t=1$ (all three equal 0). The point is $(2,6,3)$ and the distance is $t\,|(1,2,3)|=\sqrt{14}$.

### M-TDG-12 · A — JEE Main 2025 · Jan session · set Q3 · MCQ

If the square of the shortest distance between the lines $\dfrac{x-2}1=\dfrac{y-1}2=\dfrac{z+3}{-3}$ and $\dfrac{x+1}2=\dfrac{y+3}4=\dfrac{z+5}{-5}$ is $\dfrac mn$, where $m,n$ are coprime, then $m+n$ is equal to:

(1) 21  (2) 9  (3) 14  (4) 6

**Answer: (2)** · key (compiled)

**Solution.** $\vec d_1\times\vec d_2=(1,2,-3)\times(2,4,-5)=(2,-1,0)$. The vector between the points $(2,1,-3)$ and $(-1,-3,-5)$ is $(-3,-4,-2)$, whose dot product with the cross product is $-6+4=-2$. $d^2=\dfrac{4}{|(2,-1,0)|^2}=\dfrac45$, so $m+n=9$.

### M-TDG-13 · A — JEE Main 2025 · Jan session · set Q4 · MCQ

If the image of the point $(4,4,3)$ in the line $\dfrac{x-1}2=\dfrac{y-2}1=\dfrac{z-1}3$ is $(\alpha,\beta,\gamma)$, then $\alpha+\beta+\gamma$ is equal to:

(1) 9  (2) 12  (3) 7  (4) 8

**Answer: (1)** · key (compiled)

**Solution.** A point of the line is $(1+2k,2+k,1+3k)$. Perpendicularity of the join to $(4,4,3)$ with the direction $(2,1,3)$: $2(2k-3)+(k-2)+3(3k-2)=0\Rightarrow14k=14$, $k=1$, so the foot is $(3,3,4)$. The image is $2(3,3,4)-(4,4,3)=(2,2,5)$, so $\alpha+\beta+\gamma=9$.

### M-TDG-14 · A — JEE Main 2025 · Apr session · set Q2 · MCQ

The line $L_1$ is parallel to the vector $\vec a=-3\hat i+2\hat j+4\hat k$ and passes through the point $(7,6,2)$, and the line $L_2$ is parallel to the vector $\vec b=2\hat i+\hat j+3\hat k$ and passes through the point $(5,3,4)$. The shortest distance between the lines $L_1$ and $L_2$ is:

(1) $\dfrac{23}{\sqrt{38}}$  (2) $\dfrac{21}{\sqrt{57}}$  (3) $\dfrac{23}{\sqrt{57}}$  (4) $\dfrac{21}{\sqrt{38}}$

**Answer: (1)** · key (compiled)

**Solution.** $\vec a\times\vec b=(2\cdot3-4\cdot1,\ 4\cdot2-(-3)\cdot3,\ -3\cdot1-2\cdot2)=(2,17,-7)$, of magnitude $\sqrt{342}=3\sqrt{38}$. The vector between the given points is $(-2,-3,2)$ and its dot product with the cross product is $-4-51-14=-69$. Distance $=\dfrac{69}{3\sqrt{38}}=\dfrac{23}{\sqrt{38}}$.

### M-TDG-15 · A — JEE Main 2025 · Apr session · set Q3 · MCQ

Let the shortest distance between the lines $\dfrac{x-3}3=\dfrac{y-\alpha}{-1}=\dfrac{z-3}1$ and $\dfrac{x+3}{-3}=\dfrac{y+7}2=\dfrac{z-\beta}4$ be $3\sqrt{30}$. Then the positive value of $5\alpha+\beta$ is:

(1) 42  (2) 46  (3) 48  (4) 40

**Answer: (2)** · key (compiled)

**Solution.** $\vec d_1\times\vec d_2=(3,-1,1)\times(-3,2,4)=(-6,-15,3)$, of magnitude $3\sqrt{30}$. The vector between the points $(3,\alpha,3)$ and $(-3,-7,\beta)$ is $(-6,-7-\alpha,\beta-3)$, and its dot product with the cross product is $36+15(7+\alpha)+3\beta-9=132+15\alpha+3\beta$. Setting the distance $=3\sqrt{30}$: $|132+15\alpha+3\beta|=270$, so $15\alpha+3\beta=138$ or $-402$, i.e. $5\alpha+\beta=46$ or $-134$. The positive value is 46.

### M-TDG-16 · A — JEE Main 2025 · Apr session · set Q6 · MCQ

If the image of the point $P(1,0,3)$ in the line joining the points $A(4,7,1)$ and $B(3,5,3)$ is $Q(\alpha,\beta,\gamma)$, then $\alpha+\beta+\gamma$ is equal to:

(1) $\tfrac{47}3$  (2) $\tfrac{46}3$  (3) 18  (4) 13

**Answer: (2)** · key (compiled)

**Solution.** Direction $\vec{AB}=(-1,-2,2)$; a point of the line is $(4-k,7-2k,1+2k)$. Perpendicularity: $(3-k,7-2k,-2+2k)\cdot(-1,-2,2)=9k-21=0\Rightarrow k=\tfrac73$, so the foot is $\left(\tfrac53,\tfrac73,\tfrac{17}3\right)$. The image is $2\cdot\text{foot}-P=\left(\tfrac73,\tfrac{14}3,\tfrac{25}3\right)$ with sum $\tfrac{46}3$.

### M-TDG-17 · A — JEE Main 2024 · 29 Jan Shift 1 · Q79 · MCQ

Let $PQR$ be a triangle with $R(-1,4,2)$. Suppose $M(2,1,2)$ is the midpoint of $PQ$. The distance of the centroid of $\triangle PQR$ from the point of intersection of the lines $\dfrac{x-2}0=\dfrac y2=\dfrac{z+3}{-1}$ and $\dfrac{x-1}1=\dfrac{y+3}{-3}=\dfrac{z+1}1$ is

(1) 69  (2) 9  (3) $\sqrt{69}$  (4) $\sqrt{99}$

**Answer: (3)** · key ✔

**Solution.** Lines: $(2,2s,-3-s)$ and $(1+t,-3-3t,-1+t)$. From $x$: $t=1$; from $y$: $2s=-6\Rightarrow s=-3$; check $z$: $-3+3=0=-1+1$ ✓. Intersection $(2,-6,0)$. The centroid divides median $RM$ in $2:1$ from $R$: $G=R+\tfrac23(M-R)=(1,2,2)$. Distance $=\sqrt{1+64+4}=\sqrt{69}$.

### M-TDG-18 · B — JEE Main 2024 · 27 Jan Shift 1 · Q80 · MCQ

If the shortest distance between the lines $\dfrac{x-4}1=\dfrac{y+1}2=\dfrac z{-3}$ and $\dfrac{x-\lambda}2=\dfrac{y+1}4=\dfrac{z-2}{-5}$ is $\dfrac6{\sqrt5}$, then the sum of all possible values of $\lambda$ is

(1) 5  (2) 8  (3) 7  (4) 10

**Answer: (2)** · key ✔

**Solution.** $\vec d_1\times\vec d_2=(1,2,-3)\times(2,4,-5)=(2,-1,0)$ with magnitude $\sqrt5$. The join of the given points is $(\lambda-4,0,2)$, and $\left|(\lambda-4,0,2)\cdot(2,-1,0)\right|=2|\lambda-4|$. So $\dfrac{2|\lambda-4|}{\sqrt5}=\dfrac6{\sqrt5}\Rightarrow\lambda=1$ or $7$; the sum is $8$.

### M-TDG-19 · B — JEE Main 2024 · 27 Jan Shift 2 · Q90 · Numerical

The lines $\dfrac{x-2}2=\dfrac y{-2}=\dfrac{z-7}{16}$ and $\dfrac{x+3}4=\dfrac{y+2}3=\dfrac{z+2}1$ intersect at the point $P$. If the distance of $P$ from the line $\dfrac{x+1}2=\dfrac{y-1}3=\dfrac{z-1}1$ is $l$, then $14l^2$ is equal to ______.

**Answer: 108** · key ✔

**Solution.** Points: $(2+2s,-2s,7+16s)=(-3+4t,-2+3t,-2+t)$. From $y$: $s=1-\tfrac32t$; from $x$: $4-3t=-3+4t\Rightarrow t=1,\ s=-\tfrac12$. Check $z$: $7-8=-1=-2+1$ ✓. So $P=(1,1,-1)$. Take $Q(-1,1,1)$ on the third line with direction $\vec d=(2,3,1)$, $\vec{QP}=(2,0,-2)$. $\vec{QP}\times\vec d=(6,-6,6)$, so $l^2=\dfrac{108}{14}$ and $14l^2=108$.

### M-TDG-20 · B — JEE Main 2024 · 29 Jan Shift 2 · Q90 · Numerical

Let $O$ be the origin, and $M$ and $N$ points on the lines $\dfrac{x-5}4=\dfrac{y-4}1=\dfrac{z-5}3$ and $\dfrac{x+8}{12}=\dfrac{y+2}5=\dfrac{z+11}9$ respectively, such that $MN$ is the shortest distance between the given lines. Then $\overrightarrow{OM}\cdot\overrightarrow{ON}$ is equal to ______.

**Answer: 9** · key ✔

**Solution.** $\vec d_1\times\vec d_2=(4,1,3)\times(12,5,9)=(-6,0,8)$, so $\overrightarrow{MN}\parallel(-3,0,4)$. With $M=(5+4s,4+s,5+3s)$ and $N=(-8+12t,-2+5t,-11+9t)$, the $y$-component of $\overrightarrow{MN}$ is zero: $5t-s=6\Rightarrow s=5t-6$. Then $\overrightarrow{MN}=(11-8t,\,0,\,2-6t)\parallel(-3,0,4)\Rightarrow4(11-8t)=-3(2-6t)\Rightarrow t=1,\ s=-1$. So $M=(1,3,2)$, $N=(4,3,-2)$ and $\overrightarrow{OM}\cdot\overrightarrow{ON}=4+9-4=9$.

### M-TDG-21 · B — JEE Main 2024 · 31 Jan Shift 2 · Q78 · MCQ

Let $(\alpha,\beta,\gamma)$ be the mirror image of the point $(2,3,5)$ in the line $\dfrac{x-1}2=\dfrac{y-2}3=\dfrac{z-3}4$. Then $2\alpha+3\beta+4\gamma$ is equal to

(1) 32  (2) 33  (3) 31  (4) 34

**Answer: (2)** · key ✔

**Solution.** A point on the line: $(1+2t,2+3t,3+4t)$. Perpendicular from $(2,3,5)$: $(2t-1)2+(3t-1)3+(4t-2)4=0\Rightarrow29t=13$. Foot $=\left(\tfrac{55}{29},\tfrac{97}{29},\tfrac{139}{29}\right)$. Image $=2\cdot\text{foot}-(2,3,5)=\left(\tfrac{52}{29},\tfrac{107}{29},\tfrac{133}{29}\right)$. $2\alpha+3\beta+4\gamma=\dfrac{104+321+532}{29}=\dfrac{957}{29}=33$.

