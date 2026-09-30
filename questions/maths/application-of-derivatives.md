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

