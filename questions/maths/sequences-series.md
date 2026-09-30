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

