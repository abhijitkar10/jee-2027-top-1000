# Units, Dimensions & Errors — theory

> Questions: [../../questions/physics/units-measurements.md](../../questions/physics/units-measurements.md)

## Key ideas
- **Dimensional formula** of a quantity: powers of $[M],[L],[T],[A],[K]$. Use it to check equations, derive relations (up to a constant) and convert units. Only quantities with the *same* dimensions can be added/equated; arguments of $\sin,\log,e^{x}$ are dimensionless.
- Useful dimensions: force $[MLT^{-2}]$, energy/work/torque $[ML^2T^{-2}]$, pressure/stress/energy density $[ML^{-1}T^{-2}]$, angular momentum/Planck's $h$ $[ML^2T^{-1}]$, $G$ $[M^{-1}L^3T^{-2}]$, $\varepsilon_0$ $[M^{-1}L^{-3}T^4A^2]$, $\mu_0$ $[MLT^{-2}A^{-2}]$, $B$ $[MT^{-2}A^{-1}]$, specific heat $[L^2T^{-2}K^{-1}]$, latent heat $[L^2T^{-2}]$.
- **Errors.** Sum/difference: $\Delta(A\pm B)=\Delta A+\Delta B$. Product/quotient: $\dfrac{\Delta Z}{Z}=\sum p_i\dfrac{\Delta x_i}{x_i}$ for $Z=\prod x_i^{p_i}$. Percentage errors add (never subtract).
- **Significant figures:** multiplication/division keeps the *fewest* significant figures; addition/subtraction keeps the *fewest decimal places*. Leading zeros are not significant; trailing zeros after a decimal point are.
- **Least count:** vernier $=1$ MSD $-1$ VSD; screw gauge $=\dfrac{\text{pitch}}{\text{no. of circular divisions}}$. Zero error is subtracted (with sign).
## Common traps
- Order of magnitude: $a\times10^b$ with $a\le5$ (rounded down) or $a>5$ (rounded up to $b+1$).
- Maximum error uses the *sum of absolute* fractional errors, whereas the graph/least-count "smallest scale division" is used as $\Delta$.
