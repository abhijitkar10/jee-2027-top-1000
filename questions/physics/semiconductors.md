# Semiconductors & Electronic Devices

> Theory: [../../theory/physics/semiconductors.md](../../theory/physics/semiconductors.md)

### P-SEM-01 — JEE Main 2024 · 1 Feb Shift 2 · Q20 · MCQ

The conductivity of a photodiode changes only if the wavelength of incident light is less than $660$ nm. The band gap is $\dfrac X8$ eV. $X$ is: ($h=6.6\times10^{-34}$ J s, $e=1.6\times10^{-19}$ C)

(1) 15  (2) 11  (3) 13  (4) 21

**Answer: (1)** · key ✔

**Solution.** $E_g=\dfrac{hc}{\lambda}=\dfrac{6.6\times10^{-34}\times3\times10^8}{660\times10^{-9}}=3\times10^{-19}$ J $=\dfrac{3}{1.6}=\dfrac{15}{8}$ eV. So $X=15$.

### P-SEM-02 — JEE Main 2024 · 6 Apr Shift 2 · Q19 · MCQ

The energy needed to create a hole in a p-type semiconductor is $6$ eV (acceptor-level related). The maximum wavelength of light that can create a hole is ($hc=1242$ eV nm):

(1) 414 nm  (2) 103.5 nm  (3) 207 nm  (4) 407 nm

**Answer: (3)** · key ✔

**Solution.** $\lambda_{max}=\dfrac{hc}{E}=\dfrac{1242}{6}=207$ nm.

### P-SEM-03 — JEE Main 2023 · 24 Jan Shift 1 · Q19 · MCQ

Assertion A: Photodiodes are preferably operated in reverse bias condition for light intensity measurement.
Reason R: The current in the forward bias is more than the current in the reverse bias for a $p$–$n$ junction diode.

(1) A false, R true  (2) Both true, R is NOT the correct explanation of A  (3) A true, R false  (4) Both true, R is the correct explanation of A

**Answer: (2)** · key ✔

**Solution.** In reverse bias the dark current is tiny, so the small photo-generated current (proportional to light intensity) is a large fractional change and is easily measured: A is true. R is also a true statement about a $p$–$n$ junction, but it does not explain A (the explanation is the small reverse dark current, not the size of the forward current).

### § — JEE Main 2026 · 28 Jan Shift 2 · set Q2 · MCQ

Two $p$–$n$ junction diodes $D_1$ and $D_2$ are connected as shown in the figure. $A$ and $B$ are input signals and $C$ is the output. The given circuit will function as a ______.

![Figure](../../figures/j26_phy_semiconductors/q2-1.png)

(1) NOR gate  (2) NAND gate  (3) OR gate  (4) AND gate

**Answer: (4)** · key (compiled)

**Solution.** The cathodes of $D_1,D_2$ are at the inputs and their anodes are joined to the output $C$, which is pulled up to $5$ V through $R$. If either input is $0$ the corresponding diode is forward biased and pulls $C$ down to about $0$ V. Only when $A=B=1$ are both diodes off, no current flows through $R$ and $C$ stays at $5$ V (logic 1). So $C=A\cdot B$: an AND gate.

### § — JEE Main 2026 · 24 Jan Shift 2 · set Q3 · MCQ

Identify the correct truth table of the given logic circuit.

Outputs $Y$ for $(A,B)=(0,0),(0,1),(1,0),(1,1)$ in that order:

![Figure](../../figures/j26_phy_semiconductors/q3-1.png)

(1) $1,0,1,0$  (2) $1,1,1,0$  (3) $0,1,1,0$  (4) $0,0,1,0$

**Answer: (4)** · key (compiled)

**Solution.** The top path passes $A$ unchanged (a gate with both inputs tied), the lower path is $\overline{A\cdot B}$ (NAND followed by a tied-input buffer), and the final AND gate combines them: $Y=A\cdot\overline{A\cdot B}=A(\bar A+\bar B)=A\bar B$. This is $1$ only for $A=1,B=0$, i.e. $0,0,1,0$.

### § — JEE Main 2026 · 22 Jan Shift 2 · set Q4 · MCQ

The correct truth table for the given input data of the following logic circuit is:

Outputs $Y$ for $(A,B,C,D)=(1,1,0,1),(0,0,1,1),(1,0,1,0),(1,1,1,1)$ in that order:

![Figure](../../figures/j26_phy_semiconductors/q4-1.png)

(1) $0,0,1,1$  (2) $0,1,1,1$  (3) $1,0,0,1$  (4) $1,0,1,0$

**Answer: (3)** · key (compiled)

**Solution.** $A,B$ go to an AND gate followed by NOT, $C,D$ to an OR gate, these two outputs go to an AND gate followed by NOT. So $Y=\overline{\overline{AB}\cdot(C+D)}=AB+\overline{C+D}$. Evaluating: $(1,1,0,1)\to1$; $(0,0,1,1)\to0$; $(1,0,1,0)\to0$; $(1,1,1,1)\to1$. Output column $1,0,0,1$.

### § — JEE Main 2026 · 22 Jan Shift 1 · set Q5 · MCQ

Find the correct combination of $A,B,C$ and $D$ inputs which can cause the LED to glow.

![Figure](../../figures/j26_phy_semiconductors/q5-1.png)

(1) 1101  (2) 0011  (3) 1000  (4) 0100

**Answer: (1)** · key (compiled)

**Solution.** The LED glows when it is forward biased: its $p$-side (the output of the upper NAND gate) must be high and its $n$-side (the output of the NOR gate on $C,D$) must be low. The upper NAND receives $\bar A$ and $\bar B$ (tied-input NOR gates act as NOT), so $Y_1=\overline{\bar A\bar B}=A+B$. The lower gate gives $Y_2=\overline{C+D}$. Need $Y_1=1$ and $Y_2=0$, i.e. $A+B=1$ and $C+D=1$. Only $1101$ satisfies both.

### § — JEE Main 2026 · 23 Jan Shift 2 · set Q6 · MCQ

For the given logic gate circuit, which of the following is the correct truth table?

Outputs $z$ for $(n,m)=(0,0),(0,1),(1,1),(1,0)$ in that order:

![Figure](../../figures/j26_phy_semiconductors/q6-1.png)

(1) $0,1,0,1$  (2) $1,0,1,0$  (3) $1,0,0,0$  (4) $1,1,0,0$

**Answer: (4)** · key (compiled)

**Solution.** An OR gate gives $y=n+m$, and a NAND gate takes $n$ and $y$: $z=\overline{n\cdot(n+m)}=\overline{n}$ (absorption: $n(n+m)=n$). So $z=1,1,0,0$ for the four rows.

### § — JEE Main 2026 · 21 Jan Shift 1 · set Q7 · MCQ

The given circuit works as:

![Figure](../../figures/j26_phy_semiconductors/q7-1.png)

(1) AND gate  (2) NAND gate  (3) NOR gate  (4) OR gate

**Answer: (2)** · key (compiled)

**Solution.** A NOR gate with both inputs tied acts as a NOT gate. The first two NOR gates give $\bar A$ and $\bar B$; the third NOR gate gives $\overline{\bar A+\bar B}=A\cdot B$; the last (tied-input) NOR inverts it: $Y=\overline{A\cdot B}$. This is a NAND gate.

### § — JEE Main 2026 · 28 Jan Shift 1 · set Q8 · MCQ

Assuming a voltage drop of $0.7$ V across a silicon diode in forward bias, the current through the diode $D_1$ in the circuit is ______ mA. (Assume all diodes in the circuit are identical.)

![Figure](../../figures/j26_phy_semiconductors/q8-1.png)

(1) 17.6  (2) 18.8  (3) 11.7  (4) 20.15

**Answer: (2)** · key (compiled)

**Solution.** $D_2$ is reverse biased, so $D_1$ and $D_3$ conduct in parallel, each dropping $0.7$ V. Current through the $0.3\ \text{k}\Omega$ resistor $I=\dfrac{12-0.7}{300}=37.7$ mA, shared equally by $D_1$ and $D_3$: $I_1=18.8$ mA.

### § — JEE Main 2026 · 24 Jan Shift 1 · set Q9 · Numerical

A voltage regulating circuit consisting of a Zener diode with breakdown voltage $10$ V and maximum power dissipation $0.4$ W is operated from a $15$ V source. The approximate value of the protective (series) resistance in this circuit is ______ $\Omega$.

**Answer: 125** · key (compiled)

**Solution.** Maximum Zener current $I_{Z,max}=\dfrac{P_{max}}{V_Z}=\dfrac{0.4}{10}=0.04$ A. The series resistor must drop $15-10=5$ V at that current: $R_s=\dfrac{5}{0.04}=125\ \Omega$.

