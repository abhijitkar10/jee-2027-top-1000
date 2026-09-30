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

