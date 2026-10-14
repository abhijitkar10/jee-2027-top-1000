# Differentiation & Application of Derivatives

> Theory: [../../theory/maths/application-of-derivatives.md](../../theory/maths/application-of-derivatives.md)

### M-AOD-01 · A — JEE Main 2026 · 21 Jan Shift 2 · Differentiation set Q1 · MCQ

Let $f(x)=x^3+x^2f'(1)+2xf''(2)+f'''(3)$, $x\in\mathbb R$. Then the value of $f'(5)$ is:

(1) $\dfrac{117}5$  (2) $\dfrac{657}5$  (3) $\dfrac25$  (4) $\dfrac{62}5$

**Answer: (1)** · key (compiled)

**Solution.** Let $a=f'(1)$, $b=f''(2)$, $c=f'''(3)$, so $f(x)=x^3+ax^2+2bx+c$, $f'=3x^2+2ax+2b$, $f''=6x+2a$, $f'''=6$. Then $a=f'(1)=3+2a+2b\Rightarrow a=-3-2b$; $b=f''(2)=12+2a$. Substituting: $b=12-6-4b\Rightarrow b=\tfrac65$ and $a=-\tfrac{27}5$. $f'(5)=75+10a+2b=75-54+\tfrac{12}5=\dfrac{117}5$.

### M-AOD-02 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q2 · Numerical

Let $f$ be a differentiable function satisfying $f(x)=1-2x+\int_0^xe^{(x-t)}f(t)\,dt$, $x\in\mathbb R$ and let $g(x)=\int_0^x(f(t)+2)^{15}(t-4)^6(t+12)^{17}dt$, $x\in\mathbb R$. If $p$ and $q$ are respectively the points of local minima and local maxima of $g$, then the value of $|p+q|$ is equal to ______.

**Answer: 9** · key (compiled)

**Solution.** Write $f(x)=1-2x+e^x\int_0^xe^{-t}f(t)dt$ and differentiate: $f'(x)=-2+\left(f(x)-1+2x\right)+f(x)$, i.e. $f'-2f=2x-3$. Trying $f=1-x$ satisfies it, and $f(0)=1$ fixes the constant (the homogeneous part $Ce^{2x}$ has $C=0$). So $f(x)=1-x$ and $f(t)+2=3-t$. $g'(x)=(3-x)^{15}(x-4)^6(x+12)^{17}$. The factors $(x-4)^6$ (even power) do not change sign. $g'<0$ for $x<-12$, $>0$ on $(-12,3)$, $<0$ for $x>3$: local minimum at $p=-12$, local maximum at $q=3$. $|p+q|=9$.

### M-AOD-03 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q3 · MCQ

Consider the following three statements for the function $f:(0,\infty)\to\mathbb R$ defined by $f(x)=|\log_ex|-|x-1|$: (I) $f$ is differentiable at all $x>0$. (II) $f$ is increasing in $(0,1)$. (III) $f$ is decreasing in $(1,\infty)$. Then:

(1) All (I), (II) and (III) are TRUE.  (2) Only (II) and (III) are TRUE.  (3) Only (I) is TRUE.  (4) Only (I) and (III) are TRUE.

**Answer: (4)** · key (compiled)

**Solution.** For $0<x<1$: $f=-\ln x-(1-x)$, $f'=-\dfrac1x+1<0$. For $x>1$: $f=\ln x-(x-1)$, $f'=\dfrac1x-1<0$. At $x=1$ both one-sided derivatives are $0$, so the kinks of $|\ln x|$ and $|x-1|$ cancel: $f$ is differentiable at 1 (I true). On $(0,1)$ $f$ is *decreasing*, so (II) is false; on $(1,\infty)$ it is decreasing, so (III) is true.

### M-AOD-04 · A — JEE Main 2026 · 22 Jan Shift 1 · set Q4 · MCQ

Let $f(x)=x^{2025}-x^{2000}$, $x\in[0,1]$ and the minimum value of the function $f(x)$ in the interval $[0,1]$ be $(80)^{80}(n)^{-81}$. Then $n$ is equal to:

(1) $-40$  (2) $-41$  (3) $-80$  (4) $-81$

**Answer: (4)** · key (compiled)

**Solution.** $f'(x)=2025x^{2024}-2000x^{1999}=x^{1999}\left(2025x^{25}-2000\right)=0\Rightarrow x^{25}=\dfrac{80}{81}$ (the minimum, as $f(0)=f(1)=0$). With $s=x^{25}$: $f=x^{2000}(x^{25}-1)=s^{80}(s-1)=\left(\tfrac{80}{81}\right)^{80}\left(-\tfrac1{81}\right)=-\dfrac{80^{80}}{81^{81}}$. Matching $(80)^{80}n^{-81}$: $n^{-81}=-81^{-81}$, so $n=-81$.

### M-AOD-05 · B — JEE Main 2026 · 21 Jan Shift 1 · set Q5 · Numerical

Let $f:\mathbb R\to\mathbb R$ be a twice differentiable function such that the quadratic equation $f(x)m^2-2f'(x)m+f''(x)=0$ in $m$ has two equal roots for every $x\in\mathbb R$. If $f(0)=1$, $f'(0)=2$, and $(\alpha,\beta)$ is the largest interval in which the function $f(\log_ex-x)$ is increasing, then $\alpha+\beta$ is equal to ______.

**Answer: 1** · key (compiled)

**Solution.** Equal roots: $4f'^2-4ff''=0\Rightarrow\dfrac{f''}{f'}=\dfrac{f'}f\Rightarrow f'=kf$ and $f=Ae^{kx}$. $f(0)=1$ gives $A=1$ and $f'(0)=2$ gives $k=2$, so $f(x)=e^{2x}$. Then $f(\ln x-x)=e^{2\ln x-2x}=x^2e^{-2x}$ (for $x>0$), with derivative $2xe^{-2x}(1-x)$. It is positive for $0<x<1$: the largest interval of increase is $(0,1)$, so $\alpha+\beta=1$.

### M-AOD-06 · B — JEE Main 2024 · 27 Jan Shift 1 · Q85 · Numerical

Let $f(x)=x^3+x^2f'(1)+xf''(2)+f'''(3)$, $x\in\mathbb R$. Then $f'(10)$ is equal to ______.

**Answer: 202** · key ✔

**Solution.** Differentiating: $f'(x)=3x^2+2xf'(1)+f''(2)$, $f''(x)=6x+2f'(1)$, $f'''=6$. So $f''(2)=12+2f'(1)$. Putting $x=1$ in $f'$: $f'(1)=3+2f'(1)+12+2f'(1)\Rightarrow f'(1)=-5$, so $f''(2)=2$. Then $f'(10)=300+20(-5)+2=202$.

### M-AOD-07 · B — JEE Main 2024 · 29 Jan Shift 2 · Q72 · MCQ

Let $y=\ln\!\left(\dfrac{1-x^2}{1+x^2}\right)$, $-1<x<1$. Then at $x=\dfrac12$, the value of $225\,(y'-y'')$ is equal to

(1) 732  (2) 746  (3) 742  (4) 736

**Answer: (4)** · key ✔

**Solution.** $y=\ln(1-x^2)-\ln(1+x^2)$, so $y'=-\dfrac{2x}{1-x^2}-\dfrac{2x}{1+x^2}$ and $y''=-\dfrac2{1-x^2}-\dfrac{4x^2}{(1-x^2)^2}-\dfrac2{1+x^2}+\dfrac{4x^2}{(1+x^2)^2}$. At $x=\tfrac12$ ($1-x^2=\tfrac34,\ 1+x^2=\tfrac54$): $y'=-\tfrac43-\tfrac45=-\tfrac{32}{15}$ and $y''=-\tfrac83-\tfrac{16}9-\tfrac85+\tfrac{16}{25}=-\tfrac{1216}{225}$. So $225(y'-y'')=-480+1216=736$.

### M-AOD-08 · C — JEE Main 2024 · 4 Apr Shift 1 · Q72 · MCQ

The sum of the maximum and minimum values of $f(x)=\dfrac{2x^2-3x+8}{2x^2+3x+8}$ is $\dfrac mn$, $\gcd(m,n)=1$. Then $m+n$ is:

(1) 195  (2) 201  (3) 217  (4) 182

**Answer: (2)** · key ✔

**Solution.** Put $y=f(x)$: $(2y-2)x^2+(3y+3)x+(8y-8)=0$ must have a real root: $9(y+1)^2-4(2y-2)(8y-8)\ge0\Rightarrow9(y+1)^2\ge64(y-1)^2\Rightarrow3|y+1|\ge8|y-1|$. This gives $y\in\left[\tfrac5{11},\tfrac{11}5\right]$. Sum $=\tfrac5{11}+\tfrac{11}5=\tfrac{146}{55}$, so $m+n=201$.

