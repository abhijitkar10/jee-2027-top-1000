# Trigonometry & Inverse Trigonometry

> Theory: [../../theory/maths/trigonometry.md](../../theory/maths/trigonometry.md)

### M-TRG-01 — JEE Main 2024 · 27 Jan Shift 1 · Q83 · Numerical

Let the set of all $a\in\mathbb R$ such that $\cos2x+a\sin x=2a-7$ has a solution be $[p,q]$, and let $r=\tan9^\circ-\tan27^\circ-\dfrac1{\cot63^\circ}+\tan81^\circ$. Then $pqr$ is ______.

**Answer: 48** · key ✔

**Solution.** With $s=\sin x$: $1-2s^2+as=2a-7\Rightarrow a(s-2)=2(s-2)(s+2)\Rightarrow a=2(s+2)$ (as $s\ne2$). For $s\in[-1,1]$, $a\in[2,6]$, so $p=2,q=6$. Next $\dfrac1{\cot63^\circ}=\tan63^\circ$, so $r=(\tan9^\circ+\tan81^\circ)-(\tan27^\circ+\tan63^\circ)=(\tan9^\circ+\cot9^\circ)-(\tan27^\circ+\cot27^\circ)=\dfrac2{\sin18^\circ}-\dfrac2{\sin54^\circ}$ (using $\tan\theta+\cot\theta=\tfrac2{\sin2\theta}$). With $\sin18^\circ=\tfrac{\sqrt5-1}4$ and $\sin54^\circ=\tfrac{\sqrt5+1}4$: $r=\tfrac8{\sqrt5-1}-\tfrac8{\sqrt5+1}=8\cdot\tfrac{2}{4}=4$. So $pqr=2\cdot6\cdot4=48$.

### M-TRG-02 — JEE Main 2024 · 27 Jan Shift 2 · Q70 · MCQ

Considering only principal values of inverse trigonometric functions, the number of positive real values of $x$ satisfying $\tan^{-1}x+\tan^{-1}2x=\dfrac\pi4$ is

(1) More than 2  (2) 1  (3) 2  (4) 0

**Answer: (2)** · key ✔

**Solution.** For $x>0$ the sum lies in $(0,\pi)$ and $2x^2<1$ is needed for the addition formula: $\dfrac{3x}{1-2x^2}=1\Rightarrow2x^2+3x-1=0\Rightarrow x=\dfrac{-3\pm\sqrt{17}}4$. Only $x=\dfrac{-3+\sqrt{17}}4\approx0.28>0$, and it satisfies $2x^2<1$. Exactly one positive solution.

### M-TRG-03 — JEE Main 2024 · 29 Jan Shift 1 · Q64 · MCQ

If $\alpha$, $-\dfrac\pi2<\alpha<\dfrac\pi2$, is the solution of $4\cos\theta+5\sin\theta=1$, then the value of $\tan\alpha$ is

(1) $\dfrac{10-\sqrt{10}}6$  (2) $\dfrac{10-\sqrt{10}}{12}$  (3) $\dfrac{\sqrt{10}-10}{12}$  (4) $\dfrac{\sqrt{10}-10}6$

**Answer: (3)** · key ✔

**Solution.** Let $m=\tan\alpha$. Since $\cos\alpha>0$ on this interval, $\cos\alpha=\dfrac1{\sqrt{1+m^2}}$ and $\sin\alpha=\dfrac m{\sqrt{1+m^2}}$, so $4+5m=\sqrt{1+m^2}$, which requires $4+5m>0$. Squaring: $24m^2+40m+15=0\Rightarrow m=\dfrac{-10\pm\sqrt{10}}{12}$. The root $\dfrac{-10-\sqrt{10}}{12}\approx-1.10$ gives $4+5m<0$ and is rejected. So $\tan\alpha=\dfrac{\sqrt{10}-10}{12}$.

### M-TRG-04 — JEE Main 2024 · 29 Jan Shift 1 · Q72 · MCQ

Consider $f:\left[\tfrac12,1\right]\to\mathbb R$, $f(x)=4\sqrt2\,x^3-3\sqrt2\,x-1$. Statements:
(I) The curve $y=f(x)$ intersects the $x$-axis at exactly one point.
(II) The curve $y=f(x)$ intersects the $x$-axis at $x=\cos\dfrac\pi{12}$.

(1) Only (II) is correct  (2) Both incorrect  (3) Only (I) is correct  (4) Both correct

**Answer: (4)** · key ✔

**Solution.** Put $x=\cos\theta$ with $\theta\in\left[0,\tfrac\pi3\right]$. Then $4x^3-3x=\cos3\theta$, so $f=\sqrt2\cos3\theta-1=0\Rightarrow\cos3\theta=\tfrac1{\sqrt2}$. For $3\theta\in[0,\pi]$ the only solution is $3\theta=\tfrac\pi4$, i.e. $\theta=\tfrac\pi{12}$. So there is exactly one intersection, at $x=\cos\tfrac\pi{12}\approx0.966\in\left[\tfrac12,1\right]$. Both are correct.

### M-TRG-05 — JEE Main 2024 · 29 Jan Shift 2 · Q65 · MCQ

The sum of the solutions $x\in\mathbb R$ of the equation $\dfrac{3\cos2x+\cos^32x}{\cos^6x-\sin^6x}=x^3-x^2+6$ is

(1) 0  (2) 1  (3) $-1$  (4) 3

**Answer: (3)** · key ✔

**Solution.** $\cos^6x-\sin^6x=\cos2x\left(1-\tfrac14\sin^22x\right)=\cos2x\cdot\dfrac{3+\cos^22x}4$, and the numerator is $\cos2x\,(3+\cos^22x)$. The LHS is therefore identically $4$ (where defined). So $x^3-x^2+6=4\Rightarrow x^3-x^2+2=0\Rightarrow(x+1)(x^2-2x+2)=0$, whose only real root is $x=-1$ (where $\cos2x\ne0$). Sum $=-1$.

### M-TRG-06 — JEE Main 2024 · 30 Jan Shift 1 · Q63 · MCQ

If $2\sin^3x+\sin2x\cos x+4\sin x-4=0$ has exactly $3$ solutions in the interval $\left[0,\dfrac{n\pi}2\right]$, $n\in\mathbb N$, then the roots of $x^2+nx+(n-3)=0$ belong to

(1) $(0,\infty)$  (2) $(-\infty,0)$  (3) $\left(-\dfrac{\sqrt{17}}2,\dfrac{\sqrt{17}}2\right)$  (4) $\mathbb Z$

**Answer: (2)** · key ✔

**Solution.** $\sin2x\cos x=2\sin x\cos^2x$, so the equation is $2\sin x(\sin^2x+\cos^2x)+4\sin x-4=0\Rightarrow\sin x=\tfrac23$. Solutions: $\alpha,\ \pi-\alpha,\ 2\pi+\alpha,\ 3\pi-\alpha,\dots$ with $\alpha=\sin^{-1}\tfrac23\approx0.73$. Exactly $3$ solutions need $2\pi+\alpha\le\tfrac{n\pi}2<3\pi-\alpha$, i.e. $4+\tfrac{2\alpha}\pi\le n<6-\tfrac{2\alpha}\pi$, i.e. $4.46\le n<5.54$, so $n=5$. Then $x^2+5x+2=0$ has roots $\dfrac{-5\pm\sqrt{17}}2$, both negative.

### M-TRG-07 — JEE Main 2024 · 31 Jan Shift 2 · Q72 · MCQ

If $a=\sin^{-1}(\sin5)$ and $b=\cos^{-1}(\cos5)$, then $a^2+b^2$ is equal to

(1) $4\pi^2+25$  (2) $8\pi^2-40\pi+50$  (3) $4\pi^2-20\pi+50$  (4) 25

**Answer: (2)** · key ✔

**Solution.** $5$ rad lies in $\left(\tfrac{3\pi}2,2\pi\right)$. The principal value of $\sin^{-1}$ must lie in $\left[-\tfrac\pi2,\tfrac\pi2\right]$: $a=5-2\pi$. For $\cos^{-1}$ (range $[0,\pi]$): $b=2\pi-5$. So $a^2+b^2=2(2\pi-5)^2=8\pi^2-40\pi+50$.

### M-TRG-08 — JEE Main 2024 · 1 Feb Shift 2 · Q65 · MCQ

The number of solutions of $4\sin^2x-4\cos^3x+9-4\cos x=0$, $x\in[-2\pi,2\pi]$ is:

(1) 1  (2) 3  (3) 2  (4) 0

**Answer: (4)** · key ✔

**Solution.** With $c=\cos x$: $4(1-c^2)-4c^3+9-4c=0\Rightarrow4c^3+4c^2+4c-13=0$. The cubic $g(c)=4c^3+4c^2+4c-13$ is increasing ($g'>0$) and $g(1)=-1<0$, so it has no root in $[-1,1]$. No solutions.

### § — JEE Main 2026 · 23 Jan Shift 1 · Identities set Q1 · MCQ

Let $\alpha$ and $\beta$ respectively be the maximum and the minimum values of the function $f(\theta)=4\left(\sin^4\!\left(\dfrac{7\pi}2-\theta\right)+\sin^4(11\pi+\theta)\right)-2\left(\sin^6\!\left(\dfrac{3\pi}2-\theta\right)+\sin^6(9\pi-\theta)\right)$, $\theta\in\mathbb R$. Then $\alpha+2\beta$ is equal to:

(1) 4  (2) 6  (3) 5  (4) 3

**Answer: (3)** · key (compiled)

**Solution.** Reduce the arguments: $\sin\left(\tfrac{7\pi}2-\theta\right)=-\cos\theta$, $\sin(11\pi+\theta)=-\sin\theta$, $\sin\left(\tfrac{3\pi}2-\theta\right)=-\cos\theta$, $\sin(9\pi-\theta)=\sin\theta$. So $f=4(\cos^4\theta+\sin^4\theta)-2(\cos^6\theta+\sin^6\theta)=4(1-2s^2c^2)-2(1-3s^2c^2)=2-2s^2c^2=2-\tfrac12\sin^22\theta$. Maximum $\alpha=2$, minimum $\beta=\tfrac32$, so $\alpha+2\beta=5$.

### § — JEE Main 2026 · 22 Jan Shift 2 · Identities set Q2 · Numerical

Let $\cos(\alpha+\beta)=-\dfrac1{10}$ and $\sin(\alpha-\beta)=\dfrac38$, where $0<\alpha<\dfrac\pi3$ and $0<\beta<\dfrac\pi4$. If $\tan2\alpha=\dfrac{3(1-r\sqrt5)}{\sqrt{11}(s+\sqrt5)}$, $r,s\in\mathbb N$, then $r+s$ is equal to ______.

**Answer: 20** · key (compiled)

**Solution.** $\alpha+\beta\in\left(0,\tfrac{7\pi}{12}\right)$ with negative cosine, so it lies in $\left(\tfrac\pi2,\tfrac{7\pi}{12}\right)$: $\sin(\alpha+\beta)=\tfrac{3\sqrt{11}}{10}$ and $\tan(\alpha+\beta)=-3\sqrt{11}$. $\alpha-\beta\in(0,\tfrac\pi3)$: $\cos(\alpha-\beta)=\tfrac{\sqrt{55}}8$ and $\tan(\alpha-\beta)=\tfrac3{\sqrt{55}}$. $\tan2\alpha=\dfrac{-3\sqrt{11}+\tfrac3{\sqrt{55}}}{1+\tfrac{9\sqrt{11}}{\sqrt{55}}}=\dfrac{3-3\sqrt{605}}{\sqrt{55}+9\sqrt{11}}=\dfrac{3(1-11\sqrt5)}{\sqrt{11}(9+\sqrt5)}$ using $\sqrt{605}=11\sqrt5$. So $r=11$, $s=9$ and $r+s=20$.

### § — JEE Main 2026 · 22 Jan Shift 1 · Identities set Q3 · Numerical

If $\dfrac{\cos^248^\circ-\sin^212^\circ}{\sin^224^\circ-\sin^26^\circ}=\dfrac{\alpha+\beta\sqrt5}2$, where $\alpha,\beta\in\mathbb N$, then $\alpha+\beta$ is equal to ______.

**Answer: 4** · key (compiled)

**Solution.** Use $\cos^2A-\sin^2B=\cos(A+B)\cos(A-B)$ and $\sin^2A-\sin^2B=\sin(A+B)\sin(A-B)$. Numerator $=\cos60^\circ\cos36^\circ=\tfrac12\cos36^\circ$; denominator $=\sin30^\circ\sin18^\circ=\tfrac12\sin18^\circ$. Ratio $=\dfrac{\cos36^\circ}{\sin18^\circ}=\dfrac{(1+\sqrt5)/4}{(\sqrt5-1)/4}=\dfrac{(1+\sqrt5)^2}{4}=\dfrac{3+\sqrt5}2$. So $\alpha=3$, $\beta=1$ and $\alpha+\beta=4$.

### § — JEE Main 2026 · 23 Jan Shift 2 · Identities set Q4 · MCQ

The least value of $\left(\cos^2\theta-6\sin\theta\cos\theta+3\sin^2\theta+2\right)$ is:

(1) $-1$  (2) 1  (3) $4-\sqrt{10}$  (4) $4+\sqrt{10}$

**Answer: (3)** · key (compiled)

**Solution.** $\cos^2\theta+3\sin^2\theta=2-\cos2\theta$ and $-6\sin\theta\cos\theta=-3\sin2\theta$. The expression is $4-(\cos2\theta+3\sin2\theta)$. Since $\cos2\theta+3\sin2\theta$ ranges over $[-\sqrt{10},\sqrt{10}]$, the least value is $4-\sqrt{10}$.

### § — JEE Main 2026 · 23 Jan Shift 2 · Identities set Q5 · MCQ

Let $\dfrac\pi2<\theta<\pi$ and $\cot\theta=-\dfrac1{2\sqrt2}$. Then the value of $\sin\left(\dfrac{15\theta}2\right)(\cos8\theta+\sin8\theta)+\cos\left(\dfrac{15\theta}2\right)(\cos8\theta-\sin8\theta)$ is equal to:

(1) $-\dfrac1{\sqrt3}$  (2) $\dfrac{\sqrt2-1}{\sqrt3}$  (3) $\dfrac{\sqrt2}{\sqrt3}$  (4) $\dfrac{1-\sqrt2}{\sqrt3}$

**Answer: (4)** · key (compiled)

**Solution.** Expanding and regrouping, the expression is $\sin\left(\tfrac{15\theta}2-8\theta\right)+\cos\left(8\theta-\tfrac{15\theta}2\right)=\sin\left(-\tfrac\theta2\right)+\cos\tfrac\theta2=\cos\tfrac\theta2-\sin\tfrac\theta2$. In the second quadrant $\sin\theta=\tfrac{2\sqrt2}3$, $\cos\theta=-\tfrac13$. With $\tfrac\theta2\in\left(\tfrac\pi4,\tfrac\pi2\right)$: $\cos\tfrac\theta2=\sqrt{\tfrac{1+\cos\theta}2}=\tfrac1{\sqrt3}$ and $\sin\tfrac\theta2=\sqrt{\tfrac{1-\cos\theta}2}=\tfrac{\sqrt2}{\sqrt3}$. The value is $\dfrac{1-\sqrt2}{\sqrt3}$.

### § — JEE Main 2026 · 21 Jan Shift 1 · Identities set Q6 · MCQ

The value of $\operatorname{cosec}10^\circ-\sqrt3\sec10^\circ$ is equal to:

(1) 8  (2) 6  (3) 2  (4) 4

**Answer: (4)** · key (compiled)

**Solution.** $\dfrac1{\sin10^\circ}-\dfrac{\sqrt3}{\cos10^\circ}=\dfrac{\cos10^\circ-\sqrt3\sin10^\circ}{\sin10^\circ\cos10^\circ}=\dfrac{2\cos70^\circ}{\tfrac12\sin20^\circ}=\dfrac{4\cos70^\circ}{\sin20^\circ}=4$.

### § — JEE Main 2026 · 28 Jan Shift 1 · Identities set Q7 · MCQ

If $\dfrac{\tan(A-B)}{\tan A}+\dfrac{\sin^2C}{\sin^2A}=1$, $A,B,C\in\left(0,\dfrac\pi2\right)$, then:

(1) $\tan A,\tan C,\tan B$ are in A.P.  (2) $\tan A,\tan B,\tan C$ are in G.P.  (3) $\tan A,\tan C,\tan B$ are in G.P.  (4) $\tan A,\tan B,\tan C$ are in A.P.

**Answer: (3)** · key (compiled)

**Solution.** Let $a=\tan A$, $b=\tan B$, $c=\tan C$. If $c^2=ab$, then $\dfrac{\tan(A-B)}{\tan A}=\dfrac{a-b}{a(1+ab)}$ and $\dfrac{\sin^2C}{\sin^2A}=\dfrac{c^2(1+a^2)}{a^2(1+c^2)}=\dfrac{b(1+a^2)}{a(1+ab)}$. Their sum is $\dfrac{(a-b)+b(1+a^2)}{a(1+ab)}=\dfrac{a(1+ab)}{a(1+ab)}=1$ ✓. So the given relation holds exactly when $\tan^2C=\tan A\tan B$, i.e. $\tan A,\tan C,\tan B$ are in G.P.

### § — JEE Main 2026 · 24 Jan Shift 1 · Identities set Q8 · MCQ

If $\cot x=\dfrac5{12}$ for some $x\in\left(\pi,\dfrac{3\pi}2\right)$, then $\sin7x\left(\cos\dfrac{13x}2+\sin\dfrac{13x}2\right)+\cos7x\left(\cos\dfrac{13x}2-\sin\dfrac{13x}2\right)$ is equal to:

(1) $\dfrac4{\sqrt{26}}$  (2) $\dfrac6{\sqrt{26}}$  (3) $\dfrac5{\sqrt{13}}$  (4) $\dfrac1{\sqrt{13}}$

**Answer: (4)** · key (compiled)

**Solution.** Regrouping, the expression is $\sin\left(7x-\tfrac{13x}2\right)+\cos\left(7x-\tfrac{13x}2\right)=\sin\tfrac x2+\cos\tfrac x2$. In the third quadrant $\cos x=-\tfrac5{13}$. Since $\tfrac x2\in\left(\tfrac\pi2,\tfrac{3\pi}4\right)$: $\cos\tfrac x2=-\sqrt{\tfrac{1+\cos x}2}=-\tfrac2{\sqrt{13}}$ and $\sin\tfrac x2=\sqrt{\tfrac{1-\cos x}2}=\tfrac3{\sqrt{13}}$. Sum $=\dfrac1{\sqrt{13}}$.

### § — JEE Main 2026 · 24 Jan Shift 1 · Identities set Q9 · MCQ

The value of $\dfrac{\sqrt3\operatorname{cosec}20^\circ-\sec20^\circ}{\cos20^\circ\cos40^\circ\cos60^\circ\cos80^\circ}$ is equal to:

(1) 16  (2) 32  (3) 64  (4) 12

**Answer: (3)** · key (compiled)

**Solution.** Numerator: $\dfrac{\sqrt3\cos20^\circ-\sin20^\circ}{\sin20^\circ\cos20^\circ}=\dfrac{2\cos50^\circ}{\tfrac12\sin40^\circ}=\dfrac{4\cos50^\circ}{\sin40^\circ}=4$. Denominator: $\cos20^\circ\cos40^\circ\cos80^\circ=\dfrac{\cos60^\circ}4=\dfrac18$ (using $\cos A\cos(60^\circ-A)\cos(60^\circ+A)=\tfrac{\cos3A}4$), and with $\cos60^\circ=\tfrac12$ the product is $\tfrac1{16}$. Ratio $=4\times16=64$.

### § — JEE Main 2026 · 21 Jan Shift 2 · Inverse set Q1 · Numerical

Let the maximum value of $(\sin^{-1}x)^2+(\cos^{-1}x)^2$ for $x\in\left[-\dfrac{\sqrt3}2,\dfrac1{\sqrt2}\right]$ be $\dfrac mn\pi^2$, where $\gcd(m,n)=1$. Then $m+n$ is equal to ______.

**Answer: 65** · key (compiled)

**Solution.** Let $\alpha=\sin^{-1}x\in\left[-\tfrac\pi3,\tfrac\pi4\right]$. Then $f=\alpha^2+\left(\tfrac\pi2-\alpha\right)^2=2\left(\alpha-\tfrac\pi4\right)^2+\tfrac{\pi^2}8$, a parabola in $\alpha$ with its vertex at $\alpha=\tfrac\pi4$ (the right end of the interval). The maximum is at the farthest end, $\alpha=-\tfrac\pi3$: $f=2\left(\tfrac{7\pi}{12}\right)^2+\tfrac{\pi^2}8=\tfrac{49\pi^2}{72}+\tfrac{9\pi^2}{72}=\tfrac{29}{36}\pi^2$. So $m+n=29+36=65$.

### § — JEE Main 2026 · 28 Jan Shift 2 · Inverse set Q2 · MCQ

Considering the principal values of inverse trigonometric functions, the value of the expression $\tan\left(2\sin^{-1}\!\left(\dfrac2{\sqrt{13}}\right)-2\cos^{-1}\!\left(\dfrac3{\sqrt{10}}\right)\right)$ is equal to:

(1) $\dfrac{16}{63}$  (2) $-\dfrac{33}{56}$  (3) $-\dfrac{16}{63}$  (4) $\dfrac{33}{56}$

**Answer: (4)** · key (compiled)

**Solution.** Let $\alpha=\sin^{-1}\dfrac2{\sqrt{13}}$: $\tan\alpha=\tfrac23$, so $\tan2\alpha=\dfrac{4/3}{1-4/9}=\dfrac{12}5$. Let $\gamma=\cos^{-1}\dfrac3{\sqrt{10}}$: $\tan\gamma=\tfrac13$, so $\tan2\gamma=\dfrac{2/3}{1-1/9}=\dfrac34$. $\tan(2\alpha-2\gamma)=\dfrac{\tfrac{12}5-\tfrac34}{1+\tfrac{12}5\cdot\tfrac34}=\dfrac{33/20}{56/20}=\dfrac{33}{56}$.

### § — JEE Main 2026 · 24 Jan Shift 2 · Inverse set Q3 · MCQ

If the domain of the function $f(x)=\sin^{-1}\!\left(\dfrac1{x^2-2x-2}\right)$ is $(-\infty,\alpha]\cup[\beta,\gamma]\cup[\delta,\infty)$, then $\alpha+\beta+\gamma+\delta$ is equal to:

(1) 2  (2) 3  (3) 4  (4) 5

**Answer: (3)** · key (compiled)

**Solution.** We need $\left|\dfrac1{x^2-2x-2}\right|\le1$, i.e. $|x^2-2x-2|\ge1$. Either $x^2-2x-2\ge1\Rightarrow(x-3)(x+1)\ge0\Rightarrow x\le-1$ or $x\ge3$; or $x^2-2x-2\le-1\Rightarrow(x-1)^2\le2\Rightarrow1-\sqrt2\le x\le1+\sqrt2$. Domain $(-\infty,-1]\cup[1-\sqrt2,1+\sqrt2]\cup[3,\infty)$, so $\alpha+\beta+\gamma+\delta=-1+(1-\sqrt2)+(1+\sqrt2)+3=4$.

### § — JEE Main 2026 · 22 Jan Shift 1 · Inverse set Q4 · MCQ

The number of solutions of $\tan^{-1}4x+\tan^{-1}6x=\dfrac\pi6$, where $-\dfrac1{2\sqrt6}<x<\dfrac1{2\sqrt6}$, is equal to:

(1) 3  (2) 0  (3) 2  (4) 1

**Answer: (4)** · key (compiled)

**Solution.** In the given range $24x^2<1$, so $\tan^{-1}4x+\tan^{-1}6x=\tan^{-1}\dfrac{10x}{1-24x^2}$ with no $\pi$ correction. Then $\dfrac{10x}{1-24x^2}=\dfrac1{\sqrt3}\Rightarrow24x^2+10\sqrt3x-1=0\Rightarrow x=\dfrac{-5\sqrt3\pm3\sqrt{11}}{24}$. $x_1\approx0.054$ lies in the interval (since $\tfrac1{2\sqrt6}\approx0.204$) and $x_2\approx-0.776$ does not. So there is 1 solution.

### § — JEE Main 2026 · 21 Jan Shift 1 · Inverse set Q5 · MCQ

If the domain of the function $f(x)=\cos^{-1}\!\left(\dfrac{2x-5}{11-3x}\right)+\sin^{-1}\!\left(2x^2-3x+1\right)$ is the interval $[\alpha,\beta]$, then $\alpha+2\beta$ is equal to:

(1) 3  (2) 5  (3) 1  (4) 2

**Answer: (1)** · key (compiled)

**Solution.** $\left|\dfrac{2x-5}{11-3x}\right|\le1\Rightarrow(2x-5)^2\le(11-3x)^2\Rightarrow(5x-16)(x-6)\ge0\Rightarrow x\le\tfrac{16}5$ or $x\ge6$. $|2x^2-3x+1|\le1$: the upper bound gives $x(2x-3)\le0\Rightarrow0\le x\le\tfrac32$, and the lower bound $2x^2-3x+2\ge0$ always holds (negative discriminant). The intersection is $\left[0,\tfrac32\right]$, so $\alpha=0$, $\beta=\tfrac32$ and $\alpha+2\beta=3$.

### § — JEE Main 2026 · 28 Jan Shift 1 · Inverse set Q6 · Numerical

If $k=\tan\left(\dfrac\pi4+\dfrac12\cos^{-1}\!\left(\dfrac23\right)\right)+\tan\left(\dfrac12\sin^{-1}\!\left(\dfrac23\right)\right)$, then the number of solutions of the equation $\sin^{-1}(kx-1)=\sin^{-1}x-\cos^{-1}x$ is ______.

**Answer: 1** · key (compiled)

**Solution.** Let $\theta=\tfrac12\sin^{-1}\tfrac23$. Since $\cos^{-1}\tfrac23=\tfrac\pi2-2\theta$, we get $\tfrac\pi4+\tfrac12\cos^{-1}\tfrac23=\tfrac\pi2-\theta$ and $k=\cot\theta+\tan\theta=\dfrac2{\sin2\theta}=\dfrac2{2/3}=3$. For $\varphi=\cos^{-1}x$: $\sin^{-1}x-\cos^{-1}x=\tfrac\pi2-2\varphi$, which lies in the range of $\sin^{-1}$ only for $\varphi\in[0,\tfrac\pi2]$, i.e. $x\in[0,1]$. Then $3x-1=\sin\left(\tfrac\pi2-2\varphi\right)=\cos2\varphi=2x^2-1\Rightarrow x(2x-3)=0\Rightarrow x=0$ (the root $\tfrac32$ is outside $[0,1]$). Check $x=0$: $\sin^{-1}(-1)=-\tfrac\pi2=0-\tfrac\pi2$ ✓. One solution.

### § — JEE Main 2026 · 23 Jan Shift 1 · Trig set Q1 · MCQ

The number of solutions of $\sqrt3\cos2\theta+8\cos\theta+3\sqrt3=0$, $\theta\in[-3\pi,2\pi]$ is:

(1) 0  (2) 5  (3) 3  (4) 4

**Answer: (2)** · key (compiled)

**Solution.** With $\cos2\theta=2\cos^2\theta-1$: $2\sqrt3\cos^2\theta+8\cos\theta+2\sqrt3=0\Rightarrow\sqrt3\cos^2\theta+4\cos\theta+\sqrt3=0\Rightarrow\cos\theta=\dfrac{-4\pm2}{2\sqrt3}$, i.e. $\cos\theta=-\dfrac1{\sqrt3}$ or $-\sqrt3$ (rejected, $|\cos\theta|\le1$). Let $\alpha=\cos^{-1}\left(-\tfrac1{\sqrt3}\right)\approx2.19$ rad; solutions are $\theta=2n\pi\pm\alpha$. In $[-3\pi,2\pi]\approx[-9.42,6.28]$: $\alpha$, $-\alpha$, $2\pi-\alpha$, $-2\pi+\alpha$, $-2\pi-\alpha$ — five values.

### § — JEE Main 2026 · 24 Jan Shift 2 · Trig set Q2 · Numerical

The number of elements in the set $\{x\in[0,180^\circ]:\tan(x+100^\circ)=\tan(x+50^\circ)\tan x\tan(x-50^\circ)\}$ is ______.

**Answer: 4** · key (compiled)

**Solution.** Put $t=\tan x$, $T=\tan50^\circ$, and use $\tan(x+50^\circ)\tan(x-50^\circ)=\dfrac{t^2-T^2}{1-t^2T^2}$ and $\tan100^\circ=\dfrac{2T}{1-T^2}=\tau$. The equation $\dfrac{t+\tau}{1-t\tau}=\dfrac{t(t^2-T^2)}{1-t^2T^2}$ reduces to $t^4-mt^3-2T^2t^2+mt+1=0$ with $m=\dfrac{1-T^4}{2T}$. Dividing by $t^2$ and setting $s=t-\dfrac1t=-2\cot2x$ gives the quadratic $s^2-ms+2(1-T^2)=0$, with roots $s\approx0.728$ and $-1.155$. Then $\tan2x=-2.75=\tan(-70^\circ)$, giving $2x=110^\circ,290^\circ$, i.e. $x=55^\circ,145^\circ$; and $\tan2x=\sqrt3$, giving $2x=60^\circ,240^\circ$, i.e. $x=30^\circ,120^\circ$. (Check $x=30^\circ$: LHS $\tan130^\circ=-1.192$ and RHS $\tan80^\circ\tan30^\circ\tan(-20^\circ)=-1.192$ ✓.) So the set has 4 elements: $\{30^\circ,55^\circ,120^\circ,145^\circ\}$.

