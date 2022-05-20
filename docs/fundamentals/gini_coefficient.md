# Gini Coefficient

Gini coefficient is one of the inequality measure, it measures statistical dispersion of data

Gini coefficient was developed by Corrado Gini and intended to represent income inequality, However, the applications can be extended to any quantitative samples such as, ecology diversity.

in contast to standard deviation, which is the first choice when dispersion of data is interested, Gini coefficient is bound from 0 to 1, where 0 means total equality and 1 means total inequality. This boundedness gives better understanding for wider audiences.

Gini coefficient is based on Lorenz curve which is a graphical representation of income distribution and also inequality.

[Video on this topic[th]](https://youtu.be/yqRwAr0eDw4)

## Definitions

### Samples

samples are group of thing, we are interested in, each sameple contains their measurable quantities such as income. a measurable quantity of a sample is represented by <img src="svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/> where <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.663225699999989pt height=21.68300969999999pt/> is the sample index. <img src="svgs/2be584587fa2addfb86cdbc696cc407f.svg?invert_in_darkmode" align=middle width=31.30620404999999pt height=24.65753399999998pt/> is the that contains the measurable quantity of every sample.

### Partial Sum

Partial sum of the <img src="svgs/3def24cf259215eefdd43e76525fb473.svg?invert_in_darkmode" align=middle width=18.32504519999999pt height=27.91243950000002pt/> term of a sequnces is the sum of the members of the sequence from first to <img src="svgs/3def24cf259215eefdd43e76525fb473.svg?invert_in_darkmode" align=middle width=18.32504519999999pt height=27.91243950000002pt/> terms
given a sequence

<p align="center"><img src="svgs/4b1c48538791749cad617097a5c4bd89.svg?invert_in_darkmode" align=middle width=119.96209335pt height=16.438356pt/></p>

Partial sum of the <img src="svgs/3def24cf259215eefdd43e76525fb473.svg?invert_in_darkmode" align=middle width=18.32504519999999pt height=27.91243950000002pt/> term of the sequnces is

<p align="center"><img src="svgs/5980a12879a5dae17207197106cb3052.svg?invert_in_darkmode" align=middle width=78.74801385pt height=49.794650399999995pt/></p>

### Sorted Sequence of a Measurable

given a set of a measurable of samples <img src="svgs/2be584587fa2addfb86cdbc696cc407f.svg?invert_in_darkmode" align=middle width=31.30620404999999pt height=24.65753399999998pt/>. Let the samples has <img src="svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> members, we sorted the sample such that

<p align="center"><img src="svgs/3f03b5d6242df310b813c530caf4b834.svg?invert_in_darkmode" align=middle width=280.2873447pt height=11.327609699999998pt/></p>

The sorted sequence of the measureable are

<p align="center"><img src="svgs/e55f13539a78824c4cef89b3f9da56ce.svg?invert_in_darkmode" align=middle width=184.3065774pt height=16.438356pt/></p>

### Lorenz Curve

Lorenz curve are tuples of partial sum of sample's proportion sequence and partial sum of sorted measurable proportion sequence

![lorenz curve](/docs/fundamentals/imgs/lorenz.svg)

Let lorenz curve of samples be <img src="svgs/57480d683548cabe23bc856a8c551c0f.svg?invert_in_darkmode" align=middle width=60.42819089999998pt height=24.65753399999998pt/>

<p align="center"><img src="svgs/f028f38509d175d80352d0142dadd76f.svg?invert_in_darkmode" align=middle width=84.18246705pt height=104.58018449999999pt/></p>

with <img src="svgs/8511332df39325a5a9da9b5aeb7be6f0.svg?invert_in_darkmode" align=middle width=45.559286849999985pt height=22.831056599999986pt/> and <img src="svgs/1cc82470061a35a5468ec096483b1d0e.svg?invert_in_darkmode" align=middle width=42.41617544999999pt height=22.831056599999986pt/>  
when there is no inequality then <img src="svgs/4857a419253496ade3d008a2348c1aca.svg?invert_in_darkmode" align=middle width=46.18040294999999pt height=18.666631500000015pt/> and
<p align="center"><img src="svgs/578d2e131ade65f06cb9572d1e23ea2c.svg?invert_in_darkmode" align=middle width=186.53096549999998pt height=47.358596999999996pt/></p> 
This is the **line of equality** <img src="svgs/85943d5fd288f0d3e4f4792c45b3d3c2.svg?invert_in_darkmode" align=middle width=63.571302299999985pt height=24.65753399999998pt/>

### Gini Coefficient Definition

Gini Coefficient is defined as the the ratio between area between line of equality and Lorenz curve and area under line of equality.

> ![area betweeen line of equality and Lorenz curve](/docs/fundamentals/imgs/lorenz_A.svg)  
The area between line of equality and Lorenz curve

> ![area under line of equality](/docs/fundamentals/imgs/lorenz_B.svg)  
The area under line of equality

using **trapizoidal method** to determined those areas

<p align="center"><img src="svgs/e43fad21794916e108796670ee142ba9.svg?invert_in_darkmode" align=middle width=307.7048997pt height=47.35857885pt/></p>

when <img src="svgs/07a573358a6c64b29111b28e8252da9d.svg?invert_in_darkmode" align=middle width=79.25610494999998pt height=24.65753399999998pt/> is constant and equal to <img src="svgs/ecd35f68213cd27c6e57c6d46f168f31.svg?invert_in_darkmode" align=middle width=24.00689774999999pt height=22.831056599999986pt/>

<p align="center"><img src="svgs/74882687419845ebe95dd4908326edce.svg?invert_in_darkmode" align=middle width=278.37079545pt height=44.89738935pt/></p>

Note that when calculating trapizoidal area of lorenz curve, index started from 0.  
Area between line of equality and Lorenz curve

Let <img src="svgs/7bfade092cda38225eaf6e3cfe962a1a.svg?invert_in_darkmode" align=middle width=78.39875835pt height=22.831056599999986pt/>

<p align="center"><img src="svgs/c12b6cfebc2c174e2930e94dcf90d3df.svg?invert_in_darkmode" align=middle width=288.12722895pt height=182.07649515pt/></p>

Area under line of equality is <img src="svgs/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode" align=middle width=6.552545999999997pt height=27.77565449999998pt/>

<p align="center"><img src="svgs/809d8c6f5a478b62aab0dc23a9564dd2.svg?invert_in_darkmode" align=middle width=288.95685885pt height=186.8949027pt/></p>

thus the Gini coefficient is

<p align="center"><img src="svgs/24967ffe14628ff44255a6071ad5aeba.svg?invert_in_darkmode" align=middle width=93.9653616pt height=32.990165999999995pt/></p>

Mean of Absolute Differences (<img src="svgs/299ea464285ce5f16fa312605bdddc08.svg?invert_in_darkmode" align=middle width=39.954444749999986pt height=22.465723500000017pt/>) is another approach of calculating Gini coefficient. half of relative mean of abosolute differences is equal to the Gini coefficient calculate through lorenz curve.

<p align="center"><img src="svgs/6cf9f414b7b0e8ba06558e050dd892a4.svg?invert_in_darkmode" align=middle width=248.40371985pt height=91.25284244999999pt/></p>

mathematically speaking, mean of absolute differences approach make more sense as a measure of inequality or dispersion

## References

[Gini Coefficient, Wikipedia](https://en.wikipedia.org/wiki/Gini_coefficient)  
[Lorenz Curve, Wikipedia](https://en.wikipedia.org/wiki/Lorenz_curve)  
