# Day ahead prices

Hourly energy rates are becoming more important every year. For my own project I needed to know the actual realtime price of electricity.

I decided to create a module to retrieve the rates from one of the energy exchanges. And then I added another for backup.

The websites change their html layout often, so as soon as the script stops working, you need to update the package. 

To install:

    pip install https://github.com/energy-automation/day-ahead-prices/archive/refs/heads/main.zip

To update:

    pip install https://github.com/energy-automation/day-ahead-prices/archive/refs/heads/main.zip --upgrade

