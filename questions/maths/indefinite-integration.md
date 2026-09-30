# Indefinite Integration

> Theory: [../../theory/maths/indefinite-integration.md](../../theory/maths/indefinite-integration.md)

### M-INT-01 — JEE Main 2024 · 27 Jan Shift 2 · Q74 · MCQ

$\displaystyle\int\frac{x^8-x^2}{\left(x^{12}+3x^6+1\right)\tan^{-1}\!\left(x^3+\dfrac1{x^3}\right)}\,dx$ is equal to

(1) $\ln\left|\tan^{-1}\!\left(x^3+\tfrac1{x^3}\right)\right|^{1/3}+C$  (2) $\ln\left|\tan^{-1}(\cdot)\right|^{1/2}+C$  (3) $\ln\left|\tan^{-1}(\cdot)\right|+C$  (4) $\ln\left|\tan^{-1}(\cdot)\right|^{3}+C$

**Answer: (1)** · key ✔

**Solution.** Let $t=x^3+x^{-3}$, so $dt=3\left(x^2-x^{-4}\right)dx=\dfrac{3(x^6-1)}{x^4}dx$. Also $x^{12}+3x^6+1=x^6(t^2+1)$ since $t^2=x^6+2+x^{-6}$. The integrand becomes $\dfrac{x^2(x^6-1)}{x^6(t^2+1)\tan^{-1}t}dx=\dfrac{dt}{3(1+t^2)\tan^{-1}t}$. Integrating: $\tfrac13\ln|\tan^{-1}t|+C$.

