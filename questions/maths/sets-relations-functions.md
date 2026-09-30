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

### M-SRF-05 — JEE Main 2024 · 29 Jan Shift 1 · Q68 · MCQ

Let $R$ be a relation on $\mathbb Z\times\mathbb Z$ defined by $(a,b)\,R\,(c,d)$ if and only if $ad-bc$ is divisible by $5$. Then $R$ is

(1) Reflexive and symmetric but not transitive  (2) Reflexive but neither symmetric nor transitive  (3) Reflexive, symmetric and transitive  (4) Reflexive and transitive but not symmetric

**Answer: (1)** · key ✔

**Solution.** Reflexive: $ab-ba=0$. Symmetric: $cb-da=-(ad-bc)$ is also divisible by $5$. Not transitive: $(1,1)R(0,0)$ and $(0,0)R(1,2)$ (both give $0$), but $(1,1)$ and $(1,2)$ give $1\cdot2-1\cdot1=1$, not divisible by $5$.

### M-SRF-06 — JEE Main 2024 · 29 Jan Shift 1 · Q71 · MCQ

Let $f(x)=\begin{cases}2+2x,&-1\le x<0\\1-\tfrac x3,&0\le x\le3\end{cases}$ and $g(x)=\begin{cases}-x,&-3\le x\le0\\x,&0<x\le1\end{cases}$. The range of $f\circ g$ is

(1) $(0,1]$  (2) $[0,3)$  (3) $[0,1]$  (4) $[0,1)$

**Answer: (3)** · key ✔

**Solution.** $g(x)=|x|$ on $[-3,1]$, so $g$ takes all values in $[0,3]$. For $u\in[0,3]$, $f(u)=1-\tfrac u3$ decreases continuously from $1$ to $0$. So $f\circ g$ takes every value in $[0,1]$.

### M-SRF-07 — JEE Main 2024 · 29 Jan Shift 2 · Q69 · MCQ

If $R$ is the smallest equivalence relation on the set $\{1,2,3,4\}$ such that $\{(1,2),(1,3)\}\subset R$, then the number of elements in $R$ is

(1) 10  (2) 12  (3) 8  (4) 15

**Answer: (1)** · key ✔

**Solution.** Symmetry and transitivity force $1,2,3$ into one class, and $4$ stays alone by reflexivity. Equivalence classes $\{1,2,3\}$ and $\{4\}$ give $3^2+1^2=9+1=10$ ordered pairs.

### M-SRF-08 — JEE Main 2024 · 30 Jan Shift 1 · Q72 · MCQ

If the domain of the function $f(x)=\cos^{-1}\!\left(\dfrac{2-|x|}4\right)+\left(\ln(3-x)\right)^{-1}$ is $[-\alpha,\beta)-\{\gamma\}$, then $\alpha+\beta+\gamma$ is equal to

(1) 12  (2) 9  (3) 11  (4) 8

**Answer: (3)** · key ✔

**Solution.** $\cos^{-1}$ needs $\left|\tfrac{2-|x|}4\right|\le1\Rightarrow|x|\le6$. The term $\dfrac1{\ln(3-x)}$ needs $3-x>0$ and $\ln(3-x)\neq0$, i.e. $x<3$ and $x\ne2$. Domain: $[-6,3)-\{2\}$, so $\alpha=6,\ \beta=3,\ \gamma=2$ and the sum is $11$.

### M-SRF-09 — JEE Main 2024 · 30 Jan Shift 1 · Q85 · Numerical

A group of $40$ students appeared in an examination of $3$ subjects: Mathematics, Physics and Chemistry. All students passed in at least one subject; $20$ passed in Mathematics, $25$ in Physics and $16$ in Chemistry; at most $11$ passed in both Mathematics and Physics, at most $15$ in both Physics and Chemistry, and at most $15$ in both Mathematics and Chemistry. The maximum number of students who passed in all three subjects is ______.

**Answer: 10** · key ✔

**Solution.** Let $a,b,c$ be the pairwise intersections (M∩P, P∩C, M∩C) and $x$ the triple intersection. Inclusion–exclusion: $40=61-(a+b+c)+x\Rightarrow a+b+c=21+x$. Also $x\le a\le11$, and $b,c\ge x$. With $a=11$: $b+c=10+x\ge2x\Rightarrow x\le10$. Check $x=10$, $b=c=10$: only-Maths $=20-21+10=9$, only-Physics $=25-21+10=14$, only-Chemistry $=16-20+10=6$, all non-negative, and total $=9+14+6+1+0+0+10=40$ ✓. So the maximum is $10$.

### M-SRF-10 — JEE Advanced 2025 · Paper 1 · Q6 · Multiple correct

$f:\mathbb N\to\mathbb Z$ and $g:\mathbb Z\to\mathbb N$ are $f(n)=\begin{cases}(n+1)/2,&n\text{ odd}\\(4-n)/2,&n\text{ even}\end{cases}$ and $g(n)=\begin{cases}3+2n,&n\ge0\\-2n,&n<0\end{cases}$. Which are TRUE?

(A) $g\circ f$ is NOT one-one and NOT onto  (B) $f\circ g$ is NOT one-one but onto  (C) $g$ is one-one and onto  (D) $f$ is NOT one-one but onto

**Answer: (A), (D)** · official key ✔ (re-derived)

**Solution.** $f$: odd $n\mapsto1,2,3,\dots$ and even $n\mapsto1,0,-1,\dots$; $f(1)=f(2)=1$ so $f$ is not one-one, but every integer occurs: onto (D true). $g$ is one-one, but its range is $\{2,3,4,5,\dots\}$ (it misses $1$), so $g$ is not onto (C false). $g\circ f$: $f(1)=f(2)$ gives $g(f(1))=g(f(2))$: not one-one, and its range lies in $\{2,3,\dots\}$: not onto (A true). $f\circ g$: $g$ takes values $\ge2$ and $f$ is one-one on $n\ge2$ and covers all integers, so $f\circ g$ is one-one and onto, making (B false).

### M-SRF-11 — JEE Advanced 2025 · Paper 1 · Q8 · Numerical

Let $\mathcal S$ be the set of all relations $R$ on $\{a,b,c,d,e,f\}$ that are reflexive and symmetric and contain exactly $10$ elements. The number of elements in $\mathcal S$ is ______.

**Answer: 105** · official key ✔ (re-derived)

**Solution.** Reflexivity puts the $6$ pairs $(x,x)$ in $R$. The other $4$ elements come in symmetric pairs $\{(x,y),(y,x)\}$, i.e. $2$ unordered pairs chosen from $\binom62=15$: $\binom{15}{2}=105$.

