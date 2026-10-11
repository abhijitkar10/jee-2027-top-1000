# Quadratic Equations & Inequalities

> Theory: [../../theory/maths/quadratic-equations.md](../../theory/maths/quadratic-equations.md)

### M-QDR-01 — JEE Main 2024 · 30 Jan Shift 1 · Q81 · Numerical

Let $\alpha,\beta\in\mathbb N$ be roots of $x^2-70x+\lambda=0$, where $\dfrac\lambda2,\dfrac\lambda3\notin\mathbb N$. If $\lambda$ assumes the minimum possible value, then $\dfrac{\left(\sqrt{\alpha-1}+\sqrt{\beta-1}\right)(\lambda+35)}{|\alpha-\beta|}$ is equal to ______.

**Answer: 60** · key ✔

**Solution.** $\alpha+\beta=70$ and $\lambda=\alpha\beta$. $\lambda$ is smaller when $\alpha,\beta$ are far apart, so test in order: $(1,69)$: $\lambda=69$, divisible by $3$; $(2,68)$: $136$, even; $(3,67)$: $201$, divisible by $3$; $(4,66)$: $264$, even; $(5,65)$: $\lambda=325$, not divisible by $2$ or $3$. So $\lambda=325$. Then $\dfrac{(2+8)(360)}{60}=60$.

### M-QDR-02 — JEE Main 2024 · 30 Jan Shift 2 · Q81 · Numerical

The number of real solutions of the equation $x\left(x^2+3|x|+5|x-1|+6|x-2|\right)=0$ is ______.

**Answer: 1** · key ✔

**Solution.** Either $x=0$ or $x^2+3|x|+5|x-1|+6|x-2|=0$. The second expression is a sum of non-negative terms and vanishes only if $x=0$, $x=1$ and $x=2$ simultaneously, which is impossible. So the only real solution is $x=0$.

### M-QDR-03 — JEE Main 2024 · 31 Jan Shift 1 · Q61 · MCQ

Let $S$ be the set of positive integral values of $a$ for which $\dfrac{ax^2+(2a+1)x+9a+4}{x^2-8x+32}<0$ for all $x\in\mathbb R$. Then the number of elements in $S$ is

(1) 1  (2) 0  (3) $\infty$  (4) 3

**Answer: (2)** · key ✔

**Solution.** The denominator $x^2-8x+32=(x-4)^2+16>0$, so we need $ax^2+(2a+1)x+9a+4<0$ for all $x$: $a<0$ and discriminant $<0$. But $a$ is a positive integer, so the first condition already fails. $S$ is empty and $n(S)=0$.

### M-QDR-04 — JEE Main 2024 · 31 Jan Shift 1 · Q68 · MCQ

Let $a$ be the sum of all coefficients in the expansion of $(1-2x+2x^2)^{2023}(3-4x^2+2x^3)^{2024}$ and $b=\displaystyle\lim_{x\to0}\dfrac{\int_0^x\frac{\ln(1+t)}{t^{2024}+1}dt}{x^2}$. If the equations $cx^2+dx+e=0$ and $2bx^2+ax+4=0$ have a common root, where $c,d,e\in\mathbb R$, then $d:c:e$ equals

(1) 2 : 1 : 4  (2) 4 : 1 : 4  (3) 1 : 2 : 4  (4) 1 : 1 : 4

**Answer: (4)** · key ✔

**Solution.** $a=(1-2+2)^{2023}(3-4+2)^{2024}=1$. For $b$, by L'Hôpital: $\dfrac{\ln(1+x)/(x^{2024}+1)}{2x}\to\dfrac12$, so $b=\dfrac12$. The second equation is $x^2+x+4=0$, with discriminant $1-16<0$, so its roots are non-real conjugates. A real-coefficient quadratic sharing one non-real root also shares its conjugate, hence the two quadratics are proportional: $c:d:e=1:1:4$.

### M-QDR-05 — JEE Main 2024 · 1 Feb Shift 1 · Q61 · MCQ

Let $S=\{x\in\mathbb R:(\sqrt3+\sqrt2)^x+(\sqrt3-\sqrt2)^x=10\}$. Then the number of elements in $S$ is:

(1) 4  (2) 0  (3) 2  (4) 1

**Answer: (3)** · key ✔

**Solution.** $(\sqrt3+\sqrt2)(\sqrt3-\sqrt2)=1$, so with $t=(\sqrt3+\sqrt2)^x>0$ the equation is $t+\tfrac1t=10$, i.e. $t^2-10t+1=0$, giving $t=5\pm2\sqrt6$ (both positive). Each $t$ gives exactly one $x$ (the map $x\mapsto t$ is one-one), so $|S|=2$.

### M-QDR-06 — JEE Main 2024 · 1 Feb Shift 2 · Q61 · MCQ

Let $\alpha,\beta$ be the roots of $px^2+qx-r=0$, $p\ne0$. If $p,q,r$ are consecutive terms of a non-constant G.P. and $\dfrac1\alpha+\dfrac1\beta=\dfrac34$, then $(\alpha-\beta)^2$ is:

(1) $\dfrac{80}{9}$  (2) $9$  (3) $\dfrac{20}{3}$  (4) $8$

**Answer: (1)** · key ✔

**Solution.** Let the G.P. ratio be $k$: $q=pk$, $r=pk^2$. $\dfrac1\alpha+\dfrac1\beta=\dfrac{\alpha+\beta}{\alpha\beta}=\dfrac{-q/p}{-r/p}=\dfrac qr=\dfrac1k=\dfrac34\Rightarrow k=\dfrac43$. Then $(\alpha-\beta)^2=(\alpha+\beta)^2-4\alpha\beta=k^2+4k^2=5k^2=\dfrac{80}{9}$.

### M-QDR-07 — JEE Main 2024 · 4 Apr Shift 1 · Q61 · MCQ

If $2$ and $6$ are the roots of $ax^2+bx+1=0$, then the quadratic equation whose roots are $\dfrac1{2a+b}$ and $\dfrac1{6a+b}$ is:

(1) $2x^2+11x+12=0$  (2) $x^2+8x+12=0$  (3) $4x^2+14x+12=0$  (4) $x^2+10x+16=0$

**Answer: (2)** · key ✔

**Solution.** Sum of roots $8=-b/a$ and product $12=1/a$, so $a=\tfrac1{12}$, $b=-\tfrac23$. Then $2a+b=-\tfrac12$ and $6a+b=-\tfrac16$, giving roots $-2$ and $-6$: $x^2+8x+12=0$.

### M-QDR-08 — JEE Advanced 2025 · Paper 1 · Q1 · MCQ

Let $a_i,b_i\in\mathbb R$ for $i\in\{1,2,3\}$ and define $f(x)=a_1+10x+a_2x^2+a_3x^3+x^4$, $g(x)=b_1+3x+b_2x^2+b_3x^3+x^4$, $h(x)=f(x+1)-g(x+2)$. If $f(x)\ne g(x)$ for every $x\in\mathbb R$, then the coefficient of $x^3$ in $h(x)$ is

(A) 8  (B) 2  (C) $-4$  (D) $-6$

**Answer: (C)** · official key ✔ (re-derived)

**Solution.** $f-g=(a_1-b_1)+7x+(a_2-b_2)x^2+(a_3-b_3)x^3$ has degree at most $3$. An odd-degree real polynomial always has a real root, and the $x^4$ terms have cancelled, so for $f-g$ to have no real root the cubic term must vanish: $a_3=b_3$ (the remaining quadratic can have negative discriminant). In $h(x)=f(x+1)-g(x+2)$ the $x^3$ coefficient is $[4+a_3]-[8+b_3]=4-8+(a_3-b_3)=-4$, since $(x+1)^4$ contributes $4x^3$ and $(x+2)^4$ contributes $8x^3$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $\alpha$ and $\beta$ be the roots of the equation $x^2+2ax+(3a+10)=0$ such that $\alpha<1<\beta$. Then the set of all possible values of $a$ is:

(1) $\left(-\infty,-\tfrac{11}{5}\right)$  (2) $(-\infty,-2)\cup(5,\infty)$  (3) $(-\infty,-3)$  (4) $\left(-\infty,-\tfrac{11}{5}\right)\cup(5,\infty)$

**Answer: (1)** · key (compiled)

**Solution.** Let $f(x)=x^2+2ax+3a+10$ (upward parabola). $\alpha<1<\beta$ means 1 lies strictly between the roots, which happens iff $f(1)<0$ (this also forces two real roots). $f(1)=1+2a+3a+10=5a+11<0\Rightarrow a<-\tfrac{11}{5}$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

A building construction work can be completed by two masons A and B together in 22.5 days. Mason A alone can complete the construction work in 24 days less than mason B alone. Then mason A alone will complete the construction work in:

(1) 30 days  (2) 36 days  (3) 24 days  (4) 42 days

**Answer: (2)** · key (compiled)

**Solution.** Let A take $a$ days and B take $a+24$ days. $\dfrac1a+\dfrac1{a+24}=\dfrac1{22.5}=\dfrac2{45}\Rightarrow45(2a+24)=2a(a+24)\Rightarrow a^2-21a-540=0\Rightarrow(a-36)(a+15)=0$. Since $a>0$, $a=36$ days.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q3 · MCQ

If $\alpha$ and $\beta$ ($\alpha<\beta$) are the roots of the equation $(-2+\sqrt3)(|\sqrt x-3|)+(x-6\sqrt x)+(9-2\sqrt3)=0$, $x\ge0$, then $\sqrt{\dfrac\beta\alpha}+\sqrt{\alpha\beta}$ is equal to:

(1) 8  (2) 11  (3) 9  (4) 10

**Answer: (4)** · key (compiled)

**Solution.** Put $t=\sqrt x\ge0$: $x-6\sqrt x+9=(t-3)^2$. With $u=|t-3|\ge0$ the equation becomes $u^2+(\sqrt3-2)u-2\sqrt3=0$, i.e. $(u-2)(u+\sqrt3)=0$, so $u=2$ (the other root is negative). Then $t=5$ or $t=1$, so $x=25$ or $x=1$: $\alpha=1,\ \beta=25$. $\sqrt{\beta/\alpha}+\sqrt{\alpha\beta}=5+5=10$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · MCQ

The smallest positive integral value of $a$ for which all the roots of $ax^4-ax^2+9=0$ are real and distinct is equal to:

(1) 4  (2) 9  (3) 3  (4) 7

**Answer: (4)** · key (compiled)

**Solution.** Put $t=x^2$: $t^2-at+9=0$. All four roots of the quartic are real and distinct iff this quadratic has two distinct *positive* roots: discriminant $a^2-36>0$, product $=9>0$, sum $=a>0$. So $a>6$ and the smallest positive integer is $a=7$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · MCQ

Let $\alpha,\beta$ be the roots of the quadratic equation $12x^2-20x+3\lambda=0$, $\lambda\in\mathbb Z$. If $\dfrac12\le|\beta-\alpha|\le\dfrac32$, then the sum of all possible values of $\lambda$ is:

(1) 1  (2) 6  (3) 3  (4) 4

**Answer: (3)** · key (compiled)

**Solution.** $\alpha+\beta=\dfrac53$, $\alpha\beta=\dfrac\lambda4$, so $|\beta-\alpha|=\sqrt{\dfrac{25}9-\lambda}=\dfrac{\sqrt{25-9\lambda}}3$. The condition gives $\dfrac32\le\sqrt{25-9\lambda}\le\dfrac92$, i.e. $\dfrac94\le25-9\lambda\le\dfrac{81}4$, so $\dfrac{19}{36}\le\lambda\le\dfrac{91}{36}$ ($0.53\le\lambda\le2.53$). Integers: $\lambda=1,2$, sum $=3$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q6 · MCQ

The sum of all the real solutions of the equation $\log_{(x+3)}(6x^2+28x+30)=5-2\log_{(6x+10)}(x^2+6x+9)$ is equal to:

(1) 2  (2) 1  (3) 0  (4) 4

**Answer: (3)** · key (compiled)

**Solution.** $6x^2+28x+30=2(3x+5)(x+3)$, $6x+10=2(3x+5)$, $x^2+6x+9=(x+3)^2$. Let $a=\log_{(x+3)}\big(2(3x+5)\big)$. LHS $=a+1$ and $\log_{2(3x+5)}(x+3)^2=\dfrac2a$. So $a+1=5-\dfrac4a\Rightarrow a^2-4a+4=0\Rightarrow a=2$, i.e. $(x+3)^2=6x+10\Rightarrow x^2=1\Rightarrow x=\pm1$. Both satisfy the domain conditions (bases $4$ and $2$, positive and $\ne1$; $6x+10>0$ and $\ne1$). Sum $=0$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q7 · MCQ

The sum of all the roots of the equation $(x-1)^2-5|x-1|+6=0$ is:

(1) 1  (2) 5  (3) 3  (4) 4

**Answer: (4)** · key (compiled)

**Solution.** Let $t=|x-1|\ge0$: $t^2-5t+6=0\Rightarrow t=2$ or $3$. $|x-1|=2\Rightarrow x=3,-1$; $|x-1|=3\Rightarrow x=4,-2$. Sum $=3-1+4-2=4$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q8 · MCQ

Let $S=\{x^3+ax^2+bx+c:\ a,b,c\in\mathbb N,\ a,b,c\le20\}$ be a set of polynomials. Then the number of polynomials in S which are divisible by $x^2+2$ is:

(1) 10  (2) 20  (3) 6  (4) 120

**Answer: (1)** · key (compiled)

**Solution.** A cubic divisible by $x^2+2$ has the form $(x^2+2)(x+k)=x^3+kx^2+2x+2k$. Comparing: $a=k$, $b=2$, $c=2a$. We need $a\ge1$ and $c=2a\le20$, so $a\in\{1,\dots,10\}$: **10** polynomials.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q9 · MCQ

If $\alpha,\beta$, where $\alpha<\beta$, are the roots of the equation $\lambda x^2-(\lambda+3)x+3=0$ such that $\dfrac1\alpha-\dfrac1\beta=\dfrac13$, then the sum of all possible values of $\lambda$ is:

(1) 8  (2) 6  (3) 2  (4) 4

**Answer: (2)** · key (compiled)

**Solution.** The quadratic factorises as $(\lambda x-3)(x-1)=0$, so the roots are $1$ and $\dfrac3\lambda$. $\dfrac1\alpha-\dfrac1\beta=\dfrac13$ with $\alpha<\beta$ needs both roots of the same sign and $\left|1-\dfrac\lambda3\right|=\dfrac13$ (the difference of the reciprocals of the roots $1$ and $\tfrac3\lambda$), so $|\lambda-3|=1$ and $\lambda=2$ or $4$. Check: $\lambda=2$: roots $1,\tfrac32$, $1-\tfrac23=\tfrac13$ ✓; $\lambda=4$: roots $\tfrac34,1$, $\tfrac43-1=\tfrac13$ ✓. Sum $=2+4=6$.

### § — JEE Main 2026 · 24 Jan Shift 1 · Modulus set Q1 · MCQ

The number of real solutions of the equation $x|x+3|+|x-1|-2=0$ is:

(1) 2  (2) 4  (3) 3  (4) 5

**Answer: (3)** · key (compiled)

**Solution.** Break at $x=-3$ and $x=1$. For $x<-3$: $-x(x+3)+(1-x)-2=0\Rightarrow x^2+4x+1=0\Rightarrow x=-2\pm\sqrt3$; only $-2-\sqrt3\approx-3.73$ lies in the range (1 solution). For $-3\le x<1$: $x(x+3)+(1-x)-2=0\Rightarrow x^2+2x-1=0\Rightarrow x=-1\pm\sqrt2$; both $0.41$ and $-2.41$ lie in $[-3,1)$ (2 solutions). For $x\ge1$: $x^2+4x-3=0\Rightarrow x=-2\pm\sqrt7$, neither is $\ge1$. Total $=3$.

