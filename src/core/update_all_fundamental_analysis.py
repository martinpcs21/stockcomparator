# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:49:22 2022
@author: m.perez-chuecos
"""

import FundamentalAnalysis
import sqlite3
from sqlalchemy import *
import os
import pandas as pd

def get_select_query_string(table):
    query_str = "SELECT Ticker FROM " + table
    return query_str

db_name = 'Fundamentals.db'

### READ TABLES AND REFRAME ###

cwd = os.getcwd()  # current working directory
db_path = os.path.normpath(os.path.join(cwd, '..', '../src/db', db_name))  # build normalized path to access db
# check if SQLite .db file exists !
if not os.path.isfile(db_path):
    raise Exception("DB not found! SQLite .db file does not exist in folder: {0}".format(db_path))

try:
    conn = sqlite3.connect(db_path)
    print(db_path)
    cur = conn.cursor()
    print(os.path.join('sqlite:///','../db/', db_name))
    engine = create_engine(os.path.join('sqlite:///','../db/', db_name))

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

fundamental_analysis_query = get_select_query_string(table='FundamentalAnalysis')
existing_tickers = pd.read_sql_query(fundamental_analysis_query, engine)
existing_tickers= existing_tickers['Ticker'].values.tolist()
#FundamentalAnalysis.fundamental_analysis
updated_tickers_pointer=[]
for ticker in existing_tickers:
    try:
        FundamentalAnalysis.fundamental_analysis(ticker)
        print('Updated fundamental analysis for',ticker)
        updated_tickers_pointer.append(True)
    except:
        print('Could not update fundamental analysis for',ticker)
        updated_tickers_pointer.append(False)

updated_tickers=pd.Series(updated_tickers_pointer, index=existing_tickers)
