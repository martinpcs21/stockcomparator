from yahooquery import Ticker
import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import *
import uuid

try:
    sqliteConnection = sqlite3.connect('../db/Fundamentals.db')
    cur = sqliteConnection.cursor()
    engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # print("Database created and Successfully Connected to SQLite")
    try:
        CurrentPriceOld = pd.read_sql_table('CurrentPrice', engine)
        uuids = pd.read_sql_table('uuid', engine)
    except:
        print('Empty CurrentPrice table')


except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

ticker_list=[]
new_uuid_list=[]
for ticker in CurrentPriceOld['Ticker'].to_list():
    print(ticker)
    if ticker not in uuids['Ticker'].to_list():
        uuid_assign = str(uuid.uuid4())
        while uuid_assign in new_uuid_list:
            uuid_assign = str(uuid.uuid4())
        new_uuid_list.append(uuid_assign)
        ticker_list.append(ticker)


df = pd.DataFrame(list(zip(new_uuid_list, ticker_list)),columns=['uuid','Ticker'])

try:
    df.to_sql("uuid",conn, if_exists='append', index=False)
except:
    print('Could not insert data into the database')



# Save (commit) the changes
conn.commit()

# Just be sure any changes have been committed or they will be lost.
conn.close()