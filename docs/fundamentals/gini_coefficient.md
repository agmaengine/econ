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

<p align="center"><img src="svgs/490e732f8013277138ec2a20eafe07c6.svg?invert_in_darkmode" align=middle width=78.3199956pt height=47.358596999999996pt/></p>

### Sorted Sequence of a Measurable

given a set of a measurable of samples <img src="svgs/2be584587fa2addfb86cdbc696cc407f.svg?invert_in_darkmode" align=middle width=31.30620404999999pt height=24.65753399999998pt/>, we sorted the sample such that

<p align="center"><img src="svgs/76028955fc262594791b51ac7d15c1f9.svg?invert_in_darkmode" align=middle width=283.80748275pt height=11.327609699999998pt/></p>

The sorted sequence of the measureable are

<p align="center"><img src="svgs/005cdab82ae7bc95f7d13b3452a886eb.svg?invert_in_darkmode" align=middle width=174.12802109999998pt height=16.438356pt/></p>

### Lorenz Curve

Lorenz curve are tuples of partial sum of sample's proportion sequence and partial sum of sorted measurable proportion sequence

Let lorenz curve of samples be <img src="svgs/57480d683548cabe23bc856a8c551c0f.svg?invert_in_darkmode" align=middle width=60.42819089999998pt height=24.65753399999998pt/>

<p align="center"><img src="svgs/999f60af757844701e7b7df03ccf297a.svg?invert_in_darkmode" align=middle width=89.3155593pt height=104.58018449999999pt/></p>

with <img src="svgs/8511332df39325a5a9da9b5aeb7be6f0.svg?invert_in_darkmode" align=middle width=45.559286849999985pt height=22.831056599999986pt/> and <img src="svgs/1cc82470061a35a5468ec096483b1d0e.svg?invert_in_darkmode" align=middle width=42.41617544999999pt height=22.831056599999986pt/>  
when there is no inequality then <img src="svgs/4857a419253496ade3d008a2348c1aca.svg?invert_in_darkmode" align=middle width=46.18040294999999pt height=18.666631500000015pt/> and
<p align="center"><img src="svgs/1985bb7540e6e3d0eb17b7d8643a0549.svg?invert_in_darkmode" align=middle width=196.79711204999998pt height=47.358596999999996pt/></p> 
This is the **line of equality** <img src="svgs/85943d5fd288f0d3e4f4792c45b3d3c2.svg?invert_in_darkmode" align=middle width=63.571302299999985pt height=24.65753399999998pt/>

### Gini Coefficient Definition

Gini Coefficient is defined as the the ratio between area between line of equality and Lorenz curve and area under line of equality.

![the area label in lorenz curve plot]()

using **trapizoidal method** to determined those areas

<p align="center"><img src="svgs/641a286e2b24bc45347e054ca277021b.svg?invert_in_darkmode" align=middle width=306.49667895pt height=47.806078649999996pt/></p>

when <img src="svgs/07a573358a6c64b29111b28e8252da9d.svg?invert_in_darkmode" align=middle width=79.25610494999998pt height=24.65753399999998pt/> is constant and equal to <img src="svgs/ecd35f68213cd27c6e57c6d46f168f31.svg?invert_in_darkmode" align=middle width=24.00689774999999pt height=22.831056599999986pt/>

<p align="center"><img src="svgs/8c889f1f665ea6af52d8c08459f1e968.svg?invert_in_darkmode" align=middle width=281.8909104pt height=47.806078649999996pt/></p>

Note that when calculate trapizoidal of lorenz curve index started from 0.  
Area between line of equality and Lorenz curve

Let <img src="svgs/7bfade092cda38225eaf6e3cfe962a1a.svg?invert_in_darkmode" align=middle width=78.39875835pt height=22.831056599999986pt/>

<p align="center"><img src="svgs/5717239c787017ec66b92f694764eec8.svg?invert_in_darkmode" align=middle width=296.78041635pt height=171.90822825pt/></p>

Area under line of equality is <img src="svgs/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode" align=middle width=6.552545999999997pt height=27.77565449999998pt/>

<p align="center"><img src="svgs/b89c5c18514012bc17a903d85fcc80b5.svg?invert_in_darkmode" align=middle width=297.6100479pt height=192.71228459999998pt/></p>

thus the Gini coefficient is

<p align="center"><img src="svgs/6b0574cfb12ec741ce19eb16c4a25a55.svg?invert_in_darkmode" align=middle width=51.84290265pt height=14.42921205pt/></p>

Mean of Absolute Differences (<img src="svgs/299ea464285ce5f16fa312605bdddc08.svg?invert_in_darkmode" align=middle width=39.954444749999986pt height=22.465723500000017pt/>) is another approach of calculating Gini coefficient. half of relative mean of abosolute differences is equal to the Gini coefficient calculate through lorenz curve.

<p align="center"><img src="svgs/6cf9f414b7b0e8ba06558e050dd892a4.svg?invert_in_darkmode" align=middle width=248.40371985pt height=91.25284244999999pt/></p>

mathematically speaking, mean of absolute differences approach make more sense as a measure of inequality or dispersion
