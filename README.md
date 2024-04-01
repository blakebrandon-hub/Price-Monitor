# ebay Price Tracker with Email Alerts

Track the prices of multiple ebay products and receive email alerts when there is a price change

1. Install requirements.txt
2. Run script

Example:
from ebay_tracker import ProductTracker
pt = ProductTracker()

# add product to track
pt.add_product(url)

# remove product
pt.remove_product(url)

# print database
pt.print_database()

# check for price changes
pt.compare_prices()

If any changes are detected, the database will update and an email alert will be sent
