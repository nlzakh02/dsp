[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
Include your Python code, results and explanation (where applicable).

**Exercise 2.4  
Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others.  
Compute Cohen’s d
to quantify the difference  between  the  groups.   How  does
it  compare  to  the  difference  in pregnancy length?**  
1. Calculate difference in means between first and other babies
```
firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
-0.12476118453549034
```
As we can see, first-born babies, on average, are slightly lighter than others. This trend is opposite to one observed for pregnancy length, where pregnancy, on average, was longer for the first babies.  

2. Calculate Cohen's D for first and other babies
```
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
-0.088672927072602006
```
Cohen's D confirms our previous observation that first babies are slightly lighter than others. In addition, it tells us that this difference represents about -0.089 of standard deviation. This difference is larger in it's absolute value than difference for pregnancy length (0.029), but it is still small to be practically meaningful.
