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

### M-LCD-07 — JEE Main 2024 · 30 Jan Shift 2 · Q72 · MCQ

Let $a$ and $b$ be real constants such that $f(x)=\begin{cases}x^2+3x+a,&x\le1\\bx+2,&x>1\end{cases}$ is differentiable on $\mathbb R$. Then $\displaystyle\int_{-2}^2f(x)\,dx$ equals

(1) $\tfrac{15}6$  (2) $\tfrac{19}6$  (3) 21  (4) 17

**Answer: (4)** · key ✔

**Solution.** Differentiability at $1$: derivatives $2+3=5=b$. Continuity: $1+3+a=b+2\Rightarrow a=3$. $\int_{-2}^1(x^2+3x+3)dx=\left[\tfrac{x^3}3+\tfrac{3x^2}2+3x\right]_{-2}^1=\tfrac{29}6-\left(-\tfrac83\right)=7.5$ and $\int_1^2(5x+2)dx=\left[\tfrac{5x^2}2+2x\right]_1^2=14-4.5=9.5$. Total $=17$.

### M-LCD-08 — JEE Main 2024 · 30 Jan Shift 2 · Q73 · MCQ

Let $f:\mathbb R-\{0\}\to\mathbb R$ satisfy $f\!\left(\dfrac xy\right)=\dfrac{f(x)}{f(y)}$ for all $x,y$ with $f(y)\ne0$. If $f'(1)=2024$, then

(1) $xf'(x)-2024f(x)=0$  (2) $xf'(x)+2024f(x)=0$  (3) $xf'(x)+f(x)=2024$  (4) $xf'(x)-2023f(x)=0$

**Answer: (1)** · key ✔

**Solution.** Differentiate with respect to $x$ (keeping $y$ fixed): $\dfrac1yf'\!\left(\dfrac xy\right)=\dfrac{f'(x)}{f(y)}$. Put $y=x$: $\dfrac1xf'(1)=\dfrac{f'(x)}{f(x)}\Rightarrow xf'(x)=2024f(x)$, i.e. $xf'(x)-2024f(x)=0$. (Indeed $f(x)=x^{2024}$ works.)

### M-LCD-09 — JEE Main 2024 · 31 Jan Shift 1 · Q67 · MCQ

$\displaystyle\lim_{x\to0}\dfrac{e^{2\sin x}-2\sin x-1}{x^2}$

(1) is equal to $-1$  (2) does not exist  (3) is equal to $1$  (4) is equal to $2$

**Answer: (4)** · key ✔

**Solution.** Let $u=2\sin x\to0$. $e^u-u-1=\dfrac{u^2}2+\dots$, so the numerator $\approx\dfrac{(2\sin x)^2}2=2\sin^2x\approx2x^2$. The limit is $2$.

### M-LCD-10 — JEE Main 2024 · 31 Jan Shift 2 · Q69 · MCQ

Let $f:\mathbb R\to(0,\infty)$ be a strictly increasing function such that $\displaystyle\lim_{x\to\infty}\frac{f(7x)}{f(x)}=1$. Then the value of $\displaystyle\lim_{x\to\infty}\left(\frac{f(5x)}{f(x)}-1\right)$ is equal to

(1) 4  (2) 0  (3) $\tfrac75$  (4) 1

**Answer: (2)** · key ✔

**Solution.** Since $f$ is strictly increasing, for $x>0$: $f(x)<f(5x)<f(7x)$, so $1<\dfrac{f(5x)}{f(x)}<\dfrac{f(7x)}{f(x)}\to1$. By the squeeze theorem $\dfrac{f(5x)}{f(x)}\to1$ and the required limit is $0$.

### M-LCD-11 — JEE Main 2024 · 1 Feb Shift 1 · Q73 · MCQ

Let $f:\mathbb R\to\mathbb R$ be $f(x)=\begin{cases}\dfrac{a-b\cos2x}{x^2}, & x<0\\ x^2+cx+2, & 0\le x\le1\\ 2x+1, & x>1\end{cases}$. If $f$ is continuous everywhere and $m$ is the number of points where $f$ is NOT differentiable, then $m+a+b+c$ equals:

(1) 1  (2) 4  (3) 3  (4) 2

**Answer: (4)** · key ✔

**Solution.** For the left limit at $0$ to exist we need $a=b$; then $\dfrac{a(1-\cos2x)}{x^2}=\dfrac{2a\sin^2x}{x^2}\to 2a$. Continuity: $2a=2\Rightarrow a=b=1$. At $x=1$: $1+c+2=3\Rightarrow c=0$. Derivatives: at $0^-$ the function $2\sin^2x/x^2=2-\tfrac23x^2+\dots$ has slope $0$, and at $0^+$ the slope is $c=0$; at $1^-$ slope is $2x+c=2$ and at $1^+$ it is $2$. So $f$ is differentiable everywhere, $m=0$, and $m+a+b+c=2$.

### M-LCD-12 — JEE Main 2024 · 4 Apr Shift 1 · Q73 · MCQ

Let $f(x)=\begin{cases}\dfrac{1-\cos2x}{x^2}, & x<0\\ \alpha, & x=0\\ \dfrac{\beta\sqrt{1-\cos x}}{x}, & x>0\end{cases}$. If $f$ is continuous at $x=0$, then $\alpha^2+\beta^2$ is:

(1) 3  (2) 12  (3) 48  (4) 6

**Answer: (2)** · key ✔

**Solution.** Left limit: $\dfrac{2\sin^2x}{x^2}\to2$. Right limit: $\dfrac{\beta\sqrt2\,|\sin(x/2)|}{x}\to\dfrac{\beta\sqrt2}{2}=\dfrac\beta{\sqrt2}$ as $x\to0^+$. Equating: $\alpha=2$, $\beta=2\sqrt2$. $\alpha^2+\beta^2=4+8=12$.

