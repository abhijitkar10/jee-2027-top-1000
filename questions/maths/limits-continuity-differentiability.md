# Limits, Continuity & Differentiability

> Theory: [../../theory/maths/limits-continuity-differentiability.md](../../theory/maths/limits-continuity-differentiability.md)

### M-LCD-01 — JEE Main 2024 · 27 Jan Shift 1 · Q69 · MCQ

Let $a=\displaystyle\lim_{x\to0}\frac{\sqrt{1+\sqrt{1+x^4}}-\sqrt2}{x^4}$ and $b=\displaystyle\lim_{x\to0}\frac{\sin^2x}{\sqrt2-\sqrt{1+\cos x}}$. Then $ab^3$ is

(1) 36  (2) 32  (3) 25  (4) 30

**Answer: (2)** · key ✔

**Solution.** With $u=x^4$: $\dfrac{d}{du}\sqrt{1+\sqrt{1+u}}\Big|_0=\dfrac1{2\sqrt2}\cdot\dfrac12$, so $a=\dfrac1{4\sqrt2}$. For $b$: $\sqrt2-\sqrt{1+\cos x}=\dfrac{1-\cos x}{\sqrt2+\sqrt{1+\cos x}}$ and $\sin^2x=(1-\cos x)(1+\cos x)$, so $b=\lim(1+\cos x)(\sqrt2+\sqrt{1+\cos x})=2\cdot2\sqrt2=4\sqrt2$. Then $ab^3=\dfrac{(4\sqrt2)^3}{4\sqrt2}=(4\sqrt2)^2=32$.

### M-LCD-02 — JEE Main 2024 · 27 Jan Shift 1 · Q74 · MCQ

Let $f(x)=\begin{cases}\dfrac{a\,(7x-12-x^2)}{b\,|x^2-7x+12|}, & x<3\\[2mm] 2\,\dfrac{\sin(x-3)}{x-[x]}, & x>3\\[2mm] b, & x=3\end{cases}$, where $[x]$ is the greatest integer $\le x$. If $S$ is the set of all ordered pairs $(a,b)$ such that $f$ is continuous at $x=3$, the number of elements in $S$ is

(1) 2  (2) Infinitely many  (3) 4  (4) 1

**Answer: (4)** · key ✔

**Solution.** For $x<3$ near 3: $x^2-7x+12=(x-3)(x-4)>0$, so $|\cdot|=(x-3)(x-4)$, while $7x-12-x^2=-(x-3)(x-4)$. Hence LHL $=-a/b$. For $x>3$ near 3: $[x]=3$, so RHL $=\lim 2\dfrac{\sin(x-3)}{x-3}=2$. Continuity: $-a/b=2=b$, so $b=2,\ a=-4$. Exactly one pair.

### M-LCD-03 — JEE Main 2024 · 27 Jan Shift 2 · Q68 · MCQ

If $\displaystyle\lim_{x\to0}\frac{3+\alpha\sin x+\beta\cos x+\ln(1-x)}{3\tan^2x}=\frac13$, then $2\alpha-\beta$ is equal to

(1) 2  (2) 7  (3) 5  (4) 1

**Answer: (3)** · key ✔

**Solution.** The denominator $\to0$, so the numerator must vanish at $0$: $3+\beta=0\Rightarrow\beta=-3$. Expanding: $\alpha x-3\left(1-\tfrac{x^2}2\right)+3-x-\tfrac{x^2}2+\dots=(\alpha-1)x+x^2+\dots$. The limit is finite only if $\alpha=1$, and then it equals $\dfrac{x^2}{3x^2}=\dfrac13$ as required. So $2\alpha-\beta=2+3=5$.

### M-LCD-04 — JEE Main 2024 · 27 Jan Shift 2 · Q72 · MCQ

Consider $f:(0,2)\to\mathbb R$, $f(x)=\dfrac x2+\dfrac2x$, and $g(x)=\begin{cases}\min\{f(t):0<t\le x\}, & 0<x\le1\\[1mm]\tfrac32+x, & 1<x<2\end{cases}$. Then

(1) $g$ is continuous but not differentiable at $x=1$  (2) $g$ is not continuous for all $x\in(0,2)$  (3) $g$ is neither continuous nor differentiable at $x=1$  (4) $g$ is continuous and differentiable for all $x\in(0,2)$

**Answer: (1)** · key ✔

**Solution.** $f'(x)=\tfrac12-\tfrac2{x^2}<0$ on $(0,2)$, so $f$ is decreasing and $\min_{0<t\le x}f(t)=f(x)$. Thus $g(x)=\tfrac x2+\tfrac2x$ on $(0,1]$ with $g(1)=\tfrac52$, and $g(1^+)=\tfrac32+1=\tfrac52$: continuous. Left derivative $\tfrac12-2=-\tfrac32$, right derivative $1$: unequal, so not differentiable at $x=1$.

### M-LCD-05 — JEE Main 2024 · 30 Jan Shift 1 · Q68 · MCQ

Let $f:\left[-\dfrac\pi2,\dfrac\pi2\right]\to\mathbb R$ be a differentiable function with $f(0)=\dfrac12$. If $\displaystyle\lim_{x\to0}\frac{x\int_0^xf(t)\,dt}{e^{x^2}-1}=\alpha$, then $8\alpha^2$ is equal to

(1) 16  (2) 2  (3) 1  (4) 4

**Answer: (2)** · key ✔

**Solution.** Near $0$: $\int_0^xf(t)dt\approx xf(0)=\tfrac x2$ and $e^{x^2}-1\approx x^2$. So the limit is $\dfrac{x\cdot x/2}{x^2}=\tfrac12=\alpha$, and $8\alpha^2=2$.

### M-LCD-06 — JEE Main 2024 · 30 Jan Shift 1 · Q87 · Numerical

If the function $f(x)=\begin{cases}\dfrac1{|x|}, & |x|\ge2\\ ax^2+2b, & |x|<2\end{cases}$ is differentiable on $\mathbb R$, then $48(a+b)$ is equal to ______.

**Answer: 15** · key ✔

**Solution.** At $x=2$: continuity gives $4a+2b=\tfrac12$. Differentiability: right derivative $-\dfrac1{x^2}=-\tfrac14$ equals left derivative $2ax=4a$, so $a=-\tfrac1{16}$. Then $-\tfrac14+2b=\tfrac12\Rightarrow b=\tfrac38$. $a+b=\tfrac5{16}$ and $48(a+b)=15$. (The function is even, so $x=-2$ gives the same conditions.)

