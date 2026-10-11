# Area Under Curves

> Theory: [../../theory/maths/area-under-curves.md](../../theory/maths/area-under-curves.md)

### M-ARE-01 — JEE Main 2024 · 27 Jan Shift 1 · Q87 · Numerical

Let the area of the region $\{(x,y):x-2y+4\ge0,\ x+2y^2\ge0,\ x+4y^2\le8,\ y\ge0\}$ be $\dfrac mn$, where $m,n$ are coprime. Then $m+n$ is equal to ______.

**Answer: 119** · key ✔

**Solution.** Integrate horizontally in $y$. Right boundary: $x=8-4y^2$. Left boundary: $x=-2y^2$ for $0\le y\le1$ and $x=2y-4$ for $1\le y\le\tfrac32$ (the curves $-2y^2=2y-4$ meet at $y=1$, and $8-4y^2=2y-4$ at $y=\tfrac32$).
$A=\int_0^1(8-2y^2)\,dy+\int_1^{3/2}(12-2y-4y^2)\,dy=\tfrac{22}3+\tfrac{19}{12}=\tfrac{107}{12}$. So $m+n=119$.

### M-ARE-02 — JEE Main 2024 · 27 Jan Shift 2 · Q88 · Numerical

If the area of the region $\{(x,y):0\le y\le\min\{2x,\ 6x-x^2\}\}$ is $A$, then $12A$ is equal to ______.

**Answer: 304** · key ✔

**Solution.** $2x=6x-x^2$ at $x=0,4$. For $0\le x\le4$ the minimum is $2x$; for $4\le x\le6$ it is $6x-x^2$. $A=\int_0^42x\,dx+\int_4^6(6x-x^2)dx=16+\left[3x^2-\tfrac{x^3}3\right]_4^6=16+36-\tfrac{80}3=\tfrac{76}3$. So $12A=304$.

### M-ARE-03 — JEE Main 2024 · 29 Jan Shift 1 · Q88 · Numerical

The area (in sq. units) of the part of the circle $x^2+y^2=169$ which is below the line $5x-y=13$ is $\dfrac{\pi\alpha}{2\beta}-\dfrac{65}2+\dfrac\alpha\beta\sin^{-1}\!\left(\dfrac{12}{13}\right)$, where $\alpha,\beta$ are coprime. Then $\alpha+\beta$ is equal to ______.

**Answer: 171** · key ✔

**Solution.** The line meets the circle at $(0,-13)$ and $(5,12)$. The origin satisfies $5x-y-13<0$, so the region below the line is the minor segment. Its distance from the centre is $\dfrac{13}{\sqrt{26}}$, so half the central angle has $\cos\dfrac\theta2=\dfrac1{\sqrt{26}}$, giving $\cos\theta=-\dfrac{12}{13}$, $\sin\theta=\dfrac5{13}$ and $\theta=\dfrac\pi2+\sin^{-1}\dfrac{12}{13}$. Segment area $=\dfrac{169}2(\theta-\sin\theta)=\dfrac{169\pi}4+\dfrac{169}2\sin^{-1}\dfrac{12}{13}-\dfrac{65}2$. Matching: $\dfrac\alpha\beta=\dfrac{169}2$, so $\alpha=169,\ \beta=2$ and $\alpha+\beta=171$.

### M-ARE-04 — JEE Main 2024 · 29 Jan Shift 2 · Q89 · Numerical

Let the area of the region $\{(x,y):0\le x\le3,\ 0\le y\le\min\{x^2+2,\ 2x+2\}\}$ be $A$. Then $12A$ is equal to ______.

**Answer: 164** · key ✔

**Solution.** $x^2+2=2x+2$ at $x=0,2$. For $0\le x\le2$ the minimum is $x^2+2$; for $2\le x\le3$ it is $2x+2$. $A=\int_0^2(x^2+2)dx+\int_2^3(2x+2)dx=\left(\tfrac83+4\right)+(15-8)=\tfrac{20}3+7=\tfrac{41}3$. So $12A=164$.

### M-ARE-05 — JEE Main 2024 · 30 Jan Shift 1 · Q75 · MCQ

The area (in square units) of the region bounded by the parabola $y^2=4(x-2)$ and the line $y=2x-8$ is

(1) 8  (2) 9  (3) 6  (4) 7

**Answer: (2)** · key ✔

**Solution.** With $x=\dfrac{y+8}2$ in the parabola: $y^2=4\left(\dfrac y2+2\right)=2y+8\Rightarrow y^2-2y-8=0\Rightarrow y=-2,\ 4$. Area $=\displaystyle\int_{-2}^4\left[\dfrac{y+8}2-\left(\dfrac{y^2}4+2\right)\right]dy=\int_{-2}^4\left(\dfrac y2+2-\dfrac{y^2}4\right)dy=\left[\dfrac{y^2}4+2y-\dfrac{y^3}{12}\right]_{-2}^4=\dfrac{20}3+\dfrac73=9$.

### M-ARE-06 — JEE Main 2024 · 30 Jan Shift 2 · Q88 · Numerical

The area of the region enclosed by the parabola $(y-2)^2=x-1$, the line $x-2y+4=0$ and the positive coordinate axes is ______.

**Answer: 5** · key ✔

**Solution.** The line $x=2y-4$ touches the parabola at $(2,3)$ (substituting gives $(y-3)^2=0$) and meets the $y$-axis at $(0,2)$; the parabola meets the $x$-axis at $(5,0)$. Integrating in $y$: for $0\le y\le2$ the region runs from $x=0$ to $x=(y-2)^2+1$; for $2\le y\le3$ it runs from the line $x=2y-4$ to the parabola. $A=\int_0^2\left[(y-2)^2+1\right]dy+\int_2^3\left[(y-2)^2+1-(2y-4)\right]dy=\tfrac{14}3+\int_2^3(y-3)^2dy=\tfrac{14}3+\tfrac13=5$.

### M-ARE-07 — JEE Main 2024 · 31 Jan Shift 2 · Q76 · MCQ

The area of the region enclosed by the parabola $y=4x-x^2$ and $3y=(x-4)^2$ is equal to

(1) $\tfrac{32}9$  (2) 4  (3) 6  (4) $\tfrac{14}3$

**Answer: (3)** · key ✔

**Solution.** Intersection: $3(4x-x^2)=(x-4)^2\Rightarrow4x^2-20x+16=0\Rightarrow x=1,4$. $A=\int_1^4\left[(4x-x^2)-\tfrac{(x-4)^2}3\right]dx=\tfrac13\int_1^4(-4x^2+20x-16)dx=\tfrac13\left[-\tfrac{4x^3}3+10x^2-16x\right]_1^4=\tfrac13(10.667+7.333)=6$.

### M-ARE-08 — JEE Main 2024 · 1 Feb Shift 1 · Q76 · MCQ

The area enclosed by the curves $xy+4y=16$ and $x+y=6$ is equal to:

(1) $28-30\log_e2$  (2) $30-28\log_e2$  (3) $30-32\log_e2$  (4) $32-30\log_e2$

**Answer: (3)** · key ✔

**Solution.** The curve is $y=\dfrac{16}{x+4}$. Intersection with $y=6-x$: $(6-x)(x+4)=16\Rightarrow x^2-2x-8=0$, so $x=-2,4$. The line is above the curve between them:
$A=\displaystyle\int_{-2}^{4}\left(6-x-\frac{16}{x+4}\right)dx=\Big[6x-\tfrac{x^2}2\Big]_{-2}^{4}-16\ln\tfrac82=30-16\ln4=30-32\ln2.$

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

If the area of the region $\{(x,y):1-2x\le y\le4-x^2,\ x\ge0,\ y\ge0\}$ is $\dfrac\alpha\beta$, $\alpha,\beta\in\mathbb N$, $\gcd(\alpha,\beta)=1$, then the value of $(\alpha+\beta)$ is:

(1) 67  (2) 91  (3) 73  (4) 85

**Answer: (3)** · key (compiled)

**Solution.** The lower boundary is $y=\max(0,\,1-2x)$ and the upper boundary is $y=4-x^2$ (down to $x=2$). Area $=\int_0^2(4-x^2)dx-\int_0^{1/2}(1-2x)dx=\left(8-\tfrac83\right)-\left(\tfrac12-\tfrac14\right)=\tfrac{16}3-\tfrac14=\tfrac{61}{12}$. So $\alpha+\beta=61+12=73$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · Numerical

Let the area of the region bounded by the curve $y=\max\{\sin x,\cos x\}$, the lines $x=0$, $x=\dfrac{3\pi}2$, and the $x$-axis be $A$. Then $A+A^2$ is equal to ______.

**Answer: 12** · key (compiled)

**Solution.** $\max\{\sin x,\cos x\}=\cos x$ on $[0,\tfrac\pi4]$, $\sin x$ on $[\tfrac\pi4,\tfrac{5\pi}4]$, $\cos x$ on $[\tfrac{5\pi}4,\tfrac{3\pi}2]$. Taking absolute values (area): $\int_0^{\pi/4}\cos x=\tfrac1{\sqrt2}$; $\int_{\pi/4}^{\pi}\sin x=1+\tfrac1{\sqrt2}$; $\int_\pi^{5\pi/4}|\sin x|=1-\tfrac1{\sqrt2}$; $\int_{5\pi/4}^{3\pi/2}|\cos x|=1-\tfrac1{\sqrt2}$. $A=3$ and $A+A^2=3+9=12$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let $P_1:y=4x^2$ and $P_2:y=x^2+27$ be two parabolas. If the area of the bounded region enclosed between $P_1$ and $P_2$ is six times the area of the bounded region enclosed between the line $y=\alpha x$, $\alpha>0$ and $P_1$, then $\alpha$ is equal to:

(1) 12  (2) 6  (3) 15  (4) 8

**Answer: (1)** · key (compiled)

**Solution.** $P_1\cap P_2$: $3x^2=27\Rightarrow x=\pm3$. Area between them $=\int_{-3}^3(27-3x^2)dx=2[27x-x^3]_0^3=108$. The line $y=\alpha x$ meets $y=4x^2$ at $x=0$ and $\tfrac\alpha4$, enclosing $\int_0^{\alpha/4}(\alpha x-4x^2)dx=\dfrac{\alpha^3}{32}-\dfrac{\alpha^3}{48}=\dfrac{\alpha^3}{96}$. Then $108=6\cdot\dfrac{\alpha^3}{96}\Rightarrow\alpha^3=1728\Rightarrow\alpha=12$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · MCQ

Let $f(\alpha)$ denote the area of the region in the first quadrant bounded by $x=0$, $x=1$, $y^2=x$ and $y=|\alpha x-5|-|1-\alpha x|+\alpha x^2$. Then $(f(0)+f(1))$ is equal to:

(1) 12  (2) 14  (3) 7  (4) 9

**Answer: (3)** · key (compiled)

**Solution.** $\alpha=0$: $y=5-1=4$, so the area between $y=4$ and $y=\sqrt x$ on $[0,1]$ is $\int_0^1(4-\sqrt x)dx=4-\tfrac23=\tfrac{10}3$. $\alpha=1$: for $0\le x\le1$, $|x-5|=5-x$ and $|1-x|=1-x$, so $y=4+x^2$; area $=\int_0^1(4+x^2-\sqrt x)dx=4+\tfrac13-\tfrac23=\tfrac{11}3$. Sum $=\tfrac{21}3=7$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · MCQ

The area of the region $A=\{(x,y):4x^2+y^2\le8\text{ and }y^2\le4x\}$ is:

(1) $\pi+4$  (2) $\pi+\dfrac23$  (3) $\dfrac\pi2+2$  (4) $\dfrac\pi2+\dfrac13$

**Answer: (2)** · key (compiled)

**Solution.** The ellipse $\tfrac{x^2}2+\tfrac{y^2}8=1$ and the parabola $y^2=4x$ meet where $4x^2+4x=8$, i.e. $x=1$, $y=\pm2$. Area $=2\int_0^12\sqrt x\,dx+2\int_1^{\sqrt2}\sqrt{8-4x^2}\,dx=\tfrac83+4\int_1^{\sqrt2}\sqrt{2-x^2}\,dx$. $\int_1^{\sqrt2}\sqrt{2-x^2}dx=\left[\tfrac x2\sqrt{2-x^2}+\sin^{-1}\tfrac x{\sqrt2}\right]_1^{\sqrt2}=\tfrac\pi2-\tfrac12-\tfrac\pi4=\tfrac\pi4-\tfrac12$. Total $=\tfrac83+\pi-2=\pi+\tfrac23$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q6 · MCQ

Let the line $x=-1$ divide the area of the region $\{(x,y):1+x^2\le y\le3-x\}$ in the ratio $m:n$, $\gcd(m,n)=1$. Then $m+n$ is equal to:

(1) 27  (2) 25  (3) 28  (4) 26

**Answer: (1)** · key (compiled)

**Solution.** The parabola $y=1+x^2$ and the line $y=3-x$ meet at $x=-2$ and $x=1$. Total area $=\int_{-2}^1(2-x-x^2)dx=\left[2x-\tfrac{x^2}2-\tfrac{x^3}3\right]_{-2}^1=\tfrac76+\tfrac{10}3=\tfrac92$. Left of $x=-1$: $\int_{-2}^{-1}(2-x-x^2)dx=\left(-\tfrac{13}6\right)-\left(-\tfrac{10}3\right)=\tfrac76$. Right: $\tfrac92-\tfrac76=\tfrac{10}3=\tfrac{20}6$. Ratio $7:20$, so $m+n=27$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q7 · MCQ

The area of the region enclosed between the circles $x^2+y^2=4$ and $x^2+(y-2)^2=4$ is:

(1) $\dfrac43(2\pi-3\sqrt3)$  (2) $\dfrac23(2\pi-3\sqrt3)$  (3) $\dfrac23(4\pi-3\sqrt3)$  (4) $\dfrac43(2\pi-\sqrt3)$

**Answer: (3)** · key (compiled)

**Solution.** Two circles of radius $r=2$ with centres $(0,0)$ and $(0,2)$ (distance $d=2$) intersect where $y=1$, $x=\pm\sqrt3$. The common (lens) region has area $2r^2\cos^{-1}\dfrac d{2r}-\dfrac d2\sqrt{4r^2-d^2}=8\cdot\dfrac\pi3-\sqrt{12}=\dfrac{8\pi}3-2\sqrt3=\dfrac23(4\pi-3\sqrt3)$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q8 · MCQ

The area of the region inside the ellipse $x^2+4y^2=4$ and outside the region bounded by the curves $y=|x|-1$ and $y=1-|x|$ is:

(1) $2\pi-1$  (2) $3(\pi-1)$  (3) $2\pi-\dfrac12$  (4) $2(\pi-1)$

**Answer: (4)** · key (compiled)

**Solution.** The ellipse $\tfrac{x^2}4+y^2=1$ has area $\pi\cdot2\cdot1=2\pi$. The two curves bound the square with vertices $(\pm1,0)$ and $(0,\pm1)$ (diagonals of length 2), of area $\tfrac12\cdot2\cdot2=2$; it lies inside the ellipse (its vertices $(0,\pm1)$ are on the ellipse). Required area $=2\pi-2=2(\pi-1)$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q9 · MCQ

The area of the region $R=\{(x,y):xy\le8,\ 1\le y\le x^2,\ x\ge0\}$ is:

(1) $\dfrac23(24\log_e2-7)$  (2) $\dfrac13(40\log_e2+27)$  (3) $\dfrac23(20\log_e2+9)$  (4) $\dfrac13(49\log_e2-15)$

**Answer: (1)** · key (compiled)

**Solution.** For a given $x$, $y$ runs from 1 up to $\min(x^2,\,8/x)$. The curves $y=x^2$ and $y=8/x$ meet at $(2,4)$; $y=x^2$ meets $y=1$ at $x=1$ and $y=\tfrac8x$ meets $y=1$ at $x=8$. Area $=\int_1^2(x^2-1)dx+\int_2^8\left(\dfrac8x-1\right)dx=\tfrac43+(16\ln2-6)=16\ln2-\tfrac{14}3=\dfrac23(24\ln2-7)$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q10 · MCQ

Let $A_1$ be the bounded area enclosed by the curves $y=x^2+2$, $x+y=8$ and the $y$-axis that lies in the first quadrant. Let $A_2$ be the bounded area enclosed by the curves $y=x^2+2$, $y^2=x$, $x=2$, and the $y$-axis that lies in the first quadrant. Then $A_1-A_2$ is equal to:

(1) $\dfrac23(3\sqrt2+1)$  (2) $\dfrac23(2\sqrt2+1)$  (3) $\dfrac23(\sqrt2+1)$  (4) $\dfrac23(4\sqrt2+1)$

**Answer: (2)** · key (compiled)

**Solution.** $y=x^2+2$ meets $x+y=8$ at $x=2$, $y=6$. $A_1=\int_0^2\left(8-x-x^2-2\right)dx=12-2-\tfrac83=\tfrac{22}3$. $A_2=\int_0^2\left(x^2+2-\sqrt x\right)dx=\tfrac83+4-\tfrac{4\sqrt2}3=\tfrac{20}3-\tfrac{4\sqrt2}3$. $A_1-A_2=\tfrac23+\tfrac{4\sqrt2}3=\dfrac23(2\sqrt2+1)$.

