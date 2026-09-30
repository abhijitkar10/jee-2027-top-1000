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

### M-AOD-08 — JEE Main 2024 · 30 Jan Shift 1 · Q66 · MCQ

The maximum area of a triangle whose one vertex is at $(0,0)$ and the other two vertices lie on the curve $y=-2x^2+54$ at points $(x,y)$ and $(-x,y)$, where $y>0$, is

(1) 88  (2) 122  (3) 92  (4) 108

**Answer: (4)** · key ✔

**Solution.** The base is $2x$ and the height is $y$, so $A=xy=54x-2x^3$. $A'=54-6x^2=0\Rightarrow x=3$ (and $A''<0$). $A_{\max}=162-54=108$.

### M-AOD-09 — JEE Main 2024 · 30 Jan Shift 1 · Q73 · MCQ

Let $g:\mathbb R\to\mathbb R$ be a non-constant twice differentiable function with $g'\!\left(\tfrac12\right)=g'\!\left(\tfrac32\right)$. If $f(x)=\tfrac12\left[g(x)+g(2-x)\right]$, then

(1) $f''(x)=0$ for at least two $x$ in $(0,2)$  (2) $f''(x)=0$ for exactly one $x$ in $(0,1)$  (3) $f''(x)=0$ for no $x$ in $(0,1)$  (4) $f'\!\left(\tfrac32\right)+f'\!\left(\tfrac12\right)=1$

**Answer: (1)** · key ✔

**Solution.** $f'(x)=\tfrac12\left[g'(x)-g'(2-x)\right]$. Then $f'\!\left(\tfrac12\right)=\tfrac12\left[g'(\tfrac12)-g'(\tfrac32)\right]=0$, $f'(1)=0$ and $f'\!\left(\tfrac32\right)=0$. By Rolle's theorem $f''$ vanishes at least once in $\left(\tfrac12,1\right)$ and at least once in $\left(1,\tfrac32\right)$: at least two zeros in $(0,2)$. (Option (4) gives $0\ne1$.)

### M-AOD-10 — JEE Main 2024 · 30 Jan Shift 2 · Q74 · MCQ

Let $f(x)=(x+3)^2(x-2)^3$, $x\in[-4,4]$. If $M$ and $m$ are the maximum and minimum values of $f$ in $[-4,4]$ respectively, then $M-m$ is

(1) 600  (2) 392  (3) 608  (4) 108

**Answer: (3)** · key ✔

**Solution.** $f'(x)=(x+3)(x-2)^2\left[2(x-2)+3(x+3)\right]=5(x+3)(x+1)(x-2)^2$, with critical points $-3,-1,2$. Values: $f(-4)=(1)(-6)^3=-216$, $f(-3)=0$, $f(-1)=4(-27)=-108$, $f(2)=0$, $f(4)=49\cdot8=392$. So $M=392$, $m=-216$ and $M-m=608$.

