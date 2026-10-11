# Differential Equations

> Theory: [../../theory/maths/differential-equations.md](../../theory/maths/differential-equations.md)

### M-DIF-01 — JEE Main 2024 · 27 Jan Shift 1 · Q88 · Numerical

If the solution of $(2x+3y-2)\,dx+(4x+6y-7)\,dy=0$, $y(0)=3$, is $\alpha x+\beta y+3\ln|2x+3y-\gamma|=6$, then $\alpha+2\beta+3\gamma$ is equal to ______.

**Answer: 29** · key ✔

**Solution.** Put $u=2x+3y$: $\dfrac{du}{dx}=2+3\dfrac{dy}{dx}=\dfrac{u-8}{2u-7}$, so $\left(2+\dfrac9{u-8}\right)du=dx\Rightarrow2u+9\ln|u-8|=x+c$. Substituting $u$: $3x+6y+9\ln|2x+3y-8|=c'$; dividing by 3: $x+2y+3\ln|2x+3y-8|=c''$. At $(0,3)$: $6+3\ln1=6$. So $\alpha=1,\beta=2,\gamma=8$ and $\alpha+2\beta+3\gamma=1+4+24=29$.

### M-DIF-02 — JEE Main 2024 · 27 Jan Shift 2 · Q76 · MCQ

If $y=y(x)$ is the solution curve of $(x^2-4)\,dy-(y^2-3y)\,dx=0$, $x>2$, $y(4)=\dfrac32$, and the slope of the curve is never zero, then $y(10)$ equals

(1) $\dfrac3{1+8^{1/4}}$  (2) $\dfrac3{1+2\sqrt2}$  (3) $\dfrac3{1-2\sqrt2}$  (4) $\dfrac3{1-8^{1/4}}$

**Answer: (1)** · key ✔

**Solution.** Separate: $\dfrac{dy}{y(y-3)}=\dfrac{dx}{x^2-4}\Rightarrow\tfrac13\ln\left|\tfrac{y-3}y\right|=\tfrac14\ln\left|\tfrac{x-2}{x+2}\right|+c$. At $(4,\tfrac32)$: $\tfrac{y-3}y=-1$ so LHS $=0$, giving $c=-\tfrac14\ln\tfrac13$. So $\ln\left|\tfrac{y-3}y\right|=\tfrac34\ln\!\left(\tfrac{3(x-2)}{x+2}\right)$. At $x=10$: $\tfrac{3\cdot8}{12}=2$, so $\left|\tfrac{y-3}y\right|=2^{3/4}=8^{1/4}$. The sign is negative as at $x=4$ ($y$ stays between $0$ and $3$), so $y-3=-8^{1/4}y\Rightarrow y=\dfrac3{1+8^{1/4}}$.

### M-DIF-03 — JEE Main 2024 · 27 Jan Shift 2 · Q89 · Numerical

If the solution curve of $\dfrac{dy}{dx}=\dfrac{x+y-2}{x-y}$ passing through $(2,1)$ is $\tan^{-1}\dfrac{y-1}{x-1}-\dfrac1\beta\ln_e\!\left(\alpha+\left(\dfrac{y-1}{x-1}\right)^2\right)=\ln_e|x-1|$, then $5\beta+\alpha$ is equal to ______.

**Answer: 11** · key ✔

**Solution.** Put $X=x-1,\ Y=y-1$: $\dfrac{dY}{dX}=\dfrac{X+Y}{X-Y}$. With $Y=vX$: $X\dfrac{dv}{dX}=\dfrac{1+v}{1-v}-v=\dfrac{1+v^2}{1-v}$, so $\int\dfrac{1-v}{1+v^2}dv=\ln|X|+c$, i.e. $\tan^{-1}v-\tfrac12\ln(1+v^2)=\ln|X|+c$. At $(2,1)$: $v=0,X=1\Rightarrow c=0$. Comparing: $\beta=2,\ \alpha=1$, so $5\beta+\alpha=11$.

### M-DIF-04 — JEE Main 2024 · 29 Jan Shift 1 · Q76 · MCQ

A function $y=f(x)$ satisfies $f(x)\sin2x+\sin x-(1+\cos^2x)f'(x)=0$ with $f(0)=0$. Then $f\!\left(\dfrac\pi2\right)$ is equal to

(1) 1  (2) 0  (3) $-1$  (4) 2

**Answer: (1)** · key ✔

**Solution.** Rewrite as $f'-\dfrac{\sin2x}{1+\cos^2x}f=\dfrac{\sin x}{1+\cos^2x}$. Since $\int\dfrac{\sin2x}{1+\cos^2x}dx=-\ln(1+\cos^2x)$, the integrating factor is $e^{\int-\frac{\sin2x}{1+\cos^2x}dx}=1+\cos^2x$. So $\dfrac d{dx}\left[f(1+\cos^2x)\right]=\sin x$, giving $f(1+\cos^2x)=-\cos x+C$. From $f(0)=0$: $0=-1+C\Rightarrow C=1$. At $x=\tfrac\pi2$: $f\cdot1=0+1$, so $f\!\left(\tfrac\pi2\right)=1$.

### M-DIF-05 — JEE Main 2024 · 29 Jan Shift 1 · Q89 · Numerical

If the solution curve $y=y(x)$ of $(1+y^2)(1+\ln x)\,dx+x\,dy=0$, $x>0$, passes through $(1,1)$ and $y(e)=\dfrac{\alpha-\tan\frac32}{\beta+\tan\frac32}$, then $\alpha+2\beta$ is ______.

**Answer: 3** · key ✔

**Solution.** Separate: $\dfrac{dy}{1+y^2}=-\dfrac{1+\ln x}{x}dx\Rightarrow\tan^{-1}y=-\left(\ln x+\tfrac{(\ln x)^2}2\right)+C$. At $(1,1)$: $C=\tfrac\pi4$. At $x=e$: $\tan^{-1}y=\tfrac\pi4-\tfrac32\Rightarrow y=\tan\!\left(\tfrac\pi4-\tfrac32\right)=\dfrac{1-\tan\frac32}{1+\tan\frac32}$. So $\alpha=\beta=1$ and $\alpha+2\beta=3$.

### M-DIF-06 — JEE Main 2024 · 29 Jan Shift 2 · Q76 · MCQ

If $y$ is the solution of the differential equation $x\cos\!\left(\dfrac yx\right)\dfrac{dy}{dx}=y\cos\!\left(\dfrac yx\right)+x$ with $y(1)=\dfrac\pi3$ and $\sin\!\left(\dfrac yx\right)=\ln|x|+\dfrac\alpha2$, then $\alpha^2$ is equal to

(1) 3  (2) 12  (3) 4  (4) 9

**Answer: (1)** · key ✔

**Solution.** Divide by $x\cos\frac yx$: $\dfrac{dy}{dx}=\dfrac yx+\sec\dfrac yx$. With $y=vx$: $v+x\dfrac{dv}{dx}=v+\sec v\Rightarrow\cos v\,dv=\dfrac{dx}x\Rightarrow\sin v=\ln|x|+C$. At $x=1$, $v=\tfrac\pi3$: $\dfrac{\sqrt3}2=C=\dfrac\alpha2\Rightarrow\alpha=\sqrt3$. So $\alpha^2=3$.

### M-DIF-07 — JEE Main 2024 · 30 Jan Shift 1 · Q76 · MCQ

Let $y=y(x)$ be the solution of $\sec x\,dy+\{2(1-x)\tan x+x(2-x)\}\,dx=0$ such that $y(0)=2$. Then $y(2)$ is equal to

(1) 2  (2) $2\{1-\sin(2)\}$  (3) $2\{\sin(2)+1\}$  (4) 1

**Answer: (1)** · key ✔

**Solution.** $\dfrac{dy}{dx}=-\cos x\{2(1-x)\tan x+x(2-x)\}=-\{2(1-x)\sin x+x(2-x)\cos x\}=-\dfrac d{dx}\left[x(2-x)\sin x\right]$, since $\dfrac d{dx}[x(2-x)]=2-2x$. So $y=-x(2-x)\sin x+C$, and $y(0)=2\Rightarrow C=2$. At $x=2$: $y(2)=0+2=2$.

### M-DIF-08 — JEE Main 2024 · 30 Jan Shift 1 · Q89 · Numerical

Let $y=y(x)$ be the solution of $(1-x^2)\,dy=\left[xy+(x^3+2)\sqrt{3(1-x^2)}\right]dx$, $-1<x<1$, $y(0)=0$. If $y\!\left(\tfrac12\right)=\dfrac mn$ with $m,n$ coprime, then $m+n$ is equal to ______.

**Answer: 97** · key ✔

**Solution.** $\dfrac{dy}{dx}-\dfrac{x}{1-x^2}y=\dfrac{(x^3+2)\sqrt3}{\sqrt{1-x^2}}$. Integrating factor: $e^{-\int\frac x{1-x^2}dx}=\sqrt{1-x^2}$. So $\dfrac d{dx}\left(y\sqrt{1-x^2}\right)=\sqrt3(x^3+2)\Rightarrow y\sqrt{1-x^2}=\sqrt3\left(\dfrac{x^4}4+2x\right)+C$, and $y(0)=0\Rightarrow C=0$. At $x=\tfrac12$: $y\cdot\dfrac{\sqrt3}2=\sqrt3\left(\dfrac1{64}+1\right)=\dfrac{65\sqrt3}{64}\Rightarrow y=\dfrac{65}{32}$. So $m+n=97$.

### M-DIF-09 — JEE Main 2024 · 31 Jan Shift 2 · Q88 · Numerical

Let $y=y(x)$ be the solution of $\sec^2x\,dx+\left(e^{2y}\tan^2x+\tan x\right)dy=0$, $0<x<\dfrac\pi2$, $y\!\left(\dfrac\pi4\right)=0$. If $y\!\left(\dfrac\pi6\right)=\alpha$, then $e^{8\alpha}$ is equal to ______.

**Answer: 9** · key ✔

**Solution.** Put $u=\tan x$: $\dfrac{du}{dy}+e^{2y}u^2+u=0$. Let $w=\dfrac1u$: $\dfrac{dw}{dy}=-u^{-2}\dfrac{du}{dy}=e^{2y}+w$, so $\dfrac{dw}{dy}-w=e^{2y}$, with integrating factor $e^{-y}$: $we^{-y}=e^{y}+C$. At $y=0$, $u=1\Rightarrow w=1\Rightarrow C=0$, so $w=e^{2y}$, i.e. $\tan x=e^{-2y}$. At $x=\tfrac\pi6$: $\tfrac1{\sqrt3}=e^{-2\alpha}\Rightarrow e^{2\alpha}=\sqrt3\Rightarrow e^{8\alpha}=(\sqrt3)^4=9$.

### M-DIF-10 — JEE Advanced 2025 · Paper 1 · Q13 · Numerical

For $x>0$: $y_1'-(\sin x)^2y_1=0$, $y_1(1)=5$; $y_2'-(\cos x)^2y_2=0$, $y_2(1)=\tfrac13$; $y_3'-\dfrac{2-x^3}{x^3}y_3=0$, $y_3(1)=\dfrac{3}{5e}$. Then $\displaystyle\lim_{x\to0^+}\frac{y_1(x)y_2(x)y_3(x)+2x}{e^{3x}\sin x}=$ ______.

**Answer: 2** · official key ✔ (re-derived)

**Solution.** $y_1=5\exp\int_1^x\sin^2t\,dt$ and $y_2=\tfrac13\exp\int_1^x\cos^2t\,dt$, so $y_1y_2=\tfrac53\exp(x-1)$, which is finite at $0$. For $y_3$: $\dfrac{y_3'}{y_3}=\dfrac2{x^3}-1$, so $y_3=Ce^{-1/x^2-x}$, and $y_3\to0$ faster than any power of $x$ as $x\to0^+$. So $y_1y_2y_3=o(x)$ and the limit is $\lim\dfrac{2x}{e^{3x}\sin x}=2$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $y=y(x)$ be the solution of the differential equation $\sec x\dfrac{dy}{dx}-2y=2+3\sin x$, $x\in\left(-\dfrac\pi2,\dfrac\pi2\right)$, $y(0)=-\dfrac74$. Then $y\left(\dfrac\pi6\right)$ is equal to:

(1) $-\dfrac54$  (2) $-\dfrac52$  (3) $-3\sqrt3-7$  (4) $-3\sqrt2-7$

**Answer: (2)** · key (compiled)

**Solution.** Multiply by $\cos x$: $\dfrac{dy}{dx}-2\cos x\,y=(2+3\sin x)\cos x$, a linear equation with integrating factor $e^{-2\sin x}$. With $s=\sin x$: $\int(2+3s)e^{-2s}ds=-e^{-2s}\left(\tfrac32s+\tfrac74\right)$. So $y=-\tfrac32\sin x-\tfrac74+Ce^{2\sin x}$; $y(0)=-\tfrac74+C=-\tfrac74\Rightarrow C=0$. $y\left(\tfrac\pi6\right)=-\tfrac34-\tfrac74=-\tfrac52$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

Let $y=y(x)$ be the solution of the differential equation $x^4dy+\left(4x^3y+2\sin x\right)dx=0$, $x>0$, $y\left(\dfrac\pi2\right)=0$. Then $\pi^4y\left(\dfrac\pi3\right)$ is equal to:

(1) 72  (2) 92  (3) 64  (4) 81

**Answer: (4)** · key (compiled)

**Solution.** $x^4dy+4x^3y\,dx=d(x^4y)$, so $d(x^4y)=-2\sin x\,dx\Rightarrow x^4y=2\cos x+C$. $y\left(\tfrac\pi2\right)=0\Rightarrow C=0$. $y\left(\tfrac\pi3\right)=\dfrac{2\cos(\pi/3)}{(\pi/3)^4}=\dfrac{81}{\pi^4}$, so $\pi^4y\left(\tfrac\pi3\right)=81$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q3 · Numerical

Let $f$ be a twice differentiable non-negative function such that $(f(x))^2=25+\int_0^x\left((f(t))^2+(f'(t))^2\right)dt$. Then the mean of $f(\log_e(1)),f(\log_e(2)),\dots,f(\log_e(625))$ is equal to ______.

**Answer: 1565** · key (compiled)

**Solution.** Differentiating: $2ff'=f^2+f'^2\Rightarrow(f-f')^2=0\Rightarrow f'=f$, so $f=Ce^x$. At $x=0$: $f(0)^2=25$ and $f\ge0$ give $f(0)=5$: $f(x)=5e^x$. Then $f(\ln k)=5k$, and the mean of $5k$ for $k=1,\dots,625$ is $5\cdot\dfrac{626}2=1565$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q4 · MCQ

Let $y=y(x)$ be the solution of the differential equation $x\dfrac{dy}{dx}-y=x^2\cot x$, $x\in(0,\pi)$. If $y\left(\dfrac\pi2\right)=\dfrac\pi2$, then $6y\left(\dfrac\pi6\right)-8y\left(\dfrac\pi4\right)$ is equal to:

(1) $3\pi$  (2) $\pi$  (3) $-\pi$  (4) $-3\pi$

**Answer: (3)** · key (compiled)

**Solution.** $\dfrac{dy}{dx}-\dfrac yx=x\cot x$ with integrating factor $\tfrac1x$: $\dfrac d{dx}\left(\dfrac yx\right)=\cot x\Rightarrow\dfrac yx=\ln\sin x+C$. $y\left(\tfrac\pi2\right)=\tfrac\pi2\Rightarrow C=1$, so $y=x\ln\sin x+x$. $6y\left(\tfrac\pi6\right)=\pi(1-\ln2)$ and $8y\left(\tfrac\pi4\right)=2\pi\left(1-\tfrac12\ln2\right)=2\pi-\pi\ln2$. The difference is $\pi-\pi\ln2-2\pi+\pi\ln2=-\pi$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q5 · MCQ

Let $y=y(x)$ be a differentiable function in the interval $(0,\infty)$ such that $y(1)=2$, and $\lim_{t\to x}\left(\dfrac{t^2y(x)-x^2y(t)}{x-t}\right)=3$ for each $x>0$. Then $2y(2)$ is equal to:

(1) 23  (2) 27  (3) 12  (4) 18

**Answer: (1)** · key (compiled)

**Solution.** The limit is $\tfrac00$; differentiate numerator and denominator with respect to $t$: $\dfrac{2ty(x)-x^2y'(t)}{-1}\to\dfrac{2xy-x^2y'}{-1}=3$, so $x^2y'-2xy=3$, i.e. $\dfrac d{dx}\left(\dfrac y{x^2}\right)=\dfrac3{x^4}$. Hence $\dfrac y{x^2}=-\dfrac1{x^3}+C$, $y=Cx^2-\dfrac1x$. $y(1)=2\Rightarrow C=3$. $y(2)=12-\tfrac12=\tfrac{23}2$ and $2y(2)=23$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q7 · MCQ

Let the solution curve of the differential equation $x\,dy-y\,dx=\sqrt{x^2+y^2}\,dx$, $x>0$, $y(1)=0$, be $y=y(x)$. Then $y(3)$ is equal to:

(1) 1  (2) 4  (3) 2  (4) 6

**Answer: (2)** · key (compiled)

**Solution.** Put $y=vx$: $x(v\,dx+x\,dv)-vx\,dx=x\sqrt{1+v^2}\,dx\Rightarrow\dfrac{dv}{\sqrt{1+v^2}}=\dfrac{dx}x\Rightarrow\sinh^{-1}v=\ln x+C$. $y(1)=0$ gives $C=0$, so $v=\sinh(\ln x)=\dfrac{x-1/x}2$ and $y=\dfrac{x^2-1}2$. $y(3)=4$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q8 · MCQ

Let $f:[1,\infty)\to\mathbb R$ be a differentiable function. If $6\int_1^xf(t)\,dt=3xf(x)+x^3-4$ for all $x\ge1$, then the value of $f(2)-f(3)$ is:

(1) $-4$  (2) 3  (3) 4  (4) $-3$

**Answer: (2)** · key (compiled)

**Solution.** Differentiate: $6f=3f+3xf'+3x^2\Rightarrow xf'-f=-x^2\Rightarrow\dfrac d{dx}\left(\dfrac fx\right)=-1\Rightarrow f=-x^2+Cx$. At $x=1$: $0=3f(1)+1-4\Rightarrow f(1)=1\Rightarrow C=2$. $f(x)=2x-x^2$: $f(2)=0$, $f(3)=-3$, so $f(2)-f(3)=3$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q9 · Numerical

If the solution curve $y=f(x)$ of the differential equation $(x^2-4)y'-2xy+2x(4-x^2)^2=0$, $x>2$, passes through the point $(3,15)$, then the local maximum value of $f$ is ______.

**Answer: 16** · key (compiled)

**Solution.** $y'-\dfrac{2x}{x^2-4}y=-2x(x^2-4)$. With integrating factor $\dfrac1{x^2-4}$: $\dfrac d{dx}\left(\dfrac y{x^2-4}\right)=-2x\Rightarrow y=(x^2-4)(C-x^2)$. $(3,15)$: $15=5(C-9)\Rightarrow C=12$, so $f(x)=(x^2-4)(12-x^2)=-x^4+16x^2-48$. $f'=-4x(x^2-8)=0\Rightarrow x=2\sqrt2$ (for $x>2$), and $f''<0$ there. Local maximum value $=(8-4)(12-8)=16$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q10 · MCQ

Let $y=y(x)$ be the solution curve of the differential equation $(1+x^2)dy+(y-\tan^{-1}x)dx=0$, $y(0)=1$. Then the value of $y(1)$ is:

(1) $\dfrac4{e^{\pi/4}}+\dfrac\pi2-1$  (2) $\dfrac2{e^{\pi/4}}+\dfrac\pi4-1$  (3) $\dfrac2{e^{\pi/4}}-\dfrac\pi4-1$  (4) $\dfrac4{e^{\pi/4}}-\dfrac\pi2-1$

**Answer: (2)** · key (compiled)

**Solution.** $\dfrac{dy}{dx}+\dfrac y{1+x^2}=\dfrac{\tan^{-1}x}{1+x^2}$, integrating factor $e^{\tan^{-1}x}$. With $t=\tan^{-1}x$: $ye^t=\int te^tdt=e^t(t-1)+C$, so $y=\tan^{-1}x-1+Ce^{-\tan^{-1}x}$. $y(0)=1\Rightarrow C=2$. $y(1)=\dfrac\pi4-1+2e^{-\pi/4}$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q11 · MCQ

Let $y=y(x)$ be the solution of the differential equation $x\dfrac{dy}{dx}-\sin2y=x^3(2-x^3)\cos^2y$, $x\ne0$. If $y(2)=0$, then $\tan(y(1))$ is equal to:

(1) $-\dfrac34$  (2) $\dfrac34$  (3) $-\dfrac74$  (4) $\dfrac74$

**Answer: (4)** · key (compiled)

**Solution.** Divide by $\cos^2y$: $x\sec^2y\dfrac{dy}{dx}-2\tan y=x^3(2-x^3)$. With $v=\tan y$: $\dfrac{dv}{dx}-\dfrac{2v}x=x^2(2-x^3)$. Integrating factor $x^{-2}$: $\dfrac d{dx}\left(\dfrac v{x^2}\right)=2-x^3\Rightarrow v=2x^3-\dfrac{x^6}4+Cx^2$. $y(2)=0\Rightarrow v(2)=16-16+4C=0\Rightarrow C=0$. $\tan y(1)=2-\dfrac14=\dfrac74$.

