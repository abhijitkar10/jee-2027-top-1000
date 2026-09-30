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

