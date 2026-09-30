# Limits, Continuity & Differentiability

> Theory: [../../theory/maths/limits-continuity-differentiability.md](../../theory/maths/limits-continuity-differentiability.md)

### M-LCD-01 — JEE Main 2024 · 27 Jan Shift 1 · Q69 · MCQ

Let $a=\displaystyle\lim_{x\to0}\frac{\sqrt{1+\sqrt{1+x^4}}-\sqrt2}{x^4}$ and $b=\displaystyle\lim_{x\to0}\frac{\sin^2x}{\sqrt2-\sqrt{1+\cos x}}$. Then $ab^3$ is

(1) 36  (2) 32  (3) 25  (4) 30

**Answer: (2)** · key ✔

**Solution.** With $u=x^4$: $\dfrac{d}{du}\sqrt{1+\sqrt{1+u}}\Big|_0=\dfrac1{2\sqrt2}\cdot\dfrac12$, so $a=\dfrac1{4\sqrt2}$. For $b$: $\sqrt2-\sqrt{1+\cos x}=\dfrac{1-\cos x}{\sqrt2+\sqrt{1+\cos x}}$ and $\sin^2x=(1-\cos x)(1+\cos x)$, so $b=\lim(1+\cos x)(\sqrt2+\sqrt{1+\cos x})=2\cdot2\sqrt2=4\sqrt2$. Then $ab^3=\dfrac{(4\sqrt2)^3}{4\sqrt2}=(4\sqrt2)^2=32$.

### M-LCD-02 — JEE Main 2024 · 27 Jan Shift 1 · Q74 · MCQ

Let $f(x)=\begin{cases}\dfrac{a\,(7x-12-x^2)}{b\,|x^2-7x+12|}, & x<3\\[2mm] 2\,\dfrac{\sin(x-3)}{x-[x]}, & x>3\\[2mm] b, & x=3\end{cases}$, where $[x]$ is the greatest integer $\le x$. If $S$ is the set of all ordered pairs $(a,b)$ such that $f$ is continuous at $x=3$, the number of elements in $S$ is

(1) 2  (2) Infinitely many  (3) 4  (4) 1

**Answer: (4)** · key ✔

**Solution.** For $x<3$ near 3: $x^2-7x+12=(x-3)(x-4)>0$, so $|\cdot|=(x-3)(x-4)$, while $7x-12-x^2=-(x-3)(x-4)$. Hence LHL $=-a/b$. For $x>3$ near 3: $[x]=3$, so RHL $=\lim 2\dfrac{\sin(x-3)}{x-3}=2$. Continuity: $-a/b=2=b$, so $b=2,\ a=-4$. Exactly one pair.

