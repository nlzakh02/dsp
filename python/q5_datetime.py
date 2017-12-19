# Hint:  use Google to find python function
import datetime as dt

####a)
# date_start = '01-02-2013'
# date_stop = '07-28-2015'

date_start = dt.datetime.strptime('01-02-2013', '%m-%d-%Y')
date_stop = dt.datetime.strptime('07-28-2015', '%m-%d-%Y')
timedelta_a = date_stop - date_start
print("Question a:", timedelta_a)

####b)
# date_start = '12312013'
# date_stop = '05282015'

date_start = dt.datetime.strptime('12312013', '%m%d%Y')
date_stop = dt.datetime.strptime('05282015', '%m%d%Y')
timedelta_b = date_stop - date_start
print("Question b:", timedelta_b)

####c)
#date_start = '15-Jan-1994'
#date_stop = '14-Jul-2015'

date_start = dt.datetime.strptime('15-Jan-1994', '%d-%b-%Y')
date_stop = dt.datetime.strptime('14-Jul-2015', '%d-%b-%Y')
timedelta_c = date_stop - date_start
print("Question c:", timedelta_c)
