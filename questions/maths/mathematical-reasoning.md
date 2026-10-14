# Mathematical Reasoning

> Theory: [../../theory/maths/mathematical-reasoning.md](../../theory/maths/mathematical-reasoning.md)

### M-MRE-01 · C — JEE Main 2023 · 24 Jan Shift 2 · Logic set Q2 · MCQ

Let $p$ and $q$ be two statements. Then $\sim\big(p\wedge(p\Rightarrow\sim q)\big)$ is equivalent to:

(1) $p\vee(p\wedge(\sim q))$  (2) $p\vee((\sim p)\wedge q)$  (3) $(\sim p)\vee q$  (4) $p\vee(p\wedge q)$

**Answer: (3)** · key (compiled)

**Solution.** $p\Rightarrow\sim q\equiv\sim p\vee\sim q$. So $p\wedge(\sim p\vee\sim q)\equiv p\wedge\sim q$, whose negation is $\sim p\vee q$.

### M-MRE-02 · C — JEE Main 2023 · 25 Jan Shift 1 · Logic set Q3 · MCQ

The statement $(p\wedge(\sim q))\Rightarrow(p\Rightarrow(\sim q))$ is:

(1) equivalent to $(\sim p)\vee(\sim q)$  (2) a tautology  (3) equivalent to $p\vee q$  (4) a contradiction

**Answer: (2)** · key (compiled)

**Solution.** The antecedent $p\wedge\sim q$ is true only when $p$ is true and $q$ is false; then $p\Rightarrow\sim q$ is $T\Rightarrow T=T$. Whenever the antecedent is false the implication is true. So the statement is true in every case: a tautology.

### M-MRE-03 · C — JEE Main 2023 · 29 Jan Shift 1 · Logic set Q5 · MCQ

If $p$, $q$ and $r$ are three propositions, then which of the following combinations of truth values of $p$, $q$ and $r$ makes the logical expression $\{(p\vee q)\wedge((\sim p)\vee r)\}\to((\sim q)\vee r)$ false?

(1) $p=T,q=F,r=T$  (2) $p=T,q=T,r=F$  (3) $p=F,q=T,r=F$  (4) $p=T,q=F,r=F$

**Answer: (3)** · key (compiled)

**Solution.** An implication is false only when the antecedent is true and the consequent is false. $(\sim q)\vee r$ false needs $q=T$, $r=F$. Then $p\vee q=T$ and $(\sim p)\vee r=\sim p$ must be true, so $p=F$. The combination is $p=F$, $q=T$, $r=F$.

### M-MRE-04 · C — JEE Main 2023 · 30 Jan Shift 2 · Logic set Q8 · MCQ

Consider the following statements: $P$: I have fever; $Q$: I will not take medicine; $R$: I will take rest. The statement "If I have fever, then I will take medicine and I will take rest" is equivalent to:

(1) $((\sim P)\vee\sim Q)\wedge((\sim P)\vee R)$  (2) $((\sim P)\vee\sim Q)\wedge((\sim P)\vee\sim R)$  (3) $(P\vee Q)\wedge((\sim P)\vee R)$  (4) $(P\vee\sim Q)\wedge(P\vee\sim R)$

**Answer: (1)** · key (compiled)

**Solution.** "I will take medicine" is $\sim Q$, so the statement is $P\Rightarrow(\sim Q\wedge R)\equiv\sim P\vee(\sim Q\wedge R)\equiv(\sim P\vee\sim Q)\wedge(\sim P\vee R)$ by distributivity.

### M-MRE-05 · C — JEE Main 2022 · 24 Jun Shift 1 · Q68 · MCQ

The number of choices for $\Delta\in\{\wedge,\vee,\Rightarrow,\Leftrightarrow\}$, such that $(p\,\Delta\,q)\Rightarrow\big((p\,\Delta\,\sim q)\vee((\sim p)\,\Delta\,q)\big)$ is a tautology, is

(1) 1  (2) 2  (3) 3  (4) 4

**Answer: (2)** · key ✔

**Solution.** Test each connective.
- $\Delta=\wedge$: take $p=q=T$; antecedent $T$, consequent $(T\wedge F)\vee(F\wedge T)=F$, so the implication is false — not a tautology.
- $\Delta=\vee$: consequent $=(p\vee\sim q)\vee(\sim p\vee q)$ contains $p\vee\sim p$, a tautology, so the implication is a tautology.
- $\Delta=\Rightarrow$: consequent $=(\sim p\vee\sim q)\vee(p\vee q)$, again a tautology, so the implication is a tautology.
- $\Delta=\Leftrightarrow$: $(p\Leftrightarrow\sim q)$ and $(\sim p\Leftrightarrow q)$ are both equivalent to $\sim(p\Leftrightarrow q)$, so the statement is $(p\Leftrightarrow q)\Rightarrow\sim(p\Leftrightarrow q)$, false when $p=q$.
Two choices ($\vee$ and $\Rightarrow$).

