# Circles

> Theory: [../../theory/maths/circles.md](../../theory/maths/circles.md)

### M-CIR-01 — JEE Main 2024 · 27 Jan Shift 2 · Q84 · Numerical

Consider the circle $(x-\alpha)^2+(y-\beta)^2=50$, where $\alpha,\beta>0$. If the circle touches the line $y+x=0$ at a point $P$ whose distance from the origin is $4\sqrt2$, then $(\alpha+\beta)^2$ is equal to ______.

**Answer: 100** · key ✔

**Solution.** $P$ lies on $x+y=0$ at distance $4\sqrt2$ from $O$: $P=(4,-4)$ or $(-4,4)$. The radius is $5\sqrt2$ and the centre lies along the normal $(1,1)$: centre $=P\pm(5,5)$. With $\alpha,\beta>0$: $(9,1)$ or $(1,9)$ (the other choices give negative coordinates). In both cases $(\alpha+\beta)^2=100$.

### M-CIR-02 — JEE Main 2024 · 29 Jan Shift 1 · Q65 · MCQ

Let $\left(5,\dfrac a4\right)$ be the circumcentre of a triangle with vertices $A(a,-2)$, $B(a,6)$ and $C\!\left(\dfrac a4,-2\right)$. Let $\alpha$ denote the circumradius, $\beta$ the area and $\gamma$ the perimeter of the triangle. Then $\alpha+\beta+\gamma$ is

(1) 60  (2) 53  (3) 62  (4) 30

**Answer: (2)** · key ✔

**Solution.** $AB$ is vertical and $AC$ is horizontal, so the angle at $A$ is $90^\circ$ and the circumcentre is the midpoint of the hypotenuse $BC$: $\left(\tfrac{5a}8,2\right)=\left(5,\tfrac a4\right)\Rightarrow a=8$. Then $A(8,-2),B(8,6),C(2,-2)$: $AB=8,\ AC=6,\ BC=10$. $\alpha=5,\ \beta=24,\ \gamma=24$, so the sum is $53$.

### M-CIR-03 — JEE Main 2024 · 29 Jan Shift 1 · Q84 · Numerical

Equations of two diameters of a circle are $2x-3y=5$ and $3x-4y=7$. The line joining the points $\left(-\tfrac{22}7,-4\right)$ and $\left(-\tfrac17,3\right)$ intersects the circle at only one point $P(\alpha,\beta)$. Then $17\beta-\alpha$ is equal to ______.

**Answer: 2** · key ✔

**Solution.** The diameters meet at the centre $C(1,-1)$. The line through the two given points has slope $\dfrac{3+4}{-\frac17+\frac{22}7}=\dfrac73$: $7x-3y+10=0$. It meets the circle at exactly one point, so it is tangent and $P$ is the foot of the perpendicular from $C$: $P=C-\dfrac{7(1)-3(-1)+10}{7^2+3^2}(7,-3)=\left(1-\dfrac{140}{58},\,-1+\dfrac{60}{58}\right)=\left(-\dfrac{41}{29},\dfrac1{29}\right)$. So $17\beta-\alpha=\dfrac{17+41}{29}=2$.

### M-CIR-04 — JEE Main 2024 · 30 Jan Shift 2 · Q85 · Numerical

Consider two circles $C_1:x^2+y^2=25$ and $C_2:(x-\alpha)^2+y^2=16$, where $\alpha\in(5,9)$. Let the angle between the two radii (one to each circle) drawn from one of the intersection points of $C_1$ and $C_2$ be $\sin^{-1}\dfrac{\sqrt{63}}8$ (the acute angle). If the length of the common chord of $C_1$ and $C_2$ is $\beta$, then $(\alpha\beta)^2$ equals ______.

**Answer: 1575** · key ✔

**Solution.** In the triangle formed by the centres and an intersection point (sides $5,4,\alpha$) the angle $\theta$ at the intersection point has $\cos\theta=\tfrac18$. By the cosine rule $\alpha^2=25+16-2(5)(4)\tfrac18=36$, so $\alpha=6$. The common chord is twice the height of that triangle on base $\alpha$: area $=\sqrt{7.5\times2.5\times3.5\times1.5}=\tfrac{15\sqrt7}{4}$, and $\beta=\dfrac{4\cdot\text{Area}}\alpha=\dfrac{15\sqrt7}{6}=\dfrac{5\sqrt7}2$. Then $(\alpha\beta)^2=\left(6\cdot\tfrac{5\sqrt7}2\right)^2=(15\sqrt7)^2=1575$.

### M-CIR-05 — JEE Main 2024 · 31 Jan Shift 1 · Q65 · MCQ

If one of the diameters of the circle $x^2+y^2-10x+4y+13=0$ is a chord of another circle $C$ whose centre is the point of intersection of the lines $2x+3y=12$ and $3x-2y=5$, then the radius of the circle $C$ is

(1) $\sqrt{20}$  (2) 4  (3) 6  (4) $3\sqrt2$

**Answer: (3)** · key ✔

**Solution.** The lines meet at $(3,2)$, the centre of $C$. The first circle is $(x-5)^2+(y+2)^2=16$: centre $(5,-2)$, radius $4$. Its diameter is a chord of $C$ of length $8$ with midpoint $(5,-2)$ (the centre). The distance from $(3,2)$ to $(5,-2)$ is $\sqrt{4+16}=\sqrt{20}$. So $R^2=(\sqrt{20})^2+4^2=36$ and $R=6$.

### M-CIR-06 — JEE Main 2024 · 1 Feb Shift 1 · Q66 · MCQ

Let $C:x^2+y^2=4$ and $C':x^2+y^2-4\lambda x+9=0$ be two circles. If the set of all values of $\lambda$ for which the circles intersect at two distinct points is $\mathbb R-[a,b]$, then the point $(8a+12,\,16b-20)$ lies on the curve:

(1) $x^2+2y^2-5x+6y=3$  (2) $5x^2-y=-11$  (3) $x^2-4y^2=7$  (4) $6x^2+y^2=42$

**Answer: (4)** · key ✔

**Solution.** $C'$ has centre $(2\lambda,0)$ and radius $r=\sqrt{4\lambda^2-9}$ (needs $|\lambda|>3/2$). Two-point intersection needs $|r-2|<d<r+2$ with $d=2|\lambda|$. The condition $d<r+2$ gives $(2|\lambda|-2)^2<4\lambda^2-9\Rightarrow 8|\lambda|>13$, i.e. $|\lambda|>13/8$; the other inequality then holds automatically. So the set is $\mathbb R-[-\tfrac{13}{8},\tfrac{13}{8}]$, $a=-\tfrac{13}8$, $b=\tfrac{13}8$. The point is $(-1,\,6)$, and $6(1)+36=42$ lies on option (4).

### M-CIR-07 — JEE Main 2024 · 1 Feb Shift 2 · Q66 · MCQ

Let the locus of the mid-points of the chords of the circle $x^2+(y-1)^2=1$ drawn from the origin intersect the line $x+y=1$ at $P$ and $Q$. Then $PQ$ is:

(1) $\dfrac1{\sqrt2}$  (2) $\sqrt2$  (3) $\dfrac12$  (4) $1$

**Answer: (1)** · key ✔

**Solution.** The origin lies on the circle. The midpoint $M$ of a chord $OA$ satisfies $\angle OMC=90^\circ$ where $C=(0,1)$, so $M$ lies on the circle with diameter $OC$: $x^2+y^2-y=0$. With $y=1-x$: $2x^2-x=0$, $x=0,\tfrac12$. Points $(0,1)$ and $\left(\tfrac12,\tfrac12\right)$, distance $\sqrt{\tfrac14+\tfrac14}=\dfrac1{\sqrt2}$.

### M-CIR-08 — JEE Advanced 2025 · Paper 1 · Q7 · Multiple correct

Let $z_1=1+2i$, $z_2=3i$ and $S=\{(x,y)\in\mathbb R^2:|x+iy-z_1|=2|x+iy-z_2|\}$. Which are TRUE?

(A) $S$ is a circle with centre $\left(-\tfrac13,\tfrac{10}3\right)$  (B) $S$ is a circle with centre $\left(\tfrac13,\tfrac83\right)$  (C) $S$ is a circle with radius $\tfrac{\sqrt2}3$  (D) $S$ is a circle with radius $\tfrac{2\sqrt2}3$

**Answer: (A), (D)** · official key ✔ (re-derived)

**Solution.** $(x-1)^2+(y-2)^2=4\left[x^2+(y-3)^2\right]\Rightarrow3x^2+3y^2+2x-20y+31=0\Rightarrow x^2+y^2+\tfrac23x-\tfrac{20}3y+\tfrac{31}3=0$. Centre $\left(-\tfrac13,\tfrac{10}3\right)$; $r^2=\tfrac19+\tfrac{100}9-\tfrac{31}3=\tfrac89$, so $r=\tfrac{2\sqrt2}3$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · Numerical

If P is a point on the circle $x^2+y^2=4$, Q is a point on the straight line $5x+y+2=0$ and $x-y+1=0$ is the perpendicular bisector of PQ, then 13 times the sum of the abscissae of all such points P is ______.

**Answer: 2** · key (compiled)

**Solution.** $Q$ is the reflection of $P(p,q)$ in the line $y=x+1$, which maps $(p,q)\to(q-1,\,p+1)$. $Q$ on $5x+y+2=0$: $5(q-1)+(p+1)+2=0\Rightarrow p=2-5q$. $P$ on the circle: $(2-5q)^2+q^2=4\Rightarrow26q^2-20q=0\Rightarrow q=0$ or $\tfrac{10}{13}$, giving $p=2$ or $-\tfrac{24}{13}$. Sum of abscissae $=2-\tfrac{24}{13}=\tfrac2{13}$, so $13\times$ sum $=2$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q2 · MCQ

Let the circle $x^2+y^2=4$ intersect the $x$-axis at the points $A(a,0)$, $a>0$ and $B(b,0)$. Let $P(2\cos\alpha,2\sin\alpha)$, $0<\alpha<\dfrac\pi2$ and $Q(2\cos\beta,2\sin\beta)$ be two points such that $(\alpha-\beta)=\dfrac\pi2$. Then the point of intersection of $AQ$ and $BP$ lies on:

(1) $x^2+y^2-4y-4=0$  (2) $x^2+y^2-4x-4y=0$  (3) $x^2+y^2-4x-4=0$  (4) $x^2+y^2-4x-4y-4=0$

**Answer: (1)** · key (compiled)

**Solution.** $A=(2,0)$, $B=(-2,0)$ and $Q=(2\cos(\alpha-\tfrac\pi2),2\sin(\alpha-\tfrac\pi2))=(2\sin\alpha,-2\cos\alpha)$. Slope of $BP=\dfrac{\sin\alpha}{1+\cos\alpha}=\tan\tfrac\alpha2=t$; slope of $AQ=\dfrac{\cos\alpha}{1-\sin\alpha}=\tan\left(\tfrac\pi4+\tfrac\alpha2\right)=\dfrac{1+t}{1-t}$. For the intersection $R(h,k)$: $t=\dfrac k{h+2}$ and $\dfrac k{h-2}=\dfrac{h+2+k}{h+2-k}$. Cross-multiplying: $k(h+2-k)=(h-2)(h+2+k)\Rightarrow h^2+k^2-4k-4=0$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q3 · MCQ

Let the set of all values of $r$ for which the circles $(x+1)^2+(y+4)^2=r^2$ and $x^2+y^2-4x-2y-4=0$ intersect at two distinct points be the interval $(\alpha,\beta)$. Then $\alpha\beta$ is equal to:

(1) 21  (2) 24  (3) 20  (4) 25

**Answer: (4)** · key (compiled)

**Solution.** Centres $(-1,-4)$ with radius $r$, and $(2,1)$ with radius $3$ (since $(x-2)^2+(y-1)^2=9$). The distance between the centres is $\sqrt{9+25}=\sqrt{34}$. Two intersection points need $|r-3|<\sqrt{34}<r+3$, so $\sqrt{34}-3<r<\sqrt{34}+3$. $\alpha\beta=34-9=25$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q4 · MCQ

If the points of intersection of the ellipses $x^2+2y^2-6x-12y+23=0$ and $4x^2+2y^2-20x-12y+35=0$ lie on a circle of radius $r$ and centre $(a,b)$, then the value of $ab+18r^2$ is:

(1) 52  (2) 53  (3) 51  (4) 55

**Answer: (4)** · key (compiled)

**Solution.** Every curve through the common points is $S_1+\lambda S_2=0$; it is a circle when the $x^2$ and $y^2$ coefficients match: $1+4\lambda=2+2\lambda\Rightarrow\lambda=\tfrac12$. This gives $3x^2+3y^2-16x-18y+\tfrac{81}2=0$, i.e. $x^2+y^2-\tfrac{16}3x-6y+\tfrac{27}2=0$. Centre $(a,b)=\left(\tfrac83,3\right)$ and $r^2=\tfrac{64}9+9-\tfrac{27}2=\tfrac{47}{18}$. $ab+18r^2=8+47=55$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q5 · MCQ

Let $\vec c$ and $\vec d$ be vectors such that $|\vec c+\vec d|=\sqrt{29}$ and $\vec c\times(2\hat i+3\hat j+4\hat k)=(2\hat i+3\hat j+4\hat k)\times\vec d$. If $\lambda_1,\lambda_2$ ($\lambda_1>\lambda_2$) are the possible values of $(\vec c+\vec d)\cdot(-7\hat i+2\hat j+3\hat k)$, then the equation $K^2x^2+\left(K^2-5K+\lambda_1\right)xy+\left(3K+\dfrac{\lambda_2}2\right)y^2-8x+12y+\lambda_2=0$ represents a circle, for $K$ equal to:

(1) 1  (2) 4  (3) $-1$  (4) 2

**Answer: (1)** · key (compiled)

**Solution.** Let $\vec a=2\hat i+3\hat j+4\hat k$ ($|\vec a|^2=29$). The condition gives $\vec c\times\vec a+\vec d\times\vec a=\vec 0$, so $(\vec c+\vec d)\times\vec a=\vec0$: $\vec c+\vec d=t\vec a$ and $|t|\sqrt{29}=\sqrt{29}\Rightarrow t=\pm1$. $(\vec c+\vec d)\cdot(-7,2,3)=\pm(-14+6+12)=\pm4$, so $\lambda_1=4$, $\lambda_2=-4$. The conic is $K^2x^2+(K^2-5K+4)xy+(3K-2)y^2-8x+12y-4=0$. A circle needs equal $x^2,y^2$ coefficients, $K^2=3K-2\Rightarrow K=1,2$, and no $xy$ term, $K^2-5K+4=0\Rightarrow K=1,4$. So $K=1$ (giving $x^2+y^2-8x+12y-4=0$, a real circle).

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q6 · MCQ

Let PQ and MN be two straight lines touching the circle $x^2+y^2-4x-6y-3=0$ at the points A and B respectively. Let O be the centre of the circle and $\angle AOB=\pi/3$. Then the locus of the point of intersection of the lines PQ and MN is:

(1) $x^2+y^2-12x-18y-25=0$  (2) $3(x^2+y^2)-18x-12y+25=0$  (3) $3(x^2+y^2)-12x-18y-25=0$  (4) $x^2+y^2-18x-12y-25=0$

**Answer: (3)** · key (compiled)

**Solution.** The circle is $(x-2)^2+(y-3)^2=16$: centre $O(2,3)$, $r=4$. Tangents at $A$ and $B$ meet at $T$ with $OT\cos\tfrac{\angle AOB}2=r$, so $OT=\dfrac{4}{\cos30^\circ}=\dfrac8{\sqrt3}$. The locus of $T$ is the circle $(x-2)^2+(y-3)^2=\tfrac{64}3$, i.e. $3(x^2+y^2)-12x-18y-25=0$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q7 · MCQ

Let $y=x$ be the equation of a chord of the circle $C_1$ (in the closed half-plane $x\ge0$) of diameter 10 passing through the origin. Let $C_2$ be another circle described on the given chord as its diameter. If the equation of the chord of the circle $C_2$, which passes through the point $(2,3)$ and is farthest from the centre of $C_2$, is $x+ay+b=0$, then $a-b$ is equal to:

(1) $-2$  (2) 10  (3) $-6$  (4) 6

**Answer: (1)** · key (compiled)

**Solution.** $C_1$ has radius 5, passes through the origin and lies in $x\ge0$, so it touches the $y$-axis there: centre $(5,0)$. The chord $y=x$ meets $(x-5)^2+y^2=25$ at $(0,0)$ and $(5,5)$. $C_2$ has this chord as diameter: centre $\left(\tfrac52,\tfrac52\right)$, equation $x^2+y^2-5x-5y=0$. The point $(2,3)$ is inside $C_2$ (value $-12$). The chord through an interior point that is farthest from the centre is the one perpendicular to the line joining the centre to the point: that direction is $\left(2-\tfrac52,3-\tfrac52\right)=\left(-\tfrac12,\tfrac12\right)\propto(-1,1)$, so the chord is $-(x-2)+(y-3)=0\Rightarrow x-y+1=0$. Thus $a=-1$, $b=1$ and $a-b=-2$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q8 · MCQ

Let $S=\left\{z\in\mathbb C:\left|\dfrac{z-6i}{z-2i}\right|=1\ \text{and}\ \left|\dfrac{z-8+2i}{z+2i}\right|=\dfrac35\right\}$. Then $\sum_{z\in S}|z|^2$ is equal to:

(1) 385  (2) 398  (3) 413  (4) 423

**Answer: (1)** · key (compiled)

**Solution.** The first condition says $z$ is equidistant from $6i$ and $2i$: the line $y=4$. For the second, with $z=x+iy$: $25\left[(x-8)^2+(y+2)^2\right]=9\left[x^2+(y+2)^2\right]\Rightarrow x^2-25x+100+(y+2)^2=0$. Putting $y=4$: $x^2-25x+136=0\Rightarrow x=17$ or $8$. So $S=\{17+4i,\ 8+4i\}$ and $\sum|z|^2=(289+16)+(64+16)=385$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q9 · MCQ

Let a circle of radius 4 pass through the origin O, the points $A(-\sqrt3a,0)$ and $B(0,-\sqrt2b)$, where $a$ and $b$ are real parameters and $ab\ne0$. Then the locus of the centroid of $\triangle OAB$ is a circle of radius:

(1) $\dfrac73$  (2) $\dfrac83$  (3) $\dfrac{11}3$  (4) $\dfrac53$

**Answer: (2)** · key (compiled)

**Solution.** Let the centre be $C(h,k)$; since the circle passes through $O$ with radius 4, $h^2+k^2=16$. The centre lies on the perpendicular bisectors of $OA$ and $OB$: $h=-\dfrac{\sqrt3a}2$ and $k=-\dfrac{\sqrt2b}2$. The centroid is $G=\left(\dfrac{-\sqrt3a}3,\dfrac{-\sqrt2b}3\right)=\left(\dfrac{2h}3,\dfrac{2k}3\right)$, so $|OG|=\tfrac23\cdot4=\tfrac83$: the locus is a circle of radius $\tfrac83$ (centred at the origin).

