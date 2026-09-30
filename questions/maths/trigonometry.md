# Trigonometry & Inverse Trigonometry

> Theory: [../../theory/maths/trigonometry.md](../../theory/maths/trigonometry.md)

### M-TRG-01 — JEE Main 2024 · 27 Jan Shift 1 · Q83 · Numerical

Let the set of all $a\in\mathbb R$ such that $\cos2x+a\sin x=2a-7$ has a solution be $[p,q]$, and let $r=\tan9^\circ-\tan27^\circ-\dfrac1{\cot63^\circ}+\tan81^\circ$. Then $pqr$ is ______.

**Answer: 48** · key ✔

**Solution.** With $s=\sin x$: $1-2s^2+as=2a-7\Rightarrow a(s-2)=2(s-2)(s+2)\Rightarrow a=2(s+2)$ (as $s\ne2$). For $s\in[-1,1]$, $a\in[2,6]$, so $p=2,q=6$. Next $\dfrac1{\cot63^\circ}=\tan63^\circ$, so $r=(\tan9^\circ+\tan81^\circ)-(\tan27^\circ+\tan63^\circ)=(\tan9^\circ+\cot9^\circ)-(\tan27^\circ+\cot27^\circ)=\dfrac2{\sin18^\circ}-\dfrac2{\sin54^\circ}$ (using $\tan\theta+\cot\theta=\tfrac2{\sin2\theta}$). With $\sin18^\circ=\tfrac{\sqrt5-1}4$ and $\sin54^\circ=\tfrac{\sqrt5+1}4$: $r=\tfrac8{\sqrt5-1}-\tfrac8{\sqrt5+1}=8\cdot\tfrac{2}{4}=4$. So $pqr=2\cdot6\cdot4=48$.

