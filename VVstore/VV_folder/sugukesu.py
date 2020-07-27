
import datetime
from dateutil.relativedelta import relativedelta

today_1 = 2020-06-26 04:48:52.789474
today = "{0:%Y-%m-%d}".format(today_1)
one_month_ago = today - relativedelta(months=1)
print(one_month_ago)
