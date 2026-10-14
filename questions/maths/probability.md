# Probability

> Theory: [../../theory/maths/probability.md](../../theory/maths/probability.md)

### M-PRB-01 · A — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

A random variable $X$ takes the values $0,1,2,3$ with probabilities $\dfrac{2a+1}{30},\ \dfrac{8a-1}{30},\ \dfrac{4a+1}{30},\ b$ respectively, where $a,b\in\mathbb R$. Let $\mu$ and $\sigma$ be the mean and standard deviation of $X$ such that $\sigma^2+\mu^2=2$. Then $\dfrac ab$ is equal to:

(1) 12  (2) 30  (3) 60  (4) 3

**Answer: (3)** · key (compiled)

**Solution.** Total probability $=1$: $\dfrac{14a+1}{30}+b=1\Rightarrow b=\dfrac{29-14a}{30}$. Since $\sigma^2+\mu^2=E(X^2)$, we need $E(X^2)=2$: $\dfrac{8a-1}{30}+4\cdot\dfrac{4a+1}{30}+9b=2\Rightarrow \dfrac{24a+3}{30}+\dfrac{9(29-14a)}{30}=2\Rightarrow 264-102a=60\Rightarrow a=2$. Then $b=\dfrac1{30}$ and $\dfrac ab=60$.

### M-PRB-02 · A — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · Numerical

From the first 100 natural numbers, two numbers $a$ and then $b$ are selected at random without replacement. If the probability that $a-b\ge10$ is $\dfrac mn$, $\gcd(m,n)=1$, then $m+n$ is equal to ______.

**Answer: 311** · key (compiled)

**Solution.** Ordered pairs $(a,b)$ with $a\ne b$: $100\cdot99=9900$. For a fixed difference $d=a-b$ ($10\le d\le99$) there are $100-d$ pairs, so the favourable count is $\sum_{d=10}^{99}(100-d)=1+2+\cdots+90=\dfrac{90\cdot91}2=4095$. Probability $=\dfrac{4095}{9900}=\dfrac{91}{220}$, so $m+n=91+220=311$.

### M-PRB-03 · A — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

The probability distribution of a random variable $X$ is given below:

| $X$ | $4k$ | $\tfrac{30}7k$ | $\tfrac{32}7k$ | $\tfrac{34}7k$ | $\tfrac{36}7k$ | $\tfrac{38}7k$ | $\tfrac{40}7k$ | $6k$ |
|---|---|---|---|---|---|---|---|---|
| $P(X)$ | $\tfrac2{15}$ | $\tfrac1{15}$ | $\tfrac2{15}$ | $\tfrac15$ | $\tfrac1{15}$ | $\tfrac2{15}$ | $\tfrac15$ | $\tfrac1{15}$ |

If $E(X)=\dfrac{263}{15}$, then $P(X<20)$ is equal to:

(1) $\dfrac{11}{15}$  (2) $\dfrac35$  (3) $\dfrac{14}{15}$  (4) $\dfrac8{15}$

**Answer: (1)** · key (compiled)

**Solution.** Writing every probability over 105 and multiplying by the values: $E(X)=\dfrac k{105}(56+30+64+102+36+76+120+42)=\dfrac{526k}{105}=\dfrac{263}{15}\Rightarrow k=\dfrac72$. The values are therefore $14,15,16,17,18,19,20,21$. $P(X<20)=P(14)+\dots+P(19)=\dfrac{2+1+2+3+1+2}{15}=\dfrac{11}{15}$.

### M-PRB-04 · A — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · Numerical

Let $S$ be a set of 5 elements and $P(S)$ denote the power set of $S$. Let $E$ be the event of choosing an ordered pair $(A,B)$ from $P(S)\times P(S)$ such that $A\cap B=\emptyset$. If the probability of the event $E$ is $\dfrac{3^p}{2^q}$, where $p,q\in\mathbb N$, then $p+q$ is equal to ______.

**Answer: 15** · key (compiled)

**Solution.** Total ordered pairs $=2^5\cdot2^5=2^{10}$. For $A\cap B=\emptyset$ each of the 5 elements goes to $A$ only, $B$ only, or neither: $3^5$ ways. $P(E)=\dfrac{3^5}{2^{10}}$, so $p=5$, $q=10$ and $p+q=15$.

### M-PRB-05 · A — JEE Main 2026 · 22 Jan Shift 1 · set Q5 · MCQ

If a random variable $x$ has the probability distribution

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $P(x)$ | 0 | $2k$ | $k$ | $3k$ | $2k^2$ | $2k$ | $k^2+k$ | $7k^2$ |

then $P(3<x\le6)$ is equal to:

(1) 0.64  (2) 0.22  (3) 0.33  (4) 0.34

**Answer: (3)** · key (compiled)

**Solution.** $\sum P=9k+10k^2=1\Rightarrow(10k-1)(k+1)=0\Rightarrow k=\dfrac1{10}$ (probabilities are non-negative). $P(3<x\le6)=P(4)+P(5)+P(6)=2k^2+2k+(k^2+k)=3k^2+3k=0.03+0.30=0.33$.

### M-PRB-06 · A — JEE Main 2025 · Jan session · set Q1 · MCQ

Let $A=[a_{ij}]$ be a square matrix of order 2 with entries either 0 or 1. Let $E$ be the event that $A$ is an invertible matrix. Then the probability $P(E)$ is:

(1) $\tfrac3{16}$  (2) $\tfrac58$  (3) $\tfrac38$  (4) $\tfrac18$

**Answer: (3)** · key (compiled)

**Solution.** There are $2^4=16$ matrices. $|A|=a_{11}a_{22}-a_{12}a_{21}\ne0$ needs exactly one of the two products to be 1: $a_{11}a_{22}=1$ and $a_{12}a_{21}=0$ (3 ways) or the reverse (3 ways). That is 6 matrices, so $P(E)=\tfrac6{16}=\tfrac38$.

### M-PRB-07 · B — JEE Advanced 2025 · Paper 1 · Q2 · MCQ

Three students $S_1,S_2,S_3$ (solving independently) are given a problem. Events: $U$: at least one solves it; $V$: $S_1$ solves it given that neither $S_2$ nor $S_3$ solves it; $W$: $S_2$ solves it and $S_3$ does not; $T$: $S_3$ solves it. If $P(U)=\tfrac12$, $P(V)=\tfrac1{10}$ and $P(W)=\tfrac1{12}$, then $P(T)$ is

(A) $\tfrac{13}{36}$  (B) $\tfrac13$  (C) $\tfrac{19}{60}$  (D) $\tfrac14$

**Answer: (A)** · official key ✔ (re-derived)

**Solution.** Let $p_i=P(S_i\text{ solves})$. By independence $P(V)=p_1=\tfrac1{10}$. $P(\text{none})=1-P(U)=\tfrac12=(1-p_1)(1-p_2)(1-p_3)\Rightarrow(1-p_2)(1-p_3)=\dfrac{5}{9}$. Also $P(W)=p_2(1-p_3)=\tfrac1{12}$. Adding: $(1-p_3)\big[(1-p_2)+p_2\big]=\dfrac59+\dfrac1{12}=\dfrac{23}{36}$, so $p_3=\dfrac{13}{36}$.

### M-PRB-08 · B — JEE Main 2025 · Jan session · set Q2 · MCQ

Two numbers $k_1$ and $k_2$ are randomly chosen from the set of natural numbers. Then the probability that the value of $i^{k_1}+i^{k_2}$ ($i=\sqrt{-1}$) is non-zero equals:

(1) $\tfrac12$  (2) $\tfrac34$  (3) $\tfrac14$  (4) $\tfrac23$

**Answer: (2)** · key (compiled)

**Solution.** The powers of $i$ cycle with period 4, so each of $i,-1,-i,1$ is equally likely. The sum is zero exactly when $i^{k_2}=-i^{k_1}$, which has probability $\tfrac14$ (for any $k_1$ one of the four residues of $k_2$ works). Non-zero: $\tfrac34$.

### M-PRB-09 · B — JEE Main 2025 · Apr session · set Q1 · Numerical

A card from a pack of 52 cards is lost. From the remaining 51 cards, $n$ cards are drawn and are found to be spades. If the probability of the lost card being a spade is $\tfrac{11}{50}$, then $n$ is equal to ______.

**Answer: 2** · key (compiled)

**Solution.** By Bayes' theorem, $P(\text{lost spade}\mid n\text{ spades drawn})=\dfrac{\frac14\binom{12}n}{\frac14\binom{12}n+\frac34\binom{13}n}$. For $n=2$: $\dfrac{66}{66+3\cdot78}=\dfrac{66}{300}=\dfrac{11}{50}$. So $n=2$.

### M-PRB-10 · B — JEE Main 2025 · Apr session · set Q2 · MCQ

If the probability that the random variable $X$ takes the value $x$ is given by $P(X=x)=k(x+1)3^{-x}$, $x=0,1,2,3,\dots$, where $k$ is a constant, then $P(X\ge3)$ is equal to:

(1) $\tfrac7{27}$  (2) $\tfrac49$  (3) $\tfrac8{27}$  (4) $\tfrac19$

**Answer: (4)** · key (compiled)

**Solution.** $\sum_{x\ge0}(x+1)r^x=\dfrac1{(1-r)^2}$ with $r=\tfrac13$ equals $\tfrac94$, so $k=\tfrac49$. $P(X<3)=k\left(1+\tfrac23+\tfrac39\right)=\tfrac49\cdot2=\tfrac89$, hence $P(X\ge3)=\tfrac19$.

### M-PRB-11 · B — JEE Main 2024 · 27 Jan Shift 1 · Q90 · Numerical

A fair die is tossed repeatedly until a six is obtained. Let $X$ denote the number of tosses required, and let $a=P(X=3)$, $b=P(X\ge3)$ and $c=P(X\ge6\mid X>3)$. Then $\dfrac{b+c}a$ is equal to ______.

**Answer: 12** · key ✔

**Solution.** $X$ is geometric with success probability $\tfrac16$. $a=\left(\tfrac56\right)^2\tfrac16$, $b=P(\text{first two fail})=\left(\tfrac56\right)^2$. By memorylessness, $c=\dfrac{(5/6)^5}{(5/6)^3}=\left(\tfrac56\right)^2$. So $\dfrac{b+c}a=\dfrac{2(5/6)^2}{(5/6)^2/6}=12$.

### M-PRB-12 · C — JEE Main 2024 · 27 Jan Shift 2 · Q80 · MCQ

An urn contains $6$ white and $9$ black balls. Two successive draws of $4$ balls each are made without replacement. The probability that the first draw gives all white balls and the second draw gives all black balls is

(1) $\tfrac5{256}$  (2) $\tfrac5{715}$  (3) $\tfrac3{715}$  (4) $\tfrac3{256}$

**Answer: (3)** · key ✔

**Solution.** $P=\dfrac{{}^6C_4}{{}^{15}C_4}\times\dfrac{{}^9C_4}{{}^{11}C_4}=\dfrac{15}{1365}\times\dfrac{126}{330}=\dfrac1{91}\times\dfrac{21}{55}=\dfrac{3}{715}$.

### M-PRB-13 · C — JEE Main 2024 · 31 Jan Shift 1 · Q79 · MCQ

Two marbles are drawn in succession, with replacement after each draw, from a box containing $10$ red, $30$ white, $20$ blue and $15$ orange marbles. The probability that the first marble drawn is red and the second is white is

(1) $\tfrac2{25}$  (2) $\tfrac4{25}$  (3) $\tfrac23$  (4) $\tfrac4{75}$

**Answer: (4)** · key ✔

**Solution.** Total $=75$. Draws are independent: $\dfrac{10}{75}\times\dfrac{30}{75}=\dfrac{300}{5625}=\dfrac4{75}$.

