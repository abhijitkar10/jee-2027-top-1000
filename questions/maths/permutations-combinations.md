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

