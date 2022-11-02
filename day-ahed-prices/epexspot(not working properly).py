import time
import re
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# The url where day-ahead prices can be found. There are two tokens in the url, to be replaced at runtime
epexspot_url = "https://www.epexspot.com/en/market-data?market_area=NL&trading_date=_TRADE_&delivery_date=_DELIVERY_&underlying_year=&modality=Auction&sub_modality=DayAhead&technology=&product=60&data_mode=table&period=&production_period="


# Returns a datestring formated to the need of the website. The offset days after or before today
def epexspot_date_str(offset):
    _date = datetime.datetime.today()
    _date += datetime.timedelta(days=offset)
    return _date.strftime('%Y-%m-%d')


# Finds a substring in a string and cuts of everything before that occurrence.
def goto(haystack, needle):
    position = haystack.find(needle)

    if position == 0:
        return haystack

    return haystack[position:]



def retrieve_prices(offset):
    browser = webdriver.Edge()

    # Build url to visit, if offset is left at zero then trade day is today and delivery tomorrow.
    url = epexspot_url
    url = url.replace('_TRADE_', epexspot_date_str(offset))
    url = url.replace('_DELIVERY_', epexspot_date_str(offset + 1))

    # Print the url and fetch its content
    print(f'Final url: {url}')
    browser.get(url)
    html = browser.page_source

    # Write html content to disk for testing and debugging if needed. Also close the browser.
    with open('../content.txt', 'w') as f:
        f.write(html)

    browser.quit()

    # Read the content of the file. Look redundant, but now you can just comment out all the code above and debug.
    with open('../content.txt', 'r') as f:
        html = f.readlines()
    html = ''.join(html)
    html = html.replace('\n', '')

    # Find the start of the hours column
    html = goto(html, '<span class="fixed-head-column">Hours</span>')

    # All the hrefs contain the hours in the form 00 - 01, find them with regex.
    pattern = '<a href="#">(.+?)<\\/a>'
    _hours = re.findall(pattern, html)

    hours = []
    for h in _hours:
        hours.append(h[0:2] + '-' + h[5:7])

    # Now find the start of the prices column.
    html = goto(html, '<th>Price<br><span>')

    # Extract the prices rows completely.
    pattern = '<tr class="child.+?<\\/tr>'
    rows = re.findall(pattern, html)

    # The last <td></td> in each row contains the price
    prices = []
    for r in rows:
        p = re.findall('<td>(.+?)<\\/td>', r)
        prices.append(float(p[3]))

    l1 = len(hours)
    assert(l1 == 24)

    l2 = len(prices)
    assert(l2 == 24)

    # Zip hours and time together for safekeeping and return to sender.
    return zip(hours, prices)


if __name__ == '__main__':
    price_list = retrieve_prices(0)
    print(list(price_list))
