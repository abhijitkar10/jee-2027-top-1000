# Indefinite Integration

> Theory: [../../theory/maths/indefinite-integration.md](../../theory/maths/indefinite-integration.md)

### M-INT-01 · C — JEE Main 2026 · 23 Jan Shift 1 · Indefinite set Q1 · MCQ

Let $f(x)=\int\dfrac{(2-x^2)\cdot e^x}{(\sqrt{1+x})(1-x)^{3/2}}dx$. If $f(0)=0$, then $f\left(\dfrac12\right)$ is equal to:

(1) $\sqrt{3e}-1$  (2) $\sqrt{3e}+1$  (3) $\sqrt{2e}+1$  (4) $\sqrt{2e}-1$

**Answer: (1)** · key (compiled)

**Solution.** Write $2-x^2=(1-x)(1+x)+1$, so the integrand is $e^x\left[\sqrt{\dfrac{1+x}{1-x}}+\dfrac1{\sqrt{1+x}\,(1-x)^{3/2}}\right]$. With $g=\sqrt{\dfrac{1+x}{1-x}}$, $g'=\dfrac1{\sqrt{1+x}\,(1-x)^{3/2}}$, so the integrand is $e^x(g+g')$ and $f(x)=e^xg+C=e^x\sqrt{\dfrac{1+x}{1-x}}+C$. $f(0)=1+C=0\Rightarrow C=-1$. $f\left(\tfrac12\right)=e^{1/2}\sqrt3-1=\sqrt{3e}-1$.

### M-INT-02 · C — JEE Main 2026 · 28 Jan Shift 2 · Indefinite set Q2 · MCQ

Let $f(x)=\int\dfrac{dx}{x^{2/3}+2x^{1/2}}$ be such that $f(0)=-26+24\log_e2$. If $f(1)=a+b\log_e3$, where $a,b\in\mathbb Z$, then $a+b$ is equal to:

(1) $-26$  (2) $-11$  (3) $-5$  (4) $-18$

**Answer: (2)** · key (compiled)

**Solution.** Put $u=x^{1/6}$, $dx=6u^5du$: $\int\dfrac{6u^5}{u^4+2u^3}du=\int\dfrac{6u^2}{u+2}du=6\int\left(u-2+\dfrac4{u+2}\right)du=3u^2-12u+24\ln(u+2)+C$. At $x=0$ ($u=0$): $24\ln2+C=-26+24\ln2\Rightarrow C=-26$. At $x=1$ ($u=1$): $3-12+24\ln3-26=-35+24\ln3$. So $a=-35$, $b=24$ and $a+b=-11$.

### M-INT-03 · C — JEE Main 2026 · 22 Jan Shift 1 · Indefinite set Q3 · Numerical

If $\int(\sin x)^{-11/2}(\cos x)^{-5/2}dx=-\dfrac{p_1}{q_1}(\cot x)^{9/2}-\dfrac{p_2}{q_2}(\cot x)^{5/2}-\dfrac{p_3}{q_3}(\cot x)^{1/2}+\dfrac{p_4}{q_4}(\cot x)^{-3/2}+C$, where $p_i$ and $q_i$ are positive integers with $\gcd(p_i,q_i)=1$ for $i=1,2,3,4$ and $C$ is the constant of integration, then $\dfrac{15p_1p_2p_3p_4}{q_1q_2q_3q_4}$ is equal to ______.

**Answer: 16** · key (compiled)

**Solution.** $(\sin x)^{-11/2}(\cos x)^{-5/2}=(\cot x)^{-5/2}\csc^8x$ and $\csc^8x\,dx=(1+\cot^2x)^3\csc^2x\,dx$. With $t=\cot x$, $dt=-\csc^2x\,dx$: $-\int t^{-5/2}(1+t^2)^3dt=-\int\left(t^{-5/2}+3t^{-1/2}+3t^{3/2}+t^{7/2}\right)dt=\tfrac23t^{-3/2}-6t^{1/2}-\tfrac65t^{5/2}-\tfrac29t^{9/2}$. So $\dfrac{p_1}{q_1}=\tfrac29$, $\dfrac{p_2}{q_2}=\tfrac65$, $\dfrac{p_3}{q_3}=\tfrac61$, $\dfrac{p_4}{q_4}=\tfrac23$. The product is $\dfrac{2\cdot6\cdot6\cdot2}{9\cdot5\cdot1\cdot3}=\dfrac{144}{135}=\dfrac{16}{15}$, and $15\times\dfrac{16}{15}=16$.

### M-INT-04 · C — JEE Main 2026 · 23 Jan Shift 2 · Indefinite set Q4 · MCQ

Let $I(x)=\int\dfrac{3\,dx}{(4x+6)\left(\sqrt{4x^2+8x+3}\right)}$ and $I(0)=\dfrac{\sqrt3}4+20$. If $I\left(\dfrac12\right)=\dfrac{a\sqrt2}b+c$, where $a,b,c\in\mathbb N$, $\gcd(a,b)=1$, then $a+b+c$ is equal to:

(1) 30  (2) 31  (3) 29  (4) 28

**Answer: (2)** · key (compiled)

**Solution.** $4x^2+8x+3=(2x+1)(2x+3)$ and $4x+6=2(2x+3)$, so the integrand is $\dfrac32(2x+3)^{-3/2}(2x+1)^{-1/2}$. Let $t=\sqrt{\dfrac{2x+1}{2x+3}}$: $t^2=1-\dfrac2{2x+3}\Rightarrow t\,dt=\dfrac{2\,dx}{(2x+3)^2}$. The integrand becomes $\dfrac32\cdot\dfrac1t\cdot\dfrac{dx}{(2x+3)^2}=\dfrac34dt$, so $I(x)=\dfrac34\sqrt{\dfrac{2x+1}{2x+3}}+C$. $I(0)=\dfrac{3}{4\sqrt3}+C=\dfrac{\sqrt3}4+C\Rightarrow C=20$. $I\left(\tfrac12\right)=\dfrac34\sqrt{\tfrac24}+20=\dfrac{3\sqrt2}8+20$. So $a=3$, $b=8$, $c=20$ and $a+b+c=31$.

### M-INT-05 · C — JEE Main 2024 · 27 Jan Shift 2 · Q74 · MCQ

$\displaystyle\int\frac{x^8-x^2}{\left(x^{12}+3x^6+1\right)\tan^{-1}\!\left(x^3+\dfrac1{x^3}\right)}\,dx$ is equal to

(1) $\ln\left|\tan^{-1}\!\left(x^3+\tfrac1{x^3}\right)\right|^{1/3}+C$  (2) $\ln\left|\tan^{-1}(\cdot)\right|^{1/2}+C$  (3) $\ln\left|\tan^{-1}(\cdot)\right|+C$  (4) $\ln\left|\tan^{-1}(\cdot)\right|^{3}+C$

**Answer: (1)** · key ✔

**Solution.** Let $t=x^3+x^{-3}$, so $dt=3\left(x^2-x^{-4}\right)dx=\dfrac{3(x^6-1)}{x^4}dx$. Also $x^{12}+3x^6+1=x^6(t^2+1)$ since $t^2=x^6+2+x^{-6}$. The integrand becomes $\dfrac{x^2(x^6-1)}{x^6(t^2+1)\tan^{-1}t}dx=\dfrac{dt}{3(1+t^2)\tan^{-1}t}$. Integrating: $\tfrac13\ln|\tan^{-1}t|+C$.

