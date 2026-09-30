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

