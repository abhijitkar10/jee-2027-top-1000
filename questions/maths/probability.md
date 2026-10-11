# Probability

> Theory: [../../theory/maths/probability.md](../../theory/maths/probability.md)

### M-PRB-01 — JEE Main 2024 · 27 Jan Shift 1 · Q90 · Numerical

A fair die is tossed repeatedly until a six is obtained. Let $X$ denote the number of tosses required, and let $a=P(X=3)$, $b=P(X\ge3)$ and $c=P(X\ge6\mid X>3)$. Then $\dfrac{b+c}a$ is equal to ______.

**Answer: 12** · key ✔

**Solution.** $X$ is geometric with success probability $\tfrac16$. $a=\left(\tfrac56\right)^2\tfrac16$, $b=P(\text{first two fail})=\left(\tfrac56\right)^2$. By memorylessness, $c=\dfrac{(5/6)^5}{(5/6)^3}=\left(\tfrac56\right)^2$. So $\dfrac{b+c}a=\dfrac{2(5/6)^2}{(5/6)^2/6}=12$.

### M-PRB-02 — JEE Main 2024 · 27 Jan Shift 2 · Q80 · MCQ

An urn contains $6$ white and $9$ black balls. Two successive draws of $4$ balls each are made without replacement. The probability that the first draw gives all white balls and the second draw gives all black balls is

(1) $\tfrac5{256}$  (2) $\tfrac5{715}$  (3) $\tfrac3{715}$  (4) $\tfrac3{256}$

**Answer: (3)** · key ✔

**Solution.** $P=\dfrac{{}^6C_4}{{}^{15}C_4}\times\dfrac{{}^9C_4}{{}^{11}C_4}=\dfrac{15}{1365}\times\dfrac{126}{330}=\dfrac1{91}\times\dfrac{21}{55}=\dfrac{3}{715}$.

### M-PRB-03 — JEE Main 2024 · 29 Jan Shift 1 · Q80 · MCQ

A fair die is thrown until $6$ appears. Then the probability that $6$ appears in an even number of throws is

(1) $\tfrac56$  (2) $\tfrac16$  (3) $\tfrac5{11}$  (4) $\tfrac6{11}$

**Answer: (3)** · key ✔

**Solution.** $P=\sum_{k\ge1}\left(\tfrac56\right)^{2k-1}\tfrac16=\dfrac{\tfrac56\cdot\tfrac16}{1-\tfrac{25}{36}}=\dfrac{5/36}{11/36}=\dfrac5{11}$.

### M-PRB-04 — JEE Main 2024 · 29 Jan Shift 2 · Q80 · MCQ

An integer is chosen at random from the integers $1,2,3,\dots,50$. The probability that the chosen integer is a multiple of at least one of $4$, $6$ and $7$ is

(1) $\tfrac8{25}$  (2) $\tfrac{21}{50}$  (3) $\tfrac9{50}$  (4) $\tfrac{14}{25}$

**Answer: (2)** · key ✔

**Solution.** Inclusion–exclusion: multiples of $4$: $12$, of $6$: $8$, of $7$: $7$; of $\text{lcm}(4,6)=12$: $4$, of $28$: $1$, of $42$: $1$, of $84$: $0$. Union $=12+8+7-4-1-1+0=21$. Probability $=\dfrac{21}{50}$.

### M-PRB-05 — JEE Main 2024 · 30 Jan Shift 1 · Q80 · MCQ

Two integers $x$ and $y$ are chosen with replacement from the set $\{0,1,2,3,\dots,10\}$. Then the probability that $|x-y|>5$ is

(1) $\tfrac{30}{121}$  (2) $\tfrac{62}{121}$  (3) $\tfrac{60}{121}$  (4) $\tfrac{31}{121}$

**Answer: (1)** · key ✔

**Solution.** Total outcomes $=11^2=121$. Ordered pairs with $|x-y|=d$: $2(11-d)$. For $d=6,7,8,9,10$: $10+8+6+4+2=30$. Probability $=\dfrac{30}{121}$.

### M-PRB-06 — JEE Main 2024 · 30 Jan Shift 2 · Q80 · MCQ

Bag $A$ contains $3$ white and $7$ red balls and bag $B$ contains $3$ white and $2$ red balls. One bag is selected at random and a ball is drawn from it. The probability of drawing the ball from bag $A$, if the ball drawn is white, is

(1) $\tfrac14$  (2) $\tfrac19$  (3) $\tfrac13$  (4) $\tfrac3{10}$

**Answer: (3)** · key ✔

**Solution.** By Bayes' theorem: $P(A\mid W)=\dfrac{\tfrac12\cdot\tfrac3{10}}{\tfrac12\cdot\tfrac3{10}+\tfrac12\cdot\tfrac35}=\dfrac{3/10}{3/10+6/10}=\dfrac13$.

### M-PRB-07 — JEE Main 2024 · 31 Jan Shift 1 · Q79 · MCQ

Two marbles are drawn in succession, with replacement after each draw, from a box containing $10$ red, $30$ white, $20$ blue and $15$ orange marbles. The probability that the first marble drawn is red and the second is white is

(1) $\tfrac2{25}$  (2) $\tfrac4{25}$  (3) $\tfrac23$  (4) $\tfrac4{75}$

**Answer: (4)** · key ✔

**Solution.** Total $=75$. Draws are independent: $\dfrac{10}{75}\times\dfrac{30}{75}=\dfrac{300}{5625}=\dfrac4{75}$.

### M-PRB-08 — JEE Main 2024 · 31 Jan Shift 1 · Q80 · MCQ

Three rotten apples are accidentally mixed with fifteen good apples. If the random variable $X$ is the number of rotten apples in a draw of two apples, the variance of $X$ is

(1) $\tfrac{37}{153}$  (2) $\tfrac{57}{153}$  (3) $\tfrac{47}{153}$  (4) $\tfrac{40}{153}$

**Answer: (4)** · key ✔

**Solution.** $P(0)=\dfrac{{}^{15}C_2}{{}^{18}C_2}=\dfrac{105}{153}$, $P(1)=\dfrac{3\cdot15}{153}=\dfrac{45}{153}$, $P(2)=\dfrac{3}{153}$. $E[X]=\dfrac{45+6}{153}=\dfrac13$, $E[X^2]=\dfrac{45+12}{153}=\dfrac{57}{153}$. $\text{Var}=\dfrac{57}{153}-\dfrac19=\dfrac{57-17}{153}=\dfrac{40}{153}$.

### M-PRB-09 — JEE Main 2024 · 31 Jan Shift 2 · Q80 · MCQ

A coin is biased so that a head is twice as likely to occur as a tail. If the coin is tossed $3$ times, the probability of getting two tails and one head is

(1) $\tfrac29$  (2) $\tfrac19$  (3) $\tfrac2{27}$  (4) $\tfrac1{27}$

**Answer: (1)** · key ✔

**Solution.** $P(H)=\tfrac23,\ P(T)=\tfrac13$. Two tails and one head: $\binom31\left(\tfrac23\right)\left(\tfrac13\right)^2=3\cdot\tfrac{2}{27}=\tfrac29$.

### M-PRB-10 — JEE Main 2024 · 1 Feb Shift 1 · Q80 · MCQ

A bag contains 8 balls, each white or black. 4 balls are drawn at random without replacement and 2 are white and 2 are black. The probability that the bag contains equal numbers of white and black balls is:

(1) $\dfrac25$  (2) $\dfrac27$  (3) $\dfrac17$  (4) $\dfrac15$

**Answer: (2)** · key ✔

**Solution.** Take every composition $k=0,\dots,8$ of white balls as equally likely. $P(2W,2B\mid k)\propto\binom k2\binom{8-k}2$: $k=2:15$, $k=3:30$, $k=4:36$, $k=5:30$, $k=6:15$, total $126$. Bayes: $P(k=4)=36/126=2/7$.

### M-PRB-11 — JEE Main 2024 · 1 Feb Shift 2 · Q80 · MCQ

The probability that Ajay will not appear in the JEE exam is $p=\tfrac27$, and the probability that both Ajay and Vijay appear is $q=\tfrac15$. The probability that Ajay appears and Vijay does not is:

(1) $\tfrac9{35}$  (2) $\tfrac{18}{35}$  (3) $\tfrac{24}{35}$  (4) $\tfrac3{35}$

**Answer: (2)** · key ✔

**Solution.** $P(\text{Ajay appears})=1-\tfrac27=\tfrac57$. $P(A\cap V^c)=P(A)-P(A\cap V)=\tfrac57-\tfrac15=\dfrac{18}{35}$.

### M-PRB-12 — JEE Main 2024 · 4 Apr Shift 1 · Q80 · MCQ

Three urns A, B, C contain (7 red, 5 black), (5 red, 7 black) and (6 red, 6 black) balls respectively. One urn is chosen at random and a ball is drawn. If the ball is black, the probability that it came from urn A is:

(1) $\tfrac5{18}$  (2) $\tfrac5{16}$  (3) $\tfrac4{17}$  (4) $\tfrac7{18}$

**Answer: (1)** · key ✔

**Solution.** By Bayes with equal priors: $P(A\mid\text{black})=\dfrac{5/12}{5/12+7/12+6/12}=\dfrac5{18}$.

### M-PRB-13 — JEE Main 2024 · 5 Apr Shift 1 · Q80 · MCQ

The coefficients $a,b,c$ in the quadratic equation $ax^2+bx+c=0$ are chosen from $\{1,2,\dots,8\}$. The probability that the equation has repeated roots is:

(1) $\tfrac1{128}$  (2) $\tfrac1{64}$  (3) $\tfrac3{256}$  (4) $\tfrac3{128}$

**Answer: (2)** · key ✔

**Solution.** Total triples $=8^3=512$. Repeated roots need $b^2=4ac$: $b=2$: $ac=1$ ($1$ way); $b=4$: $ac=4$ ($3$ ways); $b=6$: $ac=9$ ($(3,3)$, $1$ way); $b=8$: $ac=16$ ($(2,8),(4,4),(8,2)$, $3$ ways). Total $=8$. $P=\dfrac{8}{512}=\dfrac1{64}$.

### M-PRB-14 — JEE Advanced 2025 · Paper 1 · Q2 · MCQ

Three students $S_1,S_2,S_3$ (solving independently) are given a problem. Events: $U$: at least one solves it; $V$: $S_1$ solves it given that neither $S_2$ nor $S_3$ solves it; $W$: $S_2$ solves it and $S_3$ does not; $T$: $S_3$ solves it. If $P(U)=\tfrac12$, $P(V)=\tfrac1{10}$ and $P(W)=\tfrac1{12}$, then $P(T)$ is

(A) $\tfrac{13}{36}$  (B) $\tfrac13$  (C) $\tfrac{19}{60}$  (D) $\tfrac14$

**Answer: (A)** · official key ✔ (re-derived)

**Solution.** Let $p_i=P(S_i\text{ solves})$. By independence $P(V)=p_1=\tfrac1{10}$. $P(\text{none})=1-P(U)=\tfrac12=(1-p_1)(1-p_2)(1-p_3)\Rightarrow(1-p_2)(1-p_3)=\dfrac{5}{9}$. Also $P(W)=p_2(1-p_3)=\tfrac1{12}$. Adding: $(1-p_3)\big[(1-p_2)+p_2\big]=\dfrac59+\dfrac1{12}=\dfrac{23}{36}$, so $p_3=\dfrac{13}{36}$.

### § — JEE Main 2026 · 21 Jan Shift 2 · set Q1 · MCQ

A random variable $X$ takes the values $0,1,2,3$ with probabilities $\dfrac{2a+1}{30},\ \dfrac{8a-1}{30},\ \dfrac{4a+1}{30},\ b$ respectively, where $a,b\in\mathbb R$. Let $\mu$ and $\sigma$ be the mean and standard deviation of $X$ such that $\sigma^2+\mu^2=2$. Then $\dfrac ab$ is equal to:

(1) 12  (2) 30  (3) 60  (4) 3

**Answer: (3)** · key (compiled)

**Solution.** Total probability $=1$: $\dfrac{14a+1}{30}+b=1\Rightarrow b=\dfrac{29-14a}{30}$. Since $\sigma^2+\mu^2=E(X^2)$, we need $E(X^2)=2$: $\dfrac{8a-1}{30}+4\cdot\dfrac{4a+1}{30}+9b=2\Rightarrow \dfrac{24a+3}{30}+\dfrac{9(29-14a)}{30}=2\Rightarrow 264-102a=60\Rightarrow a=2$. Then $b=\dfrac1{30}$ and $\dfrac ab=60$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q2 · Numerical

From the first 100 natural numbers, two numbers $a$ and then $b$ are selected at random without replacement. If the probability that $a-b\ge10$ is $\dfrac mn$, $\gcd(m,n)=1$, then $m+n$ is equal to ______.

**Answer: 311** · key (compiled)

**Solution.** Ordered pairs $(a,b)$ with $a\ne b$: $100\cdot99=9900$. For a fixed difference $d=a-b$ ($10\le d\le99$) there are $100-d$ pairs, so the favourable count is $\sum_{d=10}^{99}(100-d)=1+2+\cdots+90=\dfrac{90\cdot91}2=4095$. Probability $=\dfrac{4095}{9900}=\dfrac{91}{220}$, so $m+n=91+220=311$.

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q3 · MCQ

The probability distribution of a random variable $X$ is given below:

| $X$ | $4k$ | $\tfrac{30}7k$ | $\tfrac{32}7k$ | $\tfrac{34}7k$ | $\tfrac{36}7k$ | $\tfrac{38}7k$ | $\tfrac{40}7k$ | $6k$ |
|---|---|---|---|---|---|---|---|---|
| $P(X)$ | $\tfrac2{15}$ | $\tfrac1{15}$ | $\tfrac2{15}$ | $\tfrac15$ | $\tfrac1{15}$ | $\tfrac2{15}$ | $\tfrac15$ | $\tfrac1{15}$ |

If $E(X)=\dfrac{263}{15}$, then $P(X<20)$ is equal to:

(1) $\dfrac{11}{15}$  (2) $\dfrac35$  (3) $\dfrac{14}{15}$  (4) $\dfrac8{15}$

**Answer: (1)** · key (compiled)

**Solution.** Writing every probability over 105 and multiplying by the values: $E(X)=\dfrac k{105}(56+30+64+102+36+76+120+42)=\dfrac{526k}{105}=\dfrac{263}{15}\Rightarrow k=\dfrac72$. The values are therefore $14,15,16,17,18,19,20,21$. $P(X<20)=P(14)+\dots+P(19)=\dfrac{2+1+2+3+1+2}{15}=\dfrac{11}{15}$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q4 · Numerical

Let $S$ be a set of 5 elements and $P(S)$ denote the power set of $S$. Let $E$ be the event of choosing an ordered pair $(A,B)$ from $P(S)\times P(S)$ such that $A\cap B=\emptyset$. If the probability of the event $E$ is $\dfrac{3^p}{2^q}$, where $p,q\in\mathbb N$, then $p+q$ is equal to ______.

**Answer: 15** · key (compiled)

**Solution.** Total ordered pairs $=2^5\cdot2^5=2^{10}$. For $A\cap B=\emptyset$ each of the 5 elements goes to $A$ only, $B$ only, or neither: $3^5$ ways. $P(E)=\dfrac{3^5}{2^{10}}$, so $p=5$, $q=10$ and $p+q=15$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q5 · MCQ

If a random variable $x$ has the probability distribution

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $P(x)$ | 0 | $2k$ | $k$ | $3k$ | $2k^2$ | $2k$ | $k^2+k$ | $7k^2$ |

then $P(3<x\le6)$ is equal to:

(1) 0.64  (2) 0.22  (3) 0.33  (4) 0.34

**Answer: (3)** · key (compiled)

**Solution.** $\sum P=9k+10k^2=1\Rightarrow(10k-1)(k+1)=0\Rightarrow k=\dfrac1{10}$ (probabilities are non-negative). $P(3<x\le6)=P(4)+P(5)+P(6)=2k^2+2k+(k^2+k)=3k^2+3k=0.03+0.30=0.33$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q6 · MCQ

Two distinct numbers $a$ and $b$ are selected at random from $1,2,3,\dots,50$. The probability that their product $ab$ is divisible by 3 is:

(1) $\dfrac{272}{1225}$  (2) $\dfrac{561}{1225}$  (3) $\dfrac{664}{1225}$  (4) $\dfrac8{25}$

**Answer: (3)** · key (compiled)

**Solution.** The product is divisible by 3 unless neither number is a multiple of 3. There are 16 multiples of 3 and 34 non-multiples in $1..50$. $P(\text{neither})=\dfrac{\binom{34}2}{\binom{50}2}=\dfrac{34\cdot33}{50\cdot49}=\dfrac{561}{1225}$, so $P(3\mid ab)=1-\dfrac{561}{1225}=\dfrac{664}{1225}$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q7 · MCQ

Bag A contains 9 white and 8 black balls, while bag B contains 6 white and 4 black balls. One ball is randomly picked from bag B and mixed with the balls in bag A. Then a ball is randomly drawn from bag A. If the probability that the ball drawn is white is $\dfrac pq$, $\gcd(p,q)=1$, then $p+q$ is equal to:

(1) 23  (2) 24  (3) 21  (4) 22

**Answer: (1)** · key (compiled)

**Solution.** Condition on the colour moved from B to A (theorem of total probability). If a white ball is moved (prob. $\tfrac6{10}$), A has 10 white out of 18; if a black ball is moved (prob. $\tfrac4{10}$), A has 9 white out of 18. $P(W)=\dfrac6{10}\cdot\dfrac{10}{18}+\dfrac4{10}\cdot\dfrac9{18}=\dfrac{60+36}{180}=\dfrac8{15}$, so $p+q=23$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q8 · MCQ

A bag contains 10 balls out of which $k$ are red and $(10-k)$ are black, where $0\le k\le10$. If three balls are drawn at random without replacement and all of them are found to be black, then the probability that the bag contains 1 red and 9 black balls is:

(1) $\dfrac{14}{55}$  (2) $\dfrac7{55}$  (3) $\dfrac7{110}$  (4) $\dfrac7{11}$

**Answer: (1)** · key (compiled)

**Solution.** All 11 compositions ($k=0,\dots,10$) are taken as equally likely a priori. With $j=10-k$ black balls, $P(\text{3 black}\mid j)=\dfrac{\binom j3}{\binom{10}3}$. By Bayes' theorem, $P(j=9\mid\text{3 black})=\dfrac{\binom93}{\sum_{j=3}^{10}\binom j3}=\dfrac{84}{\binom{11}4}=\dfrac{84}{330}=\dfrac{14}{55}$ (hockey-stick identity for the sum).

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q9 · MCQ

From a lot containing 10 defective and 90 non-defective bulbs, 8 bulbs are selected one by one with replacement. Then the probability of getting at least 7 defective bulbs is:

(1) $\dfrac{67}{10^8}$  (2) $\dfrac7{10^7}$  (3) $\dfrac{81}{10^8}$  (4) $\dfrac{73}{10^8}$

**Answer: (4)** · key (compiled)

**Solution.** Each draw is defective with probability $p=\dfrac1{10}$ (binomial, $n=8$). $P(X\ge7)=\binom87p^7q+\binom88p^8=8\cdot\dfrac{9}{10^8}+\dfrac1{10^8}=\dfrac{73}{10^8}$.

### § — JEE Main 2025 · Jan session · set Q1 · MCQ

Let $A=[a_{ij}]$ be a square matrix of order 2 with entries either 0 or 1. Let $E$ be the event that $A$ is an invertible matrix. Then the probability $P(E)$ is:

(1) $\tfrac3{16}$  (2) $\tfrac58$  (3) $\tfrac38$  (4) $\tfrac18$

**Answer: (3)** · key (compiled)

**Solution.** There are $2^4=16$ matrices. $|A|=a_{11}a_{22}-a_{12}a_{21}\ne0$ needs exactly one of the two products to be 1: $a_{11}a_{22}=1$ and $a_{12}a_{21}=0$ (3 ways) or the reverse (3 ways). That is 6 matrices, so $P(E)=\tfrac6{16}=\tfrac38$.

### § — JEE Main 2025 · Jan session · set Q2 · MCQ

Two numbers $k_1$ and $k_2$ are randomly chosen from the set of natural numbers. Then the probability that the value of $i^{k_1}+i^{k_2}$ ($i=\sqrt{-1}$) is non-zero equals:

(1) $\tfrac12$  (2) $\tfrac34$  (3) $\tfrac14$  (4) $\tfrac23$

**Answer: (2)** · key (compiled)

**Solution.** The powers of $i$ cycle with period 4, so each of $i,-1,-i,1$ is equally likely. The sum is zero exactly when $i^{k_2}=-i^{k_1}$, which has probability $\tfrac14$ (for any $k_1$ one of the four residues of $k_2$ works). Non-zero: $\tfrac34$.

### § — JEE Main 2025 · Jan session · set Q3 · MCQ

Let $S$ be the set of all words that can be formed by arranging all the letters of the word GARDEN. From the set $S$, one word is selected at random. The probability that the selected word will NOT have vowels in alphabetical order is:

(1) $\tfrac12$  (2) $\tfrac14$  (3) $\tfrac23$  (4) $\tfrac13$

**Answer: (1)** · key (compiled)

**Solution.** The two vowels A and E can appear as A…E or E…A with equal frequency (by symmetry), so half the words have them in alphabetical order. The required probability is $\tfrac12$.

### § — JEE Main 2025 · Jan session · set Q4 · MCQ

Two balls are selected at random one by one without replacement from a bag containing 4 white and 6 black balls. If the probability that the first selected ball is black, given that the second selected ball is also black, is $\dfrac mn$, where $\gcd(m,n)=1$, then $m+n$ is equal to:

(1) 4  (2) 14  (3) 13  (4) 11

**Answer: (2)** · key (compiled)

**Solution.** $P(\text{2nd black})=\dfrac6{10}$ and $P(\text{both black})=\dfrac6{10}\cdot\dfrac59=\dfrac13$. $P(\text{1st black}\mid\text{2nd black})=\dfrac{1/3}{3/5}=\dfrac59$, so $m+n=14$.

### § — JEE Main 2025 · Jan session · set Q5 · MCQ

A coin is tossed three times. Let $X$ denote the number of times a tail follows a head. If $\mu$ and $\sigma^2$ denote the mean and variance of $X$, then the value of $64(\mu+\sigma^2)$ is:

(1) 51  (2) 64  (3) 32  (4) 48

**Answer: (4)** · key (compiled)

**Solution.** "HT" occurs once in HHT, HTH, HTT and THT (4 of the 8 outcomes) and not at all in HHH, THH, TTH, TTT. So $X\in\{0,1\}$ with probability $\tfrac12$ each: $\mu=\tfrac12$, $\sigma^2=\tfrac14$, and $64\cdot\tfrac34=48$.

### § — JEE Main 2025 · Jan session · set Q6 · MCQ

One die has two faces marked 1, two faces marked 2, one face marked 3 and one face marked 4. Another die has one face marked 1, two faces marked 2, two faces marked 3 and one face marked 4. The probability of getting the sum of numbers to be 4 or 5, when both the dice are thrown together, is:

(1) $\tfrac23$  (2) $\tfrac12$  (3) $\tfrac49$  (4) $\tfrac35$

**Answer: (2)** · key (compiled)

**Solution.** Counting favourable cases out of 36 (weights = number of faces). Sum 4: (1,3): $2\cdot2$, (2,2): $2\cdot2$, (3,1): $1\cdot1$ = 9. Sum 5: (1,4): $2\cdot1$, (2,3): $2\cdot2$, (3,2): $1\cdot2$, (4,1): $1\cdot1$ = 9. Probability $=\dfrac{18}{36}=\dfrac12$.

### § — JEE Main 2025 · Jan session · set Q8 · MCQ

$A$ and $B$ alternately throw a pair of dice. $A$ wins if he throws a sum of 5 before $B$ throws a sum of 8, and $B$ wins if he throws a sum of 8 before $A$ throws a sum of 5. The probability that $A$ wins if $A$ makes the first throw is:

(1) $\tfrac8{17}$  (2) $\tfrac9{19}$  (3) $\tfrac9{17}$  (4) $\tfrac8{19}$

**Answer: (2)** · key (compiled)

**Solution.** $p=P(\text{sum}=5)=\tfrac4{36}=\tfrac19$ and $q=P(\text{sum}=8)=\tfrac5{36}$. $P(A\text{ wins})=\dfrac p{1-(1-p)(1-q)}=\dfrac{1/9}{1-\frac89\cdot\frac{31}{36}}=\dfrac{1/9}{76/324}=\dfrac9{19}$.

### § — JEE Main 2025 · Jan session · set Q9 · MCQ

If $A$ and $B$ are two events such that $P(A\cap B)=0.1$, and $P(A\mid B)$ and $P(B\mid A)$ are the roots of the equation $12x^2-7x+1=0$, then the value of $\dfrac{P(\bar A\cup\bar B)}{P(\bar A\cap\bar B)}$ is:

(1) $\tfrac43$  (2) $\tfrac74$  (3) $\tfrac53$  (4) $\tfrac94$

**Answer: (4)** · key (compiled)

**Solution.** The roots are $\tfrac13$ and $\tfrac14$, so $\dfrac{0.1}{P(B)}$ and $\dfrac{0.1}{P(A)}$ are $\tfrac13,\tfrac14$: $\{P(A),P(B)\}=\{0.3,0.4\}$. $P(A\cup B)=0.3+0.4-0.1=0.6$. $\dfrac{P(\bar A\cup\bar B)}{P(\bar A\cap\bar B)}=\dfrac{1-P(A\cap B)}{1-P(A\cup B)}=\dfrac{0.9}{0.4}=\dfrac94$.

### § — JEE Main 2025 · Jan session · set Q10 · MCQ

Bag 1 contains 4 white balls and 5 black balls, and Bag 2 contains $n$ white balls and 3 black balls. One ball is drawn randomly from Bag 1 and transferred to Bag 2. A ball is then drawn randomly from Bag 2. If the probability that the ball drawn is white is $\dfrac{29}{45}$, then $n$ is equal to:

(1) 6  (2) 3  (3) 5  (4) 4

**Answer: (1)** · key (compiled)

**Solution.** Total probability: $\dfrac49\cdot\dfrac{n+1}{n+4}+\dfrac59\cdot\dfrac n{n+4}=\dfrac{9n+4}{9(n+4)}=\dfrac{29}{45}\Rightarrow5(9n+4)=29(n+4)\Rightarrow16n=96$, so $n=6$.

### § — JEE Main 2025 · Apr session · set Q1 · Numerical

A card from a pack of 52 cards is lost. From the remaining 51 cards, $n$ cards are drawn and are found to be spades. If the probability of the lost card being a spade is $\tfrac{11}{50}$, then $n$ is equal to ______.

**Answer: 2** · key (compiled)

**Solution.** By Bayes' theorem, $P(\text{lost spade}\mid n\text{ spades drawn})=\dfrac{\frac14\binom{12}n}{\frac14\binom{12}n+\frac34\binom{13}n}$. For $n=2$: $\dfrac{66}{66+3\cdot78}=\dfrac{66}{300}=\dfrac{11}{50}$. So $n=2$.

### § — JEE Main 2025 · Apr session · set Q2 · MCQ

If the probability that the random variable $X$ takes the value $x$ is given by $P(X=x)=k(x+1)3^{-x}$, $x=0,1,2,3,\dots$, where $k$ is a constant, then $P(X\ge3)$ is equal to:

(1) $\tfrac7{27}$  (2) $\tfrac49$  (3) $\tfrac8{27}$  (4) $\tfrac19$

**Answer: (4)** · key (compiled)

**Solution.** $\sum_{x\ge0}(x+1)r^x=\dfrac1{(1-r)^2}$ with $r=\tfrac13$ equals $\tfrac94$, so $k=\tfrac49$. $P(X<3)=k\left(1+\tfrac23+\tfrac39\right)=\tfrac49\cdot2=\tfrac89$, hence $P(X\ge3)=\tfrac19$.

### § — JEE Main 2025 · Apr session · set Q3 · MCQ

The probability of forming a 12-person committee from 4 engineers, 2 doctors and 10 professors containing at least 3 engineers and at least 1 doctor is:

(1) $\tfrac{129}{182}$  (2) $\tfrac{103}{182}$  (3) $\tfrac{17}{26}$  (4) $\tfrac{19}{26}$

**Answer: (1)** · key (compiled)

**Solution.** Total ways $\binom{16}{12}=1820$. Favourable (engineers, doctors, professors): (3,1,8): $4\cdot2\cdot45=360$; (3,2,7): $4\cdot1\cdot120=480$; (4,1,7): $1\cdot2\cdot120=240$; (4,2,6): $1\cdot1\cdot210=210$. Sum $=1290$, so the probability is $\dfrac{1290}{1820}=\dfrac{129}{182}$.

### § — JEE Main 2025 · Apr session · set Q4 · MCQ

Given three identical bags each containing 10 balls, whose colours are as follows: Bag I — Red 3, Blue 2, Green 5; Bag II — Red 4, Blue 3, Green 3; Bag III — Red 5, Blue 1, Green 4. A person chooses a bag at random and takes out a ball. If the ball is Red, the probability that it is from Bag I is $p$, and if the ball is Green, the probability that it is from Bag III is $q$. Then the value of $\left(\dfrac1p+\dfrac1q\right)$ is:

(1) 6  (2) 9  (3) 7  (4) 8

**Answer: (3)** · key (compiled)

**Solution.** Red: $p=\dfrac{3}{3+4+5}=\dfrac14$. Green: $q=\dfrac4{5+3+4}=\dfrac13$. $\dfrac1p+\dfrac1q=4+3=7$.

### § — JEE Main 2025 · Apr session · set Q5 · MCQ

A bag contains 19 unbiased coins and one coin with head on both sides. One coin drawn at random is tossed and head turns up. If the probability that the drawn coin was unbiased is $\dfrac mn$, $\gcd(m,n)=1$, then $n^2-m^2$ is equal to:

(1) 80  (2) 60  (3) 72  (4) 64

**Answer: (1)** · key (compiled)

**Solution.** $P(\text{unbiased}\mid H)=\dfrac{\frac{19}{20}\cdot\frac12}{\frac{19}{20}\cdot\frac12+\frac1{20}\cdot1}=\dfrac{19}{21}$. So $n^2-m^2=441-361=80$.

### § — JEE Main 2025 · Apr session · set Q6 · MCQ

A box contains 10 pens of which 3 are defective. A sample of 2 pens is drawn at random and let $X$ denote the number of defective pens. Then the variance of $X$ is:

(1) $\tfrac{11}{15}$  (2) $\tfrac{28}{75}$  (3) $\tfrac2{15}$  (4) $\tfrac35$

**Answer: (2)** · key (compiled)

**Solution.** $P(0)=\dfrac{21}{45}$, $P(1)=\dfrac{21}{45}$, $P(2)=\dfrac3{45}$. $E(X)=\dfrac{27}{45}=\dfrac35$, $E(X^2)=\dfrac{21+12}{45}=\dfrac{11}{15}$. $\text{Var}=\dfrac{11}{15}-\dfrac9{25}=\dfrac{28}{75}$.

### § — JEE Main 2025 · Apr session · set Q7 · MCQ

Let a random variable $X$ take values $0,1,2,3$ with $P(X=0)=P(X=1)=p$, $P(X=2)=P(X=3)$ and $E(X^2)=2E(X)$. Then the value of $8p-1$ is:

(1) 0  (2) 2  (3) 1  (4) 3

**Answer: (2)** · key (compiled)

**Solution.** Let $P(X=2)=P(X=3)=q$, with $2p+2q=1$. $E(X)=p+5q$ and $E(X^2)=p+13q$. The condition $p+13q=2p+10q$ gives $p=3q$; then $8q=1$, $q=\tfrac18$, $p=\tfrac38$ and $8p-1=2$.

### § — JEE Main 2025 · Apr session · set Q10 · MCQ

If $A$ and $B$ are two events such that $P(A)=0.7$, $P(B)=0.4$ and $P(A\cap\bar B)=0.5$, where $\bar B$ denotes the complement of $B$, then $P\big(B\mid(A\cup\bar B)\big)$ is equal to:

(1) $\tfrac14$  (2) $\tfrac12$  (3) $\tfrac16$  (4) $\tfrac13$

**Answer: (1)** · key (compiled)

**Solution.** $P(A\cap B)=0.7-0.5=0.2$. $A\cup\bar B$ is the complement of $\bar A\cap B$, with $P(\bar A\cap B)=0.4-0.2=0.2$, so $P(A\cup\bar B)=0.8$. $B\cap(A\cup\bar B)=A\cap B$. Hence $\dfrac{0.2}{0.8}=\dfrac14$.

