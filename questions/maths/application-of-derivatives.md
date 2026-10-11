# Differentiation & Application of Derivatives

> Theory: [../../theory/maths/application-of-derivatives.md](../../theory/maths/application-of-derivatives.md)

### M-AOD-01 — JEE Main 2024 · 27 Jan Shift 1 · Q85 · Numerical

Let $f(x)=x^3+x^2f'(1)+xf''(2)+f'''(3)$, $x\in\mathbb R$. Then $f'(10)$ is equal to ______.

**Answer: 202** · key ✔

**Solution.** Differentiating: $f'(x)=3x^2+2xf'(1)+f''(2)$, $f''(x)=6x+2f'(1)$, $f'''=6$. So $f''(2)=12+2f'(1)$. Putting $x=1$ in $f'$: $f'(1)=3+2f'(1)+12+2f'(1)\Rightarrow f'(1)=-5$, so $f''(2)=2$. Then $f'(10)=300+20(-5)+2=202$.

### M-AOD-02 — JEE Main 2024 · 27 Jan Shift 1 · Q86 · Numerical

Let $f:(0,\infty)\to\mathbb R$ satisfy $f(x)-f(y)\ge\ln\dfrac xy+x-y$ for all $x,y>0$. Then $\displaystyle\sum_{n=1}^{20}f'\!\left(\frac1{n^2}\right)$ is equal to ______.

**Answer: 2890** · key ✔

**Solution.** Let $g(x)=f(x)-\ln x-x$. The condition says $g(x)\ge g(y)$ for all $x,y$; swapping roles forces $g$ constant, so $f'(x)=\dfrac1x+1$. Then $f'(1/n^2)=n^2+1$ and $\sum_{n=1}^{20}(n^2+1)=2870+20=2890$.

### M-AOD-03 — JEE Main 2024 · 27 Jan Shift 2 · Q73 · MCQ

Let $g(x)=3f\!\left(\dfrac x3\right)+f(3-x)$ with $f''(x)>0$ for all $x\in(0,3)$. If $g$ is decreasing in $(0,\alpha)$ and increasing in $(\alpha,3)$, then $8\alpha$ is

(1) 24  (2) 0  (3) 18  (4) 20

**Answer: (3)** · key ✔

**Solution.** $g'(x)=f'\!\left(\tfrac x3\right)-f'(3-x)$. Since $f''>0$, $f'$ is strictly increasing, so $g'(x)=0\iff\tfrac x3=3-x\iff x=\tfrac94$, with $g'<0$ before and $g'>0$ after. So $\alpha=\tfrac94$ and $8\alpha=18$.

### M-AOD-04 — JEE Main 2024 · 29 Jan Shift 1 · Q87 · Numerical

Let $f(x)=2^x-x^2$, $x\in\mathbb R$. If $m$ and $n$ are respectively the numbers of points at which the curves $y=f(x)$ and $y=f'(x)$ intersect the $x$-axis, then $m+n$ is ______.

**Answer: 5** · key ✔

**Solution.** $f''(x)=2^x\ln^22-2$ has exactly one zero, so $f'$ has at most $2$ zeros and $f$ at most $3$. Zeros of $f$: $x=2$, $x=4$, and one negative root ($f(-1)=-\tfrac12<0$, $f(0)=1>0$), so $m=3$. By Rolle's theorem $f'$ vanishes between consecutive roots, giving at least $2$ zeros, so $n=2$. Hence $m+n=5$.

### M-AOD-05 — JEE Main 2024 · 29 Jan Shift 2 · Q72 · MCQ

Let $y=\ln\!\left(\dfrac{1-x^2}{1+x^2}\right)$, $-1<x<1$. Then at $x=\dfrac12$, the value of $225\,(y'-y'')$ is equal to

(1) 732  (2) 746  (3) 742  (4) 736

**Answer: (4)** · key ✔

**Solution.** $y=\ln(1-x^2)-\ln(1+x^2)$, so $y'=-\dfrac{2x}{1-x^2}-\dfrac{2x}{1+x^2}$ and $y''=-\dfrac2{1-x^2}-\dfrac{4x^2}{(1-x^2)^2}-\dfrac2{1+x^2}+\dfrac{4x^2}{(1+x^2)^2}$. At $x=\tfrac12$ ($1-x^2=\tfrac34,\ 1+x^2=\tfrac54$): $y'=-\tfrac43-\tfrac45=-\tfrac{32}{15}$ and $y''=-\tfrac83-\tfrac{16}9-\tfrac85+\tfrac{16}{25}=-\tfrac{1216}{225}$. So $225(y'-y'')=-480+1216=736$.

### M-AOD-06 — JEE Main 2024 · 29 Jan Shift 2 · Q73 · MCQ

The function $f(x)=2x+3x^{2/3}$, $x\in\mathbb R$, has

(1) exactly one point of local minima and no point of local maxima  (2) exactly one point of local maxima and no point of local minima  (3) exactly one point of local maxima and exactly one point of local minima  (4) exactly two points of local maxima and exactly one point of local minima

**Answer: (3)** · key ✔

**Solution.** $f'(x)=2+2x^{-1/3}=\dfrac{2\left(x^{1/3}+1\right)}{x^{1/3}}$, zero at $x=-1$ and undefined at $x=0$. For $x<-1$: $f'>0$; for $-1<x<0$: $f'<0$; for $x>0$: $f'>0$. So $x=-1$ is a local maximum and $x=0$ (a cusp) is a local minimum.

### M-AOD-07 — JEE Main 2024 · 29 Jan Shift 2 · Q74 · MCQ

The function $f(x)=\dfrac x{x^2-6x-16}$, $x\in\mathbb R-\{-2,8\}$,

(1) decreases in $(-2,8)$ and increases in $(-\infty,-2)\cup(8,\infty)$  (2) decreases in $(-\infty,-2)\cup(-2,8)\cup(8,\infty)$  (3) decreases in $(-\infty,-2)$ and increases in $(8,\infty)$  (4) increases in $(-\infty,-2)\cup(-2,8)\cup(8,\infty)$

**Answer: (2)** · key ✔

**Solution.** $f'(x)=\dfrac{(x^2-6x-16)-x(2x-6)}{(x^2-6x-16)^2}=\dfrac{-(x^2+16)}{(x^2-6x-16)^2}<0$ everywhere on the domain. So $f$ is decreasing on each of $(-\infty,-2),(-2,8),(8,\infty)$.

### M-AOD-08 — JEE Main 2024 · 30 Jan Shift 1 · Q73 · MCQ

Let $g:\mathbb R\to\mathbb R$ be a non-constant twice differentiable function with $g'\!\left(\tfrac12\right)=g'\!\left(\tfrac32\right)$. If $f(x)=\tfrac12\left[g(x)+g(2-x)\right]$, then

(1) $f''(x)=0$ for at least two $x$ in $(0,2)$  (2) $f''(x)=0$ for exactly one $x$ in $(0,1)$  (3) $f''(x)=0$ for no $x$ in $(0,1)$  (4) $f'\!\left(\tfrac32\right)+f'\!\left(\tfrac12\right)=1$

**Answer: (1)** · key ✔

**Solution.** $f'(x)=\tfrac12\left[g'(x)-g'(2-x)\right]$. Then $f'\!\left(\tfrac12\right)=\tfrac12\left[g'(\tfrac12)-g'(\tfrac32)\right]=0$, $f'(1)=0$ and $f'\!\left(\tfrac32\right)=0$. By Rolle's theorem $f''$ vanishes at least once in $\left(\tfrac12,1\right)$ and at least once in $\left(1,\tfrac32\right)$: at least two zeros in $(0,2)$. (Option (4) gives $0\ne1$.)

### M-AOD-09 — JEE Main 2024 · 30 Jan Shift 2 · Q74 · MCQ

Let $f(x)=(x+3)^2(x-2)^3$, $x\in[-4,4]$. If $M$ and $m$ are the maximum and minimum values of $f$ in $[-4,4]$ respectively, then $M-m$ is

(1) 600  (2) 392  (3) 608  (4) 108

**Answer: (3)** · key ✔

**Solution.** $f'(x)=(x+3)(x-2)^2\left[2(x-2)+3(x+3)\right]=5(x+3)(x+1)(x-2)^2$, with critical points $-3,-1,2$. Values: $f(-4)=(1)(-6)^3=-216$, $f(-3)=0$, $f(-1)=4(-27)=-108$, $f(2)=0$, $f(4)=49\cdot8=392$. So $M=392$, $m=-216$ and $M-m=608$.

### M-AOD-10 — JEE Main 2024 · 1 Feb Shift 1 · Q74 · MCQ

If $5f(x)+4f\!\left(\tfrac1x\right)=x^2-2$ for all $x\ne0$ and $y=9x^2f(x)$, then $y$ is strictly increasing in:

(1) $\left(0,\tfrac1{\sqrt5}\right)\cup\left(\tfrac1{\sqrt5},\infty\right)$  (2) $\left(-\tfrac1{\sqrt5},0\right)\cup\left(\tfrac1{\sqrt5},\infty\right)$  (3) $\left(-\tfrac1{\sqrt5},0\right)\cup\left(0,\tfrac1{\sqrt5}\right)$  (4) $\left(-\infty,\tfrac1{\sqrt5}\right)\cup\left(0,\tfrac1{\sqrt5}\right)$

**Answer: (2)** · key ✔

**Solution.** Replacing $x\to1/x$: $5f(1/x)+4f(x)=1/x^2-2$. Eliminate $f(1/x)$: $9f(x)=5(x^2-2)-4(1/x^2-2)=5x^2-2-4/x^2$. So $y=9x^2f(x)=5x^4-2x^2-4$ and $y'=20x^3-4x=4x(5x^2-1)$. $y'>0$ for $x\in\left(-\tfrac1{\sqrt5},0\right)\cup\left(\tfrac1{\sqrt5},\infty\right)$.

### M-AOD-11 — JEE Main 2024 · 4 Apr Shift 1 · Q72 · MCQ

The sum of the maximum and minimum values of $f(x)=\dfrac{2x^2-3x+8}{2x^2+3x+8}$ is $\dfrac mn$, $\gcd(m,n)=1$. Then $m+n$ is:

(1) 195  (2) 201  (3) 217  (4) 182

**Answer: (2)** · key ✔

**Solution.** Put $y=f(x)$: $(2y-2)x^2+(3y+3)x+(8y-8)=0$ must have a real root: $9(y+1)^2-4(2y-2)(8y-8)\ge0\Rightarrow9(y+1)^2\ge64(y-1)^2\Rightarrow3|y+1|\ge8|y-1|$. This gives $y\in\left[\tfrac5{11},\tfrac{11}5\right]$. Sum $=\tfrac5{11}+\tfrac{11}5=\tfrac{146}{55}$, so $m+n=201$.

### M-AOD-12 — JEE Main 2024 · 4 Apr Shift 1 · Q74 · MCQ

Let $f(x)=x^5+2e^{x/4}$ and $g$ be such that $(g\circ f)(x)=x$. Then $8g'(2)$ is:

(1) 2  (2) 8  (3) 4  (4) 16

**Answer: (4)** · key ✔

**Solution.** $g=f^{-1}$, so $g'(2)=\dfrac1{f'(g(2))}$. $f(0)=0+2=2\Rightarrow g(2)=0$. $f'(x)=5x^4+\tfrac12e^{x/4}$, $f'(0)=\tfrac12$. So $g'(2)=2$ and $8g'(2)=16$.

### § — JEE Main 2026 · 21 Jan Shift 2 · Differentiation set Q1 · MCQ

Let $f(x)=x^3+x^2f'(1)+2xf''(2)+f'''(3)$, $x\in\mathbb R$. Then the value of $f'(5)$ is:

(1) $\dfrac{117}5$  (2) $\dfrac{657}5$  (3) $\dfrac25$  (4) $\dfrac{62}5$

**Answer: (1)** · key (compiled)

**Solution.** Let $a=f'(1)$, $b=f''(2)$, $c=f'''(3)$, so $f(x)=x^3+ax^2+2bx+c$, $f'=3x^2+2ax+2b$, $f''=6x+2a$, $f'''=6$. Then $a=f'(1)=3+2a+2b\Rightarrow a=-3-2b$; $b=f''(2)=12+2a$. Substituting: $b=12-6-4b\Rightarrow b=\tfrac65$ and $a=-\tfrac{27}5$. $f'(5)=75+10a+2b=75-54+\tfrac{12}5=\dfrac{117}5$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $f:\mathbb R\to\mathbb R$ be a twice differentiable function such that $f''(x)>0$ for all $x\in\mathbb R$ and $f'(a-1)=0$, where $a$ is a real number. Let $g(x)=f\left(\tan^2x-2\tan x+a\right)$, $0<x<\dfrac\pi2$. Consider the following two statements: (I) $g$ is increasing in $\left(0,\dfrac\pi4\right)$. (II) $g$ is decreasing in $\left(\dfrac\pi4,\dfrac\pi2\right)$. Then,

(1) Neither (I) nor (II) is True  (2) Only (I) is True  (3) Both (I) and (II) are True  (4) Only (II) is True

**Answer: (1)** · key (compiled)

**Solution.** $f''>0$ makes $f'$ strictly increasing, and $f'(a-1)=0$, so $f'>0$ for $x>a-1$: $f$ is increasing on $[a-1,\infty)$. Let $u(x)=\tan^2x-2\tan x+a=(\tan x-1)^2+(a-1)\ge a-1$, so $g=f(u)$ is increasing in $u$. On $\left(0,\tfrac\pi4\right)$, $\tan x$ rises towards 1 so $(\tan x-1)^2$ *decreases*, hence $g$ decreases: (I) is false. On $\left(\tfrac\pi4,\tfrac\pi2\right)$, $\tan x>1$ and increasing, so $u$ and $g$ *increase*: (II) is false. Neither is true.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q2 · Numerical

Let $f$ be a differentiable function satisfying $f(x)=1-2x+\int_0^xe^{(x-t)}f(t)\,dt$, $x\in\mathbb R$ and let $g(x)=\int_0^x(f(t)+2)^{15}(t-4)^6(t+12)^{17}dt$, $x\in\mathbb R$. If $p$ and $q$ are respectively the points of local minima and local maxima of $g$, then the value of $|p+q|$ is equal to ______.

**Answer: 9** · key (compiled)

**Solution.** Write $f(x)=1-2x+e^x\int_0^xe^{-t}f(t)dt$ and differentiate: $f'(x)=-2+\left(f(x)-1+2x\right)+f(x)$, i.e. $f'-2f=2x-3$. Trying $f=1-x$ satisfies it, and $f(0)=1$ fixes the constant (the homogeneous part $Ce^{2x}$ has $C=0$). So $f(x)=1-x$ and $f(t)+2=3-t$. $g'(x)=(3-x)^{15}(x-4)^6(x+12)^{17}$. The factors $(x-4)^6$ (even power) do not change sign. $g'<0$ for $x<-12$, $>0$ on $(-12,3)$, $<0$ for $x>3$: local minimum at $p=-12$, local maximum at $q=3$. $|p+q|=9$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q3 · MCQ

Consider the following three statements for the function $f:(0,\infty)\to\mathbb R$ defined by $f(x)=|\log_ex|-|x-1|$: (I) $f$ is differentiable at all $x>0$. (II) $f$ is increasing in $(0,1)$. (III) $f$ is decreasing in $(1,\infty)$. Then:

(1) All (I), (II) and (III) are TRUE.  (2) Only (II) and (III) are TRUE.  (3) Only (I) is TRUE.  (4) Only (I) and (III) are TRUE.

**Answer: (4)** · key (compiled)

**Solution.** For $0<x<1$: $f=-\ln x-(1-x)$, $f'=-\dfrac1x+1<0$. For $x>1$: $f=\ln x-(x-1)$, $f'=\dfrac1x-1<0$. At $x=1$ both one-sided derivatives are $0$, so the kinks of $|\ln x|$ and $|x-1|$ cancel: $f$ is differentiable at 1 (I true). On $(0,1)$ $f$ is *decreasing*, so (II) is false; on $(1,\infty)$ it is decreasing, so (III) is true.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q4 · MCQ

Let $f(x)=x^{2025}-x^{2000}$, $x\in[0,1]$ and the minimum value of the function $f(x)$ in the interval $[0,1]$ be $(80)^{80}(n)^{-81}$. Then $n$ is equal to:

(1) $-40$  (2) $-41$  (3) $-80$  (4) $-81$

**Answer: (4)** · key (compiled)

**Solution.** $f'(x)=2025x^{2024}-2000x^{1999}=x^{1999}\left(2025x^{25}-2000\right)=0\Rightarrow x^{25}=\dfrac{80}{81}$ (the minimum, as $f(0)=f(1)=0$). With $s=x^{25}$: $f=x^{2000}(x^{25}-1)=s^{80}(s-1)=\left(\tfrac{80}{81}\right)^{80}\left(-\tfrac1{81}\right)=-\dfrac{80^{80}}{81^{81}}$. Matching $(80)^{80}n^{-81}$: $n^{-81}=-81^{-81}$, so $n=-81$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q5 · Numerical

Let $f:\mathbb R\to\mathbb R$ be a twice differentiable function such that the quadratic equation $f(x)m^2-2f'(x)m+f''(x)=0$ in $m$ has two equal roots for every $x\in\mathbb R$. If $f(0)=1$, $f'(0)=2$, and $(\alpha,\beta)$ is the largest interval in which the function $f(\log_ex-x)$ is increasing, then $\alpha+\beta$ is equal to ______.

**Answer: 1** · key (compiled)

**Solution.** Equal roots: $4f'^2-4ff''=0\Rightarrow\dfrac{f''}{f'}=\dfrac{f'}f\Rightarrow f'=kf$ and $f=Ae^{kx}$. $f(0)=1$ gives $A=1$ and $f'(0)=2$ gives $k=2$, so $f(x)=e^{2x}$. Then $f(\ln x-x)=e^{2\ln x-2x}=x^2e^{-2x}$ (for $x>0$), with derivative $2xe^{-2x}(1-x)$. It is positive for $0<x<1$: the largest interval of increase is $(0,1)$, so $\alpha+\beta=1$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q6 · Numerical

Let $(2\alpha,\alpha)$ be the largest interval in which the function $f(t)=\dfrac{|t+1|}{t^2}$, $t<0$, is strictly decreasing. Then the local maximum value of the function $g(x)=2\log_e(x-2)+\alpha x^2+4x-\alpha$, $x>2$, is ______.

**Answer: 4** · key (compiled)

**Solution.** For $-1<t<0$: $f=\dfrac{t+1}{t^2}$, $f'=-\dfrac{t+2}{t^3}>0$ (increasing). For $t<-1$: $f=-\dfrac{t+1}{t^2}$, $f'=\dfrac{t+2}{t^3}$, which is negative on $(-2,-1)$ and positive for $t<-2$. So the largest interval of decrease is $(-2,-1)=(2\alpha,\alpha)$ and $\alpha=-1$. $g(x)=2\ln(x-2)-x^2+4x+1$, $g'(x)=\dfrac2{x-2}-2(x-2)=0\Rightarrow(x-2)^2=1\Rightarrow x=3$, and $g''<0$ there, so it is the local maximum: $g(3)=0-9+12+1=4$.

