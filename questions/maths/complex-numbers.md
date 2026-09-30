# Complex Numbers

> Theory: [../../theory/maths/complex-numbers.md](../../theory/maths/complex-numbers.md)

### M-CMP-01 — JEE Main 2024 · 27 Jan Shift 1 · Q61 · MCQ

If $S=\{z\in\mathbb C:\ |z-i|=|z+i|=|z-1|\}$, then $n(S)$ is

(1) 1  (2) 0  (3) 3  (4) 2

**Answer: (1)** · key ✔

**Solution.** $|z-i|=|z+i|$ puts $z$ on the real axis. Then $|z-i|=|z-1|$ gives $x^2+1=(x-1)^2\Rightarrow x=0$, so $z=0$. Check: $|0-i|=|0+i|=|0-1|=1$. Exactly one point (the circumcentre of $i,-i,1$), so $n(S)=1$.

### M-CMP-02 — JEE Main 2024 · 27 Jan Shift 1 · Q81 · Numerical

If $\alpha$ satisfies $x^2+x+1=0$ and $(1+\alpha)^7=A+B\alpha+C\alpha^2$ with $A,B,C\ge0$, then $5(3A-2B-C)$ is equal to ______.

**Answer: 5** · key ✔

**Solution.** $1+\alpha=-\alpha^2$ so $(1+\alpha)^7=-\alpha^{14}=-\alpha^{2}$ (as $\alpha^3=1$). Using $-\alpha^2=1+\alpha$: $(A,B,C)=(1,1,0)$. Any other non-negative triple differs by $k(1+\alpha+\alpha^2)=0$, and $3A-2B-C$ is unchanged. Hence $3-2-0=1$ and $5\cdot1=5$.

### M-CMP-03 — JEE Main 2024 · 27 Jan Shift 2 · Q81 · Numerical

The complex numbers $\alpha$ and $\dfrac1{\bar\alpha}$ lie on the circles $|z-z_0|^2=4$ and $|z-z_0|^2=16$ respectively, where $z_0=1+i$. Then $100|\alpha|^2$ is equal to ______.

**Answer: 20** · key ✔

**Solution.** Let $r=|\alpha|$. From $|\alpha-z_0|^2=4$: $r^2-2\,\text{Re}(\bar\alpha z_0)+2=4$. For $w=1/\bar\alpha=\alpha/r^2$: $|w-z_0|^2=\dfrac1{r^2}-\dfrac{2\,\text{Re}(\bar\alpha z_0)}{r^2}+2=16$. Let $u=2\,\text{Re}(\bar\alpha z_0)$. Then $u=r^2-2$ and $1-u=14r^2$. Substituting: $3-r^2=14r^2\Rightarrow r^2=\dfrac15$, so $100|\alpha|^2=20$.

### M-CMP-04 — JEE Main 2024 · 29 Jan Shift 1 · Q81 · Numerical

Let $\alpha,\beta$ be the roots of $x^2-x+2=0$ with $\text{Im}(\alpha)>\text{Im}(\beta)$. Then $\alpha^6+\alpha^4+\beta^4-5\alpha^2$ is equal to ______.

**Answer: 13** · key ✔

**Solution.** Each root satisfies $t^2=t-2$. So $t^4=(t-2)^2=t^2-4t+4=-3t+2$ and $t^6=t^2\cdot t^4=(t-2)(-3t+2)=-3t^2+8t-4=-3(t-2)+8t-4=5t+2$. Then $\alpha^6+\alpha^4+\beta^4-5\alpha^2=(5\alpha+2)+(-3\alpha+2)+(-3\beta+2)-5(\alpha-2)=-3(\alpha+\beta)+16=-3+16=13$.

### M-CMP-05 — JEE Main 2024 · 29 Jan Shift 2 · Q82 · Numerical

Let $\alpha,\beta$ be the roots of $x^2-\sqrt6x+3=0$ with $\text{Im}(\alpha)>\text{Im}(\beta)$. Let $a,b$ be integers not divisible by $3$ and $n$ a natural number such that $\dfrac{\alpha^{99}}\beta+\alpha^{98}=3^n(a+ib)$, $i=\sqrt{-1}$. Then $n+a+b$ is equal to ______.

**Answer: 49** · key ✔

**Solution.** $x=\dfrac{\sqrt6\pm i\sqrt6}2$, so $\alpha=\sqrt3e^{i\pi/4}$ and $\beta=\bar\alpha$. Then $\dfrac1\beta=\dfrac1{\bar\alpha}=\dfrac\alpha{|\alpha|^2}=\dfrac\alpha3$, so $\dfrac{\alpha^{99}}\beta=\dfrac{\alpha^{100}}3$. The expression $=\alpha^{98}\left(\dfrac{\alpha^2}3+1\right)$, and $\alpha^2=3i$, so it equals $\alpha^{98}(1+i)$. $\alpha^{98}=3^{49}e^{i\,49\pi/2}=3^{49}e^{i\pi/2}=3^{49}i$ (since $49\pi/2=24\pi+\pi/2$). Hence $3^{49}\,i(1+i)=3^{49}(-1+i)$: $n=49,\ a=-1,\ b=1$ and $n+a+b=49$.

