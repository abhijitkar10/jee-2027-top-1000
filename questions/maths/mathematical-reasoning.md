# Mathematical Reasoning

> Theory: [../../theory/maths/mathematical-reasoning.md](../../theory/maths/mathematical-reasoning.md)

### § — JEE Main 2022 · 24 Jun Shift 1 · Q68 · MCQ

The number of choices for $\Delta\in\{\wedge,\vee,\Rightarrow,\Leftrightarrow\}$, such that $(p\,\Delta\,q)\Rightarrow\big((p\,\Delta\,\sim q)\vee((\sim p)\,\Delta\,q)\big)$ is a tautology, is

(1) 1  (2) 2  (3) 3  (4) 4

**Answer: (2)** · key ✔

**Solution.** Test each connective.
- $\Delta=\wedge$: take $p=q=T$; antecedent $T$, consequent $(T\wedge F)\vee(F\wedge T)=F$, so the implication is false — not a tautology.
- $\Delta=\vee$: consequent $=(p\vee\sim q)\vee(\sim p\vee q)$ contains $p\vee\sim p$, a tautology, so the implication is a tautology.
- $\Delta=\Rightarrow$: consequent $=(\sim p\vee\sim q)\vee(p\vee q)$, again a tautology, so the implication is a tautology.
- $\Delta=\Leftrightarrow$: $(p\Leftrightarrow\sim q)$ and $(\sim p\Leftrightarrow q)$ are both equivalent to $\sim(p\Leftrightarrow q)$, so the statement is $(p\Leftrightarrow q)\Rightarrow\sim(p\Leftrightarrow q)$, false when $p=q$.
Two choices ($\vee$ and $\Rightarrow$).

