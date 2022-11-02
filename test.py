import datetime

import dayaheadprices.entsoe as entsoe

delivery_date = datetime.datetime.today()
delivery_date += datetime.timedelta(days=0)

price_list = entsoe.retrieve_prices(delivery_date, '10YNL')
print(list(price_list))