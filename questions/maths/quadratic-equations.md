# Quadratic Equations & Inequalities

> Theory: [../../theory/maths/quadratic-equations.md](../../theory/maths/quadratic-equations.md)

### M-QDR-01 — JEE Main 2024 · 27 Jan Shift 2 · Q61 · MCQ

If $\alpha,\beta$ are the roots of $x^2-x-1=0$ and $S_n=2023\alpha^n+2024\beta^n$, then

(1) $2S_{12}=S_{11}+S_{10}$  (2) $S_{12}=S_{11}+S_{10}$  (3) $2S_{11}=S_{12}+S_{10}$  (4) $S_{11}=S_{10}+S_{12}$

**Answer: (2)** · key ✔

**Solution.** Each root satisfies $t^2=t+1$, so $t^{n}=t^{n-1}+t^{n-2}$. Multiplying by the coefficients and adding: $S_n=S_{n-1}+S_{n-2}$. Hence $S_{12}=S_{11}+S_{10}$.

### M-QDR-02 — JEE Main 2024 · 30 Jan Shift 1 · Q81 · Numerical

Let $\alpha,\beta\in\mathbb N$ be roots of $x^2-70x+\lambda=0$, where $\dfrac\lambda2,\dfrac\lambda3\notin\mathbb N$. If $\lambda$ assumes the minimum possible value, then $\dfrac{\left(\sqrt{\alpha-1}+\sqrt{\beta-1}\right)(\lambda+35)}{|\alpha-\beta|}$ is equal to ______.

**Answer: 60** · key ✔

**Solution.** $\alpha+\beta=70$ and $\lambda=\alpha\beta$. $\lambda$ is smaller when $\alpha,\beta$ are far apart, so test in order: $(1,69)$: $\lambda=69$, divisible by $3$; $(2,68)$: $136$, even; $(3,67)$: $201$, divisible by $3$; $(4,66)$: $264$, even; $(5,65)$: $\lambda=325$, not divisible by $2$ or $3$. So $\lambda=325$. Then $\dfrac{(2+8)(360)}{60}=60$.

### M-QDR-03 — JEE Main 2024 · 30 Jan Shift 2 · Q81 · Numerical

The number of real solutions of the equation $x\left(x^2+3|x|+5|x-1|+6|x-2|\right)=0$ is ______.

**Answer: 1** · key ✔

**Solution.** Either $x=0$ or $x^2+3|x|+5|x-1|+6|x-2|=0$. The second expression is a sum of non-negative terms and vanishes only if $x=0$, $x=1$ and $x=2$ simultaneously, which is impossible. So the only real solution is $x=0$.

### M-QDR-04 — JEE Main 2024 · 31 Jan Shift 1 · Q61 · MCQ

Let $S$ be the set of positive integral values of $a$ for which $\dfrac{ax^2+(2a+1)x+9a+4}{x^2-8x+32}<0$ for all $x\in\mathbb R$. Then the number of elements in $S$ is

(1) 1  (2) 0  (3) $\infty$  (4) 3

**Answer: (2)** · key ✔

**Solution.** The denominator $x^2-8x+32=(x-4)^2+16>0$, so we need $ax^2+(2a+1)x+9a+4<0$ for all $x$: $a<0$ and discriminant $<0$. But $a$ is a positive integer, so the first condition already fails. $S$ is empty and $n(S)=0$.

### M-QDR-05 — JEE Main 2024 · 31 Jan Shift 1 · Q68 · MCQ

Let $a$ be the sum of all coefficients in the expansion of $(1-2x+2x^2)^{2023}(3-4x^2+2x^3)^{2024}$ and $b=\displaystyle\lim_{x\to0}\dfrac{\int_0^x\frac{\ln(1+t)}{t^{2024}+1}dt}{x^2}$. If the equations $cx^2+dx+e=0$ and $2bx^2+ax+4=0$ have a common root, where $c,d,e\in\mathbb R$, then $d:c:e$ equals

(1) 2 : 1 : 4  (2) 4 : 1 : 4  (3) 1 : 2 : 4  (4) 1 : 1 : 4

**Answer: (4)** · key ✔

**Solution.** $a=(1-2+2)^{2023}(3-4+2)^{2024}=1$. For $b$, by L'Hôpital: $\dfrac{\ln(1+x)/(x^{2024}+1)}{2x}\to\dfrac12$, so $b=\dfrac12$. The second equation is $x^2+x+4=0$, with discriminant $1-16<0$, so its roots are non-real conjugates. A real-coefficient quadratic sharing one non-real root also shares its conjugate, hence the two quadratics are proportional: $c:d:e=1:1:4$.

