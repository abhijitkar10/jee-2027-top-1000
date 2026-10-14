# Vectors

> Theory: [../../theory/maths/vectors.md](../../theory/maths/vectors.md)

### M-VEC-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

For a triangle $ABC$, let $\vec p=\overrightarrow{BC}$, $\vec q=\overrightarrow{CA}$ and $\vec r=\overrightarrow{BA}$. If $|\vec p|=2\sqrt3$, $|\vec q|=2$ and $\cos\theta=\dfrac1{\sqrt3}$, where $\theta$ is the angle between $\vec p$ and $\vec q$, then $\left|\vec p\times(\vec q-3\vec r)\right|^2+3|\vec r|^2$ is equal to:

(1) 410  (2) 340  (3) 200  (4) 220

**Answer: (3)** · key (compiled)

**Solution.** From the triangle, $\vec r=\overrightarrow{BC}+\overrightarrow{CA}=\vec p+\vec q$. Then $\vec p\times(\vec q-3\vec r)=\vec p\times\vec q-3\vec p\times(\vec p+\vec q)=-2(\vec p\times\vec q)$. $|\vec p\times\vec q|^2=12\cdot4\cdot\sin^2\theta=48\cdot\tfrac23=32$, so the first term is $4\cdot32=128$. $\vec p\cdot\vec q=2\sqrt3\cdot2\cdot\tfrac1{\sqrt3}=4$ and $|\vec r|^2=12+4+2\cdot4=24$, so $3|\vec r|^2=72$. Total $=200$.

### M-VEC-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

Let $\vec a=-\hat i+\hat j+2\hat k$, $\vec b=\hat i-\hat j-3\hat k$, $\vec c=\vec a\times\vec b$ and $\vec d=\vec c\times\vec a$. Then $(\vec a-\vec b)\cdot\vec d$ is equal to:

(1) $-4$  (2) 4  (3) 2  (4) $-2$

**Answer: (4)** · key (compiled)

**Solution.** $\vec c=\vec a\times\vec b=(-1,-1,0)$ and $\vec d=\vec c\times\vec a=(-2,2,-2)$ (compute the determinants). $\vec a-\vec b=(-2,2,5)$. $(\vec a-\vec b)\cdot\vec d=4+4-10=-2$.

### M-VEC-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let $P$ be a point in the plane of the vectors $\overrightarrow{AB}=3\hat i+\hat j-\hat k$ and $\overrightarrow{AC}=\hat i-\hat j+3\hat k$ such that $P$ is equidistant from the lines $AB$ and $AC$. If $|\overrightarrow{AP}|=\dfrac{\sqrt5}2$, then the area of the triangle $ABP$ is:

(1) 2  (2) $\dfrac{\sqrt{30}}4$  (3) $\dfrac32$  (4) $\dfrac{\sqrt{26}}4$

**Answer: (2)** · key (compiled)

**Solution.** $|AB|=|AC|=\sqrt{11}$, so the internal bisector at $A$ is along $\overrightarrow{AB}+\overrightarrow{AC}=(4,0,2)\propto(2,0,1)$. With $|\overrightarrow{AP}|=\tfrac{\sqrt5}2$: $\overrightarrow{AP}=\pm\tfrac12(2\hat i+\hat k)$. $\overrightarrow{AB}\times\overrightarrow{AP}=\left(\tfrac12,-\tfrac52,-1\right)$ with magnitude $\sqrt{\tfrac{30}4}=\tfrac{\sqrt{30}}2$, so the area is $\tfrac12\cdot\tfrac{\sqrt{30}}2=\tfrac{\sqrt{30}}4$. (The external bisector would give $\tfrac54$, which is not among the options.)

### M-VEC-04 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · MCQ

Let $\vec a=2\hat i-5\hat j+5\hat k$ and $\vec b=\hat i-\hat j+3\hat k$. If $\vec c$ is a vector such that $2(\vec a\times\vec c)+3(\vec b\times\vec c)=\vec 0$ and $(\vec a-\vec b)\cdot\vec c=-97$, then $|\vec c\times\hat k|^2$ is equal to:

(1) 233  (2) 218  (3) 193  (4) 205

**Answer: (2)** · key (compiled)

**Solution.** $(2\vec a+3\vec b)\times\vec c=\vec0$ means $\vec c\parallel2\vec a+3\vec b=(7,-13,19)$: $\vec c=t(7,-13,19)$. $\vec a-\vec b=(1,-4,2)$ and $(\vec a-\vec b)\cdot\vec c=t(7+52+38)=97t=-97\Rightarrow t=-1$, $\vec c=(-7,13,-19)$. $\vec c\times\hat k=(13,7,0)$ and $|\vec c\times\hat k|^2=169+49=218$.

### M-VEC-05 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q6 · MCQ

Let a vector $\vec a=\sqrt2\hat i-\hat j+\lambda\hat k$, $\lambda>0$, make an obtuse angle with the vector $\vec b=-\lambda^2\hat i+4\sqrt2\hat j+4\sqrt2\hat k$ and an angle $\theta$, $\dfrac\pi6<\theta<\dfrac\pi2$, with the positive $z$-axis. If the set of all possible values of $\lambda$ is $(\alpha,\beta)-\{\gamma\}$, then $\alpha+\beta+\gamma$ is equal to ______.

**Answer: (3)** · key (compiled)

**Solution.** Angle with the $z$-axis: $\cos\theta=\dfrac\lambda{\sqrt{3+\lambda^2}}$ with $0<\cos\theta<\tfrac{\sqrt3}2\Rightarrow\lambda>0$ and $4\lambda^2<9+3\lambda^2\Rightarrow\lambda<3$. Obtuse angle with $\vec b$: $\vec a\cdot\vec b=-\sqrt2\lambda^2-4\sqrt2+4\sqrt2\lambda<0\Rightarrow\lambda^2-4\lambda+4>0\Rightarrow\lambda\ne2$. So $\lambda\in(0,3)-\{2\}$ and $\alpha+\beta+\gamma=0+3+2=5$.

### M-VEC-06 · A — JEE Main 2026 · 23 Jan Shift 2 · set Q9 · MCQ

Let $\vec a,\vec b,\vec c$ be three vectors such that $\vec a\times\vec b=2(\vec a\times\vec c)$. If $|\vec a|=1$, $|\vec b|=4$, $|\vec c|=2$, and the angle between $\vec b$ and $\vec c$ is $60^\circ$, then $|\vec a\cdot\vec c|$ is equal to:

(1) 1  (2) 2  (3) 0  (4) 4

**Answer: (1)** · key (compiled)

**Solution.** $\vec a\times(\vec b-2\vec c)=\vec0$, so $\vec b-2\vec c=k\vec a$. $\vec b\cdot\vec c=4\cdot2\cos60^\circ=4$. $|\vec b-2\vec c|^2=16-4(4)+4(4)=16=k^2|\vec a|^2\Rightarrow k=\pm4$. Dot $\vec b-2\vec c=k\vec a$ with $\vec c$: $4-8=k(\vec a\cdot\vec c)\Rightarrow\vec a\cdot\vec c=\dfrac{-4}k=\mp1$. So $|\vec a\cdot\vec c|=1$.

### M-VEC-07 · B — JEE Advanced 2025 · Paper 1 · Q9 · Numerical

$P,Q,R$ are distinct points in the plane and $S$ is inside $\triangle PQR$ with $\overrightarrow{SP}+5\overrightarrow{SQ}+6\overrightarrow{SR}=\vec0$. $E$ and $F$ are the mid-points of $PR$ and $QR$. Then $\dfrac{EF}{ES}=$ ______.

**Answer: 1.2** (accepted range $1.15$–$1.25$) · official key ✔ (re-derived)

**Solution.** From the condition, $S=\dfrac{P+5Q+6R}{12}$. $E=\dfrac{P+R}2$, so $S-E=\dfrac{P+5Q+6R-6P-6R}{12}=\dfrac{5(Q-P)}{12}$, giving $ES=\dfrac5{12}PQ$. $EF=\tfrac12PQ$ (mid-point theorem in $\triangle PQR$: $E,F$ join the mid-points of $PR$ and $QR$). $\dfrac{EF}{ES}=\dfrac{1/2}{5/12}=\dfrac65=1.2$.

### M-VEC-08 · B — JEE Main 2025 · Jan session · set Q1 · MCQ

Let $\vec a=3\hat i-\hat j+2\hat k$, $\vec b=\vec a\times(\hat i-2\hat k)$ and $\vec c=\vec b\times\hat k$. Then the projection of $\vec c-2\hat j$ on $\vec a$ is:

(1) $2\sqrt{14}$  (2) $\sqrt{14}$  (3) $3\sqrt7$  (4) $2\sqrt7$

**Answer: (1)** · key (compiled)

**Solution.** $\vec b=\vec a\times(\hat i-2\hat k)=(2,8,1)$ and $\vec c=\vec b\times\hat k=(8,-2,0)$, so $\vec c-2\hat j=(8,-4,0)$. Projection on $\vec a$: $\dfrac{(8,-4,0)\cdot(3,-1,2)}{\sqrt{14}}=\dfrac{28}{\sqrt{14}}=2\sqrt{14}$.

### M-VEC-09 · B — JEE Main 2025 · Jan session · set Q2 · MCQ

If the components of $\vec a=\alpha\hat i+\beta\hat j+\gamma\hat k$ along and perpendicular to $\vec b=3\hat i+\hat j-\hat k$ respectively are $\dfrac{16}{11}(3\hat i+\hat j-\hat k)$ and $\dfrac1{11}(-4\hat i-5\hat j-17\hat k)$, then $\alpha^2+\beta^2+\gamma^2$ is equal to:

(1) 26  (2) 18  (3) 23  (4) 16

**Answer: (1)** · key (compiled)

**Solution.** $\vec a$ is the sum of its components: $\dfrac1{11}(48-4,\ 16-5,\ -16-17)=(4,1,-3)$. $\alpha^2+\beta^2+\gamma^2=16+1+9=26$.

### M-VEC-10 · B — JEE Main 2025 · Apr session · set Q1 · MCQ

Let $ABCD$ be a tetrahedron such that the edges $AB$, $AC$ and $AD$ are mutually perpendicular. Let the areas of the triangles $ABC$, $ACD$ and $ADB$ be 5, 6 and 7 square units respectively. Then the area (in square units) of $\triangle BCD$ is equal to:

(1) $\sqrt{340}$  (2) 12  (3) $\sqrt{110}$  (4) $7\sqrt3$

**Answer: (3)** · key (compiled)

**Solution.** Put $AB=x$, $AC=y$, $AD=z$ along the axes. The face areas are $\tfrac12xy$, $\tfrac12yz$, $\tfrac12zx$, and the area of the opposite face is the vector magnitude $\tfrac12|\vec{BC}\times\vec{BD}|=\tfrac12\sqrt{x^2y^2+y^2z^2+z^2x^2}=\sqrt{5^2+6^2+7^2}=\sqrt{110}$.

### M-VEC-11 · B — JEE Main 2025 · Apr session · set Q2 · MCQ

Let the angle $\theta$, $0<\theta<\tfrac\pi2$, between two unit vectors $\hat a$ and $\hat b$ be $\sin^{-1}\!\left(\dfrac{\sqrt{65}}9\right)$. If the vector $\vec c=3\hat a+6\hat b+9(\hat a\times\hat b)$, then the value of $9(\vec c\cdot\hat a)-3(\vec c\cdot\hat b)$ is:

(1) 31  (2) 27  (3) 29  (4) 24

**Answer: (3)** · key (compiled)

**Solution.** $\cos\theta=\sqrt{1-\tfrac{65}{81}}=\tfrac49$. $\vec c\cdot\hat a=3+6\cos\theta$ and $\vec c\cdot\hat b=3\cos\theta+6$ (the cross product is perpendicular to both). $9(3+6\cos\theta)-3(3\cos\theta+6)=9+45\cos\theta=9+20=29$.

### M-VEC-12 · C — JEE Main 2024 · 27 Jan Shift 1 · Q78 · MCQ

Let $\vec a=\hat i+2\hat j+\hat k$, $\vec b=3(\hat i-\hat j+\hat k)$, and let $\vec c$ be a vector with $\vec a\times\vec c=\vec b$ and $\vec a\cdot\vec c=3$. Then $\vec a\cdot\big((\vec c\times\vec b)-\vec b-\vec c\big)$ is equal to

(1) 32  (2) 24  (3) 20  (4) 36

**Answer: (2)** · key ✔

**Solution.** $\vec a\cdot(\vec c\times\vec b)=(\vec a\times\vec c)\cdot\vec b=\vec b\cdot\vec b=9\cdot3=27$. Also $\vec a\cdot\vec b=3(1-2+1)=0$ and $\vec a\cdot\vec c=3$. So the value is $27-0-3=24$.

### M-VEC-13 · C — JEE Main 2024 · 27 Jan Shift 2 · Q77 · MCQ

The position vectors of the vertices $A,B,C$ of a triangle are $2\hat i-3\hat j+3\hat k$, $2\hat i+2\hat j+3\hat k$ and $-\hat i+\hat j+3\hat k$. Let $l$ be the length of the angle bisector $AD$ of $\angle BAC$, where $D$ lies on $BC$. Then $2l^2$ equals

(1) 49  (2) 42  (3) 50  (4) 45

**Answer: (4)** · key ✔

**Solution.** $AB=\sqrt{0+25+0}=5$ and $AC=\sqrt{9+16+0}=5$, so the triangle is isosceles and the bisector from $A$ meets $BC$ at its midpoint $D=\left(\tfrac12,\tfrac32,3\right)$. $AD^2=\left(\tfrac32\right)^2+\left(\tfrac92\right)^2=\tfrac{9+81}4=22.5$, so $2l^2=45$.

### M-VEC-14 · C — JEE Main 2024 · 29 Jan Shift 1 · Q77 · MCQ

Let $\vec a,\vec b,\vec c$ be three non-zero vectors such that $\vec b$ and $\vec c$ are non-collinear. If $\vec a+5\vec b$ is collinear with $\vec c$, $\vec b+6\vec c$ is collinear with $\vec a$, and $\vec a+\alpha\vec b+\beta\vec c=\vec0$, then $\alpha+\beta$ is equal to

(1) 35  (2) 30  (3) $-30$  (4) $-25$

**Answer: (1)** · key ✔

**Solution.** Let $\vec a+5\vec b=\lambda\vec c$, so $\vec a=\lambda\vec c-5\vec b$. Also $\vec b+6\vec c=\mu\vec a=\mu\lambda\vec c-5\mu\vec b$. Comparing coefficients of the independent vectors $\vec b,\vec c$: $1=-5\mu\Rightarrow\mu=-\tfrac15$ and $6=\mu\lambda\Rightarrow\lambda=-30$. Then $\vec a=-30\vec c-5\vec b$, i.e. $\vec a+5\vec b+30\vec c=\vec0$, so $\alpha=5,\ \beta=30$ and $\alpha+\beta=35$.

### M-VEC-15 · C — JEE Main 2024 · 30 Jan Shift 1 · Q77 · MCQ

Let $A(2,3,5)$ and $C(-3,4,-2)$ be opposite vertices of a parallelogram $ABCD$. If the diagonal $\overrightarrow{BD}=\hat i+2\hat j+3\hat k$, then the area of the parallelogram is equal to

(1) $\tfrac12\sqrt{410}$  (2) $\tfrac12\sqrt{474}$  (3) $\tfrac12\sqrt{586}$  (4) $\tfrac12\sqrt{306}$

**Answer: (2)** · key ✔

**Solution.** Area of a parallelogram $=\tfrac12|\vec d_1\times\vec d_2|$. $\overrightarrow{AC}=(-5,1,-7)$, $\overrightarrow{BD}=(1,2,3)$. $\overrightarrow{AC}\times\overrightarrow{BD}=\big((1)(3)-(-7)(2),\ (-7)(1)-(-5)(3),\ (-5)(2)-(1)(1)\big)=(17,8,-11)$, with $|\cdot|^2=289+64+121=474$. Area $=\tfrac12\sqrt{474}$.

