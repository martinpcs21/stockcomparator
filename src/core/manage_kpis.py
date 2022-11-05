from yahooquery import Ticker
import pandas as pd
import sqlite3
from sqlalchemy import *
import uuid

query_str = "SELECT DISTINCT KPI FROM AnnualReports;"

try:

    engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # print("Database created and Successfully Connected to SQLite")
    try:
        company_KPIs = pd.read_sql_query(query_str, engine)
        KPIs_table = pd.read_sql_table('KPIs', engine)
    except:
        print('Error')

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

new_KPI_list=[]
new_KPI_uuid_list=[]

for i in (range(len(company_KPIs['kpi'].to_list())-1)):
    if company_KPIs['kpi'].iloc[i] not in KPIs_table['KPI'].to_list():
        new_KPI_list.append(company_KPIs['kpi'].to_list()[i])
        uuid_assign = str(uuid.uuid4())
        while uuid_assign in KPIs_table['id'].to_list():
            uuid_assign = str(uuid.uuid4())
        new_KPI_uuid_list.append(uuid_assign)


df = pd.DataFrame(list(zip(new_KPI_list,new_KPI_uuid_list)),columns=['KPI','id'])

try:
    df.to_sql("KPIs",conn, if_exists='append', index=False)
except:
    print('Could not insert data into the database')

# Save (commit) the changes
conn.commit()

# Just be sure any changes have been committed or they will be lost.
conn.close()