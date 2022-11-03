# Day ahead prices

![Day ahead prices from the Entsoe website](http://energyautomation.tech/wp-content/uploads/2022/11/2022-11-03.png)

Hourly energy rates are becoming more important every year. For my own project I needed to know the actual realtime price of electricity.

I decided to create a module to retrieve the rates from one of the energy exchanges. And then I added another for backup.

The websites change their html layout often, so as soon as the script stops working, you need to update the package. 

To install:

    pip install https://github.com/energy-automation/day-ahead-prices/archive/refs/heads/main.zip

To update:

    pip install https://github.com/energy-automation/day-ahead-prices/archive/refs/heads/main.zip --upgrade

# Example

    import datetime
    
    import dayaheadprices.chrome_entsoe as entsoe
    
    delivery_date = datetime.datetime.today()
    delivery_date += datetime.timedelta(days=0)
    
    price_list = entsoe.retrieve_prices(delivery_date, '10YNL')
    print(list(price_list))

If all goes well the result will be an array containing 24 prices for each hour of the specified day.

    [66.88, 52.3, 30.26, 38.92, 33.49, 63.58, 84.38, 99.7, 107.9, 105.51, 94.15, 105.95, 103.96, 128.87, 110.5, 135.4, 131.01, 134.32, 144.42, 128.44, 126.1, 115.66, 125.32, 113.54]


# Available exchanges

### Enstsoe

Website: [https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show](https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show)

Modules: chrome_entsoe, edge_entsoe

Products: In the form 10YAL for Albania or 10YNL for the Netherlands, please have a look at their website for all available codes.

Select a bidding zone in the left column and find the code in the URL.