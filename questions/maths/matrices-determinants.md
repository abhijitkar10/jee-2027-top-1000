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

### M-MAT-05 — JEE Main 2024 · 29 Jan Shift 1 · Q70 · MCQ

Let $A$ be a square matrix with $AA^T=I$. Then $\dfrac12A\left[(A+A^T)^2+(A-A^T)^2\right]$ is equal to

(1) $A^2+I$  (2) $A^3+I$  (3) $A^2+A^T$  (4) $A^3+A^T$

**Answer: (4)** · key ✔

**Solution.** $(A+A^T)^2+(A-A^T)^2=2A^2+2(A^T)^2$. So the expression is $A\left[A^2+(A^T)^2\right]=A^3+(AA^T)A^T=A^3+A^T$.

### M-MAT-06 — JEE Main 2024 · 29 Jan Shift 2 · Q70 · MCQ

Let $A=\begin{pmatrix}2&1&2\\6&2&11\\3&3&2\end{pmatrix}$ and $P=\begin{pmatrix}1&2&0\\5&0&2\\7&1&5\end{pmatrix}$. The sum of the prime factors of $\left|P^{-1}AP-2I\right|$ is

(1) 26  (2) 27  (3) 66  (4) 23

**Answer: (1)** · key ✔

**Solution.** $P^{-1}AP-2I=P^{-1}(A-2I)P$, so its determinant equals $|A-2I|$. $A-2I=\begin{pmatrix}0&1&2\\6&0&11\\3&3&0\end{pmatrix}$, with determinant $0-1(0-33)+2(18-0)=33+36=69=3\times23$. Sum of prime factors $=3+23=26$.

### M-MAT-07 — JEE Main 2024 · 29 Jan Shift 2 · Q86 · Numerical

For any three distinct consecutive terms $a,b,c$ of an A.P., the lines $ax+by+c=0$ are concurrent at the point $P$. Let $Q(\alpha,\beta)$ be a point such that the system $x+y+z=6$, $2x+5y+\alpha z=\beta$, $x+2y+3z=4$ has infinitely many solutions. Then $(PQ)^2$ is equal to ______.

**Answer: 113** · key ✔

**Solution.** $2b=a+c\Rightarrow a-2b+c=0$, so every such line passes through $P(1,-2)$. For infinitely many solutions: $\begin{vmatrix}1&1&1\\2&5&\alpha\\1&2&3\end{vmatrix}=8-\alpha=0\Rightarrow\alpha=8$. Subtracting the third equation from the first: $y+2z=-2$ (i). Eliminating $x$ from the second (with $\alpha=8$) using twice the first: $3y+6z=\beta-12$, i.e. $3(y+2z)=\beta-12\Rightarrow-6=\beta-12\Rightarrow\beta=6$. So $Q(8,6)$ and $(PQ)^2=7^2+8^2=113$.

### M-MAT-08 — JEE Main 2024 · 30 Jan Shift 1 · Q70 · MCQ

If $f(x)=\begin{vmatrix}2\cos^4x&2\sin^4x&3+\sin^22x\\3+2\cos^4x&2\sin^4x&\sin^22x\\2\cos^4x&3+2\sin^4x&\sin^22x\end{vmatrix}$, then $\dfrac15f'(0)$ is equal to

(1) 0  (2) 1  (3) 2  (4) 6

**Answer: (1)** · key ✔

**Solution.** Apply $R_2\to R_2-R_1$ and $R_3\to R_3-R_1$: rows become $(3,0,-3)$ and $(0,3,-3)$. Expanding along the top row: $f(x)=2\cos^4x(9)-2\sin^4x(-9)+(3+\sin^22x)(9)=18(\cos^4x+\sin^4x)+27+9\sin^22x$. Since $\cos^4x+\sin^4x=1-\tfrac12\sin^22x$: $f(x)=18-9\sin^22x+27+9\sin^22x=45$. A constant, so $f'(0)=0$.

### M-MAT-09 — JEE Main 2024 · 30 Jan Shift 2 · Q69 · MCQ

Consider the system of linear equations $x+y+z=5$, $x+2y+\lambda^2z=9$, $x+3y+\lambda z=\mu$, where $\lambda,\mu\in\mathbb R$. Which of the following statements is **not** correct?

(1) The system has infinitely many solutions if $\lambda=1$ and $\mu=13$  (2) The system is inconsistent if $\lambda=1$ and $\mu\ne13$  (3) The system has a unique solution if $\lambda\ne1$ and $\mu\ne13$  (4) The system is consistent if $\lambda\ne1$ and $\mu=13$

**Answer: (3)** · key ✔

**Solution.** The coefficient determinant is $\begin{vmatrix}1&1&1\\1&2&\lambda^2\\1&3&\lambda\end{vmatrix}=-(2\lambda+1)(\lambda-1)$, which vanishes at $\lambda=1$ and $\lambda=-\tfrac12$. So a unique solution exists exactly when $\lambda\ne1$ and $\lambda\ne-\tfrac12$ (for any $\mu$); (3) omits the case $\lambda=-\tfrac12$ and is wrong. For $\lambda=1$: the first two equations give $y=4,\ x+z=1$, so the third requires $\mu=13$: (1) and (2) are right. (4) holds too (e.g. at $\lambda=-\tfrac12,\mu=13$ the equations are consistent).

### M-MAT-10 — JEE Main 2024 · 31 Jan Shift 1 · Q69 · MCQ

If $f(x)=\begin{vmatrix}x^3&2x^2+1&1+3x\\3x^2+2&2x&x^3+6\\x^3-x&4&x^2-2\end{vmatrix}$ for all $x\in\mathbb R$, then $2f(0)+f'(0)$ is equal to

(1) 48  (2) 24  (3) 42  (4) 18

**Answer: (3)** · key ✔

**Solution.** $f(0)=\begin{vmatrix}0&1&1\\2&0&6\\0&4&-2\end{vmatrix}=-1(-4-0)+1(8-0)=12$. Differentiating row by row and setting $x=0$ (derivative rows $(0,0,3)$, $(0,2,0)$, $(-1,0,0)$): the three determinants are $24$, $0$ and $-6$. So $f'(0)=18$ and $2f(0)+f'(0)=24+18=42$.

### M-MAT-11 — JEE Main 2024 · 31 Jan Shift 2 · Q86 · Numerical

Let $A$ be a $3\times3$ matrix with $\det A=2$. If $n=\det\!\big(\underbrace{\text{adj}(\text{adj}(\cdots\text{adj}(A)))}_{2024\text{ times}}\big)$, then the remainder when $n$ is divided by $9$ is equal to ______.

**Answer: 7** · key ✔

**Solution.** For a $3\times3$ matrix $\det(\text{adj}M)=(\det M)^2$. Each application squares the determinant, so after $k$ applications $\det=2^{2^k}$; here $n=2^{2^{2024}}$. Modulo $9$ the powers of $2$ cycle with period $6$, and $2^{2024}\equiv4\pmod6$ (since $2^k\equiv4\pmod6$ for even $k\ge2$). So $n\equiv2^4=16\equiv7\pmod9$.

