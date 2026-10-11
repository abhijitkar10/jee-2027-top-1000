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

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

The positive integer $n$, for which the solutions of the equation $x(x+2)+(x+2)(x+4)+\cdots+(x+2n-2)(x+2n)=\dfrac{8n}3$ are two consecutive even integers, is:

(1) 3  (2) 12  (3) 9  (4) 6

**Answer: (1)** · answer derived (no key in source)

**Solution.** Telescope using $P(k)=(x+2k-2)(x+2k)(x+2k+2)$: $P(k+1)-P(k)=6(x+2k)(x+2k+2)$. So the sum $=\dfrac{P(n)-P(0)}6$ with $P(n)=(y-2)y(y+2)=y^3-4y$ for $y=x+2n$ and $P(0)=x^3-4x$. The equation becomes $(x+2n)^3-x^3-8n=16n$, i.e. $6nx^2+12n^2x+8n^3-24n=0$, i.e. $3x^2+6nx+4n^2-12=0$. The difference of the roots is $\dfrac{\sqrt{144-12n^2}}3=2\Rightarrow144-12n^2=36\Rightarrow n=3$ (roots $-2,-4$).

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q2 · MCQ

Let $a_1,\dfrac{a_2}2,\dfrac{a_3}{2^2},\dots,\dfrac{a_{10}}{2^9}$ be a G.P. of common ratio $\dfrac1{\sqrt2}$. If $a_1+a_2+\dots+a_{10}=62$, then $a_1$ is equal to:

(1) $2-\sqrt2$  (2) $2(2-\sqrt2)$  (3) $\sqrt2-1$  (4) $2(\sqrt2-1)$

**Answer: (4)** · answer derived (no key in source)

**Solution.** $\dfrac{a_k}{2^{k-1}}=a_1\left(\dfrac1{\sqrt2}\right)^{k-1}\Rightarrow a_k=a_1(\sqrt2)^{k-1}$, so $a_k$ is a G.P. of ratio $\sqrt2$. $a_1\dfrac{(\sqrt2)^{10}-1}{\sqrt2-1}=a_1\dfrac{31}{\sqrt2-1}=62\Rightarrow a_1=2(\sqrt2-1)$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

Let the arithmetic mean of $\dfrac1a$ and $\dfrac1b$ be $\dfrac5{16}$, $a>2$. If $\alpha$ is such that $a,4,\alpha,b$ are in A.P., then the equation $\alpha x^2-ax+2(\alpha-2b)=0$ has:

(1) one root in $(0,2)$ and another in $(-4,-2)$  (2) one root in $(1,4)$ and another in $(-2,0)$  (3) both roots in the interval $(-2,0)$  (4) complex roots of magnitude less than 2

**Answer: (2)** · answer derived (no key in source)

**Solution.** With common difference $d=4-a$: $\alpha=8-a$, $b=12-2a$. $\dfrac1a+\dfrac1b=\dfrac58\Rightarrow\dfrac{12-a}{a(12-2a)}=\dfrac58\Rightarrow5a^2-34a+48=0\Rightarrow a=\dfrac{24}5$ or $2$; since $a>2$, $a=\dfrac{24}5$, $\alpha=\dfrac{16}5$, $b=\dfrac{12}5$. The equation is $\dfrac{16}5x^2-\dfrac{24}5x+2\left(\dfrac{16}5-\dfrac{24}5\right)=0\Rightarrow2x^2-3x-2=0\Rightarrow(2x+1)(x-2)=0$, roots $2\in(1,4)$ and $-\tfrac12\in(-2,0)$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q4 · MCQ

$\dfrac6{3^{26}}+\dfrac{10\cdot1}{3^{25}}+\dfrac{10\cdot2}{3^{24}}+\dfrac{10\cdot2^2}{3^{23}}+\cdots+\dfrac{10\cdot2^{24}}3$ is equal to:

(1) $2^{26}$  (2) $3^{25}$  (3) $3^{26}$  (4) $2^{25}$

**Answer: (1)** · answer derived (no key in source)

**Solution.** The terms after the first are $\dfrac{10\cdot2^k}{3^{25-k}}$ for $k=0,\dots,24$: $\dfrac{10}{3^{25}}\sum_{k=0}^{24}6^k=\dfrac{10}{3^{25}}\cdot\dfrac{6^{25}-1}5=\dfrac{2\cdot6^{25}-2}{3^{25}}=2^{26}-\dfrac2{3^{25}}$. Adding $\dfrac6{3^{26}}=\dfrac2{3^{25}}$ gives $2^{26}$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q5 · Numerical

If $\sum_{r=1}^{25}\left(\dfrac r{r^4+r^2+1}\right)=\dfrac pq$, where $p$ and $q$ are positive integers such that $\gcd(p,q)=1$, then $p+q$ is equal to ______.

**Answer: 976** · answer derived (no key in source)

**Solution.** $r^4+r^2+1=(r^2-r+1)(r^2+r+1)$ and $\dfrac r{r^4+r^2+1}=\dfrac12\left[\dfrac1{r^2-r+1}-\dfrac1{r^2+r+1}\right]$. Since $(r+1)^2-(r+1)+1=r^2+r+1$, the sum telescopes: $\dfrac12\left[1-\dfrac1{25^2+25+1}\right]=\dfrac12\left(1-\dfrac1{651}\right)=\dfrac{325}{651}$. $\gcd(325,651)=1$ ($651=3\cdot7\cdot31$), so $p+q=976$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q6 · MCQ

Let $a_1,a_2,a_3,a_4$ be an A.P. of four terms such that each term of the A.P. and its common difference $l$ are integers. If $a_1+a_2+a_3+a_4=48$ and $a_1a_2a_3a_4+l^4=361$, then the largest term of the A.P. is equal to:

(1) 23  (2) 21  (3) 27  (4) 24

**Answer: (3)** · answer derived (no key in source)

**Solution.** The sum gives $4a_1+6l=48\Rightarrow2a_1+3l=24$, so $l=2t$ is even and the terms are $12-3t,\ 12-t,\ 12+t,\ 12+3t$. The product is $(144-9t^2)(144-t^2)$, and $l^4=16t^4$. So $(144-9t^2)(144-t^2)+16t^4=361\Rightarrow5t^4-288t^2+4075=0\Rightarrow t^2=25$ (the other root $32.6$ is not a perfect square). $t=5$: terms $-3,7,17,27$ (check: product $-9639$, $+10^4=361$ ✓). Largest term $=27$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q7 · MCQ

$\left(\dfrac13+\dfrac47\right)+\left(\dfrac1{3^2}+\dfrac13\times\dfrac47+\dfrac{4^2}{7^2}\right)+\left(\dfrac1{3^3}+\dfrac1{3^2}\times\dfrac47+\dfrac13\times\dfrac{4^2}{7^2}+\dfrac{4^3}{7^3}\right)+\cdots$ up to infinite terms is equal to:

(1) $\dfrac43$  (2) $\dfrac65$  (3) $\dfrac52$  (4) $\dfrac74$

**Answer: (3)** · answer derived (no key in source)

**Solution.** With $x=\dfrac13$, $y=\dfrac47$, the $n$th bracket is $\sum_{k=0}^nx^{n-k}y^k=\dfrac{x^{n+1}-y^{n+1}}{x-y}$. Summing over $n\ge1$: $\dfrac1{x-y}\left[\dfrac{x^2}{1-x}-\dfrac{y^2}{1-y}\right]=\dfrac{\tfrac16-\tfrac{16}{21}}{\tfrac13-\tfrac47}=\dfrac{-\tfrac{25}{42}}{-\tfrac5{21}}=\dfrac52$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q8 · Numerical

Suppose $a,b,c$ are in A.P. and $a^2,2b^2,c^2$ are in G.P. If $a<b<c$ and $a+b+c=1$, then $9(a^2+b^2+c^2)$ is equal to ______.

**Answer: 9** · answer derived (no key in source)

**Solution.** A.P. with $a+b+c=1$ gives $3b=1$, $b=\tfrac13$, $a+c=\tfrac23$. G.P.: $(2b^2)^2=a^2c^2\Rightarrow ac=\pm2b^2=\pm\tfrac29$. $ac=\tfrac29$ gives complex $a,c$ (discriminant $\tfrac49-\tfrac89<0$), so $ac=-\tfrac29$ (with $a=\tfrac{1-\sqrt3}3<b<c=\tfrac{1+\sqrt3}3$). $a^2+b^2+c^2=(a+c)^2-2ac+b^2=\tfrac49+\tfrac49+\tfrac19=1$, so $9(a^2+b^2+c^2)=9$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q9 · MCQ

If the sum of the first four terms of an A.P. is 6 and the sum of its first six terms is 4, then the sum of its first twelve terms is:

(1) $-22$  (2) $-24$  (3) $-20$  (4) $-26$

**Answer: (1)** · answer derived (no key in source)

**Solution.** $S_4=2(2a+3d)=6\Rightarrow2a+3d=3$; $S_6=3(2a+5d)=4\Rightarrow2a+5d=\tfrac43$. Subtract: $2d=-\tfrac53$, $d=-\tfrac56$, $2a=3+\tfrac52=\tfrac{11}2$. $S_{12}=6(2a+11d)=6\left(\tfrac{11}2-\tfrac{55}6\right)=6\cdot\left(-\tfrac{22}6\right)=-22$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q10 · MCQ

Let $\sum_{k=1}^na_k=\alpha n^2+\beta n$. If $a_{10}=59$ and $a_6=7a_1$, then $\alpha+\beta$ is equal to:

(1) 3  (2) 12  (3) 7  (4) 5

**Answer: (4)** · answer derived (no key in source)

**Solution.** $a_n=S_n-S_{n-1}=\alpha(2n-1)+\beta$. $a_{10}=19\alpha+\beta=59$. $a_6=11\alpha+\beta=7a_1=7(\alpha+\beta)\Rightarrow4\alpha=6\beta\Rightarrow\beta=\tfrac23\alpha$. Then $19\alpha+\tfrac23\alpha=\tfrac{59}3\alpha=59\Rightarrow\alpha=3$, $\beta=2$, so $\alpha+\beta=5$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q11 · MCQ

Let $a_1,a_2,a_3,\dots$ be a G.P. of increasing positive terms such that $a_2\cdot a_3\cdot a_4=64$ and $a_1+a_3+a_5=\dfrac{813}7$. Then $a_3+a_5+a_7$ is equal to:

(1) 3244  (2) 3248  (3) 3252  (4) 3256

**Answer: (3)** · answer derived (no key in source)

**Solution.** $a_2a_3a_4=a_3^3=64\Rightarrow a_3=4$. With ratio $r$ and $u=r^2$: $\dfrac4u+4+4u=\dfrac{813}7\Rightarrow u+\dfrac1u=\dfrac{785}{28}\Rightarrow28u^2-785u+28=0\Rightarrow u=28$ or $\tfrac1{28}$ (discriminant $783^2$). Increasing means $r>1$, so $u=28$. $a_3+a_5+a_7=4(1+u+u^2)=4(1+28+784)=3252$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q12 · Numerical

Let $a_1=1$ and for $n\ge1$, $a_{n+1}=\dfrac12a_n+\dfrac{n^2-2n-1}{n^2(n+1)^2}$. Then $\left|\sum_{n=1}^\infty\left(a_n-\dfrac2{n^2}\right)\right|$ is equal to ______.

**Answer: 2** · answer derived (no key in source)

**Solution.** Try $b_n=a_n-\dfrac c{n^2}$ with $b_{n+1}=\tfrac12b_n$: this needs $\dfrac{n^2-2n-1}{n^2(n+1)^2}=\dfrac c{(n+1)^2}-\dfrac c{2n^2}=\dfrac{c(n^2-2n-1)}{2n^2(n+1)^2}$, so $c=2$. Then $b_n=a_n-\dfrac2{n^2}$ is a G.P. with $b_1=1-2=-1$ and ratio $\tfrac12$, so $\sum b_n=\dfrac{-1}{1-\tfrac12}=-2$ and the absolute value is 2.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q13 · MCQ

The common difference of the A.P. $a_1,a_2,\dots,a_m$ is 13 more than the common difference of the A.P. $b_1,b_2,\dots,b_n$. If $b_{31}=-277$, $b_{43}=-385$ and $a_{78}=327$, then $a_1$ is equal to:

(1) 16  (2) 21  (3) 19  (4) 24

**Answer: (3)** · answer derived (no key in source)

**Solution.** For the $b$-progression: $d_b=\dfrac{b_{43}-b_{31}}{12}=\dfrac{-108}{12}=-9$. So $d_a=-9+13=4$. $a_{78}=a_1+77\cdot4=327\Rightarrow a_1=327-308=19$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q14 · MCQ

The value of $\sum_{k=1}^\infty(-1)^{k+1}\left(\dfrac{k(k+1)}{k!}\right)$ is:

(1) $2/e$  (2) $1/e$  (3) $e/2$  (4) $\sqrt e$

**Answer: (2)** · answer derived (no key in source)

**Solution.** $\dfrac{k(k+1)}{k!}=\dfrac{k+1}{(k-1)!}$. With $j=k-1$: $\sum_{j\ge0}(-1)^j\dfrac{j+2}{j!}=\sum_{j\ge1}\dfrac{(-1)^j}{(j-1)!}+2\sum_{j\ge0}\dfrac{(-1)^j}{j!}=-e^{-1}+2e^{-1}=\dfrac1e$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q15 · Numerical

In a G.P., if the product of the first three terms is 27 and the set of all possible values for the sum of its first three terms is $\mathbb R-(a,b)$, then $a^2+b^2$ is equal to ______.

**Answer: 90** · answer derived (no key in source)

**Solution.** Write the terms as $\dfrac3r,3,3r$ (product $27$). The sum is $3\left(1+r+\dfrac1r\right)$. For $r>0$: $r+\dfrac1r\ge2$, so the sum is $\ge9$. For $r<0$: $r+\dfrac1r\le-2$, so the sum is $\le-3$. The set of sums is $(-\infty,-3]\cup[9,\infty)=\mathbb R-(-3,9)$, so $a^2+b^2=9+81=90$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q16 · MCQ

Consider an A.P.: $a_1,a_2,\dots,a_n$; $a_1>0$. If $a_2-a_1=-\dfrac34$, $a_n=\dfrac14a_1$, and $\sum_{i=1}^na_i=\dfrac{525}2$, then $\sum_{i=1}^{17}a_i$ is equal to:

(1) 136  (2) 476  (3) 238  (4) 952

**Answer: (3)** · answer derived (no key in source)

**Solution.** $a_n=a_1+(n-1)\left(-\tfrac34\right)=\tfrac14a_1\Rightarrow\tfrac34a_1=\tfrac34(n-1)\Rightarrow a_1=n-1$. $S_n=\dfrac n2\left(a_1+\tfrac14a_1\right)=\dfrac{5n(n-1)}8=\dfrac{525}2\Rightarrow n(n-1)=420\Rightarrow n=21$, $a_1=20$. $S_{17}=\dfrac{17}2\left(40+16\cdot\left(-\tfrac34\right)\right)=\dfrac{17}2\cdot28=238$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q17 · MCQ

Let $729,81,9,1,\dots$ be a sequence and $P_n$ denote the product of the first $n$ terms of this sequence. If $2\sum_{n=1}^{40}(P_n)^{1/n}=\dfrac{3^\alpha-1}{3^\beta}$ and $\gcd(\alpha,\beta)=1$, then $\alpha+\beta$ is equal to:

(1) 74  (2) 76  (3) 73  (4) 75

**Answer: (3)** · answer derived (no key in source)

**Solution.** The sequence is a G.P. with $a_k=3^{6-2(k-1)}=3^{8-2k}$. $P_n=3^{\sum(8-2k)}=3^{8n-n(n+1)}=3^{7n-n^2}$, so $(P_n)^{1/n}=3^{7-n}$. $\sum_{n=1}^{40}3^{7-n}=3^6\dfrac{1-3^{-40}}{1-\tfrac13}=\dfrac{3^7-3^{-33}}2$, so $2\sum=3^7-3^{-33}=\dfrac{3^{40}-1}{3^{33}}$. Thus $\alpha=40$, $\beta=33$ ($\gcd=1$) and $\alpha+\beta=73$.

