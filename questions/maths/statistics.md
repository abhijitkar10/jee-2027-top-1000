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

