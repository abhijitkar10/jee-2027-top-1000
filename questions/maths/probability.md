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

