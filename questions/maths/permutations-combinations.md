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

### M-PNC-07 — JEE Main 2024 · 31 Jan Shift 1 · Q82 · Numerical

The total number of words (with or without meaning) that can be formed out of the letters of the word "DISTRIBUTION" taken four at a time is equal to ______.

**Answer: 3734** · key ✔

**Solution.** Letters: $I\times3$, $T\times2$ and seven single letters $D,S,R,B,U,O,N$. Cases: all four distinct from $9$ types: $P(9,4)=3024$. Exactly one letter repeated twice ($I$ or $T$) with two other distinct letters: $2\times\binom82\times\dfrac{4!}{2!}=2\times28\times12=672$. Two pairs ($II\,TT$): $\dfrac{4!}{2!2!}=6$. Three $I$'s and one other letter: $8\times\dfrac{4!}{3!}=32$. Total $=3024+672+6+32=3734$.

### M-PNC-08 — JEE Main 2024 · 1 Feb Shift 2 · Q81 · Numerical

The lines $L_1,\dots,L_{20}$ are distinct. For $n=1,\dots,10$ all lines $L_{2n-1}$ are parallel to each other and all lines $L_{2n}$ pass through a given point $P$. The maximum number of points of intersection of pairs of lines from the set is ______.

**Answer: 101** · key ✔

**Solution.** Total pairs $\binom{20}{2}=190$. The $10$ parallel lines give no points: subtract $\binom{10}2=45$. The $10$ concurrent lines meet in one point instead of $45$: subtract $45$, add $1$. Total $=190-45-45+1=101$.

### M-PNC-09 — JEE Advanced 2025 · Paper 1 · Q10 · Numerical

Let $S$ be the set of all seven-digit numbers formed using the digits $0,1,2$ (the leading digit is nonzero). The number of elements $x\in S$ such that at least one of the digits $0$ and $1$ appears exactly twice in $x$ is ______.

**Answer: 762** · official key ✔ (re-derived)

**Solution.** Inclusion–exclusion. $A$ = $0$ appears exactly twice: choose $2$ of the $6$ non-leading positions ($15$ ways), fill the other $5$ positions with $1$ or $2$ ($2^5$): $480$. $B$ = $1$ appears exactly twice: if the leading position holds a $1$ ($6$ ways to place the other one) the other $5$ digits are from $\{0,2\}$: $6\cdot32$; if not ($15$ ways) the leading digit must be $2$ and the other $4$ from $\{0,2\}$: $15\cdot16$; total $432$. $A\cap B$: arrangements of $\{0,0,1,1,2,2,2\}$ are $\dfrac{7!}{2!2!3!}=210$, minus those starting with $0$ ($\dfrac{6!}{1!2!3!}=60$): $150$. $|A\cup B|=480+432-150=762$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

The largest $n\in\mathbb N$ for which $7^n$ divides $101!$ is:

(1) 16  (2) 15  (3) 18  (4) 19

**Answer: (1)** · key (compiled)

**Solution.** Exponent of 7 in $101!$ is $\left\lfloor\dfrac{101}7\right\rfloor+\left\lfloor\dfrac{101}{49}\right\rfloor+\left\lfloor\dfrac{101}{343}\right\rfloor=14+2+0=16$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · Numerical

The number of 4-letter words, with or without meaning, which can be formed using the letters of PQRPQRSTUVP, is ______.

**Answer: 1422** · key (compiled)

**Solution.** The letters are P ×3, Q ×2, R ×2 and S, T, U, V once each (7 distinct letters). All distinct: $7\cdot6\cdot5\cdot4=840$. One letter twice + two other distinct letters: $3\ (\text{P, Q or R})\times\binom62\times\dfrac{4!}{2!}=3\times15\times12=540$. Two letters twice each: $\binom32\times\dfrac{4!}{2!2!}=3\times6=18$. P three times + one other: $6\times\dfrac{4!}{3!}=24$. Total $=840+540+18+24=1422$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · Numerical

Three persons enter a lift at the ground floor. The lift will go up to the 10th floor. The number of ways in which the three persons can exit the lift at three different floors, if the lift does not stop at the first, second and third floors, is equal to ______.

**Answer: 210** · key (compiled)

**Solution.** The available floors are 4th to 10th: 7 floors. Three persons exit at three different floors: ${}^7P_3=7\cdot6\cdot5=210$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · MCQ

The largest value of $n$ for which $40^n$ divides $60!$ is:

(1) 11  (2) 12  (3) 14  (4) 13

**Answer: (3)** · key (compiled)

**Solution.** $40^n=2^{3n}5^n$. In $60!$, the exponent of 5 is $12+2=14$ and the exponent of 2 is $30+15+7+3+1=56$, which allows $\lfloor56/3\rfloor=18$. The limiting factor is 5: $n=14$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q5 · MCQ

The letters of the word "UDAYPUR" are written in all possible ways with or without meaning and these words are arranged as in a dictionary. The rank of the word "UDAYPUR" is:

(1) 1579  (2) 1581  (3) 1578  (4) 1580

**Answer: (4)** · key (compiled)

**Solution.** Sorted letters: A, D, P, R, U, U, Y. Words starting with A, D, P or R: $4\times\dfrac{6!}{2!}=1440$. Starting with U: second letter A (before D): $5!=120$. Then "UD" with third letter A (nothing smaller): 0. "UDA" with fourth letter Y: letters before Y are P, R, U: $3\times3!=18$. "UDAY" fifth letter P: 0. "UDAYP" sixth letter U: R is smaller: $1\times1!=1$. The word itself adds 1. Rank $=1440+120+18+1+1=1580$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q6 · Numerical

Let ABC be a triangle. Consider four points $p_1,\dots,p_4$ on the side AB, five points $p_5,\dots,p_9$ on the side BC and four points $p_{10},\dots,p_{13}$ on the side AC. None of these points is a vertex of the triangle ABC. Then the total number of pentagons that can be formed by taking all the vertices from the points $p_1,p_2,\dots,p_{13}$ is ______.

**Answer: 660** · key (compiled)

**Solution.** Three points on one side are collinear, so a pentagon uses at most 2 points from each side: the split is $2,2,1$. One from AB: $4\times\binom52\binom42=4\times10\times6=240$. One from BC: $5\times\binom42\binom42=5\times36=180$. One from AC: $4\times\binom42\binom52=240$. Total $=660$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q7 · MCQ

The number of ways in which 16 oranges can be distributed to four children such that each child gets at least one orange is:

(1) 455  (2) 429  (3) 403  (4) 384

**Answer: (1)** · key (compiled)

**Solution.** Give each child one orange first; distribute the remaining 12 freely among 4 children: $\binom{12+3}3=\binom{15}3=455$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q8 · Numerical

Let S denote the set of 4-digit numbers $abcd$ such that $a>b>c>d$ and P denote the set of 5-digit numbers having the product of its digits equal to 20. Then $n(S)+n(P)$ is equal to ______.

**Answer: 260** · key (compiled)

**Solution.** $S$: choose 4 distinct digits from 0–9 and write them in decreasing order (the first digit is then automatically non-zero): $\binom{10}4=210$. $P$: $20=2^2\cdot5$ gives digit multisets $\{1,1,1,4,5\}$ ($\tfrac{5!}{3!}=20$ numbers) and $\{1,1,2,2,5\}$ ($\tfrac{5!}{2!2!}=30$ numbers): 50. Total $=260$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q9 · MCQ

The number of strictly increasing functions $f$ from the set $\{1,2,3,4,5,6\}$ to the set $\{1,2,3,\dots,9\}$ such that $f(i)\ne i$ for $1\le i\le6$ is equal to:

(1) 27  (2) 22  (3) 21  (4) 28

**Answer: (4)** · key (compiled)

**Solution.** A strictly increasing $f$ is determined by its 6-element image $a_1<\dots<a_6$ with $f(i)=a_i\ge i$. $f(i)\ne i$ for all $i$ means $a_i\ge i+1$ for all $i$, which is equivalent to $a_1\ge2$ (i.e. the image avoids the element 1). So choose 6 elements from $\{2,\dots,9\}$: $\binom86=28$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q10 · Numerical

Let $S=\{(m,n):m,n\in\{1,2,3,\dots,50\}\}$. If the number of elements $(m,n)$ in $S$ such that $6^m+9^n$ is a multiple of 5 is $p$ and the number of elements $(m,n)$ in $S$ such that $m+n$ is a square of a prime number is $q$, then $p+q$ is equal to ______.

**Answer: 1333** · key (compiled)

**Solution.** $6^m\equiv1$ and $9^n\equiv(-1)^n\pmod5$, so $6^m+9^n\equiv1+(-1)^n$, which is $0$ iff $n$ is odd. $p=50\times25=1250$. For $q$: $m+n\in\{4,9,25,49\}$ (squares of 2, 3, 5, 7); the number of pairs with $m+n=s$ is $s-1$ (for $s\le51$): $3+8+24+48=83$. So $p+q=1250+83=1333$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q11 · MCQ

Let $S=\{1,2,3,4,5,6,7,8,9\}$. Let $x$ be the number of 9-digit numbers formed using the digits of the set S such that only one digit is repeated and it is repeated exactly twice. Let $y$ be the number of 9-digit numbers formed using the digits of the set S such that only two digits are repeated and each of these is repeated exactly twice. Then:

(1) $56x=9y$  (2) $29x=5y$  (3) $45x=7y$  (4) $21x=4y$

**Answer: (4)** · key (compiled)

**Solution.** $x$: choose the repeated digit (9 ways) and the 7 other distinct digits from the remaining 8 ($\binom87=8$), then arrange: $x=9\cdot8\cdot\dfrac{9!}{2!}=36\cdot9!$. $y$: choose the two repeated digits ($\binom92=36$) and the 5 singles from the remaining 7 ($\binom75=21$), then arrange: $y=36\cdot21\cdot\dfrac{9!}{2!2!}=189\cdot9!$. $\dfrac xy=\dfrac{36}{189}=\dfrac4{21}$, i.e. $21x=4y$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q12 · Numerical

The number of numbers greater than 5000, less than 9000 and divisible by 3 that can be formed using the digits 0, 1, 2, 5, 9, if repetition of the digits is allowed, is ______.

**Answer: 42** · key (compiled)

**Solution.** A 4-digit number in $(5000,9000)$ must start with 5 (9 is excluded and 6, 7, 8 are unavailable). It is divisible by 3 iff $5+a+b+c\equiv0$, i.e. $a+b+c\equiv1\pmod3$. Residues of the digits: $\{0,9\}\to0$ (2 digits), $\{1\}\to1$ (1 digit), $\{2,5\}\to2$ (2 digits). Residue patterns with sum $\equiv1$: $(0,0,1)$: $3\times(2\cdot2\cdot1)=12$; $(1,1,2)$: $3\times(1\cdot1\cdot2)=6$; $(0,2,2)$: $3\times(2\cdot2\cdot2)=24$. Total $=42$.

