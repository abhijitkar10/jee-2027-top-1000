# Statistics

> Theory: [../../theory/maths/statistics.md](../../theory/maths/statistics.md)

### M-STA-01 · C — JEE Main 2026 · 23 Jan Shift 1 · set Q1 · MCQ

Let the mean and variance of the 8 numbers $-10,-7,-1,x,y,9,2,16$ be $\dfrac72$ and $\dfrac{293}4$ respectively. Then the mean of the 4 numbers $x,\ y,\ x+y+1,\ |x-y|$ is:

(1) 11  (2) 12  (3) 10  (4) 9

**Answer: (1)** · key (compiled)

**Solution.** Sum $=8\cdot\tfrac72=28$ and the known numbers add to $9$, so $x+y=19$. Variance gives $\sum x_i^2=8\left(\tfrac{293}4+\tfrac{49}4\right)=684$; the known squares add to $491$, so $x^2+y^2=193$. Then $2xy=19^2-193=168$, $xy=84$ and $(x-y)^2=361-336=25$, so $|x-y|=5$ (the numbers are $12$ and $7$). Required mean $=\dfrac{x+y+(x+y+1)+|x-y|}4=\dfrac{19+20+5}4=11$.

### M-STA-02 · C — JEE Main 2026 · 24 Jan Shift 2 · set Q2 · MCQ

Let $X=\{x\in\mathbb N:1\le x\le19\}$ and, for some $a,b\in\mathbb R$, $Y=\{ax+b:x\in X\}$. If the mean and variance of the elements of $Y$ are $30$ and $750$ respectively, then the sum of all possible values of $b$ is:

(1) 60  (2) 100  (3) 80  (4) 20

**Answer: (1)** · key (compiled)

**Solution.** For $X=\{1,\dots,19\}$: mean $=10$ and variance $=\dfrac{19^2-1}{12}=30$. For $Y=aX+b$: variance $=a^2\cdot30=750\Rightarrow a=\pm5$, and mean $=10a+b=30\Rightarrow b=30-10a$. So $b=-20$ (for $a=5$) or $b=80$ (for $a=-5$); the sum is $60$.

### M-STA-03 · C — JEE Main 2026 · 22 Jan Shift 2 · set Q3 · MCQ

If the mean deviation about the median of the numbers $k,2k,3k,\dots,1000k$ is $500$, then $k^2$ is equal to:

(1) 9  (2) 1  (3) 4  (4) 16

**Answer: (3)** · key (compiled)

**Solution.** With $n=1000$ the median is $\dfrac{500k+501k}2=500.5k$. Mean deviation $=\dfrac{k}{1000}\sum_{i=1}^{1000}|i-500.5|=\dfrac k{1000}\cdot2\sum_{i=1}^{500}(500.5-i)=\dfrac k{1000}\cdot2\cdot125000=250k$. So $250k=500$, $k=2$ and $k^2=4$.

### M-STA-04 · C — JEE Main 2026 · 23 Jan Shift 2 · set Q4 · MCQ

If the mean and the variance of the data

| Class | 4–8 | 8–12 | 12–16 | 16–20 |
|---|---|---|---|---|
| Frequency | 3 | $\lambda$ | 4 | 7 |

are $\mu$ and $19$ respectively, then the value of $\lambda+\mu$ is:

(1) 21  (2) 19  (3) 20  (4) 18

**Answer: (2)** · key (compiled)

**Solution.** Class marks $6,10,14,18$; $N=14+\lambda$. $\sum fx=200+10\lambda$ and $\sum fx^2=3160+100\lambda$. Variance $=\dfrac{\sum fx^2}N-\mu^2=19$ gives $(3160+100\lambda)(14+\lambda)-(200+10\lambda)^2=19(14+\lambda)^2$, which simplifies to $19\lambda^2-28\lambda-516=0$, so $\lambda=6$. Then $\mu=\dfrac{260}{20}=13$ and $\lambda+\mu=19$.

### M-STA-05 · C — JEE Main 2024 · 27 Jan Shift 1 · Q70 · MCQ

Let $a_1,a_2,\dots,a_{10}$ be observations such that $\sum_{k=1}^{10}a_k=50$ and $\sum_{k<j}a_ka_j=1100$. The standard deviation of $a_1,\dots,a_{10}$ is

(1) 5  (2) $\sqrt5$  (3) 10  (4) $\sqrt{115}$

**Answer: (2)** · key ✔

**Solution.** $(\sum a_k)^2=\sum a_k^2+2\sum_{k<j}a_ka_j\Rightarrow2500=\sum a_k^2+2200\Rightarrow\sum a_k^2=300$. Variance $=\dfrac{300}{10}-\left(\dfrac{50}{10}\right)^2=30-25=5$, so SD $=\sqrt5$.

### M-STA-06 · C — JEE Main 2024 · 27 Jan Shift 2 · Q85 · Numerical

The mean and standard deviation of $15$ observations were found to be $12$ and $3$. On rechecking, one observation was found to have been read as $10$ instead of $12$. If $\mu$ and $\sigma^2$ denote the mean and variance of the correct observations, then $15\left(\mu+\mu^2+\sigma^2\right)$ is equal to ______.

**Answer: 2521** · key ✔

**Solution.** Correct sum $=15\cdot12-10+12=182$, so $15\mu=182$. Original $\sum x_i^2=15(9+144)=2295$; corrected $\sum x_i^2=2295-100+144=2339$. Since $\mu^2+\sigma^2=\dfrac{\sum x_i^2}{15}$: $15(\mu+\mu^2+\sigma^2)=182+2339=2521$.

