## Use this script to locally import the csv file to MySQL from the command line

- Monitor MySQL Server from the command line

  ```
  mysql -uMYSQL_USER -pMYSQL_PASSWORD database

  # mysql -uroot -p123password db0
  ```

* Create table if not exists

  ```
  CREATE TABLE IF NOT EXISTS tablename (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL DEFAULT '0',
  `product` varchar(255) NOT NULL DEFAULT '',
  `quantity` int NOT NULL DEFAULT '0',
  `price_each` float NOT NULL DEFAULT '0',
  `order_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `purchase_address` varchar(255) DEFAULT '',
  `sales` float DEFAULT '0',
  `month_num` int DEFAULT '0',
  `month_name` varchar(255) DEFAULT '',
  `street` varchar(255) DEFAULT '',
  `city_state` varchar(255) DEFAULT '',
  `city` varchar(255) DEFAULT '',
  `states` varchar(255) DEFAULT '',
  `zipcode` int DEFAULT '0',
  `dow` int DEFAULT '0',
  `day_name` varchar(255) DEFAULT '',
  `hour_order` int DEFAULT '0',
  `paired` varchar(255) DEFAULT NULL,
  `combination` varchar(255) DEFAULT NULL,
  `frequency` int DEFAULT NULL,
  `product_num` int DEFAULT NULL,
  PRIMARY KEY (`id`)
  );
  ```

* Import data to the server
  ```
  LOAD DATA LOCAL INFILE %PATH%/filename
  INTO TABLE tablename
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\r'
  IGNORE 1 LINES;
  ```
* Troubleshoot

  - ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides

    - Check the local_infile value
      ```
      SHOW GLOBAL VARIABLES LIKE 'local_infile';
      ```
    - Change its value to True
      ```
      SET GLOBAL local_infile=1;
      ```

## Use this script to generate sql dump file

```
mysqldump -uMYSQL_USER -pMYSQL_PASSWORD database tablename > %PATH%/filename
```
