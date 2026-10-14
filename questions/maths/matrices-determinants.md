# Matrices & Determinants

> Theory: [../../theory/maths/matrices-determinants.md](../../theory/maths/matrices-determinants.md)

### M-MAT-01 · A — JEE Main 2026 · 21 Jan Shift 2 · Matrices set Q1 · MCQ

For the matrices $A=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}$ and $B=\begin{bmatrix}-29&49\\-13&18\end{bmatrix}$, if $(A^{15}+B)\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}$, then among the following which one is true?

(1) $x=5,\ y=7$  (2) $x=18,\ y=11$  (3) $x=11,\ y=2$  (4) $x=16,\ y=3$

**Answer: (3)** · key (compiled)

**Solution.** $\operatorname{tr}A=2$, $\det A=1$, so $(A-I)^2=0$. With $N=A-I=\begin{bmatrix}2&-4\\1&-2\end{bmatrix}$, $N^2=0$ and $A^n=I+nN=\begin{bmatrix}2n+1&-4n\\n&1-2n\end{bmatrix}$. $A^{15}=\begin{bmatrix}31&-60\\15&-29\end{bmatrix}$ and $A^{15}+B=\begin{bmatrix}2&-11\\2&-11\end{bmatrix}$. The system reduces to $2x-11y=0$, i.e. $x=\tfrac{11y}2$: $y=2$, $x=11$.

### M-MAT-02 · A — JEE Main 2026 · 23 Jan Shift 1 · Matrices set Q2 · Numerical

Let $|A|=6$, where $A$ is a $3\times3$ matrix. If $\left|\operatorname{adj}\big(3\operatorname{adj}(A^2\cdot\operatorname{adj}(2A))\big)\right|=2^m\cdot3^n$, $m,n\in\mathbb N$, then $m+n$ is equal to ______.

**Answer: 62** · key (compiled)

**Solution.** For a $3\times3$ matrix $M$: $|\operatorname{adj}M|=|M|^2$ and $|kM|=k^3|M|$. $|2A|=8\cdot6=48$, so $|\operatorname{adj}(2A)|=48^2$. Let $P=A^2\operatorname{adj}(2A)$: $|P|=36\cdot48^2=2^{10}\cdot3^4$. $|3\operatorname{adj}P|=27|P|^2$, and $|\operatorname{adj}(3\operatorname{adj}P)|=|3\operatorname{adj}P|^2=3^6|P|^4=3^6\cdot2^{40}\cdot3^{16}=2^{40}\cdot3^{22}$. $m+n=62$.

### M-MAT-03 · A — JEE Main 2026 · 28 Jan Shift 2 · Matrices set Q3 · Numerical

Let $A=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}$ and $B$ be two matrices such that $A^{100}=100B+I$. Then the sum of all the elements of $B^{100}$ is ______.

**Answer: 0** · key (compiled)

**Solution.** With $N=A-I$, $N^2=0$ and $A^{100}=I+100N$. So $100B+I=I+100N$ gives $B=N$, and $B^{100}=N^{100}=0$. The sum of all elements is $0$.

### M-MAT-04 · A — JEE Main 2026 · 24 Jan Shift 2 · Matrices set Q4 · MCQ

Let $f(x)=\int\dfrac{7x^{10}+9x^8}{(1+x^2+2x^9)^2}dx$, $x>0$, $\lim_{x\to0}f(x)=0$ and $f(1)=\dfrac14$. If $A=\begin{bmatrix}0&0&1\\\tfrac14&f'(1)&1\\\alpha^2&4&1\end{bmatrix}$ and $B=\operatorname{adj}(\operatorname{adj}A)$ be such that $|B|=81$, then $\alpha^2$ is equal to:

(1) 2  (2) 1  (3) 3  (4) 4

**Answer: (4)** · key (compiled)

**Solution.** Divide numerator and denominator by $x^{18}$ and put $t=x^{-9}+x^{-7}+2$, $dt=-(9x^{-10}+7x^{-8})dx$: $f(x)=\dfrac1t+C=\dfrac{x^9}{1+x^2+2x^9}+C$; $\lim_{x\to0}f=0$ gives $C=0$ (and $f(1)=\tfrac14$ ✓). $f'(x)=\dfrac{9x^8(1+x^2+2x^9)-x^9(2x+18x^8)}{(1+x^2+2x^9)^2}$, so $f'(1)=\dfrac{36-20}{16}=1$. Expanding along the first row, $|A|=1\cdot\left(\tfrac14\cdot4-1\cdot\alpha^2\right)=1-\alpha^2$. For $3\times3$, $|\operatorname{adj}(\operatorname{adj}A)|=|A|^{(n-1)^2}=|A|^4=81\Rightarrow|A|=\pm3$, so $1-\alpha^2=-3$ (the value $+3$ would give $\alpha^2=-2$): $\alpha^2=4$.

### M-MAT-05 · A — JEE Main 2026 · 22 Jan Shift 2 · Matrices set Q6 · MCQ

If $X=\begin{bmatrix}x\\y\\z\end{bmatrix}$ is a solution of the system of equations $AX=B$, where $\operatorname{adj}A=\begin{bmatrix}4&2&2\\-5&0&5\\1&-2&3\end{bmatrix}$ and $B=\begin{bmatrix}4\\0\\2\end{bmatrix}$, then $|x+y+z|$ is equal to:

(1) 2  (2) $\dfrac32$  (3) 1  (4) 3

**Answer: (1)** · key (compiled)

**Solution.** $|\operatorname{adj}A|=4(0+10)-2(-15-5)+2(10-0)=100=|A|^2$, so $|A|=\pm10$. $X=A^{-1}B=\dfrac{(\operatorname{adj}A)B}{|A|}$ and $(\operatorname{adj}A)B=\begin{bmatrix}16+4\\-20+10\\4+6\end{bmatrix}=\begin{bmatrix}20\\-10\\10\end{bmatrix}$. So $x+y+z=\dfrac{20}{|A|}$ and $|x+y+z|=\dfrac{20}{10}=2$.

### M-MAT-06 · A — JEE Main 2026 · 22 Jan Shift 1 · Matrices set Q7 · MCQ

If $A=\begin{bmatrix}2&3\\3&5\end{bmatrix}$, then the determinant of the matrix $(A^{2025}-3A^{2024}+A^{2023})$ is:

(1) 12  (2) 28  (3) 24  (4) 16

**Answer: (4)** · key (compiled)

**Solution.** $A^{2025}-3A^{2024}+A^{2023}=A^{2023}(A^2-3A+I)$ and $|A|=1$. $A^2=\begin{bmatrix}13&21\\21&34\end{bmatrix}$, so $A^2-3A+I=\begin{bmatrix}8&12\\12&20\end{bmatrix}$ with determinant $160-144=16$. The required determinant is $|A|^{2023}\cdot16=16$.

### M-MAT-07 · A — JEE Main 2026 · 23 Jan Shift 2 · Matrices set Q9 · Numerical

Let $A=\begin{bmatrix}0&2&-3\\-2&0&1\\3&-1&0\end{bmatrix}$ and $B$ be a matrix such that $B(I-A)=I+A$. Then the sum of the diagonal elements of $B^TB$ is equal to ______.

**Answer: 3** · key (compiled)

**Solution.** $A^T=-A$. $B=(I+A)(I-A)^{-1}$, so $B^T=\left((I-A)^{-1}\right)^T(I+A)^T=(I+A)^{-1}(I-A)$. Since $I+A$ and $I-A$ commute, $B^TB=(I+A)^{-1}(I-A)(I+A)(I-A)^{-1}=(I+A)^{-1}(I+A)(I-A)(I-A)^{-1}=I$. The trace of $I_3$ is 3.

### M-MAT-08 · A — JEE Main 2026 · 21 Jan Shift 1 · Matrices set Q10 · Numerical

For some $\alpha,\beta\in\mathbb R$, let $A=\begin{bmatrix}\alpha&2\\1&2\end{bmatrix}$ and $B=\begin{bmatrix}1&1\\1&\beta\end{bmatrix}$ be such that $A^2-4A+2I=B^2-3B+I=O$. Then $\left(\det\left(\operatorname{adj}\left(A^3-B^3\right)\right)\right)^2$ is equal to ______.

**Answer: 225** · key (compiled)

**Solution.** By Cayley–Hamilton $A^2-(\alpha+2)A+(2\alpha-2)I=O$; comparing with $A^2-4A+2I=O$ gives $\alpha=2$. Similarly $B^2-(1+\beta)B+(\beta-1)I=O$ gives $\beta=2$. $A^2=\begin{bmatrix}6&8\\4&6\end{bmatrix}$, $A^3=\begin{bmatrix}20&28\\14&20\end{bmatrix}$; $B^2=\begin{bmatrix}2&3\\3&5\end{bmatrix}$, $B^3=\begin{bmatrix}5&8\\8&13\end{bmatrix}$. $A^3-B^3=\begin{bmatrix}15&20\\6&7\end{bmatrix}$ with $\det=105-120=-15$. For a $2\times2$ matrix $\det(\operatorname{adj}M)=\det M$, so the answer is $(-15)^2=225$.

### M-MAT-09 · B — JEE Advanced 2025 · Paper 1 · Q4 · MCQ

Let $P=\begin{pmatrix}2&0&0\\0&2&0\\0&0&3\end{pmatrix}$. The number of $3\times3$ invertible matrices $Q$ with integer entries such that $Q^{-1}=Q^T$ and $PQ=QP$ is

(A) 32  (B) 8  (C) 16  (D) 24

**Answer: (C)** · official key ✔ (re-derived)

**Solution.** An integer matrix with $Q^TQ=I$ has orthonormal integer columns, so each column is $\pm e_i$: $Q$ is a signed permutation matrix. $PQ=QP$ means $Q$ preserves the eigenspaces of $P$ ($\text{span}\{e_1,e_2\}$ for $2$ and $\text{span}\{e_3\}$ for $3$), so $Q=\text{diag}(B,\pm1)$ with $B$ a $2\times2$ signed permutation matrix. There are $2!\cdot2^2=8$ such $B$ and $2$ signs for the last entry: $8\times2=16$.

### M-MAT-10 · B — JEE Main 2025 · Jan session · set Q1 · MCQ

Let $A=[a_{ij}]$ be a $3\times3$ matrix such that $A\begin{bmatrix}0\\1\\0\end{bmatrix}=\begin{bmatrix}0\\0\\1\end{bmatrix}$, $A\begin{bmatrix}4\\1\\3\end{bmatrix}=\begin{bmatrix}0\\1\\0\end{bmatrix}$ and $A\begin{bmatrix}2\\1\\2\end{bmatrix}=\begin{bmatrix}1\\0\\0\end{bmatrix}$. Then $a_{23}$ equals:

(1) $-1$  (2) 2  (3) 1  (4) 0

**Answer: (1)** · key (compiled)

**Solution.** Let $C_1,C_2,C_3$ be the columns of $A$. The first relation gives $C_2=(0,0,1)^T$. Then $4C_1+3C_3=(0,1,-1)^T$ and $2C_1+2C_3=(1,0,-1)^T$, so $C_1+C_3=\left(\tfrac12,0,-\tfrac12\right)$. Hence $C_3=(2,0,-2)^T-(0,1,-1)^T=(2,-1,-1)^T$, and $a_{23}$ is the second entry of $C_3$: $-1$.

### M-MAT-11 · B — JEE Main 2025 · Jan session · set Q2 · MCQ

Let $A=[a_{ij}]$ be a matrix of order $3\times3$ with $a_{ij}=(\sqrt2)^{i+j}$. If the sum of all the elements in the third row of $A^2$ is $\alpha+\beta\sqrt2$, $\alpha,\beta\in\mathbb Z$, then $\alpha+\beta$ is equal to:

(1) 280  (2) 224  (3) 210  (4) 168

**Answer: (2)** · key (compiled)

**Solution.** $a_{ij}=u_iu_j$ with $u_i=(\sqrt2)^i=(\sqrt2,2,2\sqrt2)$, so $A=uu^T$ and $A^2=(u^Tu)\,uu^T=14\,uu^T$. The third-row sum is $14\,u_3\sum_ju_j=14\cdot2\sqrt2\,(3\sqrt2+2)=168+56\sqrt2$. So $\alpha+\beta=224$.

### M-MAT-12 · B — JEE Main 2025 · Jan session · set Q3 · MCQ

For a $3\times3$ matrix $M$, let $\operatorname{trace}(M)$ denote the sum of all the diagonal elements of $M$. Let $A$ be a $3\times3$ matrix such that $|A|=\tfrac12$ and $\operatorname{trace}(A)=3$. If $B=\operatorname{adj}(\operatorname{adj}(2A))$, then the value of $|B|+\operatorname{trace}(B)$ equals:

(1) 56  (2) 132  (3) 174  (4) 280

**Answer: (4)** · key (compiled)

**Solution.** For a $3\times3$ matrix $\operatorname{adj}(\operatorname{adj}M)=|M|^{n-2}M=|M|\,M$. With $M=2A$: $|2A|=8\cdot\tfrac12=4$, so $B=4\cdot2A=8A$. $|B|=8^3\cdot\tfrac12=256$ and $\operatorname{trace}(B)=8\cdot3=24$. Sum $=280$.

### M-MAT-13 · B — JEE Main 2025 · Apr session · set Q2 · Numerical

The number of singular matrices of order 2, whose elements are from the set $\{2,3,6,9\}$, is ______.

**Answer: 36** · key (compiled)

**Solution.** Singular means $ad=bc$. Count ordered pairs from the set by their product: 4 (1 way), 6 (2), 9 (1), 12 (2), 18 (4: (2,9),(9,2),(3,6),(6,3)), 27 (2), 36 (1), 54 (2), 81 (1). The number of matrices with $ad=bc$ is $\sum(\text{count})^2=1+4+1+4+16+4+1+4+1=36$.

### M-MAT-14 · B — JEE Main 2025 · Apr session · set Q3 · MCQ

Let $A=\begin{bmatrix}\alpha&-1\\6&\beta\end{bmatrix}$, $\alpha>0$, such that $\det(A)=0$ and $\alpha+\beta=1$. If $I$ denotes the $2\times2$ identity matrix, then the matrix $(I+A)^8$ is:

(1) $\begin{bmatrix}4&-1\\6&-1\end{bmatrix}$  (2) $\begin{bmatrix}257&-64\\514&-127\end{bmatrix}$  (3) $\begin{bmatrix}1025&-511\\2024&-1024\end{bmatrix}$  (4) $\begin{bmatrix}766&-255\\1530&-509\end{bmatrix}$

**Answer: (4)** · key (compiled)

**Solution.** $\alpha\beta+6=0$ and $\alpha+\beta=1$ give $\alpha=3$, $\beta=-2$. The matrix has trace 1 and determinant 0, so $A^2=A$ and $A^k=A$. $(I+A)^8=I+(2^8-1)A=I+255A=\begin{bmatrix}766&-255\\1530&-509\end{bmatrix}$.

### M-MAT-15 · B — JEE Main 2025 · Apr session · set Q4 · MCQ

Let $\alpha$ be a solution of $x^2+x+1=0$, and for some $a$ and $b$ in $\mathbb R$, $[4\ \ a\ \ b]\begin{bmatrix}1&16&13\\-1&-1&2\\-2&-14&-8\end{bmatrix}=[0\ \ 0\ \ 0]$. If $\dfrac4{\alpha^4}+\dfrac m{\alpha^a}+\dfrac n{\alpha^b}=3$, then $m+n$ is equal to:

(1) 3  (2) 11  (3) 7  (4) 8

**Answer: (2)** · key (compiled)

**Solution.** The three column equations: $4-a-2b=0$, $64-a-14b=0$, $52+2a-8b=0$. The first two give $b=5$, $a=-6$ (the third checks). With $\alpha=\omega$ ($\alpha^3=1$, $1+\alpha+\alpha^2=0$): $\alpha^4=\alpha$, $\alpha^{a}=\alpha^{-6}=1$, $\alpha^b=\alpha^5=\alpha^2$. The equation becomes $4\alpha^2+m+n\alpha=3$, i.e. $-4\alpha-4+m+n\alpha=3$, so $n=4$, $m=7$ and $m+n=11$.

### M-MAT-16 · C — JEE Main 2024 · 27 Jan Shift 1 · Q72 · MCQ

Consider $f(x)=\begin{pmatrix}\cos x&-\sin x&0\\\sin x&\cos x&0\\0&0&1\end{pmatrix}$.  
Statement I: $f(-x)$ is the inverse of $f(x)$.  
Statement II: $f(x)f(y)=f(x+y)$.

(1) I false, II true  (2) Both false  (3) I true, II false  (4) Both true

**Answer: (4)** · key ✔

**Solution.** $f(x)$ is a rotation about the $z$-axis. Multiplying gives $f(x)f(y)=f(x+y)$ (angle addition), so II is true. Taking $y=-x$: $f(x)f(-x)=f(0)=I$, so I is true.

### M-MAT-17 · C — JEE Main 2024 · 27 Jan Shift 2 · Q86 · Numerical

Let $A$ be a $2\times2$ real matrix and $I$ the identity matrix of order $2$. If the roots of $|A-xI|=0$ are $-1$ and $3$, then the sum of the diagonal elements of $A^2$ is ______.

**Answer: 10** · key ✔

**Solution.** The roots of $|A-xI|=0$ are the eigenvalues $\lambda_1=-1,\lambda_2=3$. $A^2$ has eigenvalues $\lambda_i^2$, so $\text{tr}(A^2)=1+9=10$.

### M-MAT-18 · C — JEE Main 2024 · 29 Jan Shift 1 · Q69 · MCQ

Let $A=\begin{pmatrix}1&0&0\\0&\alpha&\beta\\0&\beta&\alpha\end{pmatrix}$ and $|2A|^3=2^{21}$, where $\alpha,\beta\in\mathbb Z$. A value of $\alpha$ is

(1) 3  (2) 5  (3) 17  (4) 9

**Answer: (2)** · key ✔

**Solution.** $|2A|=2^3|A|$, so $2^9|A|^3=2^{21}\Rightarrow|A|^3=2^{12}\Rightarrow|A|=16$. $|A|=\alpha^2-\beta^2=16\Rightarrow(\alpha-\beta)(\alpha+\beta)=16$. Integer solutions include $\alpha=5,\beta=3$ ($25-9=16$). $\alpha=3,9,17$ would need $\beta^2=-7,65,273$, none a perfect square.

### M-MAT-19 · C — JEE Main 2024 · 29 Jan Shift 2 · Q70 · MCQ

Let $A=\begin{pmatrix}2&1&2\\6&2&11\\3&3&2\end{pmatrix}$ and $P=\begin{pmatrix}1&2&0\\5&0&2\\7&1&5\end{pmatrix}$. The sum of the prime factors of $\left|P^{-1}AP-2I\right|$ is

(1) 26  (2) 27  (3) 66  (4) 23

**Answer: (1)** · key ✔

**Solution.** $P^{-1}AP-2I=P^{-1}(A-2I)P$, so its determinant equals $|A-2I|$. $A-2I=\begin{pmatrix}0&1&2\\6&0&11\\3&3&0\end{pmatrix}$, with determinant $0-1(0-33)+2(18-0)=33+36=69=3\times23$. Sum of prime factors $=3+23=26$.

### M-MAT-20 · C — JEE Main 2024 · 30 Jan Shift 1 · Q70 · MCQ

If $f(x)=\begin{vmatrix}2\cos^4x&2\sin^4x&3+\sin^22x\\3+2\cos^4x&2\sin^4x&\sin^22x\\2\cos^4x&3+2\sin^4x&\sin^22x\end{vmatrix}$, then $\dfrac15f'(0)$ is equal to

(1) 0  (2) 1  (3) 2  (4) 6

**Answer: (1)** · key ✔

**Solution.** Apply $R_2\to R_2-R_1$ and $R_3\to R_3-R_1$: rows become $(3,0,-3)$ and $(0,3,-3)$. Expanding along the top row: $f(x)=2\cos^4x(9)-2\sin^4x(-9)+(3+\sin^22x)(9)=18(\cos^4x+\sin^4x)+27+9\sin^22x$. Since $\cos^4x+\sin^4x=1-\tfrac12\sin^22x$: $f(x)=18-9\sin^22x+27+9\sin^22x=45$. A constant, so $f'(0)=0$.

