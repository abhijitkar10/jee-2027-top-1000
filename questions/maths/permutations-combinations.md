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

