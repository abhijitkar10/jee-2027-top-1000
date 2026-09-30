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

