# Trigonometry & Inverse Trigonometry

> Theory: [../../theory/maths/trigonometry.md](../../theory/maths/trigonometry.md)

### M-TRG-01 — JEE Main 2024 · 27 Jan Shift 1 · Q83 · Numerical

Let the set of all $a\in\mathbb R$ such that $\cos2x+a\sin x=2a-7$ has a solution be $[p,q]$, and let $r=\tan9^\circ-\tan27^\circ-\dfrac1{\cot63^\circ}+\tan81^\circ$. Then $pqr$ is ______.

**Answer: 48** · key ✔

**Solution.** With $s=\sin x$: $1-2s^2+as=2a-7\Rightarrow a(s-2)=2(s-2)(s+2)\Rightarrow a=2(s+2)$ (as $s\ne2$). For $s\in[-1,1]$, $a\in[2,6]$, so $p=2,q=6$. Next $\dfrac1{\cot63^\circ}=\tan63^\circ$, so $r=(\tan9^\circ+\tan81^\circ)-(\tan27^\circ+\tan63^\circ)=(\tan9^\circ+\cot9^\circ)-(\tan27^\circ+\cot27^\circ)=\dfrac2{\sin18^\circ}-\dfrac2{\sin54^\circ}$ (using $\tan\theta+\cot\theta=\tfrac2{\sin2\theta}$). With $\sin18^\circ=\tfrac{\sqrt5-1}4$ and $\sin54^\circ=\tfrac{\sqrt5+1}4$: $r=\tfrac8{\sqrt5-1}-\tfrac8{\sqrt5+1}=8\cdot\tfrac{2}{4}=4$. So $pqr=2\cdot6\cdot4=48$.

### M-TRG-02 — JEE Main 2024 · 27 Jan Shift 2 · Q70 · MCQ

Considering only principal values of inverse trigonometric functions, the number of positive real values of $x$ satisfying $\tan^{-1}x+\tan^{-1}2x=\dfrac\pi4$ is

(1) More than 2  (2) 1  (3) 2  (4) 0

**Answer: (2)** · key ✔

**Solution.** For $x>0$ the sum lies in $(0,\pi)$ and $2x^2<1$ is needed for the addition formula: $\dfrac{3x}{1-2x^2}=1\Rightarrow2x^2+3x-1=0\Rightarrow x=\dfrac{-3\pm\sqrt{17}}4$. Only $x=\dfrac{-3+\sqrt{17}}4\approx0.28>0$, and it satisfies $2x^2<1$. Exactly one positive solution.

