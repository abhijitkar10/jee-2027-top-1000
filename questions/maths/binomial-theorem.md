# Binomial Theorem

> Theory: [../../theory/maths/binomial-theorem.md](../../theory/maths/binomial-theorem.md)

### M-BIN-01 — JEE Main 2024 · 27 Jan Shift 2 · Q82 · Numerical

The coefficient of $x^{2012}$ in the expansion of $(1-x)^{2008}(1+x+x^2)^{2007}$ is equal to ______.

**Answer: 0** · key ✔

**Solution.** $(1-x)(1+x+x^2)=1-x^3$, so the product is $(1-x)\,(1-x^3)^{2007}$. Terms of $(1-x^3)^{2007}$ have exponents divisible by $3$, so the product has exponents $\equiv0$ or $1\pmod3$. $2012\equiv2\pmod3$, so the coefficient is $0$.

### M-BIN-02 — JEE Main 2024 · 29 Jan Shift 1 · Q83 · Numerical

If $\dfrac{{}^{11}C_1}2+\dfrac{{}^{11}C_2}3+\cdots+\dfrac{{}^{11}C_9}{10}=\dfrac nm$ with $\gcd(n,m)=1$, then $n+m$ is equal to ______.

**Answer: 2041** · key ✔

**Solution.** $\dfrac{{}^{11}C_r}{r+1}=\dfrac{{}^{12}C_{r+1}}{12}$. So the sum is $\dfrac1{12}\sum_{k=2}^{10}{}^{12}C_k=\dfrac1{12}\left(2^{12}-1-12-12-1\right)=\dfrac{4070}{12}=\dfrac{2035}6$. With $\gcd(2035,6)=1$: $n+m=2041$.

### M-BIN-03 — JEE Main 2024 · 29 Jan Shift 2 · Q83 · Numerical

The remainder when $64^{32^{32}}$ is divided by $9$ is equal to ______.

**Answer: 1** · key ✔

**Solution.** $64=63+1\equiv1\pmod9$ (as $63=7\cdot9$), so every positive integer power of $64$ leaves remainder $1$. Equivalently, $64^N=(63+1)^N$ and every term but the last is divisible by $9$.

### M-BIN-04 — JEE Main 2024 · 30 Jan Shift 1 · Q83 · Numerical

The number of integral terms in the expansion of $\left\{7^{1/2}+11^{1/6}\right\}^{824}$ is equal to ______.

**Answer: 138** · key ✔

**Solution.** $T_{r+1}={}^{824}C_r\,7^{(824-r)/2}\,11^{r/6}$. This is an integer when $6\mid r$ (for $11^{r/6}$) and $(824-r)$ is even (for the power of 7). As $824$ is even, $r$ must be even, which multiples of $6$ already satisfy. So $r=0,6,12,\dots,822$: $\dfrac{822}6+1=138$ terms.

### M-BIN-05 — JEE Main 2024 · 30 Jan Shift 2 · Q63 · MCQ

Suppose $28-p,\ p,\ 70-\alpha,\ \alpha$ are the coefficients of four consecutive terms in the expansion of $(1+x)^n$. Then $2\alpha-3p$ equals

(1) 7  (2) 10  (3) 4  (4) 6

**Answer: (1)** · key ✔

**Solution.** Let the coefficients be ${}^nC_{r-1},{}^nC_r,{}^nC_{r+1},{}^nC_{r+2}$. Adding the first two: ${}^{n+1}C_r=28$; adding the last two: ${}^{n+1}C_{r+2}=70$. Since ${}^8C_2=28$ and ${}^8C_4=70$: $n+1=8,\ r=2$, so $n=7$. Then $28-p={}^7C_1=7\Rightarrow p=21$ and $\alpha={}^7C_4=35$. So $2\alpha-3p=70-63=7$.

### M-BIN-06 — JEE Main 2024 · 31 Jan Shift 2 · Q82 · Numerical

Let the coefficient of $x^r$ in the expansion of $(x+3)^{n-1}+(x+3)^{n-2}(x+2)+(x+3)^{n-3}(x+2)^2+\cdots+(x+2)^{n-1}$ be $\alpha_r$. If $\displaystyle\sum_{r=0}^n\alpha_r=\beta^n-\gamma^n$, $\beta,\gamma\in\mathbb N$, then $\beta^2+\gamma^2$ equals ______.

**Answer: 25** · key ✔

**Solution.** $\sum\alpha_r$ is the sum of coefficients, i.e. the value at $x=1$: $4^{n-1}+4^{n-2}3+\dots+3^{n-1}$, a geometric series with ratio $\tfrac34$, equal to $\dfrac{4^n-3^n}{4-3}=4^n-3^n$. So $\beta=4,\ \gamma=3$ and $\beta^2+\gamma^2=25$.

### M-BIN-07 — JEE Main 2024 · 1 Feb Shift 2 · Q64 · MCQ

Let $m$ and $n$ be the coefficients of the seventh and thirteenth terms respectively in the expansion of $\left(\tfrac13x^{1/3}+\tfrac1{2x^{2/3}}\right)^{18}$. Then $\left(\dfrac nm\right)^{1/3}$ is:

(1) $\dfrac49$  (2) $\dfrac19$  (3) $\dfrac14$  (4) $\dfrac94$

**Answer: (4)** · key ✔

**Solution.** $m=T_7$ coefficient $=\binom{18}{6}\left(\tfrac13\right)^{12}\left(\tfrac12\right)^6$, $n=T_{13}$ coefficient $=\binom{18}{12}\left(\tfrac13\right)^{6}\left(\tfrac12\right)^{12}$. Since $\binom{18}{6}=\binom{18}{12}$: $\dfrac nm=3^6/2^6=\left(\tfrac32\right)^6$, so $\left(\tfrac nm\right)^{1/3}=\left(\tfrac32\right)^2=\dfrac94$.

### M-BIN-08 — JEE Main 2024 · 4 Apr Shift 1 · Q65 · MCQ

The sum of all rational terms in the expansion of $\left(2^{1/5}+5^{1/3}\right)^{15}$ is:

(1) 3133  (2) 931  (3) 6131  (4) 633

**Answer: (1)** · key ✔

**Solution.** $T_{r+1}=\binom{15}{r}2^{(15-r)/5}5^{r/3}$. Rational needs $3\mid r$ and $5\mid(15-r)$, so $r\in\{0,15\}$. $r=0$: $2^3=8$; $r=15$: $5^5=3125$. Sum $=3133$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · Numerical

If $\left(\dfrac1{{}^{15}C_0}+\dfrac1{{}^{15}C_1}\right)\left(\dfrac1{{}^{15}C_1}+\dfrac1{{}^{15}C_2}\right)\cdots\left(\dfrac1{{}^{15}C_{12}}+\dfrac1{{}^{15}C_{13}}\right)=\dfrac{\alpha^{13}}{{}^{14}C_0\,{}^{14}C_1\cdots{}^{14}C_{12}}$, then $30\alpha$ is equal to ______.

**Answer: 32** · key (compiled)

**Solution.** Use ${}^{15}C_r=\dfrac{15}r{}^{14}C_{r-1}$ and ${}^{15}C_{r-1}=\dfrac{15}{16-r}{}^{14}C_{r-1}$. Then $\dfrac1{{}^{15}C_{r-1}}+\dfrac1{{}^{15}C_r}=\dfrac{(16-r)+r}{15\,{}^{14}C_{r-1}}=\dfrac{16}{15\,{}^{14}C_{r-1}}$. The product over $r=1,\dots,13$ is $\dfrac{(16/15)^{13}}{{}^{14}C_0\cdots{}^{14}C_{12}}$, so $\alpha=\dfrac{16}{15}$ and $30\alpha=32$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · MCQ

The value of $\dfrac{{}^{100}C_{50}}{51}+\dfrac{{}^{100}C_{51}}{52}+\cdots+\dfrac{{}^{100}C_{100}}{101}$ is:

(1) $\dfrac{2^{101}}{100}$  (2) $\dfrac{2^{100}}{100}$  (3) $\dfrac{2^{101}}{101}$  (4) $\dfrac{2^{100}}{101}$

**Answer: (4)** · key (compiled)

**Solution.** ${}^{100}C_r\cdot\dfrac1{r+1}=\dfrac{{}^{101}C_{r+1}}{101}$. So the sum is $\dfrac1{101}\sum_{k=51}^{101}{}^{101}C_k$. Since $101$ is odd, the coefficients with $k\ge51$ are exactly half of the total $2^{101}$, i.e. $2^{100}$. The sum is $\dfrac{2^{100}}{101}$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q3 · MCQ

The sum of all possible values of $n\in\mathbb N$, so that the coefficients of $x$, $x^2$ and $x^3$ in the expansion of $(1+x^2)^2(1+x)^n$ are in arithmetic progression, is:

(1) 12  (2) 7  (3) 3  (4) 9

**Answer: (4)** · key (compiled)

**Solution.** $(1+x^2)^2=1+2x^2+x^4$, so the coefficients are: $x$: $n$; $x^2$: ${}^nC_2+2$; $x^3$: ${}^nC_3+2n$. A.P.: $2\left({}^nC_2+2\right)=n+{}^nC_3+2n\Rightarrow n(n-1)+4=3n+\dfrac{n(n-1)(n-2)}6\Rightarrow n^3-9n^2+26n-24=0\Rightarrow(n-2)(n-3)(n-4)=0$. All three values are valid, and their sum is $9$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q4 · MCQ

Given below are two statements: Statement I: $25^{13}+20^{13}+8^{13}+3^{13}$ is divisible by 7. Statement II: The integral part of $(7+4\sqrt3)^{25}$ is an odd number.

(1) Statement I is true but Statement II is false  (2) Both Statement I and Statement II are true  (3) Statement I is false but Statement II is true  (4) Both Statement I and Statement II are false

**Answer: (2)** · key (compiled)

**Solution.** I: $25^{13}+3^{13}$ is divisible by $25+3=28$ and $20^{13}+8^{13}$ by $20+8=28$ (odd power), so the total is divisible by 7. II: let $\alpha=7+4\sqrt3$, $\beta=7-4\sqrt3$ ($0<\beta<1$, $\alpha\beta=1$, $\alpha+\beta=14$). $S_n=\alpha^n+\beta^n$ satisfies $S_n=14S_{n-1}-S_{n-2}$ with $S_0=2$, $S_1=14$, so every $S_n$ is an even integer. Then $\alpha^{25}=S_{25}-\beta^{25}$ with $0<\beta^{25}<1$, so its integral part is $S_{25}-1$, an odd number.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q5 · MCQ

The sum of the coefficients of $x^{499}$ and $x^{500}$ in $(1+x)^{1000}+x(1+x)^{999}+x^2(1+x)^{998}+\cdots+x^{1000}$ is:

(1) ${}^{1002}C_{500}$  (2) ${}^{1002}C_{501}$  (3) ${}^{1001}C_{501}$  (4) ${}^{1000}C_{501}$

**Answer: (1)** · key (compiled)

**Solution.** This is a G.P. with first term $(1+x)^{1000}$, ratio $\dfrac x{1+x}$ and 1001 terms: $S=(1+x)^{1000}\dfrac{1-\left(\frac x{1+x}\right)^{1001}}{1-\frac x{1+x}}=(1+x)^{1001}-x^{1001}$. The coefficients of $x^{499}$ and $x^{500}$ are ${}^{1001}C_{499}$ and ${}^{1001}C_{500}$; their sum is ${}^{1002}C_{500}$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q6 · MCQ

Let $C_r$ denote the coefficient of $x^r$ in the binomial expansion of $(1+x)^n$, $n\in\mathbb N$, $0\le r\le n$. If $P_n=C_0-C_1+\dfrac{2^2}3C_2-\dfrac{2^3}4C_3+\cdots+\dfrac{(-2)^n}{n+1}C_n$, then the value of $\sum_{n=1}^{25}\dfrac1{P_{2n}}$ equals:

(1) 650  (2) 675  (3) 525  (4) 580

**Answer: (2)** · key (compiled)

**Solution.** $P_n=\sum_{r=0}^n\dfrac{(-2)^rC_r}{r+1}$ and $\dfrac{C_r}{r+1}=\dfrac{{}^{n+1}C_{r+1}}{n+1}$, so $P_n=\dfrac1{n+1}\cdot\dfrac1{-2}\sum_{s=1}^{n+1}(-2)^s\,{}^{n+1}C_s=\dfrac{1-(-1)^{n+1}}{2(n+1)}$. For even index $2n$: $P_{2n}=\dfrac1{2n+1}$. $\sum_{n=1}^{25}(2n+1)=2\cdot\dfrac{25\cdot26}2+25=675$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q7 · MCQ

The coefficient of $x^{48}$ in $(1+x)+2(1+x)^2+3(1+x)^3+\dots+100(1+x)^{100}$ is equal to:

(1) $100\cdot{}^{100}C_{49}-{}^{100}C_{48}$  (2) ${}^{100}C_{50}+{}^{101}C_{49}$  (3) $100\cdot{}^{101}C_{49}-{}^{101}C_{50}$  (4) $100\cdot{}^{100}C_{49}-{}^{100}C_{50}$

**Answer: (3)** · key (compiled)

**Solution.** The required coefficient is $\sum_{k=48}^{100}k\,{}^kC_{48}$. Write $k\,{}^kC_{48}=49\,{}^{k+1}C_{49}-{}^kC_{48}$. By the hockey-stick identity $\sum_{k=48}^{100}{}^{k+1}C_{49}={}^{102}C_{50}$ and $\sum_{k=48}^{100}{}^kC_{48}={}^{101}C_{49}$. So the coefficient is $49\,{}^{102}C_{50}-{}^{101}C_{49}$. With ${}^{102}C_{50}={}^{101}C_{50}+{}^{101}C_{49}$ this is $49\,{}^{101}C_{50}+48\,{}^{101}C_{49}$; and ${}^{101}C_{50}={}^{101}C_{49}\cdot\dfrac{52}{50}$, giving ${}^{101}C_{49}\cdot98.96$, which equals $100\cdot{}^{101}C_{49}-{}^{101}C_{50}=(100-1.04)\,{}^{101}C_{49}$ – option (3).

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q8 · MCQ

If the coefficient of $x$ in the expansion of $(ax^2+bx+c)(1-2x)^{26}$ is $-56$ and the coefficients of $x^2$ and $x^3$ are both zero, then $a+b+c$ is equal to:

(1) 1500  (2) 1300  (3) 1403  (4) 1483

**Answer: (3)** · key (compiled)

**Solution.** $(1-2x)^{26}=1-52x+1300x^2-20800x^3+\cdots$. Coefficient of $x$: $b-52c=-56$. Of $x^2$: $a-52b+1300c=0$. Of $x^3$: $-52a+1300b-20800c=0$. From the first, $b=52c-56$; the second gives $a=52b-1300c=1404c-2912$. Substituting in the third: $-26208c+78624=0\Rightarrow c=3$, then $b=100$, $a=1300$. $a+b+c=1403$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q9 · MCQ

Let $S=\dfrac1{25!}+\dfrac1{3!\,23!}+\dfrac1{5!\,21!}+\dots$ up to 13 terms. If $13S=\dfrac{2^k}{n!}$, $k\in\mathbb N$, then $n+k$ is equal to:

(1) 50  (2) 49  (3) 52  (4) 51

**Answer: (2)** · key (compiled)

**Solution.** The $r$th term is $\dfrac1{(2r-1)!(27-2r)!}=\dfrac1{26!}{}^{26}C_{2r-1}$, so $S=\dfrac1{26!}\left({}^{26}C_1+{}^{26}C_3+\cdots+{}^{26}C_{25}\right)=\dfrac{2^{25}}{26!}$. Then $13S=\dfrac{13\cdot2^{25}}{26!}=\dfrac{2^{25}}{2\cdot25!}=\dfrac{2^{24}}{25!}$. So $k=24$, $n=25$ and $n+k=49$.

