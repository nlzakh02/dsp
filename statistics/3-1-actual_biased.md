[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

__Exercise  3.1  
Something  like  the  class  size  paradox  appears  if  you  survey
children and ask how many children are in their family.  Families with many
children are more likely to appear in your sample, and families with no children have no chance to be in the sample.  
Use the NSFG respondent variable NUMKDHH to construct the actual distribution
for the number of children under 18 in the household.  
Now compute the biased
distribution we would see if we surveyed the children and asked them how many
children under 18 (including themselves) are in their household.  
Plot  the  actual  and  biased  distributions,  and  compute  their  means.__

```
resp = nsfg.ReadFemResp()

# create PMF for actual distribution
pmf_actual = thinkstats2.Pmf(resp.numkdhh, label='actual')

# function for creating PMF for biased distribution
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

# create PMF for biased distribution
pmf_biased = BiasPmf(pmf_actual, label='biased')

# plot both PMF's
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_actual, pmf_biased])
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')

# calculate and print means for each distribution
print('Actual mean', pmf_actual.Mean())
print('Biased mean', pmf_biased.Mean())
```

### Results

[<img src="statistics/actual_biased.png" title="PMF of function `random`"/>]

```
Actual mean 1.02420515504
Biased mean 2.40367910066
```
