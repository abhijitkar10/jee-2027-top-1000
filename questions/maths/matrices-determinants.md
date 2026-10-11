# Matrices & Determinants

> Theory: [../../theory/maths/matrices-determinants.md](../../theory/maths/matrices-determinants.md)

### M-MAT-01 — JEE Main 2024 · 27 Jan Shift 1 · Q72 · MCQ

Consider $f(x)=\begin{pmatrix}\cos x&-\sin x&0\\\sin x&\cos x&0\\0&0&1\end{pmatrix}$.
Statement I: $f(-x)$ is the inverse of $f(x)$.
Statement II: $f(x)f(y)=f(x+y)$.

(1) I false, II true  (2) Both false  (3) I true, II false  (4) Both true

**Answer: (4)** · key ✔

**Solution.** $f(x)$ is a rotation about the $z$-axis. Multiplying gives $f(x)f(y)=f(x+y)$ (angle addition), so II is true. Taking $y=-x$: $f(x)f(-x)=f(0)=I$, so I is true.

### M-MAT-02 — JEE Main 2024 · 27 Jan Shift 1 · Q84 · Numerical

Let $A=\begin{pmatrix}2&0&1\\1&1&0\\1&0&1\end{pmatrix}$ and $B=[B_1\ B_2\ B_3]$ where $B_1,B_2,B_3$ are column matrices with $AB_1=\begin{pmatrix}1\\0\\0\end{pmatrix}$, $AB_2=\begin{pmatrix}2\\3\\0\end{pmatrix}$, $AB_3=\begin{pmatrix}3\\2\\1\end{pmatrix}$. If $\alpha=|B|$ and $\beta$ is the sum of the diagonal elements of $B$, then $\alpha^3+\beta^3$ is ______.

**Answer: 28** · key ✔

**Solution.** $AB=\begin{pmatrix}1&2&3\\0&3&2\\0&0&1\end{pmatrix}$ has determinant $3$, and $|A|=2(1)-0+1(0-1)=1$, so $\alpha=|B|=3$. Also $\operatorname{adj}A=\begin{pmatrix}1&0&-1\\-1&1&1\\-1&0&2\end{pmatrix}=A^{-1}$, giving $B=A^{-1}(AB)=\begin{pmatrix}1&2&2\\-1&1&0\\-1&-2&-1\end{pmatrix}$ with trace $\beta=1$. Hence $\alpha^3+\beta^3=27+1=28$.

### M-MAT-03 — JEE Main 2024 · 27 Jan Shift 2 · Q86 · Numerical

Let $A$ be a $2\times2$ real matrix and $I$ the identity matrix of order $2$. If the roots of $|A-xI|=0$ are $-1$ and $3$, then the sum of the diagonal elements of $A^2$ is ______.

**Answer: 10** · key ✔

**Solution.** The roots of $|A-xI|=0$ are the eigenvalues $\lambda_1=-1,\lambda_2=3$. $A^2$ has eigenvalues $\lambda_i^2$, so $\text{tr}(A^2)=1+9=10$.

### M-MAT-04 — JEE Main 2024 · 29 Jan Shift 1 · Q69 · MCQ

Let $A=\begin{pmatrix}1&0&0\\0&\alpha&\beta\\0&\beta&\alpha\end{pmatrix}$ and $|2A|^3=2^{21}$, where $\alpha,\beta\in\mathbb Z$. A value of $\alpha$ is

(1) 3  (2) 5  (3) 17  (4) 9

**Answer: (2)** · key ✔

**Solution.** $|2A|=2^3|A|$, so $2^9|A|^3=2^{21}\Rightarrow|A|^3=2^{12}\Rightarrow|A|=16$. $|A|=\alpha^2-\beta^2=16\Rightarrow(\alpha-\beta)(\alpha+\beta)=16$. Integer solutions include $\alpha=5,\beta=3$ ($25-9=16$). $\alpha=3,9,17$ would need $\beta^2=-7,65,273$, none a perfect square.

### M-MAT-05 — JEE Main 2024 · 29 Jan Shift 2 · Q70 · MCQ

Let $A=\begin{pmatrix}2&1&2\\6&2&11\\3&3&2\end{pmatrix}$ and $P=\begin{pmatrix}1&2&0\\5&0&2\\7&1&5\end{pmatrix}$. The sum of the prime factors of $\left|P^{-1}AP-2I\right|$ is

(1) 26  (2) 27  (3) 66  (4) 23

**Answer: (1)** · key ✔

**Solution.** $P^{-1}AP-2I=P^{-1}(A-2I)P$, so its determinant equals $|A-2I|$. $A-2I=\begin{pmatrix}0&1&2\\6&0&11\\3&3&0\end{pmatrix}$, with determinant $0-1(0-33)+2(18-0)=33+36=69=3\times23$. Sum of prime factors $=3+23=26$.

### M-MAT-06 — JEE Main 2024 · 29 Jan Shift 2 · Q86 · Numerical

For any three distinct consecutive terms $a,b,c$ of an A.P., the lines $ax+by+c=0$ are concurrent at the point $P$. Let $Q(\alpha,\beta)$ be a point such that the system $x+y+z=6$, $2x+5y+\alpha z=\beta$, $x+2y+3z=4$ has infinitely many solutions. Then $(PQ)^2$ is equal to ______.

**Answer: 113** · key ✔

**Solution.** $2b=a+c\Rightarrow a-2b+c=0$, so every such line passes through $P(1,-2)$. For infinitely many solutions: $\begin{vmatrix}1&1&1\\2&5&\alpha\\1&2&3\end{vmatrix}=8-\alpha=0\Rightarrow\alpha=8$. Subtracting the third equation from the first: $y+2z=-2$ (i). Eliminating $x$ from the second (with $\alpha=8$) using twice the first: $3y+6z=\beta-12$, i.e. $3(y+2z)=\beta-12\Rightarrow-6=\beta-12\Rightarrow\beta=6$. So $Q(8,6)$ and $(PQ)^2=7^2+8^2=113$.

### M-MAT-07 — JEE Main 2024 · 30 Jan Shift 1 · Q70 · MCQ

If $f(x)=\begin{vmatrix}2\cos^4x&2\sin^4x&3+\sin^22x\\3+2\cos^4x&2\sin^4x&\sin^22x\\2\cos^4x&3+2\sin^4x&\sin^22x\end{vmatrix}$, then $\dfrac15f'(0)$ is equal to

(1) 0  (2) 1  (3) 2  (4) 6

**Answer: (1)** · key ✔

**Solution.** Apply $R_2\to R_2-R_1$ and $R_3\to R_3-R_1$: rows become $(3,0,-3)$ and $(0,3,-3)$. Expanding along the top row: $f(x)=2\cos^4x(9)-2\sin^4x(-9)+(3+\sin^22x)(9)=18(\cos^4x+\sin^4x)+27+9\sin^22x$. Since $\cos^4x+\sin^4x=1-\tfrac12\sin^22x$: $f(x)=18-9\sin^22x+27+9\sin^22x=45$. A constant, so $f'(0)=0$.

### M-MAT-08 — JEE Main 2024 · 30 Jan Shift 2 · Q69 · MCQ

Consider the system of linear equations $x+y+z=5$, $x+2y+\lambda^2z=9$, $x+3y+\lambda z=\mu$, where $\lambda,\mu\in\mathbb R$. Which of the following statements is **not** correct?

(1) The system has infinitely many solutions if $\lambda=1$ and $\mu=13$  (2) The system is inconsistent if $\lambda=1$ and $\mu\ne13$  (3) The system has a unique solution if $\lambda\ne1$ and $\mu\ne13$  (4) The system is consistent if $\lambda\ne1$ and $\mu=13$

**Answer: (3)** · key ✔

**Solution.** The coefficient determinant is $\begin{vmatrix}1&1&1\\1&2&\lambda^2\\1&3&\lambda\end{vmatrix}=-(2\lambda+1)(\lambda-1)$, which vanishes at $\lambda=1$ and $\lambda=-\tfrac12$. So a unique solution exists exactly when $\lambda\ne1$ and $\lambda\ne-\tfrac12$ (for any $\mu$); (3) omits the case $\lambda=-\tfrac12$ and is wrong. For $\lambda=1$: the first two equations give $y=4,\ x+z=1$, so the third requires $\mu=13$: (1) and (2) are right. (4) holds too (e.g. at $\lambda=-\tfrac12,\mu=13$ the equations are consistent).

### M-MAT-09 — JEE Main 2024 · 31 Jan Shift 1 · Q69 · MCQ

If $f(x)=\begin{vmatrix}x^3&2x^2+1&1+3x\\3x^2+2&2x&x^3+6\\x^3-x&4&x^2-2\end{vmatrix}$ for all $x\in\mathbb R$, then $2f(0)+f'(0)$ is equal to

(1) 48  (2) 24  (3) 42  (4) 18

**Answer: (3)** · key ✔

**Solution.** $f(0)=\begin{vmatrix}0&1&1\\2&0&6\\0&4&-2\end{vmatrix}=-1(-4-0)+1(8-0)=12$. Differentiating row by row and setting $x=0$ (derivative rows $(0,0,3)$, $(0,2,0)$, $(-1,0,0)$): the three determinants are $24$, $0$ and $-6$. So $f'(0)=18$ and $2f(0)+f'(0)=24+18=42$.

### M-MAT-10 — JEE Main 2024 · 31 Jan Shift 2 · Q86 · Numerical

Let $A$ be a $3\times3$ matrix with $\det A=2$. If $n=\det\!\big(\underbrace{\text{adj}(\text{adj}(\cdots\text{adj}(A)))}_{2024\text{ times}}\big)$, then the remainder when $n$ is divided by $9$ is equal to ______.

**Answer: 7** · key ✔

**Solution.** For a $3\times3$ matrix $\det(\text{adj}M)=(\det M)^2$. Each application squares the determinant, so after $k$ applications $\det=2^{2^k}$; here $n=2^{2^{2024}}$. Modulo $9$ the powers of $2$ cycle with period $6$, and $2^{2024}\equiv4\pmod6$ (since $2^k\equiv4\pmod6$ for even $k\ge2$). So $n\equiv2^4=16\equiv7\pmod9$.

### M-MAT-11 — JEE Main 2024 · 1 Feb Shift 1 · Q70 · MCQ

If $A=\begin{pmatrix}\sqrt2&1\\-1&\sqrt2\end{pmatrix}$, $B=\begin{pmatrix}1&0\\1&1\end{pmatrix}$, $C=ABA^T$ and $X=A^TC^2A$, then $\det X$ is equal to:

(1) 243  (2) 729  (3) 27  (4) 891

**Answer: (2)** · key ✔

**Solution.** $\det A=2+1=3$, $\det B=1$, so $\det C=3\cdot1\cdot3=9$. Then $\det X=\det(A^T)\,(\det C)^2\det A=3\cdot81\cdot3=729$.

### M-MAT-12 — JEE Advanced 2025 · Paper 1 · Q4 · MCQ

Let $P=\begin{pmatrix}2&0&0\\0&2&0\\0&0&3\end{pmatrix}$. The number of $3\times3$ invertible matrices $Q$ with integer entries such that $Q^{-1}=Q^T$ and $PQ=QP$ is

(A) 32  (B) 8  (C) 16  (D) 24

**Answer: (C)** · official key ✔ (re-derived)

**Solution.** An integer matrix with $Q^TQ=I$ has orthonormal integer columns, so each column is $\pm e_i$: $Q$ is a signed permutation matrix. $PQ=QP$ means $Q$ preserves the eigenspaces of $P$ ($\text{span}\{e_1,e_2\}$ for $2$ and $\text{span}\{e_3\}$ for $3$), so $Q=\text{diag}(B,\pm1)$ with $B$ a $2\times2$ signed permutation matrix. There are $2!\cdot2^2=8$ such $B$ and $2$ signs for the last entry: $8\times2=16$.

### § — JEE Main 2026 · 21 Jan Shift 2 · Matrices set Q1 · MCQ

For the matrices $A=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}$ and $B=\begin{bmatrix}-29&49\\-13&18\end{bmatrix}$, if $(A^{15}+B)\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}$, then among the following which one is true?

(1) $x=5,\ y=7$  (2) $x=18,\ y=11$  (3) $x=11,\ y=2$  (4) $x=16,\ y=3$

**Answer: (3)** · key (compiled)

**Solution.** $\operatorname{tr}A=2$, $\det A=1$, so $(A-I)^2=0$. With $N=A-I=\begin{bmatrix}2&-4\\1&-2\end{bmatrix}$, $N^2=0$ and $A^n=I+nN=\begin{bmatrix}2n+1&-4n\\n&1-2n\end{bmatrix}$. $A^{15}=\begin{bmatrix}31&-60\\15&-29\end{bmatrix}$ and $A^{15}+B=\begin{bmatrix}2&-11\\2&-11\end{bmatrix}$. The system reduces to $2x-11y=0$, i.e. $x=\tfrac{11y}2$: $y=2$, $x=11$.

### § — JEE Main 2026 · 23 Jan Shift 1 · Matrices set Q2 · Numerical

Let $|A|=6$, where $A$ is a $3\times3$ matrix. If $\left|\operatorname{adj}\big(3\operatorname{adj}(A^2\cdot\operatorname{adj}(2A))\big)\right|=2^m\cdot3^n$, $m,n\in\mathbb N$, then $m+n$ is equal to ______.

**Answer: 62** · key (compiled)

**Solution.** For a $3\times3$ matrix $M$: $|\operatorname{adj}M|=|M|^2$ and $|kM|=k^3|M|$. $|2A|=8\cdot6=48$, so $|\operatorname{adj}(2A)|=48^2$. Let $P=A^2\operatorname{adj}(2A)$: $|P|=36\cdot48^2=2^{10}\cdot3^4$. $|3\operatorname{adj}P|=27|P|^2$, and $|\operatorname{adj}(3\operatorname{adj}P)|=|3\operatorname{adj}P|^2=3^6|P|^4=3^6\cdot2^{40}\cdot3^{16}=2^{40}\cdot3^{22}$. $m+n=62$.

### § — JEE Main 2026 · 28 Jan Shift 2 · Matrices set Q3 · Numerical

Let $A=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}$ and $B$ be two matrices such that $A^{100}=100B+I$. Then the sum of all the elements of $B^{100}$ is ______.

**Answer: 0** · key (compiled)

**Solution.** With $N=A-I$, $N^2=0$ and $A^{100}=I+100N$. So $100B+I=I+100N$ gives $B=N$, and $B^{100}=N^{100}=0$. The sum of all elements is $0$.

### § — JEE Main 2026 · 24 Jan Shift 2 · Matrices set Q4 · MCQ

Let $f(x)=\int\dfrac{7x^{10}+9x^8}{(1+x^2+2x^9)^2}dx$, $x>0$, $\lim_{x\to0}f(x)=0$ and $f(1)=\dfrac14$. If $A=\begin{bmatrix}0&0&1\\\tfrac14&f'(1)&1\\\alpha^2&4&1\end{bmatrix}$ and $B=\operatorname{adj}(\operatorname{adj}A)$ be such that $|B|=81$, then $\alpha^2$ is equal to:

(1) 2  (2) 1  (3) 3  (4) 4

**Answer: (4)** · key (compiled)

**Solution.** Divide numerator and denominator by $x^{18}$ and put $t=x^{-9}+x^{-7}+2$, $dt=-(9x^{-10}+7x^{-8})dx$: $f(x)=\dfrac1t+C=\dfrac{x^9}{1+x^2+2x^9}+C$; $\lim_{x\to0}f=0$ gives $C=0$ (and $f(1)=\tfrac14$ ✓). $f'(x)=\dfrac{9x^8(1+x^2+2x^9)-x^9(2x+18x^8)}{(1+x^2+2x^9)^2}$, so $f'(1)=\dfrac{36-20}{16}=1$. Expanding along the first row, $|A|=1\cdot\left(\tfrac14\cdot4-1\cdot\alpha^2\right)=1-\alpha^2$. For $3\times3$, $|\operatorname{adj}(\operatorname{adj}A)|=|A|^{(n-1)^2}=|A|^4=81\Rightarrow|A|=\pm3$, so $1-\alpha^2=-3$ (the value $+3$ would give $\alpha^2=-2$): $\alpha^2=4$.

### § — JEE Main 2026 · 24 Jan Shift 2 · Matrices set Q5 · MCQ

Let $P=[p_{ij}]$ and $Q=[q_{ij}]$ be two square matrices of order 3 such that $q_{ij}=2^{(i+j-1)}p_{ij}$ and $\det(Q)=2^{10}$. Then the value of $\det(\operatorname{adj}(\operatorname{adj}P))$ is:

(1) 81  (2) 16  (3) 124  (4) 32

**Answer: (2)** · key (compiled)

**Solution.** $q_{ij}=2^i\cdot2^{j-1}p_{ij}$, so $Q=\operatorname{diag}(2,4,8)\,P\,\operatorname{diag}(1,2,4)$ and $\det Q=(2\cdot4\cdot8)(1\cdot2\cdot4)\det P=512\det P=2^{10}\Rightarrow\det P=2$. For order 3, $\det(\operatorname{adj}(\operatorname{adj}P))=(\det P)^{(3-1)^2}=2^4=16$.

### § — JEE Main 2026 · 22 Jan Shift 2 · Matrices set Q6 · MCQ

If $X=\begin{bmatrix}x\\y\\z\end{bmatrix}$ is a solution of the system of equations $AX=B$, where $\operatorname{adj}A=\begin{bmatrix}4&2&2\\-5&0&5\\1&-2&3\end{bmatrix}$ and $B=\begin{bmatrix}4\\0\\2\end{bmatrix}$, then $|x+y+z|$ is equal to:

(1) 2  (2) $\dfrac32$  (3) 1  (4) 3

**Answer: (1)** · key (compiled)

**Solution.** $|\operatorname{adj}A|=4(0+10)-2(-15-5)+2(10-0)=100=|A|^2$, so $|A|=\pm10$. $X=A^{-1}B=\dfrac{(\operatorname{adj}A)B}{|A|}$ and $(\operatorname{adj}A)B=\begin{bmatrix}16+4\\-20+10\\4+6\end{bmatrix}=\begin{bmatrix}20\\-10\\10\end{bmatrix}$. So $x+y+z=\dfrac{20}{|A|}$ and $|x+y+z|=\dfrac{20}{10}=2$.

### § — JEE Main 2026 · 22 Jan Shift 1 · Matrices set Q7 · MCQ

If $A=\begin{bmatrix}2&3\\3&5\end{bmatrix}$, then the determinant of the matrix $(A^{2025}-3A^{2024}+A^{2023})$ is:

(1) 12  (2) 28  (3) 24  (4) 16

**Answer: (4)** · key (compiled)

**Solution.** $A^{2025}-3A^{2024}+A^{2023}=A^{2023}(A^2-3A+I)$ and $|A|=1$. $A^2=\begin{bmatrix}13&21\\21&34\end{bmatrix}$, so $A^2-3A+I=\begin{bmatrix}8&12\\12&20\end{bmatrix}$ with determinant $160-144=16$. The required determinant is $|A|^{2023}\cdot16=16$.

### § — JEE Main 2026 · 22 Jan Shift 1 · Matrices set Q8 · Numerical

Let $A$ be a $3\times3$ matrix such that $A+A^T=O$. If $A\begin{bmatrix}1\\-1\\0\end{bmatrix}=\begin{bmatrix}3\\3\\2\end{bmatrix}$, $A^2\begin{bmatrix}1\\-1\\0\end{bmatrix}=\begin{bmatrix}-3\\19\\-24\end{bmatrix}$ and $\det(\operatorname{adj}(2\operatorname{adj}(A+I)))=(2)^\alpha\cdot(3)^\beta\cdot(11)^\gamma$, where $\alpha,\beta,\gamma$ are non-negative integers, then $\alpha+\beta+\gamma$ is equal to ______.

**Answer: 18** · key (compiled)

**Solution.** Let $A=\begin{bmatrix}0&p&q\\-p&0&r\\-q&-r&0\end{bmatrix}$. $A(1,-1,0)^T=(-p,-p,r-q)^T=(3,3,2)^T$ gives $p=-3$, $r-q=2$. $A(3,3,2)^T=(3p+2q,\,-3p+2r,\,-3q-3r)^T=(-3,19,-24)^T$ gives $q=3$, $r=5$. For a $3\times3$ skew-symmetric $A$, $\det(I+A)=1+p^2+q^2+r^2=1+9+9+25=44=2^2\cdot11$. With $M=A+I$: $\det(\operatorname{adj}(2\operatorname{adj}M))=\det(2\operatorname{adj}M)^2=\left(8\cdot44^2\right)^2=2^6\cdot44^4=2^{14}\cdot11^4$. So $\alpha=14$, $\beta=0$, $\gamma=4$ and the sum is 18.

### § — JEE Main 2026 · 23 Jan Shift 2 · Matrices set Q9 · Numerical

Let $A=\begin{bmatrix}0&2&-3\\-2&0&1\\3&-1&0\end{bmatrix}$ and $B$ be a matrix such that $B(I-A)=I+A$. Then the sum of the diagonal elements of $B^TB$ is equal to ______.

**Answer: 3** · key (compiled)

**Solution.** $A^T=-A$. $B=(I+A)(I-A)^{-1}$, so $B^T=\left((I-A)^{-1}\right)^T(I+A)^T=(I+A)^{-1}(I-A)$. Since $I+A$ and $I-A$ commute, $B^TB=(I+A)^{-1}(I-A)(I+A)(I-A)^{-1}=(I+A)^{-1}(I+A)(I-A)(I-A)^{-1}=I$. The trace of $I_3$ is 3.

### § — JEE Main 2026 · 21 Jan Shift 1 · Matrices set Q10 · Numerical

For some $\alpha,\beta\in\mathbb R$, let $A=\begin{bmatrix}\alpha&2\\1&2\end{bmatrix}$ and $B=\begin{bmatrix}1&1\\1&\beta\end{bmatrix}$ be such that $A^2-4A+2I=B^2-3B+I=O$. Then $\left(\det\left(\operatorname{adj}\left(A^3-B^3\right)\right)\right)^2$ is equal to ______.

**Answer: 225** · key (compiled)

**Solution.** By Cayley–Hamilton $A^2-(\alpha+2)A+(2\alpha-2)I=O$; comparing with $A^2-4A+2I=O$ gives $\alpha=2$. Similarly $B^2-(1+\beta)B+(\beta-1)I=O$ gives $\beta=2$. $A^2=\begin{bmatrix}6&8\\4&6\end{bmatrix}$, $A^3=\begin{bmatrix}20&28\\14&20\end{bmatrix}$; $B^2=\begin{bmatrix}2&3\\3&5\end{bmatrix}$, $B^3=\begin{bmatrix}5&8\\8&13\end{bmatrix}$. $A^3-B^3=\begin{bmatrix}15&20\\6&7\end{bmatrix}$ with $\det=105-120=-15$. For a $2\times2$ matrix $\det(\operatorname{adj}M)=\det M$, so the answer is $(-15)^2=225$.

### § — JEE Main 2026 · 28 Jan Shift 1 · Matrices set Q11 · MCQ

Let $A,B$ and $C$ be three $2\times2$ matrices with real entries such that $B=(I+A)^{-1}$ and $A+C=I$. If $BC=\begin{bmatrix}1&-5\\-1&2\end{bmatrix}$ and $CB\begin{bmatrix}x_1\\x_2\end{bmatrix}=\begin{bmatrix}12\\-6\end{bmatrix}$, then $x_1+x_2$ is:

(1) 2  (2) $-2$  (3) 0  (4) 4

**Answer: (3)** · key (compiled)

**Solution.** $B(I+A)=I=(I+A)B$ gives $B+BA=I=B+AB$, so $A$ and $B$ commute and $BA=AB=I-B$. With $C=I-A$: $BC=B-BA=2B-I$ and $CB=B-AB=2B-I$. So $CB=BC=\begin{bmatrix}1&-5\\-1&2\end{bmatrix}$. Then $x_1-5x_2=12$ and $-x_1+2x_2=-6$; adding gives $-3x_2=6$, $x_2=-2$, $x_1=2$. $x_1+x_2=0$.

### § — JEE Main 2026 · 24 Jan Shift 1 · Matrices set Q12 · Numerical

The number of $3\times2$ matrices $A$, which can be formed using the elements of the set $\{-2,-1,0,1,2\}$ such that the sum of all the diagonal elements of $A^TA$ is 5, is ______.

**Answer: 312** · key (compiled)

**Solution.** $\operatorname{tr}(A^TA)=\sum a_{ij}^2=5$ over the six entries. The squares are $0,1,4$ (with $\pm1$ and $\pm2$ each having 2 choices). Either one entry is $\pm2$ and one is $\pm1$ (rest 0): $6\cdot5\cdot2\cdot2=120$; or five entries are $\pm1$ and one is 0: $6\cdot2^5=192$. Total $=120+192=312$.

### § — JEE Main 2026 · 21 Jan Shift 2 · Determinants set Q1 · MCQ

If the system of equations $3x+y+4z=3$, $2x+\alpha y-z=-3$, $x+2y+z=4$ has no solution, then the value of $\alpha$ is equal to:

(1) 19  (2) 4  (3) 13  (4) 23

**Answer: (1)** · key (compiled)

**Solution.** No solution requires $\Delta=0$: $\Delta=3(\alpha+2)-1(2+1)+4(4-\alpha)=19-\alpha=0\Rightarrow\alpha=19$. For $\alpha=19$, $\Delta_x=\begin{vmatrix}3&1&4\\-3&19&-1\\4&2&1\end{vmatrix}=3(21)+1(-1)+4(-82)=-266\ne0$, so the system is inconsistent (no solution), not dependent.

### § — JEE Main 2026 · 23 Jan Shift 1 · Determinants set Q2 · MCQ

Among the statements: I: If $\begin{vmatrix}1&\cos\alpha&\cos\beta\\\cos\alpha&1&\cos\gamma\\\cos\beta&\cos\gamma&1\end{vmatrix}=\begin{vmatrix}0&\cos\alpha&\cos\beta\\\cos\alpha&0&\cos\gamma\\\cos\beta&\cos\gamma&0\end{vmatrix}$, then $\cos^2\alpha+\cos^2\beta+\cos^2\gamma=\dfrac32$, and II: If $\begin{vmatrix}x^2+x&x+1&x-2\\2x^2+3x-1&3x&3x-3\\x^2+2x+3&2x-1&2x-1\end{vmatrix}=px+q$, then $p^2=196q^2$:

(1) only II is true  (2) both are false  (3) both are true  (4) only I is true

**Answer: (2)** · key (compiled)

**Solution.** I: the left determinant is $1-\sum\cos^2+2\cos\alpha\cos\beta\cos\gamma$ and the right is $2\cos\alpha\cos\beta\cos\gamma$; equality gives $\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1$, not $\tfrac32$, so I is false. II: $R_2\to R_2-2R_1$ gives $(x-1,\,x-2,\,x+1)$ and $R_3\to R_3-R_1$ gives $(x+3,\,x-2,\,x+1)$; then $R_3-R_2=(4,0,0)$. Expanding along that row: $4\begin{vmatrix}x+1&x-2\\x-2&x+1\end{vmatrix}=4\big[(x+1)^2-(x-2)^2\big]=4(6x-3)=24x-12$. So $p=24$, $q=-12$ and $p^2=576=4q^2\ne196q^2$: II is false. Both are false.

### § — JEE Main 2026 · 22 Jan Shift 2 · Determinants set Q3 · MCQ

Let $n$ be the number obtained on rolling a fair die. If the probability that the system $x-ny+z=6$, $x+(n-2)y+(n+1)z=8$, $(n-1)y+z=1$ has a unique solution is $\dfrac k6$, then the sum of $k$ and all possible values of $n$ is:

(1) 20  (2) 24  (3) 21  (4) 22

**Answer: (4)** · key (compiled)

**Solution.** $\det\begin{bmatrix}1&-n&1\\1&n-2&n+1\\0&n-1&1\end{bmatrix}=(n-2)-(n^2-1)+n+(n-1)=-(n-1)(n-2)$. A unique solution needs $n\ne1,2$, i.e. $n\in\{3,4,5,6\}$: probability $\tfrac46$, so $k=4$. Sum $=4+(3+4+5+6)=22$.

### § — JEE Main 2026 · 23 Jan Shift 2 · Determinants set Q4 · MCQ

The system of linear equations $x+y+z=6$, $2x+5y+az=36$, $x+2y+3z=b$ has:

(1) a unique solution for $a=8$ and $b=16$  (2) infinitely many solutions for $a=8$ and $b=16$  (3) a unique solution for $a=8$ and $b=14$  (4) infinitely many solutions for $a=8$ and $b=14$

**Answer: (4)** · key (compiled)

**Solution.** $\Delta=\begin{vmatrix}1&1&1\\2&5&a\\1&2&3\end{vmatrix}=(15-2a)-(6-a)+(4-5)=8-a$. For $a=8$, $\Delta=0$, so a unique solution is impossible. Then $R_2-2R_1$: $3y+6z=24\Rightarrow y+2z=8$, and $R_3-R_1$: $y+2z=b-6$. The equations are consistent (infinitely many solutions) iff $b-6=8$, i.e. $b=14$; for $b\ne14$ there is no solution.

