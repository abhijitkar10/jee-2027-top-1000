# Area Under Curves

> Theory: [../../theory/maths/area-under-curves.md](../../theory/maths/area-under-curves.md)

### M-ARE-01 — JEE Main 2024 · 27 Jan Shift 1 · Q87 · Numerical

Let the area of the region $\{(x,y):x-2y+4\ge0,\ x+2y^2\ge0,\ x+4y^2\le8,\ y\ge0\}$ be $\dfrac mn$, where $m,n$ are coprime. Then $m+n$ is equal to ______.

**Answer: 119** · key ✔

**Solution.** Integrate horizontally in $y$. Right boundary: $x=8-4y^2$. Left boundary: $x=-2y^2$ for $0\le y\le1$ and $x=2y-4$ for $1\le y\le\tfrac32$ (the curves $-2y^2=2y-4$ meet at $y=1$, and $8-4y^2=2y-4$ at $y=\tfrac32$).
$A=\int_0^1(8-2y^2)\,dy+\int_1^{3/2}(12-2y-4y^2)\,dy=\tfrac{22}3+\tfrac{19}{12}=\tfrac{107}{12}$. So $m+n=119$.

### M-ARE-02 — JEE Main 2024 · 27 Jan Shift 2 · Q88 · Numerical

If the area of the region $\{(x,y):0\le y\le\min\{2x,\ 6x-x^2\}\}$ is $A$, then $12A$ is equal to ______.

**Answer: 304** · key ✔

**Solution.** $2x=6x-x^2$ at $x=0,4$. For $0\le x\le4$ the minimum is $2x$; for $4\le x\le6$ it is $6x-x^2$. $A=\int_0^42x\,dx+\int_4^6(6x-x^2)dx=16+\left[3x^2-\tfrac{x^3}3\right]_4^6=16+36-\tfrac{80}3=\tfrac{76}3$. So $12A=304$.

