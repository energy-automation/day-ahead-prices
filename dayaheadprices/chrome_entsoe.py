import time
import re
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# The url where day-ahead prices can be found. There are two tokens in the url, to be replaced at runtime
entsoe_url = "https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={0}+00:00|CET|DAY&biddingZone.values=CTY|{1}----------L!BZN|{1}----------L&resolution.values=PT60M&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)"


# Returns a datestring formated to the need of the website. The offset days after or before today
def entsoe_date_str(dt):
    return dt.strftime('%d.%m.%Y')


def retrieve_prices(delivery_date, what):
    browser = webdriver.Chrome()

    # Build url to visit
    url = entsoe_url.format(entsoe_date_str(delivery_date), what)

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

    # Extract the list of prices
    pattern = 'data-view-detail-link<\/span>"&gt;<\/span>(.*?)<span'
    matches = re.findall(pattern, html)

    if len(matches) == 24:
        print(pattern)
    else:
        pattern = ';" class="data-view-detail-link">(.*?)<\/span'
        matches = re.findall(pattern, html)

    if len(matches) == 24:
        print(pattern)

    # Display all the matches
    # for m in matches:
    #     print(m)

    # Make sure there are exactly 24 prices
    assert (len(matches) == 24)

    # Return as numbers
    return [float(i) for i in matches]


