# Circles

> Theory: [../../theory/maths/circles.md](../../theory/maths/circles.md)

### M-CIR-01 · C — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · Numerical

If P is a point on the circle $x^2+y^2=4$, Q is a point on the straight line $5x+y+2=0$ and $x-y+1=0$ is the perpendicular bisector of PQ, then 13 times the sum of the abscissae of all such points P is ______.

**Answer: 2** · key (compiled)

**Solution.** $Q$ is the reflection of $P(p,q)$ in the line $y=x+1$, which maps $(p,q)\to(q-1,\,p+1)$. $Q$ on $5x+y+2=0$: $5(q-1)+(p+1)+2=0\Rightarrow p=2-5q$. $P$ on the circle: $(2-5q)^2+q^2=4\Rightarrow26q^2-20q=0\Rightarrow q=0$ or $\tfrac{10}{13}$, giving $p=2$ or $-\tfrac{24}{13}$. Sum of abscissae $=2-\tfrac{24}{13}=\tfrac2{13}$, so $13\times$ sum $=2$.

### M-CIR-02 · C — JEE Main 2026 · 28 Jan Shift 2 · set Q2 · MCQ

Let the circle $x^2+y^2=4$ intersect the $x$-axis at the points $A(a,0)$, $a>0$ and $B(b,0)$. Let $P(2\cos\alpha,2\sin\alpha)$, $0<\alpha<\dfrac\pi2$ and $Q(2\cos\beta,2\sin\beta)$ be two points such that $(\alpha-\beta)=\dfrac\pi2$. Then the point of intersection of $AQ$ and $BP$ lies on:

(1) $x^2+y^2-4y-4=0$  (2) $x^2+y^2-4x-4y=0$  (3) $x^2+y^2-4x-4=0$  (4) $x^2+y^2-4x-4y-4=0$

**Answer: (1)** · key (compiled)

**Solution.** $A=(2,0)$, $B=(-2,0)$ and $Q=(2\cos(\alpha-\tfrac\pi2),2\sin(\alpha-\tfrac\pi2))=(2\sin\alpha,-2\cos\alpha)$. Slope of $BP=\dfrac{\sin\alpha}{1+\cos\alpha}=\tan\tfrac\alpha2=t$; slope of $AQ=\dfrac{\cos\alpha}{1-\sin\alpha}=\tan\left(\tfrac\pi4+\tfrac\alpha2\right)=\dfrac{1+t}{1-t}$. For the intersection $R(h,k)$: $t=\dfrac k{h+2}$ and $\dfrac k{h-2}=\dfrac{h+2+k}{h+2-k}$. Cross-multiplying: $k(h+2-k)=(h-2)(h+2+k)\Rightarrow h^2+k^2-4k-4=0$.

### M-CIR-03 · C — JEE Main 2026 · 21 Jan Shift 1 · set Q5 · MCQ

Let $\vec c$ and $\vec d$ be vectors such that $|\vec c+\vec d|=\sqrt{29}$ and $\vec c\times(2\hat i+3\hat j+4\hat k)=(2\hat i+3\hat j+4\hat k)\times\vec d$. If $\lambda_1,\lambda_2$ ($\lambda_1>\lambda_2$) are the possible values of $(\vec c+\vec d)\cdot(-7\hat i+2\hat j+3\hat k)$, then the equation $K^2x^2+\left(K^2-5K+\lambda_1\right)xy+\left(3K+\dfrac{\lambda_2}2\right)y^2-8x+12y+\lambda_2=0$ represents a circle, for $K$ equal to:

(1) 1  (2) 4  (3) $-1$  (4) 2

**Answer: (1)** · key (compiled)

**Solution.** Let $\vec a=2\hat i+3\hat j+4\hat k$ ($|\vec a|^2=29$). The condition gives $\vec c\times\vec a+\vec d\times\vec a=\vec 0$, so $(\vec c+\vec d)\times\vec a=\vec0$: $\vec c+\vec d=t\vec a$ and $|t|\sqrt{29}=\sqrt{29}\Rightarrow t=\pm1$. $(\vec c+\vec d)\cdot(-7,2,3)=\pm(-14+6+12)=\pm4$, so $\lambda_1=4$, $\lambda_2=-4$. The conic is $K^2x^2+(K^2-5K+4)xy+(3K-2)y^2-8x+12y-4=0$. A circle needs equal $x^2,y^2$ coefficients, $K^2=3K-2\Rightarrow K=1,2$, and no $xy$ term, $K^2-5K+4=0\Rightarrow K=1,4$. So $K=1$ (giving $x^2+y^2-8x+12y-4=0$, a real circle).

### M-CIR-04 · C — JEE Main 2026 · 24 Jan Shift 1 · set Q8 · MCQ

Let $S=\left\{z\in\mathbb C:\left|\dfrac{z-6i}{z-2i}\right|=1\ \text{and}\ \left|\dfrac{z-8+2i}{z+2i}\right|=\dfrac35\right\}$. Then $\sum_{z\in S}|z|^2$ is equal to:

(1) 385  (2) 398  (3) 413  (4) 423

**Answer: (1)** · key (compiled)

**Solution.** The first condition says $z$ is equidistant from $6i$ and $2i$: the line $y=4$. For the second, with $z=x+iy$: $25\left[(x-8)^2+(y+2)^2\right]=9\left[x^2+(y+2)^2\right]\Rightarrow x^2-25x+100+(y+2)^2=0$. Putting $y=4$: $x^2-25x+136=0\Rightarrow x=17$ or $8$. So $S=\{17+4i,\ 8+4i\}$ and $\sum|z|^2=(289+16)+(64+16)=385$.

### M-CIR-05 · C — JEE Advanced 2025 · Paper 1 · Q7 · Multiple correct

Let $z_1=1+2i$, $z_2=3i$ and $S=\{(x,y)\in\mathbb R^2:|x+iy-z_1|=2|x+iy-z_2|\}$. Which are TRUE?

(A) $S$ is a circle with centre $\left(-\tfrac13,\tfrac{10}3\right)$  (B) $S$ is a circle with centre $\left(\tfrac13,\tfrac83\right)$  (C) $S$ is a circle with radius $\tfrac{\sqrt2}3$  (D) $S$ is a circle with radius $\tfrac{2\sqrt2}3$

**Answer: (A), (D)** · official key ✔ (re-derived)

**Solution.** $(x-1)^2+(y-2)^2=4\left[x^2+(y-3)^2\right]\Rightarrow3x^2+3y^2+2x-20y+31=0\Rightarrow x^2+y^2+\tfrac23x-\tfrac{20}3y+\tfrac{31}3=0$. Centre $\left(-\tfrac13,\tfrac{10}3\right)$; $r^2=\tfrac19+\tfrac{100}9-\tfrac{31}3=\tfrac89$, so $r=\tfrac{2\sqrt2}3$.

### M-CIR-06 · C — JEE Main 2024 · 27 Jan Shift 2 · Q84 · Numerical

Consider the circle $(x-\alpha)^2+(y-\beta)^2=50$, where $\alpha,\beta>0$. If the circle touches the line $y+x=0$ at a point $P$ whose distance from the origin is $4\sqrt2$, then $(\alpha+\beta)^2$ is equal to ______.

**Answer: 100** · key ✔

**Solution.** $P$ lies on $x+y=0$ at distance $4\sqrt2$ from $O$: $P=(4,-4)$ or $(-4,4)$. The radius is $5\sqrt2$ and the centre lies along the normal $(1,1)$: centre $=P\pm(5,5)$. With $\alpha,\beta>0$: $(9,1)$ or $(1,9)$ (the other choices give negative coordinates). In both cases $(\alpha+\beta)^2=100$.

### M-CIR-07 · C — JEE Main 2024 · 29 Jan Shift 1 · Q65 · MCQ

Let $\left(5,\dfrac a4\right)$ be the circumcentre of a triangle with vertices $A(a,-2)$, $B(a,6)$ and $C\!\left(\dfrac a4,-2\right)$. Let $\alpha$ denote the circumradius, $\beta$ the area and $\gamma$ the perimeter of the triangle. Then $\alpha+\beta+\gamma$ is

(1) 60  (2) 53  (3) 62  (4) 30

**Answer: (2)** · key ✔

**Solution.** $AB$ is vertical and $AC$ is horizontal, so the angle at $A$ is $90^\circ$ and the circumcentre is the midpoint of the hypotenuse $BC$: $\left(\tfrac{5a}8,2\right)=\left(5,\tfrac a4\right)\Rightarrow a=8$. Then $A(8,-2),B(8,6),C(2,-2)$: $AB=8,\ AC=6,\ BC=10$. $\alpha=5,\ \beta=24,\ \gamma=24$, so the sum is $53$.

