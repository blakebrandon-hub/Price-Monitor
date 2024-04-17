# eBay Price Tracker with Email Alerts

This command-line tool tracks the prices and availability of products on eBay and can send email alerts if any changes are detected. Email credentials must be entered for alert functionality.



### Requirements: 

1. Install Beautiful Soup


#### How to generate an app password with gmail:
<url>https://support.google.com/accounts/answer/185833?hl=en</url>

<br>

### Adding a product to track
<code>add_product(url)</code>


### Stop tracking a product
<code>remove_product(url)</code>


### Print database of tracked products
<code>print_database()</code>


### Check for price changes
<code>compare_prices()</code>

<br>

### Configuration Settings 

KEEP_RUNNING: If set to False script will run ONLY once. If set to True script will continue to run in the background

INTERVAL_IN_SECONDS: Frequency the script will run if KEEP_RUNNING is set to True


