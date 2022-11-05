import streamlit as st
import sqlite3
from sqlalchemy import *
import os
import pandas as pd
import matplotlib
import sys
import datetime as dt
import time
from yahooquery import Ticker

sys.path.insert(0,'../')
# noinspection PyUnresolvedReferences
from GetCompanyData import get_company_data


# Add sidebar to the app
st.sidebar.markdown("### Stock Comparator")
st.sidebar.markdown("")

# Add title and subtitle to the main interface of the app


if st.button('Update Reports'):

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
    container = st.empty()
    my_bar = st.progress(0)

    for i in range(len(existing_tickers)):
        try:
            ticker = existing_tickers[i]
            progress_percent = float(i / len(existing_tickers))
            st.write('Updated report for: '+ ticker)
            my_bar.progress(progress_percent)
            get_company_data(ticker)
            print('Updated data for ' + ticker)
            time.sleep(10)

        except:
            pass







#st.markdown("Where are the hottest housing markets in the U.S.? Select the housing market metrics you are interested in and your insights are just a couple clicks away. Hover over the map to view more details.")

