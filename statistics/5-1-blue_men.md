[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

__Exercise 5.1  
In the BRFSS (see Section 5.4), the distribution of heights is roughly normal
with parameters μ = 178 cm and σ = 7.7 cm for men, and μ = 163 cm and σ = 7.3
cm for women.__

**In order to join Blue Man Group, you have to be male between 5’10” and
6’1” (see http://bluemancasting.com).  What percentage of the U.S. male
population is in this range?  
Hint: use scipy.stats.norm.cdf.**

```
def mixed_to_in(mixed_height_raw):
  mixed_height = mixed_height_raw.split("'")  
  return int(mixed_height[1]) + (12 * int(mixed_height[0]))

def in_to_cm(inches):
  return 2.54 * inches

height_range = ["5'10", "6'1"]
height_range_in = [mixed_to_in(i) for i in height_range]
height_range_cm = [in_to_cm(i) for i in height_range_in]

# calculate z-scores for limiting heights
low = (height_range_cm[0] - mu) / sigma
high = (height_range_cm[1] - mu) / sigma

# calculate percent of men fitting criteria
blue = (dist.cdf(mu + high) - dist.cdf(mu + low)) * 100

print('Percent ready to be BLUE: %.2f' % blue)
```
### Output:
```
Percent ready to be BLUE: 5.11```
