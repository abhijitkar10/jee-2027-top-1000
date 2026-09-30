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

