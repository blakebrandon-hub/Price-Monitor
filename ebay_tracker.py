import requests
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import sqlite3
from datetime import datetime

class ProductTracker:
	def __init__(self):
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
		self.conn = sqlite3.connect('ebay_products.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute('CREATE TABLE IF NOT EXISTS products (product_title TEXT, product_price REAL, product_url TEXT)')
		self.conn.commit()
		self.price_changes = []

	def print_database(self):
		products = self.cursor.execute('SELECT * FROM products')
		for product in products:
			print(product)

	def add_product(self, url):
		response = requests.get(url, headers=self.headers)
		soup = BeautifulSoup(response.content, 'lxml')
		data_price = soup.find('div', class_='x-price-primary').text
		title = soup.find('div', class_='vim x-item-title').text
		price_string = float(data_price.split('$')[1])
		product_data = [(title[1:], price_string, url)]
		self.cursor.executemany('INSERT INTO products (product_title, product_price, product_url) VALUES (?, ?, ?)', product_data)
		self.conn.commit()
		print(f'{title} added to database')

	def remove_product(self, url):
		sql_string = f"DELETE FROM products WHERE product_url = '{url}'"
		self.cursor.execute(sql_string)
		self.conn.commit()
		print('Product removed from database')

	def compare_prices(self, keep_running):
		if keep_running:
			interval = input('How often to check prices (in seconds)?')
	
		while True:
			products = self.cursor.execute("SELECT * FROM products")
			for product in products:
				response = requests.get(product[2], headers=self.headers)
				time.sleep(1)
				soup = BeautifulSoup(response.content, 'lxml')
				data_price = soup.find('div', class_='x-price-primary').text
				price_string = float(data_price.split('$')[1])
				message = ''
				current_time = datetime.now()
				formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

				if price_string > product[1]:
					message = f"{product[0]} has increased in price by ${round(price_string - product[1], 2)}"
				elif price_string < product[1]:
					message = f"{product[0]} has decreased in price by ${round(product[1] - price_string), 2}"
				else:
					message = "No price changes detected"

				if message != 'No price changes detected':
					
					update_query = """
					    UPDATE products
					    SET product_title = ?,
					        product_price = ?,
					        product_url = ?
					    WHERE product_url = ?;
					"""

					new_values = (product[0], price_string, product[2], product[2])

					self.cursor.execute(update_query, new_values)
					self.conn.commit()
					time.sleep(1)
					self.price_changes.append(message)
					print(f"({formatted_time}) {message}")
					self.send_email()

			if keep_running == False:
				break
			else:
				time.sleep(int(interval_in_seconds))

	def send_email(self):
	    myEmail = ''
	    myPass = ''
	    smtp_server = 'smtp.gmail.com'
	    smtp_port = 587
	    message = '\n'.join(self.price_changes)

	    msg = MIMEText(message)
	    msg['Subject'] = f'Price change detected for ({len(self.price_changes)}) Ebay item(s)'
	    msg['From'] = myEmail
	    msg['To'] = myEmail

	    server = smtplib.SMTP(smtp_server, smtp_port)
	    server.starttls()
	    server.login(myEmail, myPass)

	    server.send_message(msg)
	    server.quit()
