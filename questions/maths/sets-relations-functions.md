# Sets, Relations & Functions

> Theory: [../../theory/maths/sets-relations-functions.md](../../theory/maths/sets-relations-functions.md)

### M-SRF-01 — JEE Main 2024 · 27 Jan Shift 1 · Q71 · MCQ

Let $S=\{1,2,\dots,10\}$ and let $M$ be the set of all subsets of $S$. The relation $R=\{(A,B):A\cap B\neq\phi;\ A,B\in M\}$ is

(1) symmetric and reflexive only  (2) reflexive only  (3) symmetric and transitive only  (4) symmetric only

**Answer: (4)** · key ✔

**Solution.** Symmetric: $A\cap B=B\cap A$. Not reflexive: $A=\phi$ gives $\phi\cap\phi=\phi$. Not transitive: $A=\{1,2\},B=\{2,3\},C=\{3,4\}$ has $A\cap B\neq\phi,\ B\cap C\neq\phi$ but $A\cap C=\phi$. So symmetric only.

### M-SRF-02 — JEE Main 2024 · 27 Jan Shift 1 · Q73 · MCQ

The function $f:\mathbb N-\{1\}\to\mathbb N$, $f(n)=$ the highest prime factor of $n$, is

(1) both one-one and onto  (2) one-one only  (3) onto only  (4) neither one-one nor onto

**Answer: (4)** · key ✔

**Solution.** Not one-one: $f(2)=f(4)=2$. Not onto: $1\in\mathbb N$ but every $n\ge2$ has a highest prime factor $\ge2$, so $1$ is never attained.

### M-SRF-03 — JEE Main 2024 · 27 Jan Shift 2 · Q65 · MCQ

Let $A$ and $B$ be finite sets with $m$ and $n$ elements. The number of subsets of $A$ is $56$ more than the number of subsets of $B$. The distance of $P(m,n)$ from $Q(-2,-3)$ is

(1) 10  (2) 6  (3) 4  (4) 8

**Answer: (1)** · key ✔

**Solution.** $2^m-2^n=56\Rightarrow2^n(2^{m-n}-1)=8\cdot7$. The odd factor forces $2^n=8$, $2^{m-n}-1=7$, so $n=3,\ m=6$. $PQ=\sqrt{(6+2)^2+(3+3)^2}=10$.

### M-SRF-04 — JEE Main 2024 · 27 Jan Shift 2 · Q71 · MCQ

Let $f:\mathbb R-\{-\tfrac12\}\to\mathbb R$ and $g:\mathbb R-\{-\tfrac52\}\to\mathbb R$ be $f(x)=\dfrac{2x+3}{2x+1}$ and $g(x)=\dfrac{|x|+1}{2x+5}$. The domain of $f\circ g$ is

(1) $\mathbb R-\{-\tfrac52\}$  (2) $\mathbb R$  (3) $\mathbb R-\{-\tfrac74\}$  (4) $\mathbb R-\{-\tfrac52,-\tfrac74\}$

**Answer: (1)** · key ✔

**Solution.** We need $x\neq-\tfrac52$ and $g(x)\neq-\tfrac12$. Solve $\dfrac{|x|+1}{2x+5}=-\dfrac12\Rightarrow2|x|+2=-2x-5$. For $x<0$: $-2x+2=-2x-5$ is impossible. For $x\ge0$: $2x+2=-2x-5\Rightarrow x=-\tfrac74$, rejected since $x\ge0$. So no extra exclusion; the domain is $\mathbb R-\{-\tfrac52\}$.

