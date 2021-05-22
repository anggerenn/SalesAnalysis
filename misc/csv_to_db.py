import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import urllib.parse as up

load_dotenv()

filepath = '../data/2020_Sales.csv'

schema = os.environ['MYSQL_SCHEMA']
user = os.environ['MYSQL_USER']
pwd = up.quote_plus(os.environ['MYSQL_PASSWORD'])
host = os.environ['MYSQL_HOST']
db = os.environ['MYSQL_DB']
url = f'{schema}://{user}:{pwd}@{host}/{db}'

engine = create_engine(url)

with engine.begin() as connection:
    for df in pd.read_csv(filepath, chunksize=1000):
        df.to_sql('mock_data', con=connection, index=False, if_exists='append')
