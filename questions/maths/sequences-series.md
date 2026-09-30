# Sequences & Series

> Theory: [../../theory/maths/sequences-series.md](../../theory/maths/sequences-series.md)

### M-SEQ-01 — JEE Main 2024 · 27 Jan Shift 1 · Q62 · MCQ

The number of common terms in the progressions $4,9,14,19,\dots$ up to the 25th term and $3,6,9,12,\dots$ up to the 37th term is

(1) 9  (2) 5  (3) 7  (4) 8

**Answer: (3)** · key ✔

**Solution.** The first AP ends at $4+24\cdot5=124$ and the second at $3\cdot37=111$, so common terms are $\le111$. A common term is $\equiv4\pmod5$ and $\equiv0\pmod3$, i.e. $\equiv9\pmod{15}$: $9,24,39,54,69,84,99$ (next $114>111$). That is $7$ terms.

### M-SEQ-02 — JEE Main 2024 · 27 Jan Shift 1 · Q82 · Numerical

If $8=3+\dfrac14(3+p)+\dfrac1{4^2}(3+2p)+\dfrac1{4^3}(3+3p)+\cdots\infty$, then $p$ is ______.

**Answer: 9** · key ✔

**Solution.** $\sum_{n\ge1}\dfrac{3}{4^n}=3\cdot\dfrac{1/4}{3/4}=1$ and $\sum_{n\ge1}\dfrac{n}{4^n}=\dfrac{1/4}{(3/4)^2}=\dfrac49$. So $8=3+1+\tfrac49p\Rightarrow p=9$.

### M-SEQ-03 — JEE Main 2024 · 27 Jan Shift 2 · Q63 · MCQ

The 20th term from the end of the progression $20,\ 19\tfrac14,\ 18\tfrac12,\ 17\tfrac34,\ \dots,\ -129\tfrac14$ is

(1) $-118$  (2) $-110$  (3) $-115$  (4) $-100$

**Answer: (3)** · key ✔

**Solution.** $a=20,\ d=-\tfrac34$. Number of terms: $n=1+\dfrac{20+129.25}{0.75}=200$. The 20th from the end is term $200-20+1=181$: $a_{181}=20-\tfrac34(180)=20-135=-115$.

### M-SEQ-04 — JEE Main 2024 · 29 Jan Shift 1 · Q62 · MCQ

In an A.P., the sixth term $a_6=2$. If the product $a_1a_4a_5$ is the greatest, then the common difference of the A.P. is equal to

(1) $\tfrac32$  (2) $\tfrac85$  (3) $\tfrac23$  (4) $\tfrac58$

**Answer: (2)** · key ✔

**Solution.** With common difference $d$: $a_1=2-5d,\ a_4=2-2d,\ a_5=2-d$. $P(d)=(2-5d)(2-2d)(2-d)=8-32d+34d^2-10d^3$. $P'(d)=-32+68d-30d^2=0\Rightarrow15d^2-34d+16=0\Rightarrow d=\tfrac85$ or $\tfrac23$. $P''(d)=68-60d$: at $d=\tfrac85$, $P''<0$ (maximum); at $d=\tfrac23$, $P''>0$ (minimum). So $d=\tfrac85$.

### M-SEQ-05 — JEE Main 2024 · 29 Jan Shift 2 · Q63 · MCQ

If $\ln a,\ \ln b,\ \ln c$ are in A.P. and $\ln a-\ln2b,\ \ln2b-\ln3c,\ \ln3c-\ln a$ are also in A.P., then $a:b:c$ is equal to

(1) 9 : 6 : 4  (2) 16 : 4 : 1  (3) 25 : 10 : 4  (4) 6 : 3 : 2

**Answer: (1)** · key ✔

**Solution.** First A.P. gives $b^2=ac$. Second: $2(\ln2b-\ln3c)=(\ln a-\ln2b)+(\ln3c-\ln a)=\ln3c-\ln2b\Rightarrow3\ln\dfrac{2b}{3c}=0\Rightarrow2b=3c$. Take $b=3k$: $c=2k$, $a=\dfrac{b^2}c=\dfrac{9k}2$. So $a:b:c=\dfrac92:3:2=9:6:4$.

### M-SEQ-06 — JEE Main 2024 · 29 Jan Shift 2 · Q64 · MCQ

Each term of a geometric progression $a_1,a_2,a_3,\dots$ with $a_1=\dfrac18$ and $a_2\ne a_1$ is the arithmetic mean of the next two terms. Let $S_n=a_1+\cdots+a_n$. Then $S_{20}-S_{18}$ is equal to

(1) $2^{15}$  (2) $-2^{18}$  (3) $2^{18}$  (4) $-2^{15}$

**Answer: (4)** · key ✔

**Solution.** $2a_n=a_{n+1}+a_{n+2}\Rightarrow2=r+r^2\Rightarrow r=1$ or $-2$; since $a_2\neq a_1$, $r=-2$. $S_{20}-S_{18}=a_{19}+a_{20}=a_1r^{18}(1+r)=\tfrac18\cdot2^{18}\cdot(-1)=-2^{15}$.

### M-SEQ-07 — JEE Main 2024 · 30 Jan Shift 1 · Q62 · MCQ

Let $S_n$ denote the sum of the first $n$ terms of an arithmetic progression. If $S_{20}=790$ and $S_{10}=145$, then $S_{15}-S_5$ is

(1) 395  (2) 390  (3) 405  (4) 410

**Answer: (1)** · key ✔

**Solution.** $S_n=\tfrac n2\left(2a+(n-1)d\right)$: $S_{20}=790\Rightarrow2a+19d=79$; $S_{10}=145\Rightarrow2a+9d=29$. Subtract: $10d=50\Rightarrow d=5$, $a=-8$. $S_{15}-S_5$ is the sum of terms $6$ to $15$: $\tfrac{10}{2}(a_6+a_{15})=5(17+62)=395$.

### M-SEQ-08 — JEE Main 2024 · 30 Jan Shift 1 · Q82 · Numerical

Let $\alpha=1^2+4^2+8^2+13^2+19^2+26^2+\cdots$ up to $10$ terms and $\beta=\sum_{n=1}^{10}n^4$. If $4\alpha-\beta=55k+40$, then $k$ is equal to ______.

**Answer: 353** · key ✔

**Solution.** The terms $1,4,8,13,19,26,\dots$ have differences $3,4,5,\dots$, so $a_n=\dfrac{n^2+3n-2}2$. Then $4a_n^2=(n^2+3n-2)^2=n^4+6n^3+5n^2-12n+4$, so $4\alpha-\beta=6\sum n^3+5\sum n^2-12\sum n+4(10)=6(3025)+5(385)-12(55)+40=19455$. So $55k=19415\Rightarrow k=353$.

### M-SEQ-09 — JEE Main 2024 · 30 Jan Shift 2 · Q62 · MCQ

Let $a$ and $b$ be two distinct positive real numbers. The $11^{th}$ term of a GP whose first term is $a$ and third term is $b$ equals the $p^{th}$ term of another GP whose first term is $a$ and fifth term is $b$. Then $p$ is equal to

(1) 20  (2) 25  (3) 21  (4) 24

**Answer: (3)** · key ✔

**Solution.** First GP: $r_1^2=\tfrac ba$, so the $11^{th}$ term is $ar_1^{10}=a\left(\tfrac ba\right)^5$. Second GP: $r_2^4=\tfrac ba$, so the $p^{th}$ term is $ar_2^{p-1}=a\left(\tfrac ba\right)^{(p-1)/4}$. Equating exponents: $5=\dfrac{p-1}4\Rightarrow p=21$.

### M-SEQ-10 — JEE Main 2024 · 30 Jan Shift 2 · Q83 · Numerical

Let $S_n$ be the sum to $n$ terms of the arithmetic progression $3,7,11,\dots$. If $40<\dfrac6{n(n+1)}\displaystyle\sum_{k=1}^nS_k<42$, then $n$ equals ______.

**Answer: 9** · key ✔

**Solution.** $S_k=\tfrac k2\left(6+4(k-1)\right)=k(2k+1)$. $\sum_{k=1}^nS_k=2\cdot\dfrac{n(n+1)(2n+1)}6+\dfrac{n(n+1)}2=\dfrac{n(n+1)(4n+5)}6$. Then $\dfrac6{n(n+1)}\sum S_k=4n+5$, and $40<4n+5<42\Rightarrow35<4n<37\Rightarrow n=9$.

### M-SEQ-11 — JEE Advanced 2025 · Paper 1 · Q12 · Numerical

$f:\mathbb R\to\mathbb R$ satisfies $f(x)>0$ and $f(x+y)=f(x)f(y)$. Real numbers $a_1,\dots,a_{50}$ are in AP with $f(a_{31})=64f(a_{25})$ and $\sum_{i=1}^{50}f(a_i)=3(2^{25}+1)$. Then $\sum_{i=6}^{30}f(a_i)=$ ______.

**Answer: 96** · official key ✔ (re-derived)

**Solution.** Since $a_i$ form an AP, $f(a_{i+1})=f(a_i)f(d)$: the values $f(a_i)$ form a GP with ratio $r=f(d)>0$. $f(a_{31})=64f(a_{25})\Rightarrow r^6=64\Rightarrow r=2$. With first term $c$: $c(2^{50}-1)=3(2^{25}+1)\Rightarrow c=\dfrac{3}{2^{25}-1}$. $\sum_{i=6}^{30}=c\,2^5\dfrac{2^{25}-1}{2-1}=32\times3=96$.

