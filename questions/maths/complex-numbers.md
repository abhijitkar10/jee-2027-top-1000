# Complex Numbers

> Theory: [../../theory/maths/complex-numbers.md](../../theory/maths/complex-numbers.md)

### M-CMP-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $z$ be the complex number satisfying $|z-5|\le3$ and having maximum positive principal argument. Then $34\left|\dfrac{5z-12}{5iz+16}\right|^2$ is equal to:

(1) 26  (2) 12  (3) 20  (4) 16

**Answer: (3)** · key (compiled)

**Solution.** $|z-5|\le3$ is the disc with centre $(5,0)$ and radius 3. The largest argument is attained at the tangent point from the origin. The tangent length is $\sqrt{25-9}=4$ and $\sin\theta=\tfrac35$, $\cos\theta=\tfrac45$, so $z=4(\cos\theta+i\sin\theta)=\dfrac{16+12i}5$. Then $5z-12=4+12i$ and $5iz+16=i(16+12i)+16=4+16i$. $34\cdot\dfrac{16+144}{16+256}=34\cdot\dfrac{160}{272}=20$.

### M-CMP-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

Let $S=\{z:3\le|2z-3(1+i)|\le7\}$ be a set of complex numbers. Then $\min_{z\in S}\left|z+\tfrac12(5+3i)\right|$ is equal to:

(1) 2  (2) $\dfrac52$  (3) $\dfrac32$  (4) $\dfrac12$

**Answer: (3)** · key (compiled)

**Solution.** $|2z-3(1+i)|=2\left|z-\tfrac32(1+i)\right|$, so $\tfrac32\le\left|z-\tfrac32(1+i)\right|\le\tfrac72$: an annulus centred at $C=\left(\tfrac32,\tfrac32\right)$. The point $P=-\tfrac12(5+3i)=\left(-\tfrac52,-\tfrac32\right)$ is at distance $CP=\sqrt{4^2+3^2}=5>\tfrac72$, i.e. outside the outer circle. The minimum distance from $P$ to the annulus is $5-\tfrac72=\tfrac32$.

### M-CMP-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let $A=\{z\in\mathbb C:|z-2|\le4\}$ and $B=\{z\in\mathbb C:|z-2|+|z+2|=5\}$. Then the maximum value of $\{|z_1-z_2|:z_1\in A,\ z_2\in B\}$ is:

(1) $\dfrac{17}2$  (2) 8  (3) 9  (4) $\dfrac{15}2$

**Answer: (1)** · key (compiled)

**Solution.** $B$ is the ellipse with foci $(\pm2,0)$ and major axis $2a=5$. $A$ is the disc of radius 4 about the focus $(2,0)$. For $z_2\in B$ the farthest point of $A$ is at distance $|z_2-2|+4$. The distance from a focus to points of the ellipse is at most $a+c=\tfrac52+2=\tfrac92$ (at the far vertex $\left(-\tfrac52,0\right)$). Maximum $=\tfrac92+4=\tfrac{17}2$.

### M-CMP-04 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · Numerical

Let $z=(1+i)(1+2i)(1+3i)\cdots(1+ni)$, where $i=\sqrt{-1}$. If $|z|^2=44200$, then $n$ is equal to ______.

**Answer: 5** · key (compiled)

**Solution.** $|z|^2=\prod_{k=1}^n|1+ki|^2=\prod_{k=1}^n(1+k^2)$. Multiply: $2\cdot5=10$, $\cdot10=100$, $\cdot17=1700$, $\cdot26=44200$. So $n=5$.

### M-CMP-05 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · MCQ

Let $S=\{z\in\mathbb C:4z^2+\bar z=0\}$. Then $\sum_{z\in S}|z|^2$ is equal to:

(1) $\dfrac5{64}$  (2) $\dfrac1{16}$  (3) $\dfrac3{16}$  (4) $\dfrac7{64}$

**Answer: (3)** · key (compiled)

**Solution.** Let $z=x+iy$. $4(x^2-y^2+2ixy)+x-iy=0$: real part $4x^2-4y^2+x=0$, imaginary part $y(8x-1)=0$. If $y=0$: $x(4x+1)=0\Rightarrow z=0$ or $z=-\tfrac14$ ($|z|^2=\tfrac1{16}$). If $x=\tfrac18$: $\tfrac1{16}+\tfrac18=4y^2\Rightarrow y^2=\tfrac3{64}$, giving $z=\tfrac18\pm i\tfrac{\sqrt3}8$ with $|z|^2=\tfrac1{64}+\tfrac3{64}=\tfrac1{16}$ each. Sum $=0+\tfrac1{16}+\tfrac1{16}+\tfrac1{16}=\tfrac3{16}$.

### M-CMP-06 · B — JEE Main 2026 · 22 Jan Shift 1 · set Q6 · Numerical

Let $\alpha=\dfrac{-1+i\sqrt3}2$ and $\beta=\dfrac{-1-i\sqrt3}2$, $i=\sqrt{-1}$. If $(7-7\alpha+9\beta)^{20}+(9+7\alpha-7\beta)^{20}+(-7+9\alpha+7\beta)^{20}+(14+7\alpha+7\beta)^{20}=m^{10}$, then $m$ is ______.

**Answer: 49** · key (compiled)

**Solution.** $\alpha=\omega$, $\beta=\omega^2$ (cube roots of unity), $\alpha+\beta=-1$. Let $T_1=7-7\omega+9\omega^2$. Then $\omega T_1=7\omega-7\omega^2+9=9+7\omega-7\omega^2=T_2$ and $\omega T_2=-7+9\omega+7\omega^2=T_3$. So $T_1^{20}+T_2^{20}+T_3^{20}=T_1^{20}(1+\omega^{20}+\omega^{40})=T_1^{20}(1+\omega^2+\omega)=0$. The last term is $(14-7)^{20}=7^{20}=(7^2)^{10}$, so $m=49$.

### M-CMP-07 · B — JEE Main 2026 · 23 Jan Shift 2 · set Q7 · MCQ

If $z=\dfrac{\sqrt3}2+\dfrac i2$, $i=\sqrt{-1}$, then $(z^{201}-i)^8$ is equal to:

(1) 1  (2) 256  (3) $-1$  (4) 0

**Answer: (2)** · key (compiled)

**Solution.** $z=e^{i\pi/6}$, so $z^{201}=e^{i\,201\pi/6}=e^{i(33.5\pi)}=e^{i(32\pi+3\pi/2)}=-i$. Then $z^{201}-i=-2i$ and $(-2i)^8=2^8\,i^8=256$.

### M-CMP-08 · B — JEE Main 2024 · 27 Jan Shift 1 · Q61 · MCQ

If $S=\{z\in\mathbb C:\ |z-i|=|z+i|=|z-1|\}$, then $n(S)$ is

(1) 1  (2) 0  (3) 3  (4) 2

**Answer: (1)** · key ✔

**Solution.** $|z-i|=|z+i|$ puts $z$ on the real axis. Then $|z-i|=|z-1|$ gives $x^2+1=(x-1)^2\Rightarrow x=0$, so $z=0$. Check: $|0-i|=|0+i|=|0-1|=1$. Exactly one point (the circumcentre of $i,-i,1$), so $n(S)=1$.

### M-CMP-09 · B — JEE Main 2024 · 27 Jan Shift 2 · Q81 · Numerical

The complex numbers $\alpha$ and $\dfrac1{\bar\alpha}$ lie on the circles $|z-z_0|^2=4$ and $|z-z_0|^2=16$ respectively, where $z_0=1+i$. Then $100|\alpha|^2$ is equal to ______.

**Answer: 20** · key ✔

**Solution.** Let $r=|\alpha|$. From $|\alpha-z_0|^2=4$: $r^2-2\,\text{Re}(\bar\alpha z_0)+2=4$. For $w=1/\bar\alpha=\alpha/r^2$: $|w-z_0|^2=\dfrac1{r^2}-\dfrac{2\,\text{Re}(\bar\alpha z_0)}{r^2}+2=16$. Let $u=2\,\text{Re}(\bar\alpha z_0)$. Then $u=r^2-2$ and $1-u=14r^2$. Substituting: $3-r^2=14r^2\Rightarrow r^2=\dfrac15$, so $100|\alpha|^2=20$.

### M-CMP-10 · C — JEE Main 2024 · 29 Jan Shift 1 · Q81 · Numerical

Let $\alpha,\beta$ be the roots of $x^2-x+2=0$ with $\text{Im}(\alpha)>\text{Im}(\beta)$. Then $\alpha^6+\alpha^4+\beta^4-5\alpha^2$ is equal to ______.

**Answer: 13** · key ✔

**Solution.** Each root satisfies $t^2=t-2$. So $t^4=(t-2)^2=t^2-4t+4=-3t+2$ and $t^6=t^2\cdot t^4=(t-2)(-3t+2)=-3t^2+8t-4=-3(t-2)+8t-4=5t+2$. Then $\alpha^6+\alpha^4+\beta^4-5\alpha^2=(5\alpha+2)+(-3\alpha+2)+(-3\beta+2)-5(\alpha-2)=-3(\alpha+\beta)+16=-3+16=13$.

### M-CMP-11 · C — JEE Main 2024 · 29 Jan Shift 2 · Q82 · Numerical

Let $\alpha,\beta$ be the roots of $x^2-\sqrt6x+3=0$ with $\text{Im}(\alpha)>\text{Im}(\beta)$. Let $a,b$ be integers not divisible by $3$ and $n$ a natural number such that $\dfrac{\alpha^{99}}\beta+\alpha^{98}=3^n(a+ib)$, $i=\sqrt{-1}$. Then $n+a+b$ is equal to ______.

**Answer: 49** · key ✔

**Solution.** $x=\dfrac{\sqrt6\pm i\sqrt6}2$, so $\alpha=\sqrt3e^{i\pi/4}$ and $\beta=\bar\alpha$. Then $\dfrac1\beta=\dfrac1{\bar\alpha}=\dfrac\alpha{|\alpha|^2}=\dfrac\alpha3$, so $\dfrac{\alpha^{99}}\beta=\dfrac{\alpha^{100}}3$. The expression $=\alpha^{98}\left(\dfrac{\alpha^2}3+1\right)$, and $\alpha^2=3i$, so it equals $\alpha^{98}(1+i)$. $\alpha^{98}=3^{49}e^{i\,49\pi/2}=3^{49}e^{i\pi/2}=3^{49}i$ (since $49\pi/2=24\pi+\pi/2$). Hence $3^{49}\,i(1+i)=3^{49}(-1+i)$: $n=49,\ a=-1,\ b=1$ and $n+a+b=49$.

