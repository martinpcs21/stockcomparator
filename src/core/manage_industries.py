from yahooquery import Ticker
import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import *
import uuid

query_str = "SELECT DISTINCT Sector, Industry FROM Companies;"

try:

    engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # print("Database created and Successfully Connected to SQLite")
    try:
        company_sectors = pd.read_sql_query(query_str, engine)
        sectors_table = pd.read_sql_table('Sector', engine)
        industry_table = pd.read_sql_table('Industry', engine)
    except:
        print('Error')

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

new_sector_list=[]
new_sector_uuid_list=[]
new_industry_list=[]
new_industry_uuid_list=[]


for i in (range(len(company_sectors['Industry'].to_list()))):
    if (company_sectors['Industry'].iloc[i] not in industry_table['industry'].to_list()):
        new_industry_list.append(company_sectors['Industry'].to_list()[i])
        new_sector_list.append(company_sectors['Sector'].to_list()[i])
        sectors_id_df= sectors_table.loc[sectors_table['sector'] == company_sectors['Sector'][i]]
        sector_series = sectors_id_df['id'] #series
        sector_assign= str((sector_series.values)[0])
        new_sector_uuid_list.append(sector_assign)
        uuid_assign = str(uuid.uuid4())
        while uuid_assign in industry_table['id'].to_list():
            uuid_assign = str(uuid.uuid4())
        new_industry_uuid_list.append(uuid_assign)


df = pd.DataFrame(list(zip(new_industry_uuid_list, new_industry_list, new_sector_uuid_list, new_sector_list)),columns=['id','industry','sectorId','sector'])

try:
    df.to_sql("Industry",conn, if_exists='append', index=False)
except:
    print('Could not insert data into the database')

# Save (commit) the changes
conn.commit()

# Just be sure any changes have been committed or they will be lost.
conn.close()