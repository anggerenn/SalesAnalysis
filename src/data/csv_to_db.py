import pandas as pd
import os
import urllib.parse as up
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

fn = './data/2020_Sales.csv'
pathname = os.path.join(Path(__file__).resolve().parents[2],fn)
df = pd.read_csv(pathname)

schema = os.environ['MYSQL_SCHEMA']
user = os.environ['MYSQL_USER']
pwd = up.quote_plus(os.environ['MYSQL_PASSWORD'])
host = os.environ['MYSQL_HOST']
db = os.environ['MYSQL_DB']
table = 'mock_data'

url = f'{schema}://{user}:{pwd}@{host}/{db}'

engine = create_engine(url)

with engine.begin() as connection:
    for df in pd.read_csv(pathname, chunksize=1000):
        df.to_sql(table, con=connection, index=False, if_exists='append')
