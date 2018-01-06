[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Solutions to these exercises are in chap03soln.ipynb and chap03soln.py

>> Exercise  3.1
Something  like  the  class  size  paradox  appears  if  you  survey
children and ask how many children are in their family.  Families with many
children are more likely to appear in your sample, and families with no chil-
dren have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution
for the number of children under 18 in the household. Now compute the biased
distribution we would see if we surveyed the children and asked them how many
children under 18 (including themselves) are in their household.
Plot  the  actual  and  biased  distributions,  and  compute  their  means.
As  a starting place, you can use chap03ex.ipynb.

resp = nsfg.ReadFemResp()

pmf_actual = thinkstats2.Pmf(resp.numkdhh, label='actual')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

pmf_biased = BiasPmf(pmf_actual, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_actual, pmf_biased])
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')

print('Actual mean', pmf_actual.Mean())

print('Biased mean', pmf_biased.Mean())


Actual mean 1.02420515504
Biased mean 2.40367910066
