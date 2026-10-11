# Definite Integration

> Theory: [../../theory/maths/definite-integration.md](../../theory/maths/definite-integration.md)

### M-DEF-01 — JEE Main 2024 · 27 Jan Shift 1 · Q75 · MCQ

If $\displaystyle\int_0^1\frac{dx}{\sqrt{3+x}+\sqrt{1+x}}=a+b\sqrt2+c\sqrt3$, where $a,b,c$ are rational, then $2a+3b-4c$ is equal to

(1) 4  (2) 10  (3) 7  (4) 8

**Answer: (4)** · key ✔

**Solution.** Rationalise: $\dfrac1{\sqrt{3+x}+\sqrt{1+x}}=\dfrac{\sqrt{3+x}-\sqrt{1+x}}2$. So the integral is $\tfrac12\cdot\tfrac23\big[(3+x)^{3/2}-(1+x)^{3/2}\big]_0^1=\tfrac13\big[(8-2\sqrt2)-(3\sqrt3-1)\big]=3-\tfrac23\sqrt2-\sqrt3$. Thus $a=3,\ b=-\tfrac23,\ c=-1$ and $2a+3b-4c=6-2+4=8$.

### M-DEF-02 — JEE Main 2024 · 27 Jan Shift 1 · Q76 · MCQ

If $(a,b)$ is the orthocentre of the triangle with vertices $(1,2),(2,3),(3,1)$ and $I_1=\int_a^b x\sin(4x-x^2)\,dx,\ I_2=\int_a^b\sin(4x-x^2)\,dx$, then $\dfrac{36I_1}{I_2}$ is equal to

(1) 72  (2) 88  (3) 80  (4) 66

**Answer: (1)** · key ✔

**Solution.** Altitudes $y-2=\tfrac12(x-1)$ and $y-3=2(x-2)$ meet at $\left(\tfrac53,\tfrac73\right)$, so $a+b=4$. Since $4x-x^2$ is symmetric about $x=2$, King's property $x\to a+b-x=4-x$ gives $I_1=\int_a^b(4-x)\sin(4x-x^2)\,dx=4I_2-I_1$, so $I_1=2I_2$. Hence $36I_1/I_2=72$.

### M-DEF-03 — JEE Main 2024 · 27 Jan Shift 2 · Q75 · MCQ

For $0<a<1$, the value of $\displaystyle\int_0^\pi\frac{dx}{1-2a\cos x+a^2}$ is

(1) $\dfrac{\pi^2}{\pi+a^2}$  (2) $\dfrac{\pi^2}{\pi-a^2}$  (3) $\dfrac{\pi}{1-a^2}$  (4) $\dfrac{\pi}{1+a^2}$

**Answer: (3)** · key ✔

**Solution.** Use $t=\tan\frac x2$: $\cos x=\dfrac{1-t^2}{1+t^2}$, $dx=\dfrac{2\,dt}{1+t^2}$, and $1-2a\cos x+a^2=\dfrac{(1-a)^2+(1+a)^2t^2}{1+t^2}$. The integral becomes $\displaystyle\int_0^\infty\frac{2\,dt}{(1-a)^2+(1+a)^2t^2}=\frac{2}{(1-a)(1+a)}\cdot\frac\pi2=\frac{\pi}{1-a^2}$.

### M-DEF-04 — JEE Main 2024 · 29 Jan Shift 1 · Q75 · MCQ

For $x\in\left(-\dfrac\pi2,\dfrac\pi2\right)$, let $y(x)=\displaystyle\int\frac{\csc x+\sin x}{\csc x\sec x+\tan x\sin^2x}\,dx$ with $\displaystyle\lim_{x\to(\pi/2)^-}y(x)=0$. Then $y\!\left(\dfrac\pi4\right)$ is

(1) $\tan^{-1}\dfrac1{\sqrt2}$  (2) $\tfrac12\tan^{-1}\dfrac1{\sqrt2}$  (3) $-\dfrac1{\sqrt2}\tan^{-1}\dfrac1{\sqrt2}$  (4) $\dfrac1{\sqrt2}\tan^{-1}\!\left(-\tfrac12\right)$

**Answer: (4)** · key ✔

**Solution.** Numerator: $\dfrac{1+\sin^2x}{\sin x}$. Denominator: $\dfrac{1+\sin^4x}{\sin x\cos x}$. The integrand is $\dfrac{\cos x\,(1+\sin^2x)}{1+\sin^4x}$. With $u=\sin x$: $\displaystyle\int\frac{1+u^2}{1+u^4}du=\frac1{\sqrt2}\tan^{-1}\!\left(\frac{u-1/u}{\sqrt2}\right)+C$. As $x\to\tfrac\pi2$, $u\to1$ and the $\tan^{-1}$ term $\to0$, so $C=0$. At $x=\tfrac\pi4$, $u=\tfrac1{\sqrt2}$: $\dfrac{u-1/u}{\sqrt2}=\dfrac{-1/\sqrt2}{\sqrt2}=-\tfrac12$, giving $y=\dfrac1{\sqrt2}\tan^{-1}\!\left(-\tfrac12\right)$.

### M-DEF-05 — JEE Main 2024 · 29 Jan Shift 2 · Q88 · Numerical

If $\displaystyle\int_{\pi/6}^{\pi/3}\sqrt{1-\sin2x}\,dx=\alpha+\beta\sqrt2+\gamma\sqrt3$, where $\alpha,\beta,\gamma$ are rational numbers, then $3\alpha+4\beta-\gamma$ is equal to ______.

**Answer: 6** · key ✔

**Solution.** $\sqrt{1-\sin2x}=|\cos x-\sin x|$, which is positive for $x<\tfrac\pi4$ and negative after. $\int_{\pi/6}^{\pi/4}(\cos x-\sin x)dx=\left[\sin x+\cos x\right]=\sqrt2-\tfrac12-\tfrac{\sqrt3}2$ and $\int_{\pi/4}^{\pi/3}(\sin x-\cos x)dx=\left[-\cos x-\sin x\right]=\sqrt2-\tfrac12-\tfrac{\sqrt3}2$. Total $=-1+2\sqrt2-\sqrt3$, so $\alpha=-1,\beta=2,\gamma=-1$ and $3\alpha+4\beta-\gamma=-3+8+1=6$.

### M-DEF-06 — JEE Main 2024 · 30 Jan Shift 1 · Q74 · MCQ

The value of $\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac{n^3}{(n^2+k^2)(n^2+3k^2)}$ is

(1) $\dfrac{(2\sqrt3+3)\pi}{24}$  (2) $\dfrac{13\pi}{8(4\sqrt3+3)}$  (3) $\dfrac{13(2\sqrt3-3)\pi}8$  (4) $\dfrac\pi{8(2\sqrt3+3)}$

**Answer: (2)** · key ✔

**Solution.** Dividing by $n^4$: the sum is $\sum\dfrac1n\cdot\dfrac1{(1+(k/n)^2)(1+3(k/n)^2)}\to\int_0^1\dfrac{dx}{(1+x^2)(1+3x^2)}$. Partial fractions: $\dfrac1{(1+x^2)(1+3x^2)}=\dfrac{3/2}{1+3x^2}-\dfrac{1/2}{1+x^2}$. Integral $=\dfrac{3}{2\sqrt3}\tan^{-1}\sqrt3-\dfrac12\cdot\dfrac\pi4=\dfrac{\sqrt3}2\cdot\dfrac\pi3-\dfrac\pi8=\dfrac{(4\sqrt3-3)\pi}{24}$. Rationalising: $\dfrac{(4\sqrt3-3)(4\sqrt3+3)\pi}{24(4\sqrt3+3)}=\dfrac{39\pi}{24(4\sqrt3+3)}=\dfrac{13\pi}{8(4\sqrt3+3)}$.

### M-DEF-07 — JEE Main 2024 · 30 Jan Shift 1 · Q88 · Numerical

The value of $9\displaystyle\int_0^9\left[\sqrt{\frac{10x}{x+1}}\right]dx$, where $[t]$ denotes the greatest integer $\le t$, is ______.

**Answer: 155** · key ✔

**Solution.** $g(x)=\sqrt{\tfrac{10x}{x+1}}$ increases from $0$ to $3$ on $[0,9]$. $g\ge1\iff x\ge\tfrac19$ and $g\ge2\iff10x\ge4x+4\iff x\ge\tfrac23$. So $[g]=0$ on $[0,\tfrac19)$, $1$ on $[\tfrac19,\tfrac23)$, $2$ on $[\tfrac23,9)$ (it reaches $3$ only at $x=9$). Integral $=1\left(\tfrac23-\tfrac19\right)+2\left(9-\tfrac23\right)=\tfrac59+\tfrac{50}3=\tfrac{155}9$. Times $9$: $155$.

### M-DEF-08 — JEE Main 2024 · 30 Jan Shift 2 · Q75 · MCQ

Let $y=f(x)$ be a thrice differentiable function in $(-5,5)$. The tangents to the curve at $(1,f(1))$ and $(3,f(3))$ make angles $\dfrac\pi6$ and $\dfrac\pi4$ with the positive $x$-axis respectively. If $27\displaystyle\int_1^3\left((f'(t))^2+1\right)f''(t)\,dt=\alpha+\beta\sqrt3$, where $\alpha,\beta$ are integers, then $\alpha+\beta$ equals

(1) $-14$  (2) 26  (3) $-16$  (4) 36

**Answer: (2)** · key ✔

**Solution.** $f'(1)=\tan\tfrac\pi6=\tfrac1{\sqrt3}$ and $f'(3)=\tan\tfrac\pi4=1$. With $u=f'(t)$: $\int(u^2+1)du=\tfrac{u^3}3+u$. Evaluated from $\tfrac1{\sqrt3}$ to $1$: $\tfrac43-\left(\tfrac1{9\sqrt3}+\tfrac1{\sqrt3}\right)=\tfrac43-\tfrac{10}{9\sqrt3}=\tfrac43-\tfrac{10\sqrt3}{27}$. Times $27$: $36-10\sqrt3$, so $\alpha=36,\ \beta=-10$ and $\alpha+\beta=26$.

### M-DEF-09 — JEE Main 2024 · 30 Jan Shift 2 · Q76 · MCQ

Let $f:\mathbb R\to\mathbb R$ be $f(x)=ae^{2x}+be^x+cx$. If $f(0)=-1$, $f'(\ln2)=21$ and $\displaystyle\int_0^{\ln4}\left(f(x)-cx\right)dx=\tfrac{39}2$, then $|a+b+c|$ equals

(1) 16  (2) 10  (3) 12  (4) 8

**Answer: (4)** · key ✔

**Solution.** $f(0)=a+b=-1$. $f'(\ln2)=8a+2b+c=21$. $\int_0^{\ln4}(ae^{2x}+be^x)dx=a\cdot\tfrac{16-1}2+b(4-1)=\tfrac{15a}2+3b=\tfrac{39}2\Rightarrow5a+2b=13$. With $b=-1-a$: $3a=15\Rightarrow a=5,\ b=-6$, and $c=21-40+12=-7$. So $a+b+c=-8$ and $|a+b+c|=8$.

### M-DEF-10 — JEE Main 2024 · 31 Jan Shift 1 · Q88 · Numerical

If the integral $525\displaystyle\int_0^{\pi/2}\sin2x\cos^{11/2}x\left(1+\cos^{5/2}x\right)^{1/2}dx$ equals $n\sqrt2-64$, then $n$ is equal to ______.

**Answer: 176** · key ✔

**Solution.** With $\sin2x=2\sin x\cos x$ and $t=\cos x$: $I=\displaystyle\int_0^12t^{13/2}\left(1+t^{5/2}\right)^{1/2}dt$. Let $s=1+t^{5/2}$, so $t^{3/2}dt=\tfrac25ds$ and $t^{5}=(s-1)^2$: $I=\tfrac45\displaystyle\int_1^2(s-1)^2\sqrt s\,ds=\tfrac45\left[\tfrac27s^{7/2}-\tfrac45s^{5/2}+\tfrac23s^{3/2}\right]_1^2=\tfrac45\left(\tfrac{44\sqrt2}{105}-\tfrac{16}{105}\right)$. Then $525I=4\left(44\sqrt2-16\right)=176\sqrt2-64$, so $n=176$.

### M-DEF-11 — JEE Main 2024 · 1 Feb Shift 1 · Q75 · MCQ

The value of $\displaystyle\int_0^{\pi/4}\frac{x\,dx}{\sin^4 2x+\cos^4 2x}$ equals:

(1) $\dfrac{\sqrt2\pi^2}{8}$  (2) $\dfrac{\sqrt2\pi^2}{16}$  (3) $\dfrac{\sqrt2\pi^2}{32}$  (4) $\dfrac{\sqrt2\pi^2}{64}$

**Answer: (3)** · key ✔

**Solution.** Put $t=2x$: $I=\tfrac14\int_0^{\pi/2}\dfrac{t\,dt}{\sin^4t+\cos^4t}$. The denominator is symmetric under $t\to\tfrac\pi2-t$, so $\int_0^{\pi/2}tf=\tfrac\pi4\int_0^{\pi/2}f$. Using $\sin^4t+\cos^4t=1-\tfrac12\sin^22t$, $\int_0^{\pi/2}\dfrac{dt}{1-\frac12\sin^22t}=\dfrac{\pi}{\sqrt2}$. Hence $I=\tfrac14\cdot\tfrac\pi4\cdot\tfrac{\pi}{\sqrt2}=\dfrac{\pi^2}{16\sqrt2}=\dfrac{\sqrt2\pi^2}{32}$.

### M-DEF-12 — JEE Main 2024 · 1 Feb Shift 2 · Q74 · MCQ

The value of $\displaystyle\int_0^1\left(2x^3-3x^2-x+1\right)^{1/3}dx$ is:

(1) 0  (2) 1  (3) 2  (4) $-1$

**Answer: (1)** · key ✔

**Solution.** Let $g(x)=2x^3-3x^2-x+1$. Then $g(1-x)=-g(x)$, so $g^{1/3}(1-x)=-g^{1/3}(x)$. By the King property $I=\int_0^1g^{1/3}(1-x)dx=-I$, so $I=0$.

### M-DEF-13 — JEE Main 2024 · 1 Feb Shift 2 · Q75 · MCQ

If $\displaystyle\int_0^{\pi/3}\cos^4x\,dx=a\pi+b\sqrt3$ with $a,b$ rational, then $9a+8b$ is:

(1) 2  (2) 1  (3) 3  (4) $\dfrac32$

**Answer: (1)** · key ✔

**Solution.** $\cos^4x=\dfrac{3+4\cos2x+\cos4x}{8}$. Integrating: $\left[\tfrac{3x}8+\tfrac{\sin2x}4+\tfrac{\sin4x}{32}\right]_0^{\pi/3}=\dfrac\pi8+\dfrac{\sqrt3}8-\dfrac{\sqrt3}{64}=\dfrac\pi8+\dfrac{7\sqrt3}{64}$. So $a=\tfrac18$, $b=\tfrac7{64}$ and $9a+8b=\tfrac98+\tfrac78=2$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · Numerical

If $\int_0^14\cot^{-1}\left(1-2x+4x^2\right)dx=a\tan^{-1}(2)-b\log_e(5)$, where $a,b\in\mathbb N$, then $(2a+b)$ is equal to ______.

**Answer: 9** · key (compiled)

**Solution.** $\cot^{-1}(1-2x+4x^2)=\tan^{-1}\dfrac1{1+2x(2x-1)}=\tan^{-1}(2x)-\tan^{-1}(2x-1)$. $\int_0^1\tan^{-1}(2x)dx=\left[x\tan^{-1}2x-\tfrac14\ln(1+4x^2)\right]_0^1=\tan^{-1}2-\tfrac14\ln5$. $\int_0^1\tan^{-1}(2x-1)dx=\tfrac12\int_{-1}^1\tan^{-1}s\,ds=0$ (odd function). So $4\int=4\tan^{-1}2-\ln5$: $a=4$, $b=1$ and $2a+b=9$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

The value of the integral $\int_{\pi/24}^{5\pi/24}\dfrac{dx}{1+\sqrt[3]{\tan2x}}$ is:

(1) $\dfrac\pi3$  (2) $\dfrac\pi{12}$  (3) $\dfrac\pi{18}$  (4) $\dfrac\pi6$

**Answer: (2)** · key (compiled)

**Solution.** The limits add to $\tfrac{6\pi}{24}=\tfrac\pi4$; apply $x\to\tfrac\pi4-x$ (King's rule), under which $\tan2x\to\cot2x$. Then $I=\int\dfrac{dx}{1+\sqrt[3]{\cot2x}}=\int\dfrac{\sqrt[3]{\tan2x}}{1+\sqrt[3]{\tan2x}}dx$. Adding: $2I=\int_{\pi/24}^{5\pi/24}dx=\dfrac{4\pi}{24}=\dfrac\pi6$, so $I=\dfrac\pi{12}$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let $[\cdot]$ denote the greatest integer function. Then $\int_{-\pi/2}^{\pi/2}\left(\dfrac{12(3+[x])}{3+[\sin x]+[\cos x]}\right)dx$ is equal to:

(1) $13\pi+1$  (2) $12\pi+5$  (3) $11\pi+2$  (4) $15\pi+4$

**Answer: (3)** · key (compiled)

**Solution.** Split at $x=-1,0,1$. On $\left[-\tfrac\pi2,-1\right)$: $[x]=-2$, $[\sin x]=-1$, $[\cos x]=0$, integrand $\dfrac{12(1)}{2}=6$, length $\tfrac\pi2-1$. On $[-1,0)$: $[x]=-1$, $[\sin x]=-1$, $[\cos x]=0$: $\dfrac{12\cdot2}{2}=12$, length 1. On $(0,1)$: $[x]=0$, $[\sin x]=0$, $[\cos x]=0$: $\dfrac{36}3=12$, length 1. On $\left[1,\tfrac\pi2\right]$: $[x]=1$, $[\sin x]=0$, $[\cos x]=0$: $\dfrac{48}3=16$, length $\tfrac\pi2-1$. Total $=6\left(\tfrac\pi2-1\right)+12+12+16\left(\tfrac\pi2-1\right)=11\pi+2$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · Numerical

If $f(x)$ satisfies the relation $f(x)=e^x+\int_0^1\left(y+xe^x\right)f(y)\,dy$, then $e+f(0)$ is equal to ______.

**Answer: 2** · key (compiled)

**Solution.** Let $A=\int_0^1yf(y)dy$ and $B=\int_0^1f(y)dy$; then $f(x)=e^x+A+Bxe^x$. $B=\int_0^1(e^y+A+Bye^y)dy=(e-1)+A+B\int_0^1ye^ydy=(e-1)+A+B$ (since $\int_0^1ye^ydy=1$), so $A=1-e$ and $B$ drops out. Hence $f(0)=1+A=2-e$ and $e+f(0)=2$. (The value of $B$ itself is not needed.)

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · MCQ

Let $f(x)=[x]^2-[x+3]-3$, $x\in\mathbb R$, where $[\ ]$ is the greatest integer function. Then:

(1) $\int_0^2f(x)dx=-6$  (2) $f(x)<0$ only for $x\in[-1,3)$  (3) $f(x)>0$ only for $x\in[4,\infty)$  (4) $f(x)=0$ for finitely many values of $x$

**Answer: (2)** · key (compiled)

**Solution.** For $x\in[n,n+1)$: $f=n^2-(n+3)-3=n^2-n-6=(n-3)(n+2)$. $f<0$ iff $-2<n<3$, i.e. $n=-1,0,1,2$, i.e. $x\in[-1,3)$ – (2) true. (1) is false: $f=-6$ on $[0,1)$ and on $[1,2)$, so $\int_0^2f=-12$. (3) is false: $f>0$ also for $n\le-3$ ($x<-2$). (4) is false: $f=0$ on the whole intervals $[3,4)$ and $[-2,-1)$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q6 · Numerical

Let $[\cdot]$ be the greatest integer function. If $\alpha=\int_0^{64}\left(x^{1/3}-[x^{1/3}]\right)dx$, then $\dfrac1\pi\int_0^{\alpha\pi}\left(\dfrac{\sin^2\theta}{\sin^6\theta+\cos^6\theta}\right)d\theta$ is equal to ______.

**Answer: 36** · key (compiled)

**Solution.** With $x=u^3$: $\alpha=\int_0^4\{u\}\,3u^2du=\sum_{k=0}^3\int_k^{k+1}3u^2(u-k)du=\tfrac34+\tfrac{17}4+\tfrac{43}4+\tfrac{81}4=36$. The integrand $\dfrac{\sin^2\theta}{\sin^6\theta+\cos^6\theta}$ has period $\pi$, so the integral is $36\,J$ with $J=\int_0^\pi\dfrac{\sin^2\theta}{1-\tfrac34\sin^22\theta}d\theta$. Writing $\sin^2\theta=\tfrac{1-\cos2\theta}2$, the $\cos2\theta$ part integrates to 0 over a period, so $J=\tfrac12\int_0^\pi\dfrac{d\theta}{1-\tfrac34\sin^22\theta}=\tfrac12\cdot2\int_0^{\pi/2}\dfrac{d\varphi}{1-\tfrac34\sin^2\varphi}\cdot$ with $\int_0^{\pi/2}\dfrac{d\varphi}{1-k\sin^2\varphi}=\dfrac\pi{2\sqrt{1-k}}=\pi$, giving $J=\pi$. The required value is $\dfrac1\pi\cdot36\pi=36$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q7 · MCQ

The value of $\int_{-\pi/2}^{\pi/2}\left(\dfrac1{[x]+4}\right)dx$, where $[\cdot]$ denotes the greatest integer function, is:

(1) $\dfrac1{60}(21\pi-1)$  (2) $\dfrac7{60}(\pi-3)$  (3) $\dfrac7{60}(3\pi-1)$  (4) $\dfrac1{60}(\pi-7)$

**Answer: (3)** · key (compiled)

**Solution.** $[x]=-2$ on $\left[-\tfrac\pi2,-1\right)$ (length $\tfrac\pi2-1$), $-1$ on $[-1,0)$, $0$ on $[0,1)$ and $1$ on $\left[1,\tfrac\pi2\right]$ (length $\tfrac\pi2-1$). The integral is $\dfrac12\left(\tfrac\pi2-1\right)+\dfrac13+\dfrac14+\dfrac15\left(\tfrac\pi2-1\right)=\dfrac7{10}\left(\tfrac\pi2-1\right)+\dfrac7{12}=\dfrac{7\pi}{20}-\dfrac7{60}=\dfrac7{60}(3\pi-1)$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q8 · Numerical

The number of elements in the set $S=\left\{x:x\in[0,100]\text{ and }\int_0^xt^2\sin(x-t)\,dt=x^2\right\}$ is ______.

**Answer: 16** · key (compiled)

**Solution.** The integral is the convolution of $t^2$ and $\sin t$. Its Laplace transform is $\dfrac2{s^3}\cdot\dfrac1{s^2+1}=2\left[\dfrac1{s^3}-\dfrac1s+\dfrac s{s^2+1}\right]$, so $\int_0^xt^2\sin(x-t)dt=x^2-2+2\cos x$. Setting this equal to $x^2$ gives $\cos x=1$, i.e. $x=2k\pi$. In $[0,100]$: $2k\pi\le100\Rightarrow k\le15.9$, so $k=0,1,\dots,15$: 16 elements.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q9 · MCQ

The value of $\int_{-\pi/6}^{\pi/6}\left(\dfrac{\pi+4x^{11}}{1-\sin\left(|x|+\frac\pi6\right)}\right)dx$ is equal to:

(1) $8\pi$  (2) $6\pi$  (3) $2\pi$  (4) $4\pi$

**Answer: (4)** · key (compiled)

**Solution.** The denominator is even and $4x^{11}$ is odd, so that part integrates to 0. The rest is $2\pi\int_0^{\pi/6}\dfrac{dx}{1-\sin(x+\pi/6)}$. With $u=x+\tfrac\pi6$ the limits become $\tfrac\pi6$ to $\tfrac\pi3$ and $\dfrac1{1-\sin u}=\sec^2u+\sec u\tan u$, so the integral is $[\tan u+\sec u]_{\pi/6}^{\pi/3}=(\sqrt3+2)-\left(\tfrac1{\sqrt3}+\tfrac2{\sqrt3}\right)=2$. The value is $2\pi\cdot2=4\pi$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q10 · Numerical

$6\int_0^\pi|(\sin3x+\sin2x+\sin x)|\,dx$ is equal to ______.

**Answer: 17** · key (compiled)

**Solution.** $\sin3x+\sin x=2\sin2x\cos x$, so the integrand is $g=\sin2x(2\cos x+1)$. Its sign on $[0,\pi]$: $+$ on $\left[0,\tfrac\pi2\right]$, $-$ on $\left[\tfrac\pi2,\tfrac{2\pi}3\right]$, $+$ on $\left[\tfrac{2\pi}3,\pi\right]$. With $G=-\tfrac{\cos3x}3-\tfrac{\cos2x}2-\cos x$: $G(0)=-\tfrac{11}6$, $G\left(\tfrac\pi2\right)=\tfrac12$, $G\left(\tfrac{2\pi}3\right)=\tfrac5{12}$, $G(\pi)=\tfrac56$. $\int|g|=\left(\tfrac12+\tfrac{11}6\right)-\left(\tfrac5{12}-\tfrac12\right)+\left(\tfrac56-\tfrac5{12}\right)=\tfrac73+\tfrac1{12}+\tfrac5{12}=\tfrac{17}6$. Times 6: 17.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q11 · MCQ

Let $f$ be a polynomial function such that $f\left(x^2+1\right)=x^4+5x^2+2$, for all $x\in\mathbb R$. Then $\int_0^3f(x)dx$ is equal to:

(1) $\dfrac53$  (2) $\dfrac{41}3$  (3) $\dfrac{27}2$  (4) $\dfrac{33}2$

**Answer: (4)** · key (compiled)

**Solution.** Put $u=x^2+1$: $f(u)=(u-1)^2+5(u-1)+2=u^2+3u-2$. $\int_0^3(x^2+3x-2)dx=9+\dfrac{27}2-6=\dfrac{33}2$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q12 · MCQ

If $\int\left(\dfrac{1-5\cos^2x}{\sin^5x\cos^2x}\right)dx=f(x)+C$, where $C$ is the constant of integration, then $f\left(\dfrac\pi6\right)-f\left(\dfrac\pi4\right)$ is equal to:

(1) $\dfrac1{\sqrt3}(26+\sqrt3)$  (2) $\dfrac1{\sqrt3}(26-\sqrt3)$  (3) $\dfrac4{\sqrt3}(8-\sqrt6)$  (4) $\dfrac2{\sqrt3}(4+\sqrt6)$

**Answer: (3)** · key (compiled)

**Solution.** Differentiate $\dfrac1{\sin^4x\cos x}$: $-4\sin^{-5}x+\sin^{-3}x\cos^{-2}x=\dfrac{-4\cos^2x+\sin^2x}{\sin^5x\cos^2x}=\dfrac{1-5\cos^2x}{\sin^5x\cos^2x}$. So $f(x)=\dfrac1{\sin^4x\cos x}$. $f\left(\tfrac\pi6\right)=\dfrac1{\tfrac1{16}\cdot\tfrac{\sqrt3}2}=\dfrac{32}{\sqrt3}$ and $f\left(\tfrac\pi4\right)=\dfrac1{\tfrac14\cdot\tfrac1{\sqrt2}}=4\sqrt2$. The difference is $\dfrac{32}{\sqrt3}-4\sqrt2=\dfrac{32-4\sqrt6}{\sqrt3}=\dfrac4{\sqrt3}\left(8-\sqrt6\right)$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q13 · Numerical

The value of $\sum_{r=1}^{20}\left(\left|\sqrt{\pi\left(\int_0^rx|\sin\pi x|\,dx\right)}\right|\right)$ is ______.

**Answer: 210** · key (compiled)

**Solution.** For an integer $r$, split into unit intervals: $\int_k^{k+1}x|\sin\pi x|dx=\int_0^1(k+s)\sin\pi s\,ds=\dfrac{2k}\pi+\dfrac1\pi=\dfrac{2k+1}\pi$ (using $\int_0^1\sin\pi s\,ds=\tfrac2\pi$ and $\int_0^1s\sin\pi s\,ds=\tfrac1\pi$). Summing $k=0,\dots,r-1$ gives $\dfrac{r^2}\pi$. So $\sqrt{\pi\cdot\dfrac{r^2}\pi}=r$ and $\sum_{r=1}^{20}r=210$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q14 · Numerical

Let a differentiable function $f$ satisfy the equation $\int_0^{36}f\left(\dfrac{tx}{36}\right)dt=4\alpha f(x)$. If $y=f(x)$ is a standard parabola passing through the points $(2,1)$ and $(-4,\beta)$, then $\beta^\alpha$ is equal to ______.

**Answer: 64** · key (compiled)

**Solution.** With $u=\dfrac{tx}{36}$, $dt=\dfrac{36}x\,du$: $\dfrac{36}x\int_0^xf(u)du=4\alpha f(x)\Rightarrow9\int_0^xf=\alpha xf(x)$. Differentiating: $9f=\alpha f+\alpha xf'$, so $\dfrac{f'}f=\dfrac{9-\alpha}{\alpha x}$ and $f=Cx^{(9-\alpha)/\alpha}$. A standard parabola $y=Cx^2$ needs $\dfrac{9-\alpha}\alpha=2\Rightarrow\alpha=3$. Through $(2,1)$: $C=\tfrac14$, so $\beta=f(-4)=\tfrac{16}4=4$. $\beta^\alpha=4^3=64$.

