# eBay Price Tracker with Email Alerts

Track the prices of multiple ebay products and receive email alerts when there is a price change

1. Install requirements.txt
2. Run script

Example:

<code>from ebay_tracker import ProductTracker</code>
<code>pt = ProductTracker()</code>

# add product to track
pt.add_product(url)

# remove product
pt.remove_product(url)

# print database
pt.print_database()

# check for price changes
pt.compare_prices()

You will be prompted to enter an interval of time in seconds. This is the frequency that the script will run. Adjust as needed.

If any changes are detected, the database will be updated with the new prices and an email alert will be sent
