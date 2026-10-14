# Quadratic Equations & Inequalities

> Theory: [../../theory/maths/quadratic-equations.md](../../theory/maths/quadratic-equations.md)

### M-QDR-01 · C — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $\alpha$ and $\beta$ be the roots of the equation $x^2+2ax+(3a+10)=0$ such that $\alpha<1<\beta$. Then the set of all possible values of $a$ is:

(1) $\left(-\infty,-\tfrac{11}{5}\right)$  (2) $(-\infty,-2)\cup(5,\infty)$  (3) $(-\infty,-3)$  (4) $\left(-\infty,-\tfrac{11}{5}\right)\cup(5,\infty)$

**Answer: (1)** · key (compiled)

**Solution.** Let $f(x)=x^2+2ax+3a+10$ (upward parabola). $\alpha<1<\beta$ means 1 lies strictly between the roots, which happens iff $f(1)<0$ (this also forces two real roots). $f(1)=1+2a+3a+10=5a+11<0\Rightarrow a<-\tfrac{11}{5}$.

### M-QDR-02 · C — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

A building construction work can be completed by two masons A and B together in 22.5 days. Mason A alone can complete the construction work in 24 days less than mason B alone. Then mason A alone will complete the construction work in:

(1) 30 days  (2) 36 days  (3) 24 days  (4) 42 days

**Answer: (2)** · key (compiled)

**Solution.** Let A take $a$ days and B take $a+24$ days. $\dfrac1a+\dfrac1{a+24}=\dfrac1{22.5}=\dfrac2{45}\Rightarrow45(2a+24)=2a(a+24)\Rightarrow a^2-21a-540=0\Rightarrow(a-36)(a+15)=0$. Since $a>0$, $a=36$ days.

### M-QDR-03 · C — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · MCQ

The smallest positive integral value of $a$ for which all the roots of $ax^4-ax^2+9=0$ are real and distinct is equal to:

(1) 4  (2) 9  (3) 3  (4) 7

**Answer: (4)** · key (compiled)

**Solution.** Put $t=x^2$: $t^2-at+9=0$. All four roots of the quartic are real and distinct iff this quadratic has two distinct *positive* roots: discriminant $a^2-36>0$, product $=9>0$, sum $=a>0$. So $a>6$ and the smallest positive integer is $a=7$.

### M-QDR-04 · C — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · MCQ

Let $\alpha,\beta$ be the roots of the quadratic equation $12x^2-20x+3\lambda=0$, $\lambda\in\mathbb Z$. If $\dfrac12\le|\beta-\alpha|\le\dfrac32$, then the sum of all possible values of $\lambda$ is:

(1) 1  (2) 6  (3) 3  (4) 4

**Answer: (3)** · key (compiled)

**Solution.** $\alpha+\beta=\dfrac53$, $\alpha\beta=\dfrac\lambda4$, so $|\beta-\alpha|=\sqrt{\dfrac{25}9-\lambda}=\dfrac{\sqrt{25-9\lambda}}3$. The condition gives $\dfrac32\le\sqrt{25-9\lambda}\le\dfrac92$, i.e. $\dfrac94\le25-9\lambda\le\dfrac{81}4$, so $\dfrac{19}{36}\le\lambda\le\dfrac{91}{36}$ ($0.53\le\lambda\le2.53$). Integers: $\lambda=1,2$, sum $=3$.

### M-QDR-05 · C — JEE Main 2026 · 23 Jan Shift 2 · set Q6 · MCQ

The sum of all the real solutions of the equation $\log_{(x+3)}(6x^2+28x+30)=5-2\log_{(6x+10)}(x^2+6x+9)$ is equal to:

(1) 2  (2) 1  (3) 0  (4) 4

**Answer: (3)** · key (compiled)

**Solution.** $6x^2+28x+30=2(3x+5)(x+3)$, $6x+10=2(3x+5)$, $x^2+6x+9=(x+3)^2$. Let $a=\log_{(x+3)}\big(2(3x+5)\big)$. LHS $=a+1$ and $\log_{2(3x+5)}(x+3)^2=\dfrac2a$. So $a+1=5-\dfrac4a\Rightarrow a^2-4a+4=0\Rightarrow a=2$, i.e. $(x+3)^2=6x+10\Rightarrow x^2=1\Rightarrow x=\pm1$. Both satisfy the domain conditions (bases $4$ and $2$, positive and $\ne1$; $6x+10>0$ and $\ne1$). Sum $=0$.

### M-QDR-06 · C — JEE Main 2026 · 28 Jan Shift 1 · set Q8 · MCQ

Let $S=\{x^3+ax^2+bx+c:\ a,b,c\in\mathbb N,\ a,b,c\le20\}$ be a set of polynomials. Then the number of polynomials in S which are divisible by $x^2+2$ is:

(1) 10  (2) 20  (3) 6  (4) 120

**Answer: (1)** · key (compiled)

**Solution.** A cubic divisible by $x^2+2$ has the form $(x^2+2)(x+k)=x^3+kx^2+2x+2k$. Comparing: $a=k$, $b=2$, $c=2a$. We need $a\ge1$ and $c=2a\le20$, so $a\in\{1,\dots,10\}$: **10** polynomials.

### M-QDR-07 · C — JEE Advanced 2025 · Paper 1 · Q1 · MCQ

Let $a_i,b_i\in\mathbb R$ for $i\in\{1,2,3\}$ and define $f(x)=a_1+10x+a_2x^2+a_3x^3+x^4$, $g(x)=b_1+3x+b_2x^2+b_3x^3+x^4$, $h(x)=f(x+1)-g(x+2)$. If $f(x)\ne g(x)$ for every $x\in\mathbb R$, then the coefficient of $x^3$ in $h(x)$ is

(A) 8  (B) 2  (C) $-4$  (D) $-6$

**Answer: (C)** · official key ✔ (re-derived)

**Solution.** $f-g=(a_1-b_1)+7x+(a_2-b_2)x^2+(a_3-b_3)x^3$ has degree at most $3$. An odd-degree real polynomial always has a real root, and the $x^4$ terms have cancelled, so for $f-g$ to have no real root the cubic term must vanish: $a_3=b_3$ (the remaining quadratic can have negative discriminant). In $h(x)=f(x+1)-g(x+2)$ the $x^3$ coefficient is $[4+a_3]-[8+b_3]=4-8+(a_3-b_3)=-4$, since $(x+1)^4$ contributes $4x^3$ and $(x+2)^4$ contributes $8x^3$.

### M-QDR-08 · C — JEE Main 2024 · 30 Jan Shift 1 · Q81 · Numerical

Let $\alpha,\beta\in\mathbb N$ be roots of $x^2-70x+\lambda=0$, where $\dfrac\lambda2,\dfrac\lambda3\notin\mathbb N$. If $\lambda$ assumes the minimum possible value, then $\dfrac{\left(\sqrt{\alpha-1}+\sqrt{\beta-1}\right)(\lambda+35)}{|\alpha-\beta|}$ is equal to ______.

**Answer: 60** · key ✔

**Solution.** $\alpha+\beta=70$ and $\lambda=\alpha\beta$. $\lambda$ is smaller when $\alpha,\beta$ are far apart, so test in order: $(1,69)$: $\lambda=69$, divisible by $3$; $(2,68)$: $136$, even; $(3,67)$: $201$, divisible by $3$; $(4,66)$: $264$, even; $(5,65)$: $\lambda=325$, not divisible by $2$ or $3$. So $\lambda=325$. Then $\dfrac{(2+8)(360)}{60}=60$.

### M-QDR-09 · C — JEE Main 2024 · 30 Jan Shift 2 · Q81 · Numerical

The number of real solutions of the equation $x\left(x^2+3|x|+5|x-1|+6|x-2|\right)=0$ is ______.

**Answer: 1** · key ✔

**Solution.** Either $x=0$ or $x^2+3|x|+5|x-1|+6|x-2|=0$. The second expression is a sum of non-negative terms and vanishes only if $x=0$, $x=1$ and $x=2$ simultaneously, which is impossible. So the only real solution is $x=0$.

### M-QDR-10 · C — JEE Main 2024 · 31 Jan Shift 1 · Q61 · MCQ

Let $S$ be the set of positive integral values of $a$ for which $\dfrac{ax^2+(2a+1)x+9a+4}{x^2-8x+32}<0$ for all $x\in\mathbb R$. Then the number of elements in $S$ is

(1) 1  (2) 0  (3) $\infty$  (4) 3

**Answer: (2)** · key ✔

**Solution.** The denominator $x^2-8x+32=(x-4)^2+16>0$, so we need $ax^2+(2a+1)x+9a+4<0$ for all $x$: $a<0$ and discriminant $<0$. But $a$ is a positive integer, so the first condition already fails. $S$ is empty and $n(S)=0$.

