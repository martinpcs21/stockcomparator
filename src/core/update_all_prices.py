from yahooquery import Ticker
import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import *

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
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

# Save (commit) the changes
conn.commit()

# Just be sure any changes have been committed or they will be lost.
conn.close()


# tickers = Ticker(ticker_name)
#
# #Current Price
# current_price = [tickers.price[ticker_name]['regularMarketPrice']]
# current_price_db=pd.DataFrame({'Ticker':ticker_name,'Price':current_price})
#
#
#
#
#
#     try:
#         if ticker_name in CurrentPriceOld['Ticker'].tolist():
#             print(CurrentPriceOld['Ticker'])
#             TickerToUpdateIndex = CurrentPriceOld['Ticker'].tolist().index(ticker_name)
#             CurrentPriceOld.loc[TickerToUpdateIndex] = current_price_db.loc[0]
#             CurrentPriceOld.to_sql("CurrentPrice", conn, if_exists='replace', index=False)
#         else:
#             current_price_db.to_sql("CurrentPrice", conn, if_exists='append', index=False)
#     except:
#         current_price_db.to_sql("CurrentPrice", conn, if_exists='append', index=False)