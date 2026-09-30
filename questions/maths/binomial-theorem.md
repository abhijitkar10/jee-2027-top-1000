# Binomial Theorem

> Theory: [../../theory/maths/binomial-theorem.md](../../theory/maths/binomial-theorem.md)

### M-BIN-01 — JEE Main 2024 · 27 Jan Shift 1 · Q63 · MCQ

Let $A$ denote the sum of all coefficients in the expansion of $(1-3x+10x^2)^n$ and $B$ the sum of all coefficients in the expansion of $(1+x^2)^n$. Then

(1) $A=B^3$  (2) $3A=B$  (3) $B=A^3$  (4) $A=3B$

**Answer: (1)** · key ✔

**Solution.** Sum of coefficients means $x=1$: $A=(1-3+10)^n=8^n$ and $B=2^n$. Hence $A=(2^n)^3=B^3$.

### M-BIN-02 — JEE Main 2024 · 27 Jan Shift 2 · Q82 · Numerical

The coefficient of $x^{2012}$ in the expansion of $(1-x)^{2008}(1+x+x^2)^{2007}$ is equal to ______.

**Answer: 0** · key ✔

**Solution.** $(1-x)(1+x+x^2)=1-x^3$, so the product is $(1-x)\,(1-x^3)^{2007}$. Terms of $(1-x^3)^{2007}$ have exponents divisible by $3$, so the product has exponents $\equiv0$ or $1\pmod3$. $2012\equiv2\pmod3$, so the coefficient is $0$.

### M-BIN-03 — JEE Main 2024 · 29 Jan Shift 1 · Q83 · Numerical

If $\dfrac{{}^{11}C_1}2+\dfrac{{}^{11}C_2}3+\cdots+\dfrac{{}^{11}C_9}{10}=\dfrac nm$ with $\gcd(n,m)=1$, then $n+m$ is equal to ______.

**Answer: 2041** · key ✔

**Solution.** $\dfrac{{}^{11}C_r}{r+1}=\dfrac{{}^{12}C_{r+1}}{12}$. So the sum is $\dfrac1{12}\sum_{k=2}^{10}{}^{12}C_k=\dfrac1{12}\left(2^{12}-1-12-12-1\right)=\dfrac{4070}{12}=\dfrac{2035}6$. With $\gcd(2035,6)=1$: $n+m=2041$.

### M-BIN-04 — JEE Main 2024 · 29 Jan Shift 2 · Q83 · Numerical

The remainder when $64^{32^{32}}$ is divided by $9$ is equal to ______.

**Answer: 1** · key ✔

**Solution.** $64=63+1\equiv1\pmod9$ (as $63=7\cdot9$), so every positive integer power of $64$ leaves remainder $1$. Equivalently, $64^N=(63+1)^N$ and every term but the last is divisible by $9$.

### M-BIN-05 — JEE Main 2024 · 30 Jan Shift 1 · Q83 · Numerical

The number of integral terms in the expansion of $\left\{7^{1/2}+11^{1/6}\right\}^{824}$ is equal to ______.

**Answer: 138** · key ✔

**Solution.** $T_{r+1}={}^{824}C_r\,7^{(824-r)/2}\,11^{r/6}$. This is an integer when $6\mid r$ (for $11^{r/6}$) and $(824-r)$ is even (for the power of 7). As $824$ is even, $r$ must be even, which multiples of $6$ already satisfy. So $r=0,6,12,\dots,822$: $\dfrac{822}6+1=138$ terms.

### M-BIN-06 — JEE Main 2024 · 30 Jan Shift 2 · Q63 · MCQ

Suppose $28-p,\ p,\ 70-\alpha,\ \alpha$ are the coefficients of four consecutive terms in the expansion of $(1+x)^n$. Then $2\alpha-3p$ equals

(1) 7  (2) 10  (3) 4  (4) 6

**Answer: (1)** · key ✔

**Solution.** Let the coefficients be ${}^nC_{r-1},{}^nC_r,{}^nC_{r+1},{}^nC_{r+2}$. Adding the first two: ${}^{n+1}C_r=28$; adding the last two: ${}^{n+1}C_{r+2}=70$. Since ${}^8C_2=28$ and ${}^8C_4=70$: $n+1=8,\ r=2$, so $n=7$. Then $28-p={}^7C_1=7\Rightarrow p=21$ and $\alpha={}^7C_4=35$. So $2\alpha-3p=70-63=7$.

### M-BIN-07 — JEE Main 2024 · 31 Jan Shift 2 · Q82 · Numerical

Let the coefficient of $x^r$ in the expansion of $(x+3)^{n-1}+(x+3)^{n-2}(x+2)+(x+3)^{n-3}(x+2)^2+\cdots+(x+2)^{n-1}$ be $\alpha_r$. If $\displaystyle\sum_{r=0}^n\alpha_r=\beta^n-\gamma^n$, $\beta,\gamma\in\mathbb N$, then $\beta^2+\gamma^2$ equals ______.

**Answer: 25** · key ✔

**Solution.** $\sum\alpha_r$ is the sum of coefficients, i.e. the value at $x=1$: $4^{n-1}+4^{n-2}3+\dots+3^{n-1}$, a geometric series with ratio $\tfrac34$, equal to $\dfrac{4^n-3^n}{4-3}=4^n-3^n$. So $\beta=4,\ \gamma=3$ and $\beta^2+\gamma^2=25$.

### M-BIN-08 — JEE Main 2024 · 1 Feb Shift 2 · Q64 · MCQ

Let $m$ and $n$ be the coefficients of the seventh and thirteenth terms respectively in the expansion of $\left(\tfrac13x^{1/3}+\tfrac1{2x^{2/3}}\right)^{18}$. Then $\left(\dfrac nm\right)^{1/3}$ is:

(1) $\dfrac49$  (2) $\dfrac19$  (3) $\dfrac14$  (4) $\dfrac94$

**Answer: (4)** · key ✔

**Solution.** $m=T_7$ coefficient $=\binom{18}{6}\left(\tfrac13\right)^{12}\left(\tfrac12\right)^6$, $n=T_{13}$ coefficient $=\binom{18}{12}\left(\tfrac13\right)^{6}\left(\tfrac12\right)^{12}$. Since $\binom{18}{6}=\binom{18}{12}$: $\dfrac nm=3^6/2^6=\left(\tfrac32\right)^6$, so $\left(\tfrac nm\right)^{1/3}=\left(\tfrac32\right)^2=\dfrac94$.

