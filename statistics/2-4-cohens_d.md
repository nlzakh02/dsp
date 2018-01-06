[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
Include your Python code, results and explanation (where applicable).
>> RESPONSE
>> **Exercise 2.4
Using the variable totalwgt_lb, investigate whether first ba-
bies are lighter or heavier than others.  Compute Cohen’s d
to quantify the difference  between  the  groups.   How  does
it  compare  to  the  difference  in pregnancy length?**

firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
-0.12476118453549034

CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
-0.088672927072602006

firsts.prglngth.mean() - others.prglngth.mean()
0.07803726677754952

CohenEffectSize(firsts.prglngth, others.prglngth)
0.028879044654449883
