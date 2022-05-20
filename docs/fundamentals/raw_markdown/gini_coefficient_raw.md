# Gini Coefficient

Gini coefficient is one of the inequality measure, it measures statistical dispersion of data

Gini coefficient was developed by Corrado Gini and intended to represent income inequality, However, the applications can be extended to any quantitative samples such as, ecology diversity.

in contast to standard deviation, which is the first choice when dispersion of data is interested, Gini coefficient is bound from 0 to 1, where 0 means total equality and 1 means total inequality. This boundedness gives better understanding for wider audiences.

Gini coefficient is based on Lorenz curve which is a graphical representation of income distribution and also inequality.

[Video on this topic[th]](https://youtu.be/yqRwAr0eDw4)

## Definitions

### Samples

samples are group of thing, we are interested in, each sameple contains their measurable quantities such as income. a measurable quantity of a sample is represented by $x_i$ where $i$ is the sample index. $\{x_i\}$ is the that contains the measurable quantity of every sample.

### Partial Sum

Partial sum of the $i^{th}$ term of a sequnces is the sum of the members of the sequence from first to $i^{th}$ terms
given a sequence

$$
(a_1, a_2, a_3, a_4, ... )
$$

Partial sum of the $i^{th}$ term of the sequnces is

$$
S_i = \sum_{j=1}^i{a_j}
$$

### Sorted Sequence of a Measurable

given a set of a measurable of samples $\{x_i\}$. Let the samples has $n$ members, we sorted the sample such that

$$
x_1 < x_2 < x_3 < x_4 < ... < x_i < ... < x_n
$$

The sorted sequence of the measureable are

$$
(x_1, x_2, x_3, x_4, ..., x_i, ... x_n)
$$

### Lorenz Curve

Lorenz curve are tuples of partial sum of sample's proportion sequence and partial sum of sorted measurable proportion sequence

![lorenz curve](/docs/fundamentals/imgs/lorenz.svg)

Let lorenz curve of samples be $\{(f_i, l_i)\}$

$$
\begin{aligned}
f_i &= \sum_{n=1}^i{\frac{1}{n}} \\
l_i &= \sum_{n=1}^i{\frac{x_i}{n\bar{x}}} \\
\end{aligned}
$$

with $f_0 = 0$ and $l_0 = 0$  
when there is no inequality then $x_i = \bar{x}$ and
$$
l_i = \sum_{n=1}^i{\frac{\bar{x}}{n\bar{x}}} = \sum_{n=1}^i{\frac{1}{n}}i = f_i  
$$ 
This is the **line of equality** $\{(f_i, f_i)\}$

### Gini Coefficient Definition

Gini Coefficient is defined as the the ratio between area between line of equality and Lorenz curve and area under line of equality.

> ![area betweeen line of equality and Lorenz curve](/docs/fundamentals/imgs/lorenz_A.svg)  
The area between line of equality and Lorenz curve

> ![area under line of equality](/docs/fundamentals/imgs/lorenz_B.svg)  
The area under line of equality

using **trapizoidal method** to determined those areas

$$
\operatorname{Trapz} (x_i, y_i) = \sum_{i=1}^{n-1}{\frac{1}{2}(y_i+y_{i+1})(x_{i+1}-x_i)}
$$

when $(x_{i+1}-x_i)$ is constant and equal to $\triangle x$

$$\operatorname{Trapz}(y_i) = \bigg(\sum_{i=1}^n{y_i} - \frac{1}{2}(y_1 + y_n)\bigg)\triangle x$$

Note that when calculating trapizoidal area of lorenz curve, index started from 0.  
Area between line of equality and Lorenz curve

Let $g_i = f_i - l_i$

$$\begin{aligned}
\operatorname{Trapz}(f_i, g_i) &= \frac{1}{n}\operatorname{Trapz}(g_i) \\
&= \frac{1}{n}\bigg(\sum_{i=0}^n{g_i}-\frac{1}{2}(g_0 + g_n)\bigg) \\
&= \frac{1}{n}\sum_{i=0}^n{g_i} \\
&= \frac{n+1}{n}\bar{g}
\end{aligned}$$

Area under line of equality is $\frac{1}{2}$

$$\begin{aligned}
\operatorname{Trapz}(f_i, f_i) &= \frac{1}{n}\bigg(\sum_{i=0}^n{f_i}-\frac{1}{2}(f_0 + f_n)\bigg) \\
&= \frac{1}{n}\bigg(\frac{1}{n}\sum_{i=0}^n{i}-\frac{1}{2}(0 + 1)\bigg) \\
&= \frac{1}{n}\bigg(\frac{1}{n}\frac{n(n+1)}{2}-\frac{1}{2}\bigg) \\
&= \frac{1}{2}
\end{aligned}$$

thus the Gini coefficient is

$$
G=2 \frac{n+1}{n}\bar{g}
$$

Mean of Absolute Differences ($\operatorname{MAD}$) is another approach of calculating Gini coefficient. half of relative mean of abosolute differences is equal to the Gini coefficient calculate through lorenz curve.

$$\begin{aligned}
\operatorname{MAD}(\{x_i\}) & =\frac{1}{N^2}\sum_{i=1}^N\sum_{j=1}^N{\lvert x_i-x_j \rvert} \\
G &= \frac{1}{2\bar{x}}\operatorname{MAD}(\{x_i\})
\end{aligned}$$

mathematically speaking, mean of absolute differences approach make more sense as a measure of inequality or dispersion

## References

[Gini Coefficient, Wikipedia](https://en.wikipedia.org/wiki/Gini_coefficient)  
[Lorenz Curve, Wikipedia](https://en.wikipedia.org/wiki/Lorenz_curve)  
