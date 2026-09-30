# Permutations & Combinations

> Theory: [../../theory/maths/permutations-combinations.md](../../theory/maths/permutations-combinations.md)

### M-PNC-01 — JEE Main 2024 · 27 Jan Shift 1 · Q64 · MCQ

${}^{n-1}C_r=(k^2-8)\,{}^nC_{r+1}$ if and only if

(1) $2\sqrt2<k\le3$  (2) $2\sqrt3<k\le3\sqrt2$  (3) $2\sqrt3<k<3\sqrt3$  (4) $2\sqrt2<k<2\sqrt3$

**Answer: (1)** · key ✔

**Solution.** $\dfrac{{}^{n-1}C_r}{{}^nC_{r+1}}=\dfrac{r+1}{n}$, and $0\le r\le n-1$ makes this lie in $(0,1]$. So $0<k^2-8\le1\Rightarrow8<k^2\le9\Rightarrow2\sqrt2<k\le3$ (taking $k>0$, as in the options).

### M-PNC-02 — JEE Main 2024 · 27 Jan Shift 2 · Q62 · MCQ

Let $\alpha=\dfrac{(4!)!}{(4!)^{3!}}$ and $\beta=\dfrac{(5!)!}{(5!)^{4!}}$. Then

(1) $\alpha\in\mathbb N$ and $\beta\notin\mathbb N$  (2) $\alpha\notin\mathbb N$ and $\beta\in\mathbb N$  (3) $\alpha\in\mathbb N$ and $\beta\in\mathbb N$  (4) $\alpha\notin\mathbb N$ and $\beta\notin\mathbb N$

**Answer: (3)** · key ✔

**Solution.** Use Legendre's formula $v_p(n!)=\sum\lfloor n/p^k\rfloor$. $\alpha=24!/24^6$ with $24=2^3\cdot3$: $v_2(24!)=22\ge18$, $v_3(24!)=10\ge6$. $\beta=120!/120^{24}$ with $120=2^3\cdot3\cdot5$: $v_2(120!)=116\ge72$, $v_3(120!)=58\ge24$, $v_5(120!)=28\ge24$. In both cases every prime power in the denominator divides the numerator, so both are natural numbers.

### M-PNC-03 — JEE Main 2024 · 29 Jan Shift 1 · Q82 · Numerical

All the letters of the word GTWENTY are written in all possible ways, with or without meaning, and arranged as in a dictionary. The serial number of the word GTWENTY is ______.

**Answer: 553** · key ✔

**Solution.** Letters in order: E, G, N, T, T, W, Y (T repeats). Words starting with E: $\dfrac{6!}{2!}=360$. Then G, second letter smaller than T: E gives $\dfrac{5!}{2!}=60$ and N gives $60$: $120$. Then GT, third letter smaller than W: E, N, T each give $4!=24$: $72$. The remaining letters E, N, T, Y are already in dictionary order, adding no more words. Rank $=360+120+72+1=553$.

### M-PNC-04 — JEE Main 2024 · 29 Jan Shift 2 · Q62 · MCQ

The number of ways of arranging $8$ identical books into $4$ identical shelves, where any number of shelves may remain empty, is equal to

(1) 18  (2) 16  (3) 12  (4) 15

**Answer: (4)** · key ✔

**Solution.** Identical books into identical shelves means partitions of $8$ into at most $4$ parts. Count by number of parts: $1$ part: $1$; $2$ parts: $4$ ($7{+}1,6{+}2,5{+}3,4{+}4$); $3$ parts: $5$ ($6{+}1{+}1,5{+}2{+}1,4{+}3{+}1,4{+}2{+}2,3{+}3{+}2$); $4$ parts: $5$ ($5{+}1{+}1{+}1,4{+}2{+}1{+}1,3{+}3{+}1{+}1,3{+}2{+}2{+}1,2{+}2{+}2{+}2$). Total $=15$.

### M-PNC-05 — JEE Main 2024 · 30 Jan Shift 1 · Q86 · Numerical

Let $A=\{1,2,3,\dots,7\}$ and let $P(A)$ denote the power set of $A$. If the number of functions $f:A\to P(A)$ such that $a\in f(a)$ for all $a\in A$ is $m^n$, with $m$ and $n\in\mathbb N$ and $m$ the least, then $m+n$ is equal to ______.

**Answer: 44** · key ✔

**Solution.** For each $a$, $f(a)$ is a subset of $A$ containing $a$: the other $6$ elements are free, giving $2^6$ choices. Over $7$ elements: $(2^6)^7=2^{42}$. The least base is $m=2$ with $n=42$, so $m+n=44$.

### M-PNC-06 — JEE Main 2024 · 30 Jan Shift 2 · Q82 · Numerical

In an examination there are $20$ questions of equal marks, divided into three sections $A$, $B$ and $C$. A student must attempt a total of $15$ questions, taking at least $4$ from each section. If section $A$ has $8$ questions, section $B$ has $6$ and section $C$ has $6$, the total number of ways a student can select $15$ questions is ______.

**Answer: 11376** · key ✔

**Solution.** Let $(a,b,c)$ be the numbers chosen from $A,B,C$: $a+b+c=15$, $4\le a\le8$, $4\le b,c\le6$. Valid triples and counts: $(7,4,4)$: $8\cdot15\cdot15=1800$; $(6,4,5)$ and $(6,5,4)$: $2\times(28\cdot15\cdot6)=5040$; $(5,4,6)$ and $(5,6,4)$: $2\times(56\cdot15\cdot1)=1680$; $(5,5,5)$: $56\cdot6\cdot6=2016$; $(4,5,6)$ and $(4,6,5)$: $2\times(70\cdot6\cdot1)=840$. Total $=1800+5040+1680+2016+840=11376$.

