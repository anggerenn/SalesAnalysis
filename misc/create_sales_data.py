import pandas as pd
import numpy
import datetime
import random
import calendar

products = {
	# Product [Prices, weights]
	'iPhone': [700, 10],
	'Google Phone': [600, 8],
	'Vareebadd Phone': [400, 3],
	'20in Monitor': [109.99, 6],
	'34in Ultrawide Monitor': [379.99, 9], 
	'27in 4K Gaming Monitor': [389.99, 9],
	'27in FHD Monitor': [149.99, 1],
	'Flatscreen TV': [300, 7],
	'Macbook Pro Laptop': [1700, 7],
	'Thinkpad Laptop': [999.99, 6],
	'AA Batteries (4-pack)': [3.84, 30],
	'AAA Batteries (4-pack)': [2.99, 6],
	'USB-C Charging Cable': [11.95, 30],
	'Lightning Charging Cable': [14.95, 30],
	'Wired Headphones': [11.99, 26],
	'Bose SoundSport Headphones': [99.99, 19],
	'Apple Airpods Headphones': [150, 22],
	'LG Washing Machine': [600.00, 1],
	'LG Dryer': [600.00, 1]
}


columns = ['Order ID', 'Product', 'Quantity', 'Price Each', 'Order Date', 'Purchase Address']

def generate_random_time(month):
	# Generate a date in the format mm/dd/year H:m
	day_range = calendar.monthrange(2020,month)[1]
	random_day = random.randint(1, day_range)

	# Peak around 12:00 (Noon) and 20:00	
	if random.random() < 0.5:
		date = datetime.datetime(2020, month, random_day, 12, 0)
	else:
		date = datetime.datetime(2020, month, random_day, 20, 0)

	time_offset = numpy.random.normal(loc=0, scale=180)
	final_date = date + datetime.timedelta(minutes=time_offset)
	
	return final_date.strftime("%m/%d/%Y %H:%M:%S")

def generate_random_address():
	street_names = ['Main', '2nd', '1st', '4th', '5th', 'Park', '6th', '7th', 'Maple', 'Pine', 'Washington', '8th', 'Cedar', 'Elm', 'Walnut', '9th', '10th', 'Lake', 'Sunset', 'Lincoln', 'Jackson', 'Church', 'River', '11th', 'Willow', 'Jefferson', 'Center', '12th', 'North', 'Lakeview', 'Ridge', 'Hickory', 'Adams', 'Cherry', 'Highland', 'Johnson', 'South', 'Dogwood', 'West', 'Chestnut', '13th', 'Spruce', '14th', 'Wilson', 'Meadow', 'Forest', 'Hill', 'Madison']
	cities = ['San Francisco', 'Boston', 'New York City', 'Austin', 'Dallas', 'Atlanta', 'Portland', 'Portland', 'Los Angeles', 'Seattle']
	weights = [9,4,5,2,3,3,2,0.5,6,3]
	states = ['CA', 'MA', 'NY', 'TX', 'TX', 'GA', 'OR', 'ME', 'CA', 'WA']
	zips = ['94016', '02215', '10001', '73301', '75001', '30301', '97035', '04101', '90001', '98101']

	street = random.choice(street_names)
	index = random.choices(range(len(cities)), weights=weights)[0] # Use range index for city to correspond with state and zip code

	return f"{random.randint(1,9999)} {street} St, {cities[index]}, {states[index]} {zips[index]}"

def write_row(order_id, product, date, address):
	price = products[product][0]		
	quantity_ordered = numpy.random.geometric(p=1.0-(1.0/price), size=1)[0] # Low price High quantity orders
	output = [order_id, product, quantity_ordered, price, date, address]
	return output

def product_2_prep(product):
	products_copy = products.copy()
	products_copy.pop(str(product))

if __name__ == '__main__':
	product_list = [product for product in products]
	weights = [products[product][1] for product in products]

	order_id = 1000

	# Create monthly sales
	for month_value in range(1,13):
		if month_value <= 10:
			orders_amount = int(numpy.random.normal(loc=12000, scale=4000))

		if month_value == 11:
			orders_amount = int(numpy.random.normal(loc=20000, scale=3000)) # Slightly high sales

		if month_value == 12:
			orders_amount = int(numpy.random.normal(loc=26000, scale=3000)) # Highest sales

		df = pd.DataFrame(columns=columns)

		# Randomly select product to fill the rows
		i = 0
		while orders_amount > 0:
			address = generate_random_address()
			date = generate_random_time(month_value)
			product = random.choices(product_list, weights=weights)[0]

			df.loc[i] = write_row(order_id, product, date, address)
			i += 1
			
			if product == "iPhone":
				if random.random() < 0.15:
					df.loc[i] = write_row(order_id, "Lightning Charging Cable", date, address)
					i += 1
				if random.random() < 0.05:
					df.loc[i] = write_row(order_id, "Apple Airpods Headphones", date, address)
					i += 1
				if random.random() < 0.07:
					df.loc[i] = write_row(order_id, "Wired Headphones", date, address)
					i += 1
			
			elif product == "Google Phone" or product == "Vareebadd Phone":
				if random.random() < 0.18:
					df.loc[i] = write_row(order_id, "USB-C Charging Cable", date, address)
					i += 1
				if random.random() < 0.04:
					df.loc[i] = write_row(order_id, "Bose SoundSport Headphones", date, address)
					i += 1
				if random.random() < 0.07:
					df.loc[i] = write_row(order_id, "Wired Headphones", date, address)
					i += 1

			if random.random() <= 0.02:
				products_copied = products.copy()
				products_copied.pop(product)
				product_removed_list = [product_2 for product_2 in products_copied]
				weights_2 = [products_copied[product_2][1] for product_2 in products_copied]

				product2 = random.choices(product_removed_list, weights=weights_2)[0]
				df.loc[i] = write_row(order_id, product2, date, address)
				i += 1

			order_id += 1
			orders_amount -= 1

		month_name = calendar.month_name[month_value]

		df.to_csv(f"Sales_{month_name}_2020.csv", index=False)

		print(f"{month_name} Complete")