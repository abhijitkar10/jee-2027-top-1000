# Definite Integration

> Theory: [../../theory/maths/definite-integration.md](../../theory/maths/definite-integration.md)

### M-DEF-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · Numerical

If $\int_0^14\cot^{-1}\left(1-2x+4x^2\right)dx=a\tan^{-1}(2)-b\log_e(5)$, where $a,b\in\mathbb N$, then $(2a+b)$ is equal to ______.

**Answer: 9** · key (compiled)

**Solution.** $\cot^{-1}(1-2x+4x^2)=\tan^{-1}\dfrac1{1+2x(2x-1)}=\tan^{-1}(2x)-\tan^{-1}(2x-1)$. $\int_0^1\tan^{-1}(2x)dx=\left[x\tan^{-1}2x-\tfrac14\ln(1+4x^2)\right]_0^1=\tan^{-1}2-\tfrac14\ln5$. $\int_0^1\tan^{-1}(2x-1)dx=\tfrac12\int_{-1}^1\tan^{-1}s\,ds=0$ (odd function). So $4\int=4\tan^{-1}2-\ln5$: $a=4$, $b=1$ and $2a+b=9$.

### M-DEF-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

The value of the integral $\int_{\pi/24}^{5\pi/24}\dfrac{dx}{1+\sqrt[3]{\tan2x}}$ is:

(1) $\dfrac\pi3$  (2) $\dfrac\pi{12}$  (3) $\dfrac\pi{18}$  (4) $\dfrac\pi6$

**Answer: (2)** · key (compiled)

**Solution.** The limits add to $\tfrac{6\pi}{24}=\tfrac\pi4$; apply $x\to\tfrac\pi4-x$ (King's rule), under which $\tan2x\to\cot2x$. Then $I=\int\dfrac{dx}{1+\sqrt[3]{\cot2x}}=\int\dfrac{\sqrt[3]{\tan2x}}{1+\sqrt[3]{\tan2x}}dx$. Adding: $2I=\int_{\pi/24}^{5\pi/24}dx=\dfrac{4\pi}{24}=\dfrac\pi6$, so $I=\dfrac\pi{12}$.

### M-DEF-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let $[\cdot]$ denote the greatest integer function. Then $\int_{-\pi/2}^{\pi/2}\left(\dfrac{12(3+[x])}{3+[\sin x]+[\cos x]}\right)dx$ is equal to:

(1) $13\pi+1$  (2) $12\pi+5$  (3) $11\pi+2$  (4) $15\pi+4$

**Answer: (3)** · key (compiled)

**Solution.** Split at $x=-1,0,1$. On $\left[-\tfrac\pi2,-1\right)$: $[x]=-2$, $[\sin x]=-1$, $[\cos x]=0$, integrand $\dfrac{12(1)}{2}=6$, length $\tfrac\pi2-1$. On $[-1,0)$: $[x]=-1$, $[\sin x]=-1$, $[\cos x]=0$: $\dfrac{12\cdot2}{2}=12$, length 1. On $(0,1)$: $[x]=0$, $[\sin x]=0$, $[\cos x]=0$: $\dfrac{36}3=12$, length 1. On $\left[1,\tfrac\pi2\right]$: $[x]=1$, $[\sin x]=0$, $[\cos x]=0$: $\dfrac{48}3=16$, length $\tfrac\pi2-1$. Total $=6\left(\tfrac\pi2-1\right)+12+12+16\left(\tfrac\pi2-1\right)=11\pi+2$.

### M-DEF-04 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · MCQ

Let $f(x)=[x]^2-[x+3]-3$, $x\in\mathbb R$, where $[\ ]$ is the greatest integer function. Then:

(1) $\int_0^2f(x)dx=-6$  (2) $f(x)<0$ only for $x\in[-1,3)$  (3) $f(x)>0$ only for $x\in[4,\infty)$  (4) $f(x)=0$ for finitely many values of $x$

**Answer: (2)** · key (compiled)

**Solution.** For $x\in[n,n+1)$: $f=n^2-(n+3)-3=n^2-n-6=(n-3)(n+2)$. $f<0$ iff $-2<n<3$, i.e. $n=-1,0,1,2$, i.e. $x\in[-1,3)$ – (2) true. (1) is false: $f=-6$ on $[0,1)$ and on $[1,2)$, so $\int_0^2f=-12$. (3) is false: $f>0$ also for $n\le-3$ ($x<-2$). (4) is false: $f=0$ on the whole intervals $[3,4)$ and $[-2,-1)$.

### M-DEF-05 · A — JEE Main 2026 · 21 Jan Shift 1 · set Q9 · MCQ

The value of $\int_{-\pi/6}^{\pi/6}\left(\dfrac{\pi+4x^{11}}{1-\sin\left(|x|+\frac\pi6\right)}\right)dx$ is equal to:

(1) $8\pi$  (2) $6\pi$  (3) $2\pi$  (4) $4\pi$

**Answer: (4)** · key (compiled)

**Solution.** The denominator is even and $4x^{11}$ is odd, so that part integrates to 0. The rest is $2\pi\int_0^{\pi/6}\dfrac{dx}{1-\sin(x+\pi/6)}$. With $u=x+\tfrac\pi6$ the limits become $\tfrac\pi6$ to $\tfrac\pi3$ and $\dfrac1{1-\sin u}=\sec^2u+\sec u\tan u$, so the integral is $[\tan u+\sec u]_{\pi/6}^{\pi/3}=(\sqrt3+2)-\left(\tfrac1{\sqrt3}+\tfrac2{\sqrt3}\right)=2$. The value is $2\pi\cdot2=4\pi$.

### M-DEF-06 · A — JEE Main 2026 · 28 Jan Shift 1 · set Q11 · MCQ

Let $f$ be a polynomial function such that $f\left(x^2+1\right)=x^4+5x^2+2$, for all $x\in\mathbb R$. Then $\int_0^3f(x)dx$ is equal to:

(1) $\dfrac53$  (2) $\dfrac{41}3$  (3) $\dfrac{27}2$  (4) $\dfrac{33}2$

**Answer: (4)** · key (compiled)

**Solution.** Put $u=x^2+1$: $f(u)=(u-1)^2+5(u-1)+2=u^2+3u-2$. $\int_0^3(x^2+3x-2)dx=9+\dfrac{27}2-6=\dfrac{33}2$.

### M-DEF-07 · B — JEE Main 2025 · Jan session · set Q1 · MCQ

The integral $80\displaystyle\int_0^{\pi/4}\left(\dfrac{\sin\theta+\cos\theta}{9+16\sin2\theta}\right)d\theta$ is equal to:

(1) $3\log_e4$  (2) $4\log_e3$  (3) $6\log_e4$  (4) $2\log_e3$

**Answer: (2)** · key (compiled)

**Solution.** Put $t=\sin\theta-\cos\theta$, $dt=(\sin\theta+\cos\theta)d\theta$, and $\sin2\theta=1-t^2$, so $9+16\sin2\theta=25-16t^2$; the limits are $t=-1$ to $0$. $\int_{-1}^0\dfrac{dt}{25-16t^2}=\dfrac1{40}\ln\dfrac{5+4t}{5-4t}\Big|_{-1}^0=\dfrac1{40}\ln9$. Multiplying by 80: $2\ln9=4\ln3$.

### M-DEF-08 · B — JEE Main 2025 · Jan session · set Q4 · MCQ

Let $f(x)=\displaystyle\int_0^{x^2}\dfrac{t^2-8t+15}{e^t}\,dt$, $x\in\mathbb R$. Then the numbers of local maximum and local minimum points of $f$, respectively, are:

(1) 2 and 3  (2) 2 and 2  (3) 3 and 2  (4) 1 and 3

**Answer: (1)** · key (compiled)

**Solution.** $f'(x)=2x\,(x^4-8x^2+15)e^{-x^2}=2x(x^2-3)(x^2-5)e^{-x^2}$, with critical points $0,\pm\sqrt3,\pm\sqrt5$. The sign of $f'$ is $-,+,-,+,-,+$ across $x<-\sqrt5$, $(-\sqrt5,-\sqrt3)$, $(-\sqrt3,0)$, $(0,\sqrt3)$, $(\sqrt3,\sqrt5)$, $x>\sqrt5$. Sign changes $-\to+$ (minima) occur at $-\sqrt5,0,\sqrt5$: 3; changes $+\to-$ (maxima) at $\pm\sqrt3$: 2. So 2 maxima and 3 minima.

### M-DEF-09 · B — JEE Main 2025 · Jan session · set Q5 · MCQ

Let for some function $y=f(x)$, $\displaystyle\int_0^xt\,f(t)\,dt=x^2f(x)$, $x>0$ and $f(2)=3$. Then $f(6)$ is equal to:

(1) 1  (2) 3  (3) 6  (4) 2

**Answer: (1)** · key (compiled)

**Solution.** Differentiating: $xf(x)=2xf(x)+x^2f'(x)\Rightarrow xf'=-f$, so $f=\dfrac cx$. $f(2)=3\Rightarrow c=6$ and $f(6)=1$.

### M-DEF-10 · B — JEE Main 2025 · Apr session · set Q1 · MCQ

The integral $\displaystyle\int_0^\pi\dfrac{8x\,dx}{4\cos^2x+\sin^2x}$ is equal to:

(1) $2\pi^2$  (2) $4\pi^2$  (3) $\pi^2$  (4) $\dfrac{3\pi^2}2$

**Answer: (1)** · key (compiled)

**Solution.** The denominator is symmetric under $x\to\pi-x$, so $\int_0^\pi xf=\dfrac\pi2\int_0^\pi f$. $\int_0^\pi\dfrac{dx}{4\cos^2x+\sin^2x}=2\int_0^{\pi/2}\dfrac{\sec^2x\,dx}{4+\tan^2x}=2\cdot\dfrac12\cdot\dfrac\pi2=\dfrac\pi2$. The integral is $8\cdot\dfrac\pi2\cdot\dfrac\pi2=2\pi^2$.

### M-DEF-11 · B — JEE Main 2025 · Apr session · set Q2 · MCQ

The integral $\displaystyle\int_0^\pi\dfrac{(x+3)\sin x}{1+3\cos^2x}dx$ is equal to:

(1) $\dfrac\pi{\sqrt3}(\pi+1)$  (2) $\dfrac\pi{\sqrt3}(\pi+2)$  (3) $\dfrac\pi{3\sqrt3}(\pi+6)$  (4) $\dfrac\pi{2\sqrt3}(\pi+4)$

**Answer: (3)** · key (compiled)

**Solution.** Let $J=\int_0^\pi\dfrac{\sin x}{1+3\cos^2x}dx=\int_{-1}^1\dfrac{du}{1+3u^2}=\dfrac{2}{\sqrt3}\tan^{-1}\sqrt3=\dfrac{2\pi}{3\sqrt3}$. The $x\sin x$ part: $\int_0^\pi xf=\dfrac\pi2J=\dfrac{\pi^2}{3\sqrt3}$ (property $x\to\pi-x$). Total $=\dfrac{\pi^2}{3\sqrt3}+3J=\dfrac{\pi^2}{3\sqrt3}+\dfrac{2\pi}{\sqrt3}=\dfrac\pi{3\sqrt3}(\pi+6)$.

### M-DEF-12 · C — JEE Main 2024 · 27 Jan Shift 1 · Q75 · MCQ

If $\displaystyle\int_0^1\frac{dx}{\sqrt{3+x}+\sqrt{1+x}}=a+b\sqrt2+c\sqrt3$, where $a,b,c$ are rational, then $2a+3b-4c$ is equal to

(1) 4  (2) 10  (3) 7  (4) 8

**Answer: (4)** · key ✔

**Solution.** Rationalise: $\dfrac1{\sqrt{3+x}+\sqrt{1+x}}=\dfrac{\sqrt{3+x}-\sqrt{1+x}}2$. So the integral is $\tfrac12\cdot\tfrac23\big[(3+x)^{3/2}-(1+x)^{3/2}\big]_0^1=\tfrac13\big[(8-2\sqrt2)-(3\sqrt3-1)\big]=3-\tfrac23\sqrt2-\sqrt3$. Thus $a=3,\ b=-\tfrac23,\ c=-1$ and $2a+3b-4c=6-2+4=8$.

### M-DEF-13 · C — JEE Main 2024 · 30 Jan Shift 1 · Q74 · MCQ

The value of $\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac{n^3}{(n^2+k^2)(n^2+3k^2)}$ is

(1) $\dfrac{(2\sqrt3+3)\pi}{24}$  (2) $\dfrac{13\pi}{8(4\sqrt3+3)}$  (3) $\dfrac{13(2\sqrt3-3)\pi}8$  (4) $\dfrac\pi{8(2\sqrt3+3)}$

**Answer: (2)** · key ✔

**Solution.** Dividing by $n^4$: the sum is $\sum\dfrac1n\cdot\dfrac1{(1+(k/n)^2)(1+3(k/n)^2)}\to\int_0^1\dfrac{dx}{(1+x^2)(1+3x^2)}$. Partial fractions: $\dfrac1{(1+x^2)(1+3x^2)}=\dfrac{3/2}{1+3x^2}-\dfrac{1/2}{1+x^2}$. Integral $=\dfrac{3}{2\sqrt3}\tan^{-1}\sqrt3-\dfrac12\cdot\dfrac\pi4=\dfrac{\sqrt3}2\cdot\dfrac\pi3-\dfrac\pi8=\dfrac{(4\sqrt3-3)\pi}{24}$. Rationalising: $\dfrac{(4\sqrt3-3)(4\sqrt3+3)\pi}{24(4\sqrt3+3)}=\dfrac{39\pi}{24(4\sqrt3+3)}=\dfrac{13\pi}{8(4\sqrt3+3)}$.

### M-DEF-14 · C — JEE Main 2024 · 30 Jan Shift 2 · Q75 · MCQ

Let $y=f(x)$ be a thrice differentiable function in $(-5,5)$. The tangents to the curve at $(1,f(1))$ and $(3,f(3))$ make angles $\dfrac\pi6$ and $\dfrac\pi4$ with the positive $x$-axis respectively. If $27\displaystyle\int_1^3\left((f'(t))^2+1\right)f''(t)\,dt=\alpha+\beta\sqrt3$, where $\alpha,\beta$ are integers, then $\alpha+\beta$ equals

(1) $-14$  (2) 26  (3) $-16$  (4) 36

**Answer: (2)** · key ✔

**Solution.** $f'(1)=\tan\tfrac\pi6=\tfrac1{\sqrt3}$ and $f'(3)=\tan\tfrac\pi4=1$. With $u=f'(t)$: $\int(u^2+1)du=\tfrac{u^3}3+u$. Evaluated from $\tfrac1{\sqrt3}$ to $1$: $\tfrac43-\left(\tfrac1{9\sqrt3}+\tfrac1{\sqrt3}\right)=\tfrac43-\tfrac{10}{9\sqrt3}=\tfrac43-\tfrac{10\sqrt3}{27}$. Times $27$: $36-10\sqrt3$, so $\alpha=36,\ \beta=-10$ and $\alpha+\beta=26$.

### M-DEF-15 · C — JEE Main 2024 · 1 Feb Shift 2 · Q74 · MCQ

The value of $\displaystyle\int_0^1\left(2x^3-3x^2-x+1\right)^{1/3}dx$ is:

(1) 0  (2) 1  (3) 2  (4) $-1$

**Answer: (1)** · key ✔

**Solution.** Let $g(x)=2x^3-3x^2-x+1$. Then $g(1-x)=-g(x)$, so $g^{1/3}(1-x)=-g^{1/3}(x)$. By the King property $I=\int_0^1g^{1/3}(1-x)dx=-I$, so $I=0$.

