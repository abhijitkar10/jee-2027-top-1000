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

