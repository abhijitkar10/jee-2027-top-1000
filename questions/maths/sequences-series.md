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

