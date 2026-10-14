# Sequences & Series

> Theory: [../../theory/maths/sequences-series.md](../../theory/maths/sequences-series.md)

### M-SEQ-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

The positive integer $n$, for which the solutions of the equation $x(x+2)+(x+2)(x+4)+\cdots+(x+2n-2)(x+2n)=\dfrac{8n}3$ are two consecutive even integers, is:

(1) 3  (2) 12  (3) 9  (4) 6

**Answer: (1)** · answer derived (no key in source)

**Solution.** Telescope using $P(k)=(x+2k-2)(x+2k)(x+2k+2)$: $P(k+1)-P(k)=6(x+2k)(x+2k+2)$. So the sum $=\dfrac{P(n)-P(0)}6$ with $P(n)=(y-2)y(y+2)=y^3-4y$ for $y=x+2n$ and $P(0)=x^3-4x$. The equation becomes $(x+2n)^3-x^3-8n=16n$, i.e. $6nx^2+12n^2x+8n^3-24n=0$, i.e. $3x^2+6nx+4n^2-12=0$. The difference of the roots is $\dfrac{\sqrt{144-12n^2}}3=2\Rightarrow144-12n^2=36\Rightarrow n=3$ (roots $-2,-4$).

### M-SEQ-02 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let the arithmetic mean of $\dfrac1a$ and $\dfrac1b$ be $\dfrac5{16}$, $a>2$. If $\alpha$ is such that $a,4,\alpha,b$ are in A.P., then the equation $\alpha x^2-ax+2(\alpha-2b)=0$ has:

(1) one root in $(0,2)$ and another in $(-4,-2)$  (2) one root in $(1,4)$ and another in $(-2,0)$  (3) both roots in the interval $(-2,0)$  (4) complex roots of magnitude less than 2

**Answer: (2)** · answer derived (no key in source)

**Solution.** With common difference $d=4-a$: $\alpha=8-a$, $b=12-2a$. $\dfrac1a+\dfrac1b=\dfrac58\Rightarrow\dfrac{12-a}{a(12-2a)}=\dfrac58\Rightarrow5a^2-34a+48=0\Rightarrow a=\dfrac{24}5$ or $2$; since $a>2$, $a=\dfrac{24}5$, $\alpha=\dfrac{16}5$, $b=\dfrac{12}5$. The equation is $\dfrac{16}5x^2-\dfrac{24}5x+2\left(\dfrac{16}5-\dfrac{24}5\right)=0\Rightarrow2x^2-3x-2=0\Rightarrow(2x+1)(x-2)=0$, roots $2\in(1,4)$ and $-\tfrac12\in(-2,0)$.

### M-SEQ-03 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q6 · MCQ

Let $a_1,a_2,a_3,a_4$ be an A.P. of four terms such that each term of the A.P. and its common difference $l$ are integers. If $a_1+a_2+a_3+a_4=48$ and $a_1a_2a_3a_4+l^4=361$, then the largest term of the A.P. is equal to:

(1) 23  (2) 21  (3) 27  (4) 24

**Answer: (3)** · answer derived (no key in source)

**Solution.** The sum gives $4a_1+6l=48\Rightarrow2a_1+3l=24$, so $l=2t$ is even and the terms are $12-3t,\ 12-t,\ 12+t,\ 12+3t$. The product is $(144-9t^2)(144-t^2)$, and $l^4=16t^4$. So $(144-9t^2)(144-t^2)+16t^4=361\Rightarrow5t^4-288t^2+4075=0\Rightarrow t^2=25$ (the other root $32.6$ is not a perfect square). $t=5$: terms $-3,7,17,27$ (check: product $-9639$, $+10^4=361$ ✓). Largest term $=27$.

### M-SEQ-04 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q8 · Numerical

Suppose $a,b,c$ are in A.P. and $a^2,2b^2,c^2$ are in G.P. If $a<b<c$ and $a+b+c=1$, then $9(a^2+b^2+c^2)$ is equal to ______.

**Answer: 9** · answer derived (no key in source)

**Solution.** A.P. with $a+b+c=1$ gives $3b=1$, $b=\tfrac13$, $a+c=\tfrac23$. G.P.: $(2b^2)^2=a^2c^2\Rightarrow ac=\pm2b^2=\pm\tfrac29$. $ac=\tfrac29$ gives complex $a,c$ (discriminant $\tfrac49-\tfrac89<0$), so $ac=-\tfrac29$ (with $a=\tfrac{1-\sqrt3}3<b<c=\tfrac{1+\sqrt3}3$). $a^2+b^2+c^2=(a+c)^2-2ac+b^2=\tfrac49+\tfrac49+\tfrac19=1$, so $9(a^2+b^2+c^2)=9$.

### M-SEQ-05 · A — JEE Main 2026 · 21 Jan Shift 1 · set Q11 · MCQ

Let $a_1,a_2,a_3,\dots$ be a G.P. of increasing positive terms such that $a_2\cdot a_3\cdot a_4=64$ and $a_1+a_3+a_5=\dfrac{813}7$. Then $a_3+a_5+a_7$ is equal to:

(1) 3244  (2) 3248  (3) 3252  (4) 3256

**Answer: (3)** · answer derived (no key in source)

**Solution.** $a_2a_3a_4=a_3^3=64\Rightarrow a_3=4$. With ratio $r$ and $u=r^2$: $\dfrac4u+4+4u=\dfrac{813}7\Rightarrow u+\dfrac1u=\dfrac{785}{28}\Rightarrow28u^2-785u+28=0\Rightarrow u=28$ or $\tfrac1{28}$ (discriminant $783^2$). Increasing means $r>1$, so $u=28$. $a_3+a_5+a_7=4(1+u+u^2)=4(1+28+784)=3252$.

### M-SEQ-06 · A — JEE Main 2026 · 28 Jan Shift 1 · set Q13 · MCQ

The common difference of the A.P. $a_1,a_2,\dots,a_m$ is 13 more than the common difference of the A.P. $b_1,b_2,\dots,b_n$. If $b_{31}=-277$, $b_{43}=-385$ and $a_{78}=327$, then $a_1$ is equal to:

(1) 16  (2) 21  (3) 19  (4) 24

**Answer: (3)** · answer derived (no key in source)

**Solution.** For the $b$-progression: $d_b=\dfrac{b_{43}-b_{31}}{12}=\dfrac{-108}{12}=-9$. So $d_a=-9+13=4$. $a_{78}=a_1+77\cdot4=327\Rightarrow a_1=327-308=19$.

### M-SEQ-07 · A — JEE Main 2026 · 24 Jan Shift 1 · set Q16 · MCQ

Consider an A.P.: $a_1,a_2,\dots,a_n$; $a_1>0$. If $a_2-a_1=-\dfrac34$, $a_n=\dfrac14a_1$, and $\sum_{i=1}^na_i=\dfrac{525}2$, then $\sum_{i=1}^{17}a_i$ is equal to:

(1) 136  (2) 476  (3) 238  (4) 952

**Answer: (3)** · answer derived (no key in source)

**Solution.** $a_n=a_1+(n-1)\left(-\tfrac34\right)=\tfrac14a_1\Rightarrow\tfrac34a_1=\tfrac34(n-1)\Rightarrow a_1=n-1$. $S_n=\dfrac n2\left(a_1+\tfrac14a_1\right)=\dfrac{5n(n-1)}8=\dfrac{525}2\Rightarrow n(n-1)=420\Rightarrow n=21$, $a_1=20$. $S_{17}=\dfrac{17}2\left(40+16\cdot\left(-\tfrac34\right)\right)=\dfrac{17}2\cdot28=238$.

### M-SEQ-08 · A — JEE Main 2025 · Jan session · set Q1 · MCQ

If the first term of an A.P. is 3 and the sum of its first four terms is equal to one-fifth of the sum of the next four terms, then the sum of the first 20 terms is equal to:

(1) $-1080$  (2) $-1020$  (3) $-1200$  (4) $-120$

**Answer: (1)** · key (compiled)

**Solution.** $S_4=\tfrac15(S_8-S_4)\Rightarrow S_8=6S_4$. $S_8=24+28d$ and $S_4=12+6d$, so $24+28d=72+36d\Rightarrow d=-6$. $S_{20}=10(2\cdot3+19d)=10(6-114)=-1080$.

### M-SEQ-09 · B — JEE Advanced 2025 · Paper 1 · Q12 · Numerical

$f:\mathbb R\to\mathbb R$ satisfies $f(x)>0$ and $f(x+y)=f(x)f(y)$. Real numbers $a_1,\dots,a_{50}$ are in AP with $f(a_{31})=64f(a_{25})$ and $\sum_{i=1}^{50}f(a_i)=3(2^{25}+1)$. Then $\sum_{i=6}^{30}f(a_i)=$ ______.

**Answer: 96** · official key ✔ (re-derived)

**Solution.** Since $a_i$ form an AP, $f(a_{i+1})=f(a_i)f(d)$: the values $f(a_i)$ form a GP with ratio $r=f(d)>0$. $f(a_{31})=64f(a_{25})\Rightarrow r^6=64\Rightarrow r=2$. With first term $c$: $c(2^{50}-1)=3(2^{25}+1)\Rightarrow c=\dfrac{3}{2^{25}-1}$. $\sum_{i=6}^{30}=c\,2^5\dfrac{2^{25}-1}{2-1}=32\times3=96$.

### M-SEQ-10 · B — JEE Main 2025 · Jan session · set Q2 · Numerical

The roots of the quadratic equation $3x^2-px+q=0$ are the 10th and 11th terms of an arithmetic progression with common difference $\tfrac32$. If the sum of the first 11 terms of this arithmetic progression is 88, then $q-2p$ is equal to ______.

**Answer: 474** · key (compiled)

**Solution.** $S_{11}=11a_6=88\Rightarrow a_6=8$, so $a_{10}=8+4\cdot\tfrac32=14$ and $a_{11}=15.5$. Sum of roots $=\tfrac p3=29.5\Rightarrow p=88.5$; product $=\tfrac q3=14\cdot15.5=217\Rightarrow q=651$. $q-2p=651-177=474$.

### M-SEQ-11 · B — JEE Main 2025 · Jan session · set Q3 · MCQ

In an arithmetic progression, if $S_{40}=1030$ and $S_{12}=57$, then $S_{30}-S_{10}$ is equal to:

(1) 525  (2) 510  (3) 515  (4) 505

**Answer: (3)** · key (compiled)

**Solution.** $20(2a+39d)=1030$ gives $2a+39d=51.5$; $6(2a+11d)=57$ gives $2a+11d=9.5$. Subtracting, $d=1.5$ and $a=-3.5$. $S_{30}-S_{10}=15(2a+29d)-5(2a+9d)=20a+390d=-70+585=515$.

### M-SEQ-12 · B — JEE Main 2025 · Apr session · set Q3 · MCQ

Let $a_1,a_2,a_3,\dots$ be a G.P. of increasing positive numbers. If $a_3a_5=729$ and $a_2+a_4=\dfrac{111}4$, then $24(a_1+a_2+a_3)$ is equal to:

(1) 131  (2) 130  (3) 129  (4) 128

**Answer: (3)** · key (compiled)

**Solution.** $a_3a_5=a_4^2=729\Rightarrow a_4=27$ (positive), so $a_2=\dfrac{111}4-27=\dfrac34$ and $r^2=\dfrac{27}{3/4}=36$, $r=6$. $a_1=\dfrac18$, $a_3=\dfrac92$. $a_1+a_2+a_3=\dfrac18+\dfrac34+\dfrac92=\dfrac{43}8$ and $24\cdot\dfrac{43}8=129$.

### M-SEQ-13 · B — JEE Main 2025 · Apr session · set Q4 · MCQ

The sum $1+\dfrac{1+3}{2!}+\dfrac{1+3+5}{3!}+\dfrac{1+3+5+7}{4!}+\cdots$ up to $\infty$ terms is equal to:

(1) $6e$  (2) $4e$  (3) $3e$  (4) $2e$

**Answer: (4)** · key (compiled)

**Solution.** The $n$th term is $\dfrac{n^2}{n!}=\dfrac n{(n-1)!}=\dfrac{(n-1)+1}{(n-1)!}$. The sum is $\sum_{n\ge2}\dfrac1{(n-2)!}+\sum_{n\ge1}\dfrac1{(n-1)!}=e+e=2e$.

### M-SEQ-14 · B — JEE Main 2025 · Apr session · set Q8 · MCQ

If the sum of the second, fourth and sixth terms of a G.P. of positive terms is 21 and the sum of its eighth, tenth and twelfth terms is 15309, then the sum of its first nine terms is:

(1) 760  (2) 755  (3) 750  (4) 757

**Answer: (4)** · key (compiled)

**Solution.** Multiplying the group $a_2+a_4+a_6$ by $r^6$ gives $a_8+a_{10}+a_{12}$, so $r^6=\dfrac{15309}{21}=729$ and $r=3$. $a_2(1+9+81)=21\Rightarrow a_2=\dfrac3{13}$ and $a_1=\dfrac1{13}$. $S_9=\dfrac1{13}\cdot\dfrac{3^9-1}2=\dfrac{19682}{26}=757$.

### M-SEQ-15 · B — JEE Main 2024 · 27 Jan Shift 1 · Q62 · MCQ

The number of common terms in the progressions $4,9,14,19,\dots$ up to the 25th term and $3,6,9,12,\dots$ up to the 37th term is

(1) 9  (2) 5  (3) 7  (4) 8

**Answer: (3)** · key ✔

**Solution.** The first AP ends at $4+24\cdot5=124$ and the second at $3\cdot37=111$, so common terms are $\le111$. A common term is $\equiv4\pmod5$ and $\equiv0\pmod3$, i.e. $\equiv9\pmod{15}$: $9,24,39,54,69,84,99$ (next $114>111$). That is $7$ terms.

### M-SEQ-16 · C — JEE Main 2024 · 27 Jan Shift 2 · Q63 · MCQ

The 20th term from the end of the progression $20,\ 19\tfrac14,\ 18\tfrac12,\ 17\tfrac34,\ \dots,\ -129\tfrac14$ is

(1) $-118$  (2) $-110$  (3) $-115$  (4) $-100$

**Answer: (3)** · key ✔

**Solution.** $a=20,\ d=-\tfrac34$. Number of terms: $n=1+\dfrac{20+129.25}{0.75}=200$. The 20th from the end is term $200-20+1=181$: $a_{181}=20-\tfrac34(180)=20-135=-115$.

### M-SEQ-17 · C — JEE Main 2024 · 29 Jan Shift 2 · Q63 · MCQ

If $\ln a,\ \ln b,\ \ln c$ are in A.P. and $\ln a-\ln2b,\ \ln2b-\ln3c,\ \ln3c-\ln a$ are also in A.P., then $a:b:c$ is equal to

(1) 9 : 6 : 4  (2) 16 : 4 : 1  (3) 25 : 10 : 4  (4) 6 : 3 : 2

**Answer: (1)** · key ✔

**Solution.** First A.P. gives $b^2=ac$. Second: $2(\ln2b-\ln3c)=(\ln a-\ln2b)+(\ln3c-\ln a)=\ln3c-\ln2b\Rightarrow3\ln\dfrac{2b}{3c}=0\Rightarrow2b=3c$. Take $b=3k$: $c=2k$, $a=\dfrac{b^2}c=\dfrac{9k}2$. So $a:b:c=\dfrac92:3:2=9:6:4$.

### M-SEQ-18 · C — JEE Main 2024 · 30 Jan Shift 1 · Q62 · MCQ

Let $S_n$ denote the sum of the first $n$ terms of an arithmetic progression. If $S_{20}=790$ and $S_{10}=145$, then $S_{15}-S_5$ is

(1) 395  (2) 390  (3) 405  (4) 410

**Answer: (1)** · key ✔

**Solution.** $S_n=\tfrac n2\left(2a+(n-1)d\right)$: $S_{20}=790\Rightarrow2a+19d=79$; $S_{10}=145\Rightarrow2a+9d=29$. Subtract: $10d=50\Rightarrow d=5$, $a=-8$. $S_{15}-S_5$ is the sum of terms $6$ to $15$: $\tfrac{10}{2}(a_6+a_{15})=5(17+62)=395$.

### M-SEQ-19 · C — JEE Main 2024 · 30 Jan Shift 2 · Q62 · MCQ

Let $a$ and $b$ be two distinct positive real numbers. The $11^{th}$ term of a GP whose first term is $a$ and third term is $b$ equals the $p^{th}$ term of another GP whose first term is $a$ and fifth term is $b$. Then $p$ is equal to

(1) 20  (2) 25  (3) 21  (4) 24

**Answer: (3)** · key ✔

**Solution.** First GP: $r_1^2=\tfrac ba$, so the $11^{th}$ term is $ar_1^{10}=a\left(\tfrac ba\right)^5$. Second GP: $r_2^4=\tfrac ba$, so the $p^{th}$ term is $ar_2^{p-1}=a\left(\tfrac ba\right)^{(p-1)/4}$. Equating exponents: $5=\dfrac{p-1}4\Rightarrow p=21$.

