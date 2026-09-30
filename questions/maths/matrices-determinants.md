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

