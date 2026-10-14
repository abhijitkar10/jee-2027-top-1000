# Differential Equations

> Theory: [../../theory/maths/differential-equations.md](../../theory/maths/differential-equations.md)

### M-DIF-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $y=y(x)$ be the solution of the differential equation $\sec x\dfrac{dy}{dx}-2y=2+3\sin x$, $x\in\left(-\dfrac\pi2,\dfrac\pi2\right)$, $y(0)=-\dfrac74$. Then $y\left(\dfrac\pi6\right)$ is equal to:

(1) $-\dfrac54$  (2) $-\dfrac52$  (3) $-3\sqrt3-7$  (4) $-3\sqrt2-7$

**Answer: (2)** · key (compiled)

**Solution.** Multiply by $\cos x$: $\dfrac{dy}{dx}-2\cos x\,y=(2+3\sin x)\cos x$, a linear equation with integrating factor $e^{-2\sin x}$. With $s=\sin x$: $\int(2+3s)e^{-2s}ds=-e^{-2s}\left(\tfrac32s+\tfrac74\right)$. So $y=-\tfrac32\sin x-\tfrac74+Ce^{2\sin x}$; $y(0)=-\tfrac74+C=-\tfrac74\Rightarrow C=0$. $y\left(\tfrac\pi6\right)=-\tfrac34-\tfrac74=-\tfrac52$.

### M-DIF-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

Let $y=y(x)$ be the solution of the differential equation $x^4dy+\left(4x^3y+2\sin x\right)dx=0$, $x>0$, $y\left(\dfrac\pi2\right)=0$. Then $\pi^4y\left(\dfrac\pi3\right)$ is equal to:

(1) 72  (2) 92  (3) 64  (4) 81

**Answer: (4)** · key (compiled)

**Solution.** $x^4dy+4x^3y\,dx=d(x^4y)$, so $d(x^4y)=-2\sin x\,dx\Rightarrow x^4y=2\cos x+C$. $y\left(\tfrac\pi2\right)=0\Rightarrow C=0$. $y\left(\tfrac\pi3\right)=\dfrac{2\cos(\pi/3)}{(\pi/3)^4}=\dfrac{81}{\pi^4}$, so $\pi^4y\left(\tfrac\pi3\right)=81$.

### M-DIF-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q4 · MCQ

Let $y=y(x)$ be the solution of the differential equation $x\dfrac{dy}{dx}-y=x^2\cot x$, $x\in(0,\pi)$. If $y\left(\dfrac\pi2\right)=\dfrac\pi2$, then $6y\left(\dfrac\pi6\right)-8y\left(\dfrac\pi4\right)$ is equal to:

(1) $3\pi$  (2) $\pi$  (3) $-\pi$  (4) $-3\pi$

**Answer: (3)** · key (compiled)

**Solution.** $\dfrac{dy}{dx}-\dfrac yx=x\cot x$ with integrating factor $\tfrac1x$: $\dfrac d{dx}\left(\dfrac yx\right)=\cot x\Rightarrow\dfrac yx=\ln\sin x+C$. $y\left(\tfrac\pi2\right)=\tfrac\pi2\Rightarrow C=1$, so $y=x\ln\sin x+x$. $6y\left(\tfrac\pi6\right)=\pi(1-\ln2)$ and $8y\left(\tfrac\pi4\right)=2\pi\left(1-\tfrac12\ln2\right)=2\pi-\pi\ln2$. The difference is $\pi-\pi\ln2-2\pi+\pi\ln2=-\pi$.

### M-DIF-04 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q5 · MCQ

Let $y=y(x)$ be a differentiable function in the interval $(0,\infty)$ such that $y(1)=2$, and $\lim_{t\to x}\left(\dfrac{t^2y(x)-x^2y(t)}{x-t}\right)=3$ for each $x>0$. Then $2y(2)$ is equal to:

(1) 23  (2) 27  (3) 12  (4) 18

**Answer: (1)** · key (compiled)

**Solution.** The limit is $\tfrac00$; differentiate numerator and denominator with respect to $t$: $\dfrac{2ty(x)-x^2y'(t)}{-1}\to\dfrac{2xy-x^2y'}{-1}=3$, so $x^2y'-2xy=3$, i.e. $\dfrac d{dx}\left(\dfrac y{x^2}\right)=\dfrac3{x^4}$. Hence $\dfrac y{x^2}=-\dfrac1{x^3}+C$, $y=Cx^2-\dfrac1x$. $y(1)=2\Rightarrow C=3$. $y(2)=12-\tfrac12=\tfrac{23}2$ and $2y(2)=23$.

### M-DIF-05 · A — JEE Main 2026 · 22 Jan Shift 1 · set Q7 · MCQ

Let the solution curve of the differential equation $x\,dy-y\,dx=\sqrt{x^2+y^2}\,dx$, $x>0$, $y(1)=0$, be $y=y(x)$. Then $y(3)$ is equal to:

(1) 1  (2) 4  (3) 2  (4) 6

**Answer: (2)** · key (compiled)

**Solution.** Put $y=vx$: $x(v\,dx+x\,dv)-vx\,dx=x\sqrt{1+v^2}\,dx\Rightarrow\dfrac{dv}{\sqrt{1+v^2}}=\dfrac{dx}x\Rightarrow\sinh^{-1}v=\ln x+C$. $y(1)=0$ gives $C=0$, so $v=\sinh(\ln x)=\dfrac{x-1/x}2$ and $y=\dfrac{x^2-1}2$. $y(3)=4$.

### M-DIF-06 · A — JEE Main 2025 · Jan session · set Q1 · Numerical

Let $y=y(x)$ be the solution of the differential equation $2\cos x\dfrac{dy}{dx}=\sin2x-4y\sin x$, $x\in\left(0,\tfrac\pi2\right)$. If $y\left(\tfrac\pi3\right)=0$, then $y'\left(\tfrac\pi4\right)+y\left(\tfrac\pi4\right)$ is equal to ______.

**Answer: 1** · key (compiled)

**Solution.** Dividing by $2\cos x$: $y'+2\tan x\,y=\sin x$. The integrating factor is $\sec^2x$: $y\sec^2x=\int\sin x\sec^2x\,dx=\sec x+C$. $y(\tfrac\pi3)=0\Rightarrow0=2+C$, so $y=\cos x-2\cos^2x$. $y'=-\sin x+2\sin2x$: at $\tfrac\pi4$, $y'=-\tfrac{\sqrt2}2+2$ and $y=\tfrac{\sqrt2}2-1$, so the sum is 1.

### M-DIF-07 · B — JEE Advanced 2025 · Paper 1 · Q13 · Numerical

For $x>0$: $y_1'-(\sin x)^2y_1=0$, $y_1(1)=5$; $y_2'-(\cos x)^2y_2=0$, $y_2(1)=\tfrac13$; $y_3'-\dfrac{2-x^3}{x^3}y_3=0$, $y_3(1)=\dfrac{3}{5e}$. Then $\displaystyle\lim_{x\to0^+}\frac{y_1(x)y_2(x)y_3(x)+2x}{e^{3x}\sin x}=$ ______.

**Answer: 2** · official key ✔ (re-derived)

**Solution.** $y_1=5\exp\int_1^x\sin^2t\,dt$ and $y_2=\tfrac13\exp\int_1^x\cos^2t\,dt$, so $y_1y_2=\tfrac53\exp(x-1)$, which is finite at $0$. For $y_3$: $\dfrac{y_3'}{y_3}=\dfrac2{x^3}-1$, so $y_3=Ce^{-1/x^2-x}$, and $y_3\to0$ faster than any power of $x$ as $x\to0^+$. So $y_1y_2y_3=o(x)$ and the limit is $\lim\dfrac{2x}{e^{3x}\sin x}=2$.

### M-DIF-08 · B — JEE Main 2025 · Jan session · set Q2 · MCQ

Let $x=x(y)$ be the solution of the differential equation $y=\left(x-y\dfrac{dx}{dy}\right)\sin\left(\dfrac xy\right)$, $y>0$ and $x(1)=\dfrac\pi2$. Then $\cos(x(2))$ is equal to:

(1) $1-2(\log_e2)^2$  (2) $1-2\log_e2$  (3) $2(\log_e2)-1$  (4) $2(\log_e2)^2-1$

**Answer: (4)** · key (compiled)

**Solution.** Put $x=vy$: $x-y\dfrac{dx}{dy}=-y^2\dfrac{dv}{dy}$, so $1=-y\,v'\sin v$, i.e. $-\sin v\,dv=\dfrac{dy}y$, giving $\cos v=\ln y+C$. $y=1$, $v=\tfrac\pi2$ gives $C=0$. At $y=2$: $\cos\dfrac{x}{2}=\ln2$, so $\cos(x(2))=2\cos^2\dfrac x2-1=2(\ln2)^2-1$.

### M-DIF-09 · B — JEE Main 2025 · Apr session · set Q1 · MCQ

Let $y=y(x)$ be the solution of the differential equation $\dfrac{dy}{dx}+3(\tan^2x)\,y+3y=\sec^2x$, $y(0)=\tfrac13+e^3$. Then $y\left(\tfrac\pi4\right)$ is equal to:

(1) $\tfrac23$  (2) $\tfrac43$  (3) $\tfrac43+e^3$  (4) $\tfrac23+e^3$

**Answer: (2)** · key (compiled)

**Solution.** $3\tan^2x+3=3\sec^2x$, so $y'+3\sec^2x\,y=\sec^2x$ with integrating factor $e^{3\tan x}$: $ye^{3\tan x}=\dfrac{e^{3\tan x}}3+C$, i.e. $y=\tfrac13+Ce^{-3\tan x}$. $y(0)=\tfrac13+C=\tfrac13+e^3\Rightarrow C=e^3$. $y\left(\tfrac\pi4\right)=\tfrac13+e^3e^{-3}=\tfrac43$.

### M-DIF-10 · B — JEE Main 2025 · Apr session · set Q3 · MCQ

Let $g$ be a differentiable function such that $\displaystyle\int_0^xg(t)dt=x-\int_0^xtg(t)dt$, $x\ge0$, and let $y=y(x)$ satisfy the differential equation $\dfrac{dy}{dx}-y\tan x=2(x+1)\sec x\,g(x)$, $x\in\left[0,\tfrac\pi2\right)$. If $y(0)=0$, then $y\left(\tfrac\pi3\right)$ is equal to:

(1) $\dfrac{2\pi}{3\sqrt3}$  (2) $\dfrac{4\pi}3$  (3) $\dfrac{2\pi}3$  (4) $\dfrac{4\pi}{3\sqrt3}$

**Answer: (2)** · key (compiled)

**Solution.** Differentiating the integral relation: $g=1-xg\Rightarrow g=\dfrac1{1+x}$. The equation becomes $y'-y\tan x=2\sec x$ with integrating factor $\cos x$: $(y\cos x)'=2$, so $y\cos x=2x$ (as $y(0)=0$). $y\left(\tfrac\pi3\right)=\dfrac{2\pi/3}{1/2}=\dfrac{4\pi}3$.

### M-DIF-11 · B — JEE Main 2024 · 27 Jan Shift 2 · Q76 · MCQ

If $y=y(x)$ is the solution curve of $(x^2-4)\,dy-(y^2-3y)\,dx=0$, $x>2$, $y(4)=\dfrac32$, and the slope of the curve is never zero, then $y(10)$ equals

(1) $\dfrac3{1+8^{1/4}}$  (2) $\dfrac3{1+2\sqrt2}$  (3) $\dfrac3{1-2\sqrt2}$  (4) $\dfrac3{1-8^{1/4}}$

**Answer: (1)** · key ✔

**Solution.** Separate: $\dfrac{dy}{y(y-3)}=\dfrac{dx}{x^2-4}\Rightarrow\tfrac13\ln\left|\tfrac{y-3}y\right|=\tfrac14\ln\left|\tfrac{x-2}{x+2}\right|+c$. At $(4,\tfrac32)$: $\tfrac{y-3}y=-1$ so LHS $=0$, giving $c=-\tfrac14\ln\tfrac13$. So $\ln\left|\tfrac{y-3}y\right|=\tfrac34\ln\!\left(\tfrac{3(x-2)}{x+2}\right)$. At $x=10$: $\tfrac{3\cdot8}{12}=2$, so $\left|\tfrac{y-3}y\right|=2^{3/4}=8^{1/4}$. The sign is negative as at $x=4$ ($y$ stays between $0$ and $3$), so $y-3=-8^{1/4}y\Rightarrow y=\dfrac3{1+8^{1/4}}$.

### M-DIF-12 · C — JEE Main 2024 · 29 Jan Shift 1 · Q76 · MCQ

A function $y=f(x)$ satisfies $f(x)\sin2x+\sin x-(1+\cos^2x)f'(x)=0$ with $f(0)=0$. Then $f\!\left(\dfrac\pi2\right)$ is equal to

(1) 1  (2) 0  (3) $-1$  (4) 2

**Answer: (1)** · key ✔

**Solution.** Rewrite as $f'-\dfrac{\sin2x}{1+\cos^2x}f=\dfrac{\sin x}{1+\cos^2x}$. Since $\int\dfrac{\sin2x}{1+\cos^2x}dx=-\ln(1+\cos^2x)$, the integrating factor is $e^{\int-\frac{\sin2x}{1+\cos^2x}dx}=1+\cos^2x$. So $\dfrac d{dx}\left[f(1+\cos^2x)\right]=\sin x$, giving $f(1+\cos^2x)=-\cos x+C$. From $f(0)=0$: $0=-1+C\Rightarrow C=1$. At $x=\tfrac\pi2$: $f\cdot1=0+1$, so $f\!\left(\tfrac\pi2\right)=1$.

### M-DIF-13 · C — JEE Main 2024 · 30 Jan Shift 1 · Q76 · MCQ

Let $y=y(x)$ be the solution of $\sec x\,dy+\{2(1-x)\tan x+x(2-x)\}\,dx=0$ such that $y(0)=2$. Then $y(2)$ is equal to

(1) 2  (2) $2\{1-\sin(2)\}$  (3) $2\{\sin(2)+1\}$  (4) 1

**Answer: (1)** · key ✔

**Solution.** $\dfrac{dy}{dx}=-\cos x\{2(1-x)\tan x+x(2-x)\}=-\{2(1-x)\sin x+x(2-x)\cos x\}=-\dfrac d{dx}\left[x(2-x)\sin x\right]$, since $\dfrac d{dx}[x(2-x)]=2-2x$. So $y=-x(2-x)\sin x+C$, and $y(0)=2\Rightarrow C=2$. At $x=2$: $y(2)=0+2=2$.

