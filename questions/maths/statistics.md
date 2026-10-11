# Statistics

> Theory: [../../theory/maths/statistics.md](../../theory/maths/statistics.md)

### M-STA-01 — JEE Main 2024 · 27 Jan Shift 1 · Q70 · MCQ

Let $a_1,a_2,\dots,a_{10}$ be observations such that $\sum_{k=1}^{10}a_k=50$ and $\sum_{k<j}a_ka_j=1100$. The standard deviation of $a_1,\dots,a_{10}$ is

(1) 5  (2) $\sqrt5$  (3) 10  (4) $\sqrt{115}$

**Answer: (2)** · key ✔

**Solution.** $(\sum a_k)^2=\sum a_k^2+2\sum_{k<j}a_ka_j\Rightarrow2500=\sum a_k^2+2200\Rightarrow\sum a_k^2=300$. Variance $=\dfrac{300}{10}-\left(\dfrac{50}{10}\right)^2=30-25=5$, so SD $=\sqrt5$.

### M-STA-02 — JEE Main 2024 · 27 Jan Shift 2 · Q85 · Numerical

The mean and standard deviation of $15$ observations were found to be $12$ and $3$. On rechecking, one observation was found to have been read as $10$ instead of $12$. If $\mu$ and $\sigma^2$ denote the mean and variance of the correct observations, then $15\left(\mu+\mu^2+\sigma^2\right)$ is equal to ______.

**Answer: 2521** · key ✔

**Solution.** Correct sum $=15\cdot12-10+12=182$, so $15\mu=182$. Original $\sum x_i^2=15(9+144)=2295$; corrected $\sum x_i^2=2295-100+144=2339$. Since $\mu^2+\sigma^2=\dfrac{\sum x_i^2}{15}$: $15(\mu+\mu^2+\sigma^2)=182+2339=2521$.

### M-STA-03 — JEE Main 2024 · 29 Jan Shift 1 · Q86 · Numerical

If the mean and variance of the data $65,68,58,44,48,45,60,\alpha,\beta,60$, where $\alpha>\beta$, are $56$ and $66.2$ respectively, then $\alpha^2+\beta^2$ is equal to ______.

**Answer: 6344** · key ✔

**Solution.** $\sum x=560$ and the known values sum to $448$, so $\alpha+\beta=112$. Variance: $\dfrac{\sum x^2}{10}-56^2=66.2\Rightarrow\sum x^2=32022$. The known squares sum to $4225+4624+3364+1936+2304+2025+3600+3600=25678$. Hence $\alpha^2+\beta^2=32022-25678=6344$.

### M-STA-04 — JEE Main 2024 · 29 Jan Shift 2 · Q68 · MCQ

If the mean and variance of five observations are $\dfrac{24}5$ and $\dfrac{194}{25}$ respectively and the mean of the first four observations is $\dfrac72$, then the variance of the first four observations is equal to

(1) $\tfrac45$  (2) $\tfrac{77}{12}$  (3) $\tfrac54$  (4) $\tfrac{105}4$

**Answer: (3)** · key ✔

**Solution.** Total $=24$; the first four sum to $14$, so the fifth is $10$. $\sum x_i^2=5\left(\tfrac{194}{25}+\tfrac{576}{25}\right)=154$. For the first four: $\sum x^2=154-100=54$. Variance $=\dfrac{54}4-\left(\tfrac72\right)^2=13.5-12.25=\tfrac54$.

### M-STA-05 — JEE Main 2024 · 30 Jan Shift 2 · Q86 · Numerical

For the data below, the variance is $\sigma^2=k$. Find $[k]$, where $[\cdot]$ denotes the greatest integer function.

| $x_i$ | 0 | 1 | 5 | 6 | 10 | 12 | 17 |
|---|---|---|---|---|---|---|---|
| $f_i$ | 3 | 2 | 3 | 2 | 6 | 3 | 3 |

**Answer: 29** · key ✔

**Solution.** $N=22$, $\sum f_ix_i=0+2+15+12+60+36+51=176$, so the mean is $8$. $\sum f_ix_i^2=0+2+75+72+600+432+867=2048$. Variance $=\dfrac{2048}{22}-64=93.09-64=29.09$, so $[k]=29$.

### M-STA-06 — JEE Main 2024 · 31 Jan Shift 2 · Q70 · MCQ

The mean and the variance of the $6$ observations $a,b,68,44,48,60$ are $55$ and $194$ respectively. If $a>b$, then $a+3b$ is

(1) 200  (2) 190  (3) 180  (4) 210

**Answer: (3)** · key ✔

**Solution.** Sum $=330\Rightarrow a+b=330-220=110$. $\sum x^2=6(55^2+194)=19314$; known squares sum to $4624+1936+2304+3600=12464$, so $a^2+b^2=6850$. Then $2ab=110^2-6850=5250\Rightarrow ab=2625$. $a,b$ are roots of $t^2-110t+2625=0\Rightarrow t=75,35$. With $a>b$: $a+3b=75+105=180$.

### § — JEE Main 2026 · 23 Jan Shift 1 · set Q1 · MCQ

Let the mean and variance of the 8 numbers $-10,-7,-1,x,y,9,2,16$ be $\dfrac72$ and $\dfrac{293}4$ respectively. Then the mean of the 4 numbers $x,\ y,\ x+y+1,\ |x-y|$ is:

(1) 11  (2) 12  (3) 10  (4) 9

**Answer: (1)** · key (compiled)

**Solution.** Sum $=8\cdot\tfrac72=28$ and the known numbers add to $9$, so $x+y=19$. Variance gives $\sum x_i^2=8\left(\tfrac{293}4+\tfrac{49}4\right)=684$; the known squares add to $491$, so $x^2+y^2=193$. Then $2xy=19^2-193=168$, $xy=84$ and $(x-y)^2=361-336=25$, so $|x-y|=5$ (the numbers are $12$ and $7$). Required mean $=\dfrac{x+y+(x+y+1)+|x-y|}4=\dfrac{19+20+5}4=11$.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q2 · MCQ

Let $X=\{x\in\mathbb N:1\le x\le19\}$ and, for some $a,b\in\mathbb R$, $Y=\{ax+b:x\in X\}$. If the mean and variance of the elements of $Y$ are $30$ and $750$ respectively, then the sum of all possible values of $b$ is:

(1) 60  (2) 100  (3) 80  (4) 20

**Answer: (1)** · key (compiled)

**Solution.** For $X=\{1,\dots,19\}$: mean $=10$ and variance $=\dfrac{19^2-1}{12}=30$. For $Y=aX+b$: variance $=a^2\cdot30=750\Rightarrow a=\pm5$, and mean $=10a+b=30\Rightarrow b=30-10a$. So $b=-20$ (for $a=5$) or $b=80$ (for $a=-5$); the sum is $60$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q3 · MCQ

If the mean deviation about the median of the numbers $k,2k,3k,\dots,1000k$ is $500$, then $k^2$ is equal to:

(1) 9  (2) 1  (3) 4  (4) 16

**Answer: (3)** · key (compiled)

**Solution.** With $n=1000$ the median is $\dfrac{500k+501k}2=500.5k$. Mean deviation $=\dfrac{k}{1000}\sum_{i=1}^{1000}|i-500.5|=\dfrac k{1000}\cdot2\sum_{i=1}^{500}(500.5-i)=\dfrac k{1000}\cdot2\cdot125000=250k$. So $250k=500$, $k=2$ and $k^2=4$.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q4 · MCQ

If the mean and the variance of the data

| Class | 4–8 | 8–12 | 12–16 | 16–20 |
|---|---|---|---|---|
| Frequency | 3 | $\lambda$ | 4 | 7 |

are $\mu$ and $19$ respectively, then the value of $\lambda+\mu$ is:

(1) 21  (2) 19  (3) 20  (4) 18

**Answer: (2)** · key (compiled)

**Solution.** Class marks $6,10,14,18$; $N=14+\lambda$. $\sum fx=200+10\lambda$ and $\sum fx^2=3160+100\lambda$. Variance $=\dfrac{\sum fx^2}N-\mu^2=19$ gives $(3160+100\lambda)(14+\lambda)-(200+10\lambda)^2=19(14+\lambda)^2$, which simplifies to $19\lambda^2-28\lambda-516=0$, so $\lambda=6$. Then $\mu=\dfrac{260}{20}=13$ and $\lambda+\mu=19$.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q5 · MCQ

Let the mean and variance of the 7 observations $2,4,10,x,12,14,y$ ($x>y$) be $8$ and $16$ respectively. Two numbers are chosen from $\{1,2,3,x-4,y,5\}$ one after another without replacement. Then the probability that the smaller number among the two chosen numbers is less than $4$ is:

(1) $\dfrac35$  (2) $\dfrac13$  (3) $\dfrac25$  (4) $\dfrac45$

**Answer: (4)** · key (compiled)

**Solution.** Sum $=56$ and the known terms add to $42$, so $x+y=14$. $\sum x_i^2=7(16+64)=560$ and the known squares add to $460$, so $x^2+y^2=100$. Hence $xy=\dfrac{196-100}2=48$ and, with $x>y$, $x=8$, $y=6$. The set is $\{1,2,3,4,5,6\}$. The smaller number is not less than $4$ only when both numbers come from $\{4,5,6\}$: probability $\dfrac{\binom32}{\binom62}=\dfrac15$. Required probability $=1-\dfrac15=\dfrac45$.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q6 · MCQ

The mean and variance of 10 observations are $9$ and $34.2$ respectively. If 8 of these observations are $2,3,5,10,11,13,15,21$, then the mean deviation about the median of all the 10 observations is:

(1) 4  (2) 7  (3) 5  (4) 6

**Answer: (3)** · key (compiled)

**Solution.** Let the two unknown observations be $a,b$. Sum: $a+b=90-80=10$. Squares: $a^2+b^2=10(34.2+81)-1094=58$, so $ab=\dfrac{100-58}2=21$ and $\{a,b\}=\{3,7\}$. The ordered data are $2,3,3,5,7,10,11,13,15,21$ with median $\dfrac{7+10}2=8.5$. $\sum|x_i-8.5|=6.5+5.5+5.5+3.5+1.5+1.5+2.5+4.5+6.5+12.5=50$, so the mean deviation is $\dfrac{50}{10}=5$.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q7 · MCQ

The mean and variance of a data of 10 observations are $10$ and $2$ respectively. If an observation $\alpha$ in this data is replaced by $\beta$, then the mean and variance become $10.1$ and $1.99$ respectively. Then $\alpha+\beta$ equals:

(1) 15  (2) 5  (3) 10  (4) 20

**Answer: (4)** · key (compiled)

**Solution.** Sums: $10\cdot10.1-10\cdot10=\beta-\alpha=1$. Sums of squares: originally $10(2+100)=1020$, afterwards $10(1.99+10.1^2)=1040$, so $\beta^2-\alpha^2=20$. Hence $\alpha+\beta=\dfrac{20}{\beta-\alpha}=20$.

