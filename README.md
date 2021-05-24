# Mock Data to Dashboard

The objective of this project is to create a sales dashboard poc

### Folder Structure

```
.
├─ data
│  ├─ 2020_Sales.csv                <- Cleaned data after analysis
│  ├─ Sales_April_2020.csv
│  ├─ Sales_August_2020.csv
│  ├─ Sales_December_2020.csv
│  ├─ Sales_February_2020.csv
│  ├─ Sales_January_2020.csv
│  ├─ Sales_July_2020.csv
│  ├─ Sales_June_2020.csv
│  ├─ Sales_March_2020.csv
│  ├─ Sales_May_2020.csv
│  ├─ Sales_November_2020.csv
│  ├─ Sales_October_2020.csv
│  └─ Sales_September_2020.csv
├─ src
│  ├─ data
│  │  ├─ create_sales_data.py       <- Generates sales data
│  │  ├─ csv_to_db.py               <- Import data to server
│  │  ├─ mysql_dump.sql             <- Import data using dump file
│  │  ├─ pgsql_dump.sql             
│  │  └─ README.md                  <- Import data via command line and create backup
│  └─ img
│     └─ sales_dashboard.png
├─ README.md
├─ requirements.txt
├─ sales_analysis.ipynb             <- Data analysis and initial visualization
└─ sales_dashboard.twb              <- Data visualization
```

### The Dashboard [👀](https://public.tableau.com/views/Book1_16216000778710/SalesDashboard)

![dashboard_img](./src/img/sales_dashboard.png)

This dashboard designed to answer these questions:

- What was the best month for sales? How much was earned that month?
- Which city had the highest sales?
- On which day and when is the best time to advertise?
- Which products are most often sold together?
- Which product sold the most?
