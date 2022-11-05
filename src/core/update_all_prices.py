from yahooquery import Ticker
import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import *
import time
from yahooquery import Ticker


### HERE THE FUNCTION TO GET PRICES
def update_prices(ticker_name):
    tickers = Ticker(ticker_name)
    current_price = [tickers.price[ticker_name]['regularMarketPrice']][0]
    return current_price

def get_select_query_string(table):
    query_str = "SELECT Ticker FROM " + table
    return query_str

try:
    sqliteConnection = sqlite3.connect('../db/Fundamentals.db')
    cur = sqliteConnection.cursor()
    engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # print("Database created and Successfully Connected to SQLite")
    try:
        CurrentPriceOld = pd.read_sql_table('CurrentPrice', engine)
    except:
        print('Empty CurrentPrice table')

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

fundamental_analysis_query = get_select_query_string(table='CurrentPrice')
existing_tickers = pd.read_sql_query(fundamental_analysis_query, engine)
existing_tickers = existing_tickers['Ticker'].values.tolist()

updated_prices = []
ticker_price_index = []
for ticker in existing_tickers:
    try:
        new_price = update_prices(ticker)
        updated_prices.append(new_price)
        ticker_price_index.append(ticker)
        print('Updated price for ' + ticker + ' to ' + str(new_price))
        time.sleep(15)
    except:
        pass

df = pd.DataFrame(list(zip(ticker_price_index, updated_prices)), columns=['Ticker', 'Price'])

try:
    df.to_sql("CurrentPrice", conn, if_exists='replace', index=False)
except:
    print('Could not insert data into the database')

# Save (commit) the changes
conn.commit()

# Just be sure any changes have been committed or they will be lost.
conn.close()