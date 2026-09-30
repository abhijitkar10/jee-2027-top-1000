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

