import time
import re
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# The url where day-ahead prices can be found. There are two tokens in the url, to be replaced at runtime
entsoe_url = "view-source:https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime=_DELIVERY_+00:00|CET|DAY&biddingZone.values=CTY|10YNL----------L!BZN|10YNL----------L&resolution.values=PT60M&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)"

# Store browser and string
glob = dict()

# Returns a datestring formated to the need of the website. The offset days after or before today
def entsoe_date_str(dt):
    return dt.strftime('%d.%m.%Y')


def retrieve_prices(delivery_date):
    browser = glob['driver']

    # Build url to visit, if offset is left at zero then trade day is today and delivery tomorrow.
    url = entsoe_url
    url = url.replace('_DELIVERY_', entsoe_date_str(delivery_date))

    # Print the url and fetch its content
    print(f'Final url: {url}')
    browser.get(url)
    html = browser.page_source

    # Write html content to disk for testing and debugging if needed. Also close the browser.
    with open('content.txt', 'w') as f:
        f.write(html)

    browser.quit()

    # Read the content of the file. Look redundant, but now you can just comment out all the code above and debug.
    with open('content.txt', 'r') as f:
        html = f.readlines()
    html = ''.join(html)
    html = html.replace('\n', '')

    if glob['browser'] == 'chrome':
        pattern = ';" class="data-view-detail-link">(.*?)<\/span'
        matches = re.findall(pattern, html)

    if glob['browser'] == 'edge':
        pattern = 'data-view-detail-link<\/span>"&gt;<\/span>(.*?)<span'
        matches = re.findall(pattern, html)

    # Display all the matches
    for m in matches:
        print(m)

    # Make sure there are exactly 24 prices
    assert (len(matches) == 24)

    # Return as numbers
    return [float(i) for i in matches]


if __name__ == '__main__':
    glob['browser'] = 'edge'
    glob['driver'] = webdriver.Edge()

    delivery_date = datetime.datetime.today()
    delivery_date += datetime.timedelta(days=0)

    price_list = retrieve_prices(delivery_date)
    print(list(price_list))
