# Gini Coefficient and Mean of Absolute Differences

Gini coefficient and half of relative mean of absolute differeneces are mathematically equivalence. let $\{x_i\}$ be the measureable of samples of size $n$ and sorted such that $x_1 < x_2 < x_3 < ... < x_i, ... < x_n$

Gini coefficient is 

$$
G = 2 \frac{1}{n^2}\sum_{i=1}^{n}{\sum_{j=1}^i(1 - \frac{x_j}{\bar{x}})}$$

where,

$$
\bar{x} = \sum_{i=1}^n{x_i}
$$

consider mean of absolute different of the measurable,

$$
\operatorname{MAD}(x) = \sum_{i=1}^n{\sum_{j=1}^n{\frac{\lvert x_i - x_j \rvert}{n^2}}}
$$

$$\begin{aligned}
\sum_{i=1}^n{\sum_{j=1}^n{\lvert x_i - x_j \rvert}} &= \sum_{i=1}^n{\bigg(\sum_{j=1}^i{(x_i - x_j)} + \sum_{j=i}^n (x_j-x_i)\bigg)} \\
&= \sum_{i=1}^n{\sum_{j=1}^i{x_i}} - \sum_{i=1}^n{\sum_{j=1}^i{x_j}} + \sum_{i=1}^n{\sum_{j=i}^{n}{x_j}} - \sum_{i=1}^n{\sum_{j=i}^{n}{x_i}}
\end{aligned}$$

note that the overlaped $j=i$ is allowed because, when $i=j, x_i -x_j = 0$.

let 
$$\begin{aligned}
A &= \sum_{i=1}^n{\sum_{j=1}^i{x_i}} \\
B &= \sum_{i=1}^n{\sum_{j=1}^i{x_j}} \\
C &= \sum_{i=1}^n{\sum_{j=i}^{n}{x_j}} \\
D &= \sum_{i=1}^n{\sum_{j=i}^{n}{x_i}}
\end{aligned}
$$

consider $A$ and $D$, we see that the index is not depends on $j$

$$\begin{aligned}
A &= \sum_{i=1}^n{i x_i}\\
D &= \sum_{i=1}^n{(n-i+1)x_i}
\end{aligned}
$$

consider $B$, let $h_i = \sum_{j=1}^i{x_j}$. When we expanding $h_i$
$$\begin{aligned}
h_1 &= x_1 \\
h_2 &= x_1 + x_2 \\
h_3 &= x_1 + x_2 + x_3 \\
h_i &= x_1 + x_2 + x_3 + ... + x_i \\
h_n &= x_1 + x_2 + x_3 + ... + x_i + ... + x_n
\end{aligned}
$$

we see that $D$ and $B$ are related,

$$\begin{aligned}
\sum_{i=1}^n{h_i} &= nx_1 + (n-1)x_2 + (n-2)x_3 +... +(n-i+1)x_i + ... + x_n \\
\sum_{i=1}^n{\sum_{j=1}^i x_j} &= \sum_{i=1}^n{(n-i+1)x_i} \\

B &= D
\end{aligned}
$$

The same as in case of $B$, consider $C$, let $g_i = \sum_{j=i}^n{x_j}$, when we expanding $g_i$
$$\begin{aligned}
g_1 &= x_n+...+x_{i}+...+x_4+x_3+x_2+x_1\\
g_2 &= x_n+...+x_{i}+...+x_4+x_3+x_2 \\
g_3 &= x_n+...+x_{i}+...+x_4+x_3 \\
g_i &= x_n+...+x_{i} \\
g_n &= x_n
\end{aligned}
$$

we see that $A$ and $C$ are related,
$$\begin{aligned}
\sum_{i=1}^n{g_i} &= x_1 + 2x_2 + 3x_3 + ... + ix_i+...+nx_n \\
\sum_{i=1}^n{\sum_{j=1}^n{x_j}} &= \sum_{i=1}^n{ix_i} \\
C &= A
\end{aligned}
$$

we want to keep $B$ because Gini Coefficient contains $B$, finding relation between $B$ and $C$. We found that,

$$\begin{aligned}
B+C &= \sum_{i=1}^n{\bigg(\sum_{j=1}^i x_j + \sum_{j=i}^n x_j\bigg)} \\
&= \sum_{i=1}^n{\bigg(\sum_{j=1}^n x_j + x_i\bigg)} \\
&= n^2\bar{x} + n\bar{x} \\
&= n(n+1)\bar{x} \\
C &= n(n+1)\bar{x} - B
\end{aligned}
$$

Thus, 

$$\begin{aligned}
\operatorname{MAD}(x) &= \frac{1}{n^2}\bigg(A-B+C-D\bigg) \\
 &= \frac{1}{n^2}\bigg(2(C-B)\bigg) \\
 &= \frac{1}{n^2}\bigg(2(n(n+1)\bar{x}-2B)\bigg) \\
 &= \frac{4\bar{x}}{n^2}\bigg(\frac{n(n+1)}{2}-\frac{B}{\bar{x}}\bigg) \\
 &= \frac{4\bar{x}}{n^2}\bigg(\frac{n(n+1)}{2}-\sum_{i=1}^n{\sum_{j=1}^i{\frac{x_j}{\bar{x}}}}\bigg) \\
 &= \frac{4\bar{x}}{n^2}\bigg(\sum_{i=1}^n{\sum_{j=1}^i1}-\sum_{i=1}^n{\sum_{j=1}^i{\frac{x_j}{\bar{x}}}}\bigg) \\
 &= \frac{4\bar{x}}{n^2}\bigg(\sum_{i=1}^n{\sum_{j=1}^i{(1 - \frac{x_j}{\bar{x}})}}\bigg)
\operatorname{MAD}(x) &= 2\bar{x}G
\end{aligned}
$$

we have the relation between Gini coefficient and mean of absolute differences or Gini coefficient equal to half of relative mean of absolute differences.

$$
G = \frac{1}{2\bar{x}}\operatorname{MAD}(x)
$$
