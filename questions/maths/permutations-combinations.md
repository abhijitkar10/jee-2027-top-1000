# Permutations & Combinations

> Theory: [../../theory/maths/permutations-combinations.md](../../theory/maths/permutations-combinations.md)

### M-PNC-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

The largest $n\in\mathbb N$ for which $7^n$ divides $101!$ is:

(1) 16  (2) 15  (3) 18  (4) 19

**Answer: (1)** · key (compiled)

**Solution.** Exponent of 7 in $101!$ is $\left\lfloor\dfrac{101}7\right\rfloor+\left\lfloor\dfrac{101}{49}\right\rfloor+\left\lfloor\dfrac{101}{343}\right\rfloor=14+2+0=16$.

### M-PNC-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · Numerical

The number of 4-letter words, with or without meaning, which can be formed using the letters of PQRPQRSTUVP, is ______.

**Answer: 1422** · key (compiled)

**Solution.** The letters are P ×3, Q ×2, R ×2 and S, T, U, V once each (7 distinct letters). All distinct: $7\cdot6\cdot5\cdot4=840$. One letter twice + two other distinct letters: $3\ (\text{P, Q or R})\times\binom62\times\dfrac{4!}{2!}=3\times15\times12=540$. Two letters twice each: $\binom32\times\dfrac{4!}{2!2!}=3\times6=18$. P three times + one other: $6\times\dfrac{4!}{3!}=24$. Total $=840+540+18+24=1422$.

### M-PNC-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · Numerical

Three persons enter a lift at the ground floor. The lift will go up to the 10th floor. The number of ways in which the three persons can exit the lift at three different floors, if the lift does not stop at the first, second and third floors, is equal to ______.

**Answer: 210** · key (compiled)

**Solution.** The available floors are 4th to 10th: 7 floors. Three persons exit at three different floors: ${}^7P_3=7\cdot6\cdot5=210$.

### M-PNC-04 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · MCQ

The largest value of $n$ for which $40^n$ divides $60!$ is:

(1) 11  (2) 12  (3) 14  (4) 13

**Answer: (3)** · key (compiled)

**Solution.** $40^n=2^{3n}5^n$. In $60!$, the exponent of 5 is $12+2=14$ and the exponent of 2 is $30+15+7+3+1=56$, which allows $\lfloor56/3\rfloor=18$. The limiting factor is 5: $n=14$.

### M-PNC-05 · A — JEE Main 2026 · 22 Jan Shift 1 · set Q6 · Numerical

Let ABC be a triangle. Consider four points $p_1,\dots,p_4$ on the side AB, five points $p_5,\dots,p_9$ on the side BC and four points $p_{10},\dots,p_{13}$ on the side AC. None of these points is a vertex of the triangle ABC. Then the total number of pentagons that can be formed by taking all the vertices from the points $p_1,p_2,\dots,p_{13}$ is ______.

**Answer: 660** · key (compiled)

**Solution.** Three points on one side are collinear, so a pentagon uses at most 2 points from each side: the split is $2,2,1$. One from AB: $4\times\binom52\binom42=4\times10\times6=240$. One from BC: $5\times\binom42\binom42=5\times36=180$. One from AC: $4\times\binom42\binom52=240$. Total $=660$.

### M-PNC-06 · A — JEE Main 2026 · 23 Jan Shift 2 · set Q7 · MCQ

The number of ways in which 16 oranges can be distributed to four children such that each child gets at least one orange is:

(1) 455  (2) 429  (3) 403  (4) 384

**Answer: (1)** · key (compiled)

**Solution.** Give each child one orange first; distribute the remaining 12 freely among 4 children: $\binom{12+3}3=\binom{15}3=455$.

### M-PNC-07 · B — JEE Main 2026 · 21 Jan Shift 1 · set Q9 · MCQ

The number of strictly increasing functions $f$ from the set $\{1,2,3,4,5,6\}$ to the set $\{1,2,3,\dots,9\}$ such that $f(i)\ne i$ for $1\le i\le6$ is equal to:

(1) 27  (2) 22  (3) 21  (4) 28

**Answer: (4)** · key (compiled)

**Solution.** A strictly increasing $f$ is determined by its 6-element image $a_1<\dots<a_6$ with $f(i)=a_i\ge i$. $f(i)\ne i$ for all $i$ means $a_i\ge i+1$ for all $i$, which is equivalent to $a_1\ge2$ (i.e. the image avoids the element 1). So choose 6 elements from $\{2,\dots,9\}$: $\binom86=28$.

### M-PNC-08 · B — JEE Advanced 2025 · Paper 1 · Q10 · Numerical

Let $S$ be the set of all seven-digit numbers formed using the digits $0,1,2$ (the leading digit is nonzero). The number of elements $x\in S$ such that at least one of the digits $0$ and $1$ appears exactly twice in $x$ is ______.

**Answer: 762** · official key ✔ (re-derived)

**Solution.** Inclusion–exclusion. $A$ = $0$ appears exactly twice: choose $2$ of the $6$ non-leading positions ($15$ ways), fill the other $5$ positions with $1$ or $2$ ($2^5$): $480$. $B$ = $1$ appears exactly twice: if the leading position holds a $1$ ($6$ ways to place the other one) the other $5$ digits are from $\{0,2\}$: $6\cdot32$; if not ($15$ ways) the leading digit must be $2$ and the other $4$ from $\{0,2\}$: $15\cdot16$; total $432$. $A\cap B$: arrangements of $\{0,0,1,1,2,2,2\}$ are $\dfrac{7!}{2!2!3!}=210$, minus those starting with $0$ ($\dfrac{6!}{1!2!3!}=60$): $150$. $|A\cup B|=480+432-150=762$.

### M-PNC-09 · B — JEE Main 2024 · 27 Jan Shift 1 · Q64 · MCQ

${}^{n-1}C_r=(k^2-8)\,{}^nC_{r+1}$ if and only if

(1) $2\sqrt2<k\le3$  (2) $2\sqrt3<k\le3\sqrt2$  (3) $2\sqrt3<k<3\sqrt3$  (4) $2\sqrt2<k<2\sqrt3$

**Answer: (1)** · key ✔

**Solution.** $\dfrac{{}^{n-1}C_r}{{}^nC_{r+1}}=\dfrac{r+1}{n}$, and $0\le r\le n-1$ makes this lie in $(0,1]$. So $0<k^2-8\le1\Rightarrow8<k^2\le9\Rightarrow2\sqrt2<k\le3$ (taking $k>0$, as in the options).

### M-PNC-10 · B — JEE Main 2024 · 27 Jan Shift 2 · Q62 · MCQ

Let $\alpha=\dfrac{(4!)!}{(4!)^{3!}}$ and $\beta=\dfrac{(5!)!}{(5!)^{4!}}$. Then

(1) $\alpha\in\mathbb N$ and $\beta\notin\mathbb N$  (2) $\alpha\notin\mathbb N$ and $\beta\in\mathbb N$  (3) $\alpha\in\mathbb N$ and $\beta\in\mathbb N$  (4) $\alpha\notin\mathbb N$ and $\beta\notin\mathbb N$

**Answer: (3)** · key ✔

**Solution.** Use Legendre's formula $v_p(n!)=\sum\lfloor n/p^k\rfloor$. $\alpha=24!/24^6$ with $24=2^3\cdot3$: $v_2(24!)=22\ge18$, $v_3(24!)=10\ge6$. $\beta=120!/120^{24}$ with $120=2^3\cdot3\cdot5$: $v_2(120!)=116\ge72$, $v_3(120!)=58\ge24$, $v_5(120!)=28\ge24$. In both cases every prime power in the denominator divides the numerator, so both are natural numbers.

### M-PNC-11 · B — JEE Main 2024 · 29 Jan Shift 1 · Q82 · Numerical

All the letters of the word GTWENTY are written in all possible ways, with or without meaning, and arranged as in a dictionary. The serial number of the word GTWENTY is ______.

**Answer: 553** · key ✔

**Solution.** Letters in order: E, G, N, T, T, W, Y (T repeats). Words starting with E: $\dfrac{6!}{2!}=360$. Then G, second letter smaller than T: E gives $\dfrac{5!}{2!}=60$ and N gives $60$: $120$. Then GT, third letter smaller than W: E, N, T each give $4!=24$: $72$. The remaining letters E, N, T, Y are already in dictionary order, adding no more words. Rank $=360+120+72+1=553$.

### M-PNC-12 · C — JEE Main 2024 · 29 Jan Shift 2 · Q62 · MCQ

The number of ways of arranging $8$ identical books into $4$ identical shelves, where any number of shelves may remain empty, is equal to

(1) 18  (2) 16  (3) 12  (4) 15

**Answer: (4)** · key ✔

**Solution.** Identical books into identical shelves means partitions of $8$ into at most $4$ parts. Count by number of parts: $1$ part: $1$; $2$ parts: $4$ ($7{+}1,6{+}2,5{+}3,4{+}4$); $3$ parts: $5$ ($6{+}1{+}1,5{+}2{+}1,4{+}3{+}1,4{+}2{+}2,3{+}3{+}2$); $4$ parts: $5$ ($5{+}1{+}1{+}1,4{+}2{+}1{+}1,3{+}3{+}1{+}1,3{+}2{+}2{+}1,2{+}2{+}2{+}2$). Total $=15$.

### M-PNC-13 · C — JEE Main 2024 · 30 Jan Shift 1 · Q86 · Numerical

Let $A=\{1,2,3,\dots,7\}$ and let $P(A)$ denote the power set of $A$. If the number of functions $f:A\to P(A)$ such that $a\in f(a)$ for all $a\in A$ is $m^n$, with $m$ and $n\in\mathbb N$ and $m$ the least, then $m+n$ is equal to ______.

**Answer: 44** · key ✔

**Solution.** For each $a$, $f(a)$ is a subset of $A$ containing $a$: the other $6$ elements are free, giving $2^6$ choices. Over $7$ elements: $(2^6)^7=2^{42}$. The least base is $m=2$ with $n=42$, so $m+n=44$.

