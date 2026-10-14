# Sets, Relations & Functions

> Theory: [../../theory/maths/sets-relations-functions.md](../../theory/maths/sets-relations-functions.md)

### M-SRF-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

Let $A=\{x:|x^2-10|\le6\}$ and $B=\{x:|x-2|>1\}$. Then:

(1) $A\cup B=(-\infty,1]\cup(2,\infty)$  (2) $B-A=(-\infty,-4)\cup(-2,1)\cup(4,\infty)$  (3) $A-B=[2,3)$  (4) $A\cap B=[-4,-2]\cup[3,4]$

**Answer: (2)** · key (compiled)

**Solution.** $|x^2-10|\le6\Rightarrow4\le x^2\le16\Rightarrow A=[-4,-2]\cup[2,4]$. $|x-2|>1\Rightarrow B=(-\infty,1)\cup(3,\infty)$. Then $B-A=B\cap A^c$ with $A^c=(-\infty,-4)\cup(-2,2)\cup(4,\infty)$ gives $(-\infty,-4)\cup(-2,1)\cup(4,\infty)$ – option (2). The others are wrong: $A\cup B$ contains $[-4,-2]$; $A-B=[2,3]$ (closed at 3); $A\cap B=[-4,-2]\cup(3,4]$ (open at 3).

### M-SRF-02 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q2 · MCQ

Let $A=\{2,3,5,7,9\}$. Let R be the relation on A defined by $xRy$ if and only if $2x\le3y$. Let $l$ be the number of elements in R, and $m$ be the minimum number of elements required to be added to R to make it a symmetric relation. Then $l+m$ is equal to:

(1) 21  (2) 27  (3) 23  (4) 25

**Answer: (4)** · key (compiled)

**Solution.** $2x\le3y$ means $y\ge\tfrac{2x}3$. $x=2$: $y\ge\tfrac43$, all 5; $x=3$: $y\ge2$, all 5; $x=5$: $y\ge3.3$, $y\in\{5,7,9\}$: 3; $x=7$: $y\ge4.7$: 3; $x=9$: $y\ge6$, $\{7,9\}$: 2. So $l=18$. For symmetry we need the reverse of each pair: $(2,5),(2,7),(2,9),(3,5),(3,7),(3,9),(5,9)$ have their reverses missing, whereas $(2,3),(5,7),(7,9)$ are fine. So $m=7$ and $l+m=25$.

### M-SRF-03 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q3 · MCQ

Let $A=\{-2,-1,0,1,2,3,4\}$. Let R be a relation on A defined by $xRy$ if and only if $2x+y\le2$. Let $l$ be the number of elements in R. Let $m$ and $n$ be the minimum number of elements required to be added in R to make it reflexive and symmetric relations respectively. Then $l+m+n$ is equal to:

(1) 35  (2) 34  (3) 33  (4) 32

**Answer: (3)** · key (compiled)

**Solution.** Count pairs: $x=-2$: $y\le6$ (7); $x=-1$: $y\le4$ (7); $x=0$: $y\le2$ (5); $x=1$: $y\le0$ (3); $x=2$: $y\le-2$ (1); $x=3,4$: none. $l=23$. Reflexive needs $(x,x)$ with $3x\le2$, so $(1,1),(2,2),(3,3),(4,4)$ are missing: $m=4$. Symmetric: the pairs whose reverse $(y,x)$ fails $2y+x\le2$ are $(-2,3),(-2,4),(-1,2),(-1,3),(-1,4),(0,2)$, so $n=6$. $l+m+n=23+4+6=33$.

### M-SRF-04 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q4 · MCQ

The number of elements in the relation $R=\{(x,y):4x^2+y^2<52,\ x,y\in\mathbb Z\}$ is:

(1) 77  (2) 67  (3) 86  (4) 89

**Answer: (1)** · key (compiled)

**Solution.** $4x^2<52\Rightarrow|x|\le3$. $x=0$: $y^2<52$, $|y|\le7$: 15 values. $x=\pm1$: $y^2<48$, $|y|\le6$: $13\times2=26$. $x=\pm2$: $y^2<36$, $|y|\le5$: $11\times2=22$. $x=\pm3$: $y^2<16$, $|y|\le3$: $7\times2=14$. Total $=15+26+22+14=77$.

### M-SRF-05 · A — JEE Main 2026 · 22 Jan Shift 2 · set Q5 · Numerical

Let S be the set of the first 11 natural numbers. Then the number of elements in $A=\{B\subseteq S:\ n(B)\ge2$ and the product of all elements of B is even$\}$ is ______.

**Answer: 1979** · key (compiled)

**Solution.** Subsets with at least 2 elements: $2^{11}-1-11=2036$. The product is odd only if every element is odd; S has 6 odd numbers, so odd-only subsets with at least 2 elements number $2^6-1-6=57$. Hence $|A|=2036-57=1979$.

### M-SRF-06 · A — JEE Main 2026 · 22 Jan Shift 1 · set Q6 · MCQ

Let the relation R on the set $M=\{1,2,3,\dots,16\}$ be given by $R=\{(x,y):4y=5x-3,\ x,y\in M\}$. Then the minimum number of elements required to be added in R, in order to make the relation symmetric, is equal to:

(1) 4  (2) 1  (3) 2  (4) 3

**Answer: (3)** · key (compiled)

**Solution.** $y=\dfrac{5x-3}4$ is an integer iff $5x\equiv3\pmod4$, i.e. $x\equiv3\pmod4$: $x=3,7,11,15$ give $y=3,8,13,18$; $y=18\notin M$. So $R=\{(3,3),(7,8),(11,13)\}$. For symmetry add $(8,7)$ and $(13,11)$: **2** elements.

### M-SRF-07 · A — JEE Main 2026 · 23 Jan Shift 2 · set Q7 · MCQ

Let $A=\{0,1,2,\dots,9\}$. Let R be a relation on A defined by $(x,y)\in R$ if and only if $|x-y|$ is a multiple of 3. Given below are two statements: Statement I: $n(R)=36$. Statement II: R is an equivalence relation.

(1) Statement I is incorrect but Statement II is correct  (2) Statement I is correct but Statement II is incorrect  (3) Both Statement I and Statement II are incorrect  (4) Both Statement I and Statement II are correct

**Answer: (1)** · key (compiled)

**Solution.** $|x-y|$ a multiple of 3 means $x\equiv y\pmod3$, which is reflexive, symmetric and transitive: II is correct. The residue classes are $\{0,3,6,9\}$ (4 elements), $\{1,4,7\}$ and $\{2,5,8\}$ (3 each), so $n(R)=4^2+3^2+3^2=34\ne36$: I is incorrect.

### M-SRF-08 · A — JEE Main 2026 · 21 Jan Shift 1 · set Q8 · MCQ

The number of relations defined on the set $\{a,b,c,d\}$ which are both reflexive and symmetric is equal to:

(1) 16  (2) 1024  (3) 64  (4) 256

**Answer: (3)** · key (compiled)

**Solution.** Reflexivity forces the 4 diagonal pairs. Symmetry makes each of the $\binom42=6$ unordered off-diagonal pairs $\{x,y\}$ either both present or both absent: $2^6=64$.

### M-SRF-09 · A — JEE Main 2026 · 24 Jan Shift 1 · set Q9 · MCQ

Let R be a relation defined on the set $\{1,2,3,4\}\times\{1,2,3,4\}$ by $R=\{((a,b),(c,d)):2a+3b=3c+4d\}$. Then the number of elements in R is:

(1) 18  (2) 6  (3) 15  (4) 12

**Answer: (4)** · key (compiled)

**Solution.** List $2a+3b$ for $a,b\in\{1,..,4\}$: $5,8,11,14;\ 7,10,13,16;\ 9,12,15,18;\ 11,14,17,20$. List $3c+4d$: $7,11,15,19;\ 10,14,18,22;\ 13,17,21,25;\ 16,20,24,28$. Common values with multiplicities (left × right): $7$:1, $10$:1, $11$:$2\times1$, $13$:1, $14$:$2\times1$, $15$:1, $16$:1, $17$:1, $18$:1, $20$:1. Total $=1+1+2+1+2+1+1+1+1+1=12$.

### M-SRF-10 · A — JEE Main 2026 · 28 Jan Shift 2 · Functions set Q1 · MCQ

Given below are two statements: Statement I: The function $f:\mathbb R\to\mathbb R$ defined by $f(x)=\dfrac{x}{1+|x|}$ is one-one. Statement II: The function $f:\mathbb R\to\mathbb R$ defined by $f(x)=\dfrac{x^2+4x-30}{x^2-8x+18}$ is many-one.

(1) Both Statement I and Statement II are true  (2) Statement I is true but Statement II is false  (3) Statement I is false but Statement II is true  (4) Both Statement I and Statement II are false

**Answer: (1)** · key (compiled)

**Solution.** I: for $x\ge0$, $f=\dfrac{x}{1+x}$ and for $x<0$, $f=\dfrac{x}{1-x}$; each piece has derivative $\dfrac1{(1\pm x)^2}>0$ and $f$ is continuous at 0, so $f$ is strictly increasing on $\mathbb R$, hence one-one. II: $f(x)=1+\dfrac{12(x-4)}{x^2-8x+18}$, so with $x=4+t$, $f-1=\dfrac{12t}{t^2+2}$; $t=1$ and $t=2$ both give $4$, so $f$ is many-one.

### M-SRF-11 · B — JEE Main 2026 · 28 Jan Shift 2 · Functions set Q2 · MCQ

The sum of all the elements in the range of $f(x)=\mathrm{Sgn}(\sin x)+\mathrm{Sgn}(\cos x)+\mathrm{Sgn}(\tan x)+\mathrm{Sgn}(\cot x)$, where $x\ne\dfrac{n\pi}2$, $n\in\mathbb Z$ and $\mathrm{Sgn}(t)=\begin{cases}-1,&t<0\\1,&t>0\end{cases}$, is:

(1) 2  (2) 0  (3) 4  (4) $-2$

**Answer: (1)** · key (compiled)

**Solution.** Quadrant I: all four signs $+$: $f=4$. Quadrant II: $\sin+,\cos-,\tan-,\cot-$: $f=1-1-1-1=-2$. Quadrant III: $\sin-,\cos-,\tan+,\cot+$: $f=0$. Quadrant IV: $\sin-,\cos+,\tan-,\cot-$: $f=-2$. Range $=\{-2,0,4\}$, sum $=2$.

### M-SRF-12 · B — JEE Main 2026 · 24 Jan Shift 2 · Functions set Q3 · MCQ

Let $f$ be a function such that $3f(x)+2f\!\left(\dfrac m{19x}\right)=5x$, $x\ne0$, where $m=\sum_{i=1}^{9}i^2$. Then $f(5)-f(2)$ is equal to:

(1) 18  (2) 36  (3) 9  (4) $-9$

**Answer: (1)** · key (compiled)

**Solution.** $m=\dfrac{9\cdot10\cdot19}6=285$, so $\dfrac m{19}=15$: $3f(x)+2f(15/x)=5x$ (i). Replace $x\to15/x$: $3f(15/x)+2f(x)=\dfrac{75}x$ (ii). Eliminate $f(15/x)$: $3\times$(i) $-2\times$(ii): $5f(x)=15x-\dfrac{150}x$, so $f(x)=3x-\dfrac{30}x$. $f(5)=15-6=9$, $f(2)=6-15=-9$, so $f(5)-f(2)=18$.

### M-SRF-13 · B — JEE Main 2026 · 22 Jan Shift 1 · Functions set Q6 · MCQ

If the domain of the function $f(x)=\sin^{-1}\!\left(\dfrac{5-x}{3+2x}\right)+\dfrac1{\log_e(10-x)}$ is $(-\infty,\alpha]\cup[\beta,\gamma)-\{\delta\}$, then $6(\alpha+\beta+\gamma+\delta)$ is equal to:

(1) 67  (2) 66  (3) 70  (4) 68

**Answer: (3)** · key (compiled)

**Solution.** $\left|\dfrac{5-x}{2x+3}\right|\le1$: $\dfrac{5-x}{2x+3}\le1\Rightarrow\dfrac{3x-2}{2x+3}\ge0\Rightarrow x<-\tfrac32$ or $x\ge\tfrac23$; and $\dfrac{5-x}{2x+3}\ge-1\Rightarrow\dfrac{x+8}{2x+3}\ge0\Rightarrow x\le-8$ or $x>-\tfrac32$. Together: $x\le-8$ or $x\ge\tfrac23$. For the log term: $10-x>0$ and $\log_e(10-x)\ne0$, i.e. $x<10$, $x\ne9$. Domain $(-\infty,-8]\cup[\tfrac23,10)-\{9\}$: $\alpha=-8,\beta=\tfrac23,\gamma=10,\delta=9$. $6(-8+\tfrac23+10+9)=6\cdot\tfrac{35}3=70$.

### M-SRF-14 · B — JEE Main 2026 · 23 Jan Shift 2 · Functions set Q8 · MCQ

Consider two sets $A=\{x\in\mathbb Z:||x-3|-3|\le1\}$ and $B=\left\{x\in\mathbb R-\{1,2\}:\dfrac{(x-2)(x-4)}{x-1}\log_e|x-2|=0\right\}$. Then the number of onto functions $f:A\to B$ is equal to:

(1) 32  (2) 79  (3) 62  (4) 81

**Answer: (3)** · key (compiled)

**Solution.** $||x-3|-3|\le1\Rightarrow2\le|x-3|\le4$: $x\in\{5,6,7\}$ or $\{-1,0,1\}$, so $|A|=6$. In B the expression vanishes when $x=4$ (since $x\ne2$) or $\log_e|x-2|=0\Rightarrow x=3$ (and $x=1$ is excluded). So $B=\{3,4\}$. Onto functions from a 6-element set onto a 2-element set: $2^6-2=62$.

### M-SRF-15 · B — JEE Main 2026 · 28 Jan Shift 1 · Functions set Q9 · MCQ

If $g(x)=3x^2+2x-3$, $f(0)=-3$ and $4g(f(x))=3x^2-32x+72$, then $f(g(2))$ is equal to:

(1) $-\dfrac72$  (2) $-\dfrac{25}6$  (3) $\dfrac72$  (4) $\dfrac{25}6$

**Answer: (3)** · key (compiled)

**Solution.** The right side is quadratic, so $f(x)=ax+b$ is linear. $4g(f(x))=12(ax+b)^2+8(ax+b)-12$. Compare $x^2$: $12a^2=3\Rightarrow a=\pm\tfrac12$. Constant: $12b^2+8b-12=72\Rightarrow3b^2+2b-21=0\Rightarrow b=\tfrac73$ or $-3$; $f(0)=-3$ gives $b=-3$. Compare $x$: $24ab+8a=8a(3b+1)=-64a=-32\Rightarrow a=\tfrac12$. So $f(x)=\dfrac x2-3$. $g(2)=12+4-3=13$ and $f(13)=\dfrac{13}2-3=\dfrac72$.

### M-SRF-16 · B — JEE Main 2026 · 24 Jan Shift 1 · Functions set Q10 · MCQ

If the domain of the function $f(x)=\log_{(10x^2-17x+7)}(18x^2-11x+1)$ is $(-\infty,a)\cup(b,c)\cup(d,\infty)-\{e\}$, then $90(a+b+c+d+e)$ equals:

(1) 170  (2) 307  (3) 316  (4) 177

**Answer: (3)** · key (compiled)

**Solution.** Base: $10x^2-17x+7=(10x-7)(x-1)>0\Rightarrow x<\tfrac7{10}$ or $x>1$; base $\ne1$: $10x^2-17x+6=0\Rightarrow x=\tfrac12,\tfrac65$. Argument: $18x^2-11x+1=(2x-1)(9x-1)>0\Rightarrow x<\tfrac19$ or $x>\tfrac12$. Intersection: $(-\infty,\tfrac19)\cup(\tfrac12,\tfrac7{10})\cup(1,\infty)$ with $x=\tfrac65$ removed. So $a=\tfrac19,b=\tfrac12,c=\tfrac7{10},d=1,e=\tfrac65$ and $90\left(\tfrac19+\tfrac12+\tfrac7{10}+1+\tfrac65\right)=10+45+63+90+108=316$.

### M-SRF-17 · B — JEE Advanced 2025 · Paper 1 · Q6 · Multiple correct

$f:\mathbb N\to\mathbb Z$ and $g:\mathbb Z\to\mathbb N$ are $f(n)=\begin{cases}(n+1)/2,&n\text{ odd}\\(4-n)/2,&n\text{ even}\end{cases}$ and $g(n)=\begin{cases}3+2n,&n\ge0\\-2n,&n<0\end{cases}$. Which are TRUE?

(A) $g\circ f$ is NOT one-one and NOT onto  (B) $f\circ g$ is NOT one-one but onto  (C) $g$ is one-one and onto  (D) $f$ is NOT one-one but onto

**Answer: (A), (D)** · official key ✔ (re-derived)

**Solution.** $f$: odd $n\mapsto1,2,3,\dots$ and even $n\mapsto1,0,-1,\dots$; $f(1)=f(2)=1$ so $f$ is not one-one, but every integer occurs: onto (D true). $g$ is one-one, but its range is $\{2,3,4,5,\dots\}$ (it misses $1$), so $g$ is not onto (C false). $g\circ f$: $f(1)=f(2)$ gives $g(f(1))=g(f(2))$: not one-one, and its range lies in $\{2,3,\dots\}$: not onto (A true). $f\circ g$: $g$ takes values $\ge2$ and $f$ is one-one on $n\ge2$ and covers all integers, so $f\circ g$ is one-one and onto, making (B false).

### M-SRF-18 · B — JEE Advanced 2025 · Paper 1 · Q8 · Numerical

Let $\mathcal S$ be the set of all relations $R$ on $\{a,b,c,d,e,f\}$ that are reflexive and symmetric and contain exactly $10$ elements. The number of elements in $\mathcal S$ is ______.

**Answer: 105** · official key ✔ (re-derived)

**Solution.** Reflexivity puts the $6$ pairs $(x,x)$ in $R$. The other $4$ elements come in symmetric pairs $\{(x,y),(y,x)\}$, i.e. $2$ unordered pairs chosen from $\binom62=15$: $\binom{15}{2}=105$.

### M-SRF-19 · B — JEE Main 2024 · 27 Jan Shift 1 · Q71 · MCQ

Let $S=\{1,2,\dots,10\}$ and let $M$ be the set of all subsets of $S$. The relation $R=\{(A,B):A\cap B\neq\phi;\ A,B\in M\}$ is

(1) symmetric and reflexive only  (2) reflexive only  (3) symmetric and transitive only  (4) symmetric only

**Answer: (4)** · key ✔

**Solution.** Symmetric: $A\cap B=B\cap A$. Not reflexive: $A=\phi$ gives $\phi\cap\phi=\phi$. Not transitive: $A=\{1,2\},B=\{2,3\},C=\{3,4\}$ has $A\cap B\neq\phi,\ B\cap C\neq\phi$ but $A\cap C=\phi$. So symmetric only.

### M-SRF-20 · C — JEE Main 2024 · 27 Jan Shift 2 · Q71 · MCQ

Let $f:\mathbb R-\{-\tfrac12\}\to\mathbb R$ and $g:\mathbb R-\{-\tfrac52\}\to\mathbb R$ be $f(x)=\dfrac{2x+3}{2x+1}$ and $g(x)=\dfrac{|x|+1}{2x+5}$. The domain of $f\circ g$ is

(1) $\mathbb R-\{-\tfrac52\}$  (2) $\mathbb R$  (3) $\mathbb R-\{-\tfrac74\}$  (4) $\mathbb R-\{-\tfrac52,-\tfrac74\}$

**Answer: (1)** · key ✔

**Solution.** We need $x\neq-\tfrac52$ and $g(x)\neq-\tfrac12$. Solve $\dfrac{|x|+1}{2x+5}=-\dfrac12\Rightarrow2|x|+2=-2x-5$. For $x<0$: $-2x+2=-2x-5$ is impossible. For $x\ge0$: $2x+2=-2x-5\Rightarrow x=-\tfrac74$, rejected since $x\ge0$. So no extra exclusion; the domain is $\mathbb R-\{-\tfrac52\}$.

### M-SRF-21 · C — JEE Main 2024 · 29 Jan Shift 1 · Q68 · MCQ

Let $R$ be a relation on $\mathbb Z\times\mathbb Z$ defined by $(a,b)\,R\,(c,d)$ if and only if $ad-bc$ is divisible by $5$. Then $R$ is

(1) Reflexive and symmetric but not transitive  (2) Reflexive but neither symmetric nor transitive  (3) Reflexive, symmetric and transitive  (4) Reflexive and transitive but not symmetric

**Answer: (1)** · key ✔

**Solution.** Reflexive: $ab-ba=0$. Symmetric: $cb-da=-(ad-bc)$ is also divisible by $5$. Not transitive: $(1,1)R(0,0)$ and $(0,0)R(1,2)$ (both give $0$), but $(1,1)$ and $(1,2)$ give $1\cdot2-1\cdot1=1$, not divisible by $5$.

### M-SRF-22 · C — JEE Main 2024 · 29 Jan Shift 1 · Q71 · MCQ

Let $f(x)=\begin{cases}2+2x,&-1\le x<0\\1-\tfrac x3,&0\le x\le3\end{cases}$ and $g(x)=\begin{cases}-x,&-3\le x\le0\\x,&0<x\le1\end{cases}$. The range of $f\circ g$ is

(1) $(0,1]$  (2) $[0,3)$  (3) $[0,1]$  (4) $[0,1)$

**Answer: (3)** · key ✔

**Solution.** $g(x)=|x|$ on $[-3,1]$, so $g$ takes all values in $[0,3]$. For $u\in[0,3]$, $f(u)=1-\tfrac u3$ decreases continuously from $1$ to $0$. So $f\circ g$ takes every value in $[0,1]$.

### M-SRF-23 · C — JEE Main 2024 · 29 Jan Shift 2 · Q69 · MCQ

If $R$ is the smallest equivalence relation on the set $\{1,2,3,4\}$ such that $\{(1,2),(1,3)\}\subset R$, then the number of elements in $R$ is

(1) 10  (2) 12  (3) 8  (4) 15

**Answer: (1)** · key ✔

**Solution.** Symmetry and transitivity force $1,2,3$ into one class, and $4$ stays alone by reflexivity. Equivalence classes $\{1,2,3\}$ and $\{4\}$ give $3^2+1^2=9+1=10$ ordered pairs.

### M-SRF-24 · C — JEE Main 2024 · 30 Jan Shift 1 · Q72 · MCQ

If the domain of the function $f(x)=\cos^{-1}\!\left(\dfrac{2-|x|}4\right)+\left(\ln(3-x)\right)^{-1}$ is $[-\alpha,\beta)-\{\gamma\}$, then $\alpha+\beta+\gamma$ is equal to

(1) 12  (2) 9  (3) 11  (4) 8

**Answer: (3)** · key ✔

**Solution.** $\cos^{-1}$ needs $\left|\tfrac{2-|x|}4\right|\le1\Rightarrow|x|\le6$. The term $\dfrac1{\ln(3-x)}$ needs $3-x>0$ and $\ln(3-x)\neq0$, i.e. $x<3$ and $x\ne2$. Domain: $[-6,3)-\{2\}$, so $\alpha=6,\ \beta=3,\ \gamma=2$ and the sum is $11$.

### M-SRF-25 · C — JEE Main 2024 · 30 Jan Shift 1 · Q85 · Numerical

A group of $40$ students appeared in an examination of $3$ subjects: Mathematics, Physics and Chemistry. All students passed in at least one subject; $20$ passed in Mathematics, $25$ in Physics and $16$ in Chemistry; at most $11$ passed in both Mathematics and Physics, at most $15$ in both Physics and Chemistry, and at most $15$ in both Mathematics and Chemistry. The maximum number of students who passed in all three subjects is ______.

**Answer: 10** · key ✔

**Solution.** Let $a,b,c$ be the pairwise intersections (M∩P, P∩C, M∩C) and $x$ the triple intersection. Inclusion–exclusion: $40=61-(a+b+c)+x\Rightarrow a+b+c=21+x$. Also $x\le a\le11$, and $b,c\ge x$. With $a=11$: $b+c=10+x\ge2x\Rightarrow x\le10$. Check $x=10$, $b=c=10$: only-Maths $=20-21+10=9$, only-Physics $=25-21+10=14$, only-Chemistry $=16-20+10=6$, all non-negative, and total $=9+14+6+1+0+0+10=40$ ✓. So the maximum is $10$.

