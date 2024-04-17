# eBay Price Tracker with Email Alerts

This command-line tool was designed to track the prices of various eBay products and then send email alerts upon any changes in price or availability.



### Requirements: 

1. Install Beautiful Soup



### Adding a product to track
<code>add_product(url)</code>

### Stop tracking a product
<code>pt.remove_product(url)</code>


### Print database of tracked products
<code>print_database()</code>


### Check for price changes
<code>compare_prices(keep_running)</code>

keep_running is a boolean. If set to FALSE script will run only once. If set to TRUE, you will be prompted to enter an interval of time in seconds. This is the frequency that the script will run.

If any changes are detected, the database will be updated and an email alert will be sent. Email credentials must be entered for alert functionality
