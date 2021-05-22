CREATE TABLE IF NOT EXISTS sales (
		id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		order_id INT NOT NULL default 0,
		product VARCHAR(255) NOT NULL default '',
		quantity INT NOT NULL default 0,
		price_each FLOAT(10,6) default 0.0,
		order_date DATETIME default CURRENT_TIMESTAMP,
		shipping_address VARCHAR(255) default ''
)

INSERT INTO sales (order_id,product,quantity,price_each,order_date,shipping_address) 
	    VALUES (%s,%s,%s,%s,%s,%s)

-- PGSQL
-- CREATE TABLE IF NOT EXISTS sales(
--              id SERIAL NOT NULL UNIQUE PRIMARY KEY,
--              order_id INT NOT NULL default 0,
--              product VARCHAR(255) NOT NULL default '',
--              quantity INT NOT NULL default 0,
--              price_each FLOAT default 0.0,
--              order_date TIMESTAMP default CURRENT_TIMESTAMP,
--              shipping_address VARCHAR(255) default ''
--              )
-- INSERT INTO sales (order_id,product,quantity,price_each,order_date,shipping_address) 
-- 	    VALUES (%s,%s,%s,%s,%s,%s)