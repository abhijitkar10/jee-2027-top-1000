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

### M-LCD-05 — JEE Main 2024 · 30 Jan Shift 1 · Q87 · Numerical

If the function $f(x)=\begin{cases}\dfrac1{|x|}, & |x|\ge2\\ ax^2+2b, & |x|<2\end{cases}$ is differentiable on $\mathbb R$, then $48(a+b)$ is equal to ______.

**Answer: 15** · key ✔

**Solution.** At $x=2$: continuity gives $4a+2b=\tfrac12$. Differentiability: right derivative $-\dfrac1{x^2}=-\tfrac14$ equals left derivative $2ax=4a$, so $a=-\tfrac1{16}$. Then $-\tfrac14+2b=\tfrac12\Rightarrow b=\tfrac38$. $a+b=\tfrac5{16}$ and $48(a+b)=15$. (The function is even, so $x=-2$ gives the same conditions.)

### M-LCD-06 — JEE Main 2024 · 30 Jan Shift 2 · Q72 · MCQ

Let $a$ and $b$ be real constants such that $f(x)=\begin{cases}x^2+3x+a,&x\le1\\bx+2,&x>1\end{cases}$ is differentiable on $\mathbb R$. Then $\displaystyle\int_{-2}^2f(x)\,dx$ equals

(1) $\tfrac{15}6$  (2) $\tfrac{19}6$  (3) 21  (4) 17

**Answer: (4)** · key ✔

**Solution.** Differentiability at $1$: derivatives $2+3=5=b$. Continuity: $1+3+a=b+2\Rightarrow a=3$. $\int_{-2}^1(x^2+3x+3)dx=\left[\tfrac{x^3}3+\tfrac{3x^2}2+3x\right]_{-2}^1=\tfrac{29}6-\left(-\tfrac83\right)=7.5$ and $\int_1^2(5x+2)dx=\left[\tfrac{5x^2}2+2x\right]_1^2=14-4.5=9.5$. Total $=17$.

### M-LCD-07 — JEE Main 2024 · 30 Jan Shift 2 · Q73 · MCQ

Let $f:\mathbb R-\{0\}\to\mathbb R$ satisfy $f\!\left(\dfrac xy\right)=\dfrac{f(x)}{f(y)}$ for all $x,y$ with $f(y)\ne0$. If $f'(1)=2024$, then

(1) $xf'(x)-2024f(x)=0$  (2) $xf'(x)+2024f(x)=0$  (3) $xf'(x)+f(x)=2024$  (4) $xf'(x)-2023f(x)=0$

**Answer: (1)** · key ✔

**Solution.** Differentiate with respect to $x$ (keeping $y$ fixed): $\dfrac1yf'\!\left(\dfrac xy\right)=\dfrac{f'(x)}{f(y)}$. Put $y=x$: $\dfrac1xf'(1)=\dfrac{f'(x)}{f(x)}\Rightarrow xf'(x)=2024f(x)$, i.e. $xf'(x)-2024f(x)=0$. (Indeed $f(x)=x^{2024}$ works.)

### M-LCD-08 — JEE Main 2024 · 31 Jan Shift 2 · Q69 · MCQ

Let $f:\mathbb R\to(0,\infty)$ be a strictly increasing function such that $\displaystyle\lim_{x\to\infty}\frac{f(7x)}{f(x)}=1$. Then the value of $\displaystyle\lim_{x\to\infty}\left(\frac{f(5x)}{f(x)}-1\right)$ is equal to

(1) 4  (2) 0  (3) $\tfrac75$  (4) 1

**Answer: (2)** · key ✔

**Solution.** Since $f$ is strictly increasing, for $x>0$: $f(x)<f(5x)<f(7x)$, so $1<\dfrac{f(5x)}{f(x)}<\dfrac{f(7x)}{f(x)}\to1$. By the squeeze theorem $\dfrac{f(5x)}{f(x)}\to1$ and the required limit is $0$.

### M-LCD-09 — JEE Main 2024 · 1 Feb Shift 1 · Q73 · MCQ

Let $f:\mathbb R\to\mathbb R$ be $f(x)=\begin{cases}\dfrac{a-b\cos2x}{x^2}, & x<0\\ x^2+cx+2, & 0\le x\le1\\ 2x+1, & x>1\end{cases}$. If $f$ is continuous everywhere and $m$ is the number of points where $f$ is NOT differentiable, then $m+a+b+c$ equals:

(1) 1  (2) 4  (3) 3  (4) 2

**Answer: (4)** · key ✔

**Solution.** For the left limit at $0$ to exist we need $a=b$; then $\dfrac{a(1-\cos2x)}{x^2}=\dfrac{2a\sin^2x}{x^2}\to 2a$. Continuity: $2a=2\Rightarrow a=b=1$. At $x=1$: $1+c+2=3\Rightarrow c=0$. Derivatives: at $0^-$ the function $2\sin^2x/x^2=2-\tfrac23x^2+\dots$ has slope $0$, and at $0^+$ the slope is $c=0$; at $1^-$ slope is $2x+c=2$ and at $1^+$ it is $2$. So $f$ is differentiable everywhere, $m=0$, and $m+a+b+c=2$.

### M-LCD-10 — JEE Main 2024 · 4 Apr Shift 1 · Q73 · MCQ

Let $f(x)=\begin{cases}\dfrac{1-\cos2x}{x^2}, & x<0\\ \alpha, & x=0\\ \dfrac{\beta\sqrt{1-\cos x}}{x}, & x>0\end{cases}$. If $f$ is continuous at $x=0$, then $\alpha^2+\beta^2$ is:

(1) 3  (2) 12  (3) 48  (4) 6

**Answer: (2)** · key ✔

**Solution.** Left limit: $\dfrac{2\sin^2x}{x^2}\to2$. Right limit: $\dfrac{\beta\sqrt2\,|\sin(x/2)|}{x}\to\dfrac{\beta\sqrt2}{2}=\dfrac\beta{\sqrt2}$ as $x\to0^+$. Equating: $\alpha=2$, $\beta=2\sqrt2$. $\alpha^2+\beta^2=4+8=12$.

### M-LCD-11 — JEE Main 2024 · 4 Apr Shift 2 · Q68 · MCQ

Let $f(x)=\displaystyle\int_0^x\left(t+\sin(1-e^t)\right)dt$. Then $\displaystyle\lim_{x\to0}\frac{f(x)}{x^3}$ is:

(1) $-\tfrac16$  (2) $\tfrac23$  (3) $-\tfrac23$  (4) $\tfrac16$

**Answer: (1)** · key ✔

**Solution.** By L'Hôpital: $\lim\dfrac{x+\sin(1-e^x)}{3x^2}$. With $u=1-e^x=-x-\tfrac{x^2}{2}-\tfrac{x^3}{6}$ and $\sin u=u-\tfrac{u^3}{6}=-x-\tfrac{x^2}2-\tfrac{x^3}6+\tfrac{x^3}{6}+\dots$, we get $x+\sin u=-\tfrac{x^2}{2}+O(x^4)$. Limit $=\dfrac{-1/2}{3}=-\dfrac16$.

### M-LCD-12 — JEE Main 2024 · 4 Apr Shift 2 · Q73 · MCQ

If $f(x)=\begin{cases}\dfrac{72^x-9^x-8^x+1}{\sqrt2-\sqrt{1+\cos x}}, & x\ne0\\ a\ln2\ln3, & x=0\end{cases}$ is continuous at $x=0$, then $a^2$ is:

(1) 968  (2) 1152  (3) 746  (4) 1250

**Answer: (2)** · key ✔

**Solution.** Numerator $=(9^x-1)(8^x-1)\approx(x\ln9)(x\ln8)=6\ln2\ln3\,x^2$. Denominator: $\sqrt{1+\cos x}=\sqrt{2-x^2/2}\approx\sqrt2\left(1-\tfrac{x^2}{8}\right)$, so $\sqrt2-\sqrt{1+\cos x}\approx\dfrac{\sqrt2x^2}{8}$. Limit $=\dfrac{6\cdot8}{\sqrt2}\ln2\ln3=24\sqrt2\ln2\ln3$. So $a=24\sqrt2$ and $a^2=1152$.

### M-LCD-13 — JEE Advanced 2025 · Paper 1 · Q3 · MCQ

Define $f:\mathbb R\to\mathbb R$ by $f(x)=2-2x^2-x^2\sin\dfrac1x$ for $x\ne0$ and $f(0)=2$. Which statement is TRUE?

(A) $f$ is NOT differentiable at $x=0$  (B) There is $\delta>0$ such that $f$ is decreasing on $(0,\delta)$  (C) For any $\delta>0$, $f$ is NOT an increasing function on $(-\delta,0)$  (D) $x=0$ is a point of local minima of $f$

**Answer: (C)** · official key ✔ (re-derived)

**Solution.** $\dfrac{f(h)-f(0)}{h}=-2h-h\sin\dfrac1h\to0$, so $f'(0)=0$ and (A) is false. Because $x^2(2+\sin\tfrac1x)>0$ for $x\ne0$, $f(x)<2=f(0)$: $x=0$ is a local *maximum*, so (D) is false. For $x\ne0$, $f'(x)=-4x-2x\sin\dfrac1x+\cos\dfrac1x$; near $0$ the term $\cos\dfrac1x$ dominates and changes sign infinitely often, so $f$ is not monotonic on any $(0,\delta)$ nor $(-\delta,0)$: (B) is false and (C) is true.

### M-LCD-14 — JEE Advanced 2025 · Paper 1 · Q11 · Numerical

Let $\alpha,\beta$ be real numbers such that $\displaystyle\lim_{x\to0}\frac1{x^3}\left(\frac\alpha2\int_0^x\frac{dt}{1-t^2}+\beta x\cos x\right)=2$. Then $\alpha+\beta=$ ______.

**Answer: 2.4** (accepted range $2.35$–$2.45$) · official key ✔ (re-derived)

**Solution.** $\int_0^x\dfrac{dt}{1-t^2}=x+\dfrac{x^3}3+\cdots$ and $x\cos x=x-\dfrac{x^3}2+\cdots$. The bracket is $\left(\dfrac\alpha2+\beta\right)x+\left(\dfrac\alpha6-\dfrac\beta2\right)x^3+\cdots$. A finite limit needs $\beta=-\dfrac\alpha2$, and then $\dfrac\alpha6+\dfrac\alpha4=\dfrac{5\alpha}{12}=2\Rightarrow\alpha=\dfrac{24}5$, $\beta=-\dfrac{12}5$. $\alpha+\beta=\dfrac{12}{5}=2.4$.

### § — JEE Main 2026 · 21 Jan Shift 2 · Limits set Q1 · Numerical

Let $[\cdot]$ denote the greatest integer function and $f(x)=\lim_{n\to\infty}\dfrac1{n^3}\sum_{k=1}^{n}\left[\dfrac{k^2}{3^x}\right]$. Then $12\sum_{j=1}^\infty f(j)$ is equal to ______.

**Answer: 2** · key (compiled)

**Solution.** Write $\left[\dfrac{k^2}{3^x}\right]=\dfrac{k^2}{3^x}-\{\cdot\}$ with $0\le\{\cdot\}<1$; the fractional parts add up to at most $n$, which vanishes after dividing by $n^3$. So $f(x)=\lim\dfrac1{n^3}\cdot\dfrac{n(n+1)(2n+1)}{6\cdot3^x}=\dfrac1{3\cdot3^x}=\dfrac1{3^{x+1}}$. $\sum_{j=1}^\infty\dfrac1{3^{j+1}}=\dfrac{1/9}{1-1/3}=\dfrac16$, so $12\sum f(j)=2$.

### § — JEE Main 2026 · 22 Jan Shift 2 · Limits set Q2 · MCQ

If $\lim_{x\to0}\dfrac{e^{(a-1)x}+2\cos bx+(c-2)e^{-x}}{x\cos x-\log_e(1+x)}=2$, then $a^2+b^2+c^2$ is equal to:

(1) 5  (2) 9  (3) 3  (4) 7

**Answer: (4)** · key (compiled)

**Solution.** Denominator: $x\cos x-\ln(1+x)=\left(x-\tfrac{x^3}2\right)-\left(x-\tfrac{x^2}2+\tfrac{x^3}3\right)+\cdots=\dfrac{x^2}2+O(x^3)$. For a finite limit the numerator must be $O(x^2)$: constant term $1+2+(c-2)=0\Rightarrow c=-1$; $x$ term $(a-1)-(c-2)=a+2=0\Rightarrow a=-2$. $x^2$ coefficient: $\dfrac{(a-1)^2}2-b^2+\dfrac{c-2}2=\dfrac92-b^2-\dfrac32=3-b^2$. The limit is $\dfrac{3-b^2}{1/2}=2\Rightarrow b^2=2$. $a^2+b^2+c^2=4+2+1=7$.

### § — JEE Main 2026 · 21 Jan Shift 1 · Limits set Q3 · MCQ

Let $f:\mathbb R\to(0,\infty)$ be a twice differentiable function such that $f(3)=18$, $f'(3)=0$ and $f''(3)=4$. Then $\lim_{x\to1}\left(\log_e\left(\dfrac{f(2+x)}{f(3)}\right)^{\frac{18}{(x-1)^2}}\right)$ is equal to:

(1) 1  (2) 18  (3) 2  (4) 9

**Answer: (3)** · key (compiled)

**Solution.** The expression is $\dfrac{18}{(x-1)^2}\ln\dfrac{f(2+x)}{f(3)}$. Put $h=x-1$: $f(3+h)=f(3)+hf'(3)+\dfrac{h^2}2f''(3)+\cdots=18+2h^2+\cdots$, so $\dfrac{f(3+h)}{f(3)}=1+\dfrac{h^2}9+\cdots$ and $\ln(\cdot)\approx\dfrac{h^2}9$. The limit is $\dfrac{18}{h^2}\cdot\dfrac{h^2}9=2$.

### § — JEE Main 2026 · 28 Jan Shift 1 · Limits set Q4 · MCQ

The value of $\lim_{x\to0}\dfrac{\log_e\left(\sec(ex)\cdot\sec(e^2x)\cdot\ldots\cdot\sec(e^{10}x)\right)}{e^2-e^{2\cos x}}$ is equal to:

(1) $\dfrac{e^{20}-1}{2(e^2-1)}$  (2) $\dfrac{e^{10}-1}{2(e^2-1)}$  (3) $\dfrac{e^{10}-1}{2e^2(e^2-1)}$  (4) $\dfrac{e^{20}-1}{2e^2(e^2-1)}$

**Answer: (1)** · key (compiled)

**Solution.** Numerator $=\sum_{k=1}^{10}\ln\sec(e^kx)\approx\sum\dfrac{e^{2k}x^2}2=\dfrac{x^2}2\cdot\dfrac{e^2(e^{20}-1)}{e^2-1}$ (using $\ln\sec u\approx\tfrac{u^2}2$). Denominator: $e^2-e^{2\cos x}=e^2\left(1-e^{2(\cos x-1)}\right)\approx e^2\cdot2(1-\cos x)\approx e^2x^2$. The limit is $\dfrac{e^2(e^{20}-1)}{2(e^2-1)\,e^2}=\dfrac{e^{20}-1}{2(e^2-1)}$.

### § — JEE Main 2026 · 23 Jan Shift 1 · Continuity set Q1 · MCQ

Let $f(x)=\begin{cases}\dfrac{ax^2+2ax+3}{4x^2+4x-3},&x\ne-\tfrac32,\tfrac12\\ b,&x=-\tfrac32,\tfrac12\end{cases}$ be continuous at $x=-\dfrac32$. If $f\circ f(x)=\dfrac75$, then $x$ is equal to:

(1) 4  (2) 0  (3) 2  (4) 1

**Answer: (4)** · key (compiled)

**Solution.** $4x^2+4x-3=(2x+3)(2x-1)$. For a finite limit at $x=-\tfrac32$ the numerator must vanish there: $\tfrac94a-3a+3=0\Rightarrow a=4$. Then $4x^2+8x+3=(2x+1)(2x+3)$ and $f(x)=\dfrac{2x+1}{2x-1}$ for $x\ne-\tfrac32,\tfrac12$. $f(f(x))=\dfrac{2f+1}{2f-1}=\dfrac{6x+1}{2x+3}=\dfrac75\Rightarrow30x+5=14x+21\Rightarrow x=1$.

### § — JEE Main 2026 · 24 Jan Shift 2 · Continuity set Q2 · MCQ

Let $[t]$ denote the greatest integer less than or equal to $t$. If the function $f(x)=\begin{cases}b^2\sin\left(\dfrac\pi2\left[\dfrac\pi2(\cos x+\sin x)\cos x\right]\right),&x<0\\[2mm]\dfrac{\sin x-\tfrac12\sin2x}{x^3},&x>0\\[2mm]a,&x=0\end{cases}$ is continuous at $x=0$, then $a^2+b^2$ is equal to:

(1) $\dfrac58$  (2) $\dfrac12$  (3) $\dfrac9{16}$  (4) $\dfrac34$

**Answer: (4)** · key (compiled)

**Solution.** Right limit: $\dfrac{\sin x-\sin x\cos x}{x^3}=\dfrac{\sin x}{x}\cdot\dfrac{1-\cos x}{x^2}\to1\cdot\tfrac12=\tfrac12$, so $a=\tfrac12$. Left limit: for $x\to0^-$, $(\cos x+\sin x)\cos x=\cos^2x+\sin x\cos x$ is slightly *less* than 1, so $\tfrac\pi2(\cdot)$ is slightly less than $\tfrac\pi2\approx1.57$ and its integer part is 1. Then $f(x)=b^2\sin\tfrac\pi2=b^2$, so $b^2=a=\tfrac12$. $a^2+b^2=\tfrac14+\tfrac12=\tfrac34$.

### § — JEE Main 2026 · 22 Jan Shift 2 · Continuity set Q3 · MCQ

Let $[\cdot]$ denote the greatest integer function, and let $f(x)=\min\{\sqrt2x,x^2\}$. Let $S=\{x\in(-2,2):$ the function $g(x)=|x|[x^2]$ is discontinuous at $x\}$. Then $\sum_{x\in S}f(x)$ equals:

(1) $\sqrt6-2\sqrt2$  (2) $1-\sqrt2$  (3) $2-\sqrt2$  (4) $2\sqrt6-3\sqrt2$

**Answer: (2)** · key (compiled)

**Solution.** $[x^2]$ jumps where $x^2$ is a positive integer: $x=\pm1,\pm\sqrt2,\pm\sqrt3$ in $(-2,2)$. At each of these $|x|\ne0$, so $g$ is discontinuous; $S=\{\pm1,\pm\sqrt2,\pm\sqrt3\}$. $f(1)=\min\{\sqrt2,1\}=1$; $f(-1)=-\sqrt2$; $f(\sqrt2)=\min\{2,2\}=2$; $f(-\sqrt2)=-2$; $f(\sqrt3)=\min\{\sqrt6,3\}=\sqrt6$; $f(-\sqrt3)=-\sqrt6$. Sum $=1-\sqrt2+2-2+\sqrt6-\sqrt6=1-\sqrt2$.

### § — JEE Main 2026 · 23 Jan Shift 2 · Continuity set Q4 · MCQ

If $f(x)=\begin{cases}\dfrac{a|x|+x^2-2(\sin|x|)(\cos|x|)}{x},&x\ne0\\ b,&x=0\end{cases}$ is continuous at $x=0$, then $a+b$ is equal to:

(1) 4  (2) 1  (3) 2  (4) 0

**Answer: (3)** · key (compiled)

**Solution.** $2\sin|x|\cos|x|=\sin2|x|$. For $x\to0^+$: $f=a+x-\dfrac{\sin2x}x\to a-2$. For $x\to0^-$: $|x|=-x$, so $f=\dfrac{-ax+x^2+\sin2x}x\to-a+2$. Continuity needs $a-2=2-a=b$, so $a=2$ and $b=0$; $a+b=2$.

### § — JEE Main 2026 · 24 Jan Shift 1 · Continuity set Q5 · MCQ

If the function $f(x)=\dfrac{e^x\left(e^{\tan x-x}-1\right)+\log_e(\sec x+\tan x)-x}{\tan x-x}$ is continuous at $x=0$, then the value of $f(0)$ is equal to:

(1) $\dfrac23$  (2) 2  (3) $\dfrac32$  (4) $\dfrac12$

**Answer: (3)** · key (compiled)

**Solution.** Near 0: $\tan x-x\approx\dfrac{x^3}3$. $e^x\left(e^{\tan x-x}-1\right)\approx(1+x)\dfrac{x^3}3\approx\dfrac{x^3}3$. $\ln(\sec x+\tan x)=x+\dfrac{x^3}6+\cdots$, so $\ln(\sec x+\tan x)-x\approx\dfrac{x^3}6$. Numerator $\approx\dfrac{x^3}3+\dfrac{x^3}6=\dfrac{x^3}2$. $f(0)=\lim\dfrac{x^3/2}{x^3/3}=\dfrac32$.

### § — JEE Main 2026 · 24 Jan Shift 1 · Continuity set Q6 · MCQ

Let $\alpha,\beta\in\mathbb R$ be such that the function $f(x)=\begin{cases}2\alpha(x^2-2)+2\beta x,&x<1\\(\alpha+3)x+(\alpha-\beta),&x\ge1\end{cases}$ is differentiable at all $x\in\mathbb R$. Then $34(\alpha+\beta)$ is equal to:

(1) 36  (2) 24  (3) 84  (4) 48

**Answer: (4)** · key (compiled)

**Solution.** Differentiable at $x=1$ requires continuity and equal derivatives. Continuity: $-2\alpha+2\beta=(\alpha+3)+(\alpha-\beta)\Rightarrow4\alpha-3\beta+3=0$. Derivatives: left $4\alpha x+2\beta\to4\alpha+2\beta$; right $\alpha+3$, so $3\alpha+2\beta-3=0$. Solving: $\alpha=\tfrac3{17}$, $\beta=\tfrac{21}{17}$. $34(\alpha+\beta)=34\cdot\tfrac{24}{17}=48$.

### § — JEE Main 2026 · 28 Jan Shift 2 · LCD set Q1 · MCQ

Let $f(x)=\lim_{\theta\to0}\left(\dfrac{\cos\pi x-x^{\left(\frac2\theta\right)}\sin(x-1)}{1+x^{\left(\frac2\theta\right)}(x-1)}\right)$, $x\in\mathbb R$. Consider the following two statements: (I) $f(x)$ is discontinuous at $x=1$. (II) $f(x)$ is continuous at $x=-1$. Then,

(1) Only (II) is True  (2) Neither (I) nor (II) is True  (3) Both (I) and (II) are True  (4) Only (I) is True

**Answer: (2)** · key (compiled)

**Solution.** For $|x|<1$, $x^{2/\theta}\to0$ and $f(x)=\cos\pi x$. For $|x|>1$, $x^{2/\theta}\to\infty$ and dividing through gives $f(x)=\dfrac{-\sin(x-1)}{x-1}$. At $x=1$: $f(1)=\dfrac{\cos\pi-0}{1+0}=-1$; the left limit is $\cos\pi=-1$ and the right limit is $-\dfrac{\sin(x-1)}{x-1}\to-1$, so $f$ is continuous at 1: (I) is false. At $x=-1$: from inside, $\cos(-\pi)=-1$; from outside, $-\dfrac{\sin(-2)}{-2}=-\dfrac{\sin2}2\approx-0.45\ne-1$. The one-sided limits differ, so $f$ is discontinuous at $-1$: (II) is false. Neither is true.

