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

