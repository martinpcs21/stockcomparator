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
from FundamentalAnalysis import fundamental_analysis


# Add sidebar to the app
st.sidebar.markdown("### Stock Comparator")
st.sidebar.markdown("")

# Add title and subtitle to the main interface of the app


if st.button('Update Fundamental Analysis'):

    def get_select_query_string(table):
        query_str = "SELECT Ticker FROM " + table
        return query_str


    db_name = 'Fundamentals.db'

    ### READ TABLES AND REFRAME ###

    cwd = os.getcwd()  # current working directory
    db_path = os.path.normpath(os.path.join(cwd, '../db', db_name))  # build normalized path to access db
    db_path = '/app/stockcomparator/src/db/Fundamentals.db'

    # check if SQLite .db file exists !
    if not os.path.isfile(db_path):
        raise Exception("DB not found! SQLite .db file does not exist in folder: {0}".format(db_path))

    # For engine in SQLite : ////  -->  absoulte path ; /// --> relative path
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        engine = create_engine('sqlite:////app/stockcomparator/src/db/Fundamentals.db')

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    existing_tickers_query = get_select_query_string(table='CurrentPrice')
    existing_tickers = pd.read_sql_query(existing_tickers_query, engine)
    existing_tickers = existing_tickers['Ticker'].values.tolist()
    # FundamentalAnalysis.fundamental_analysis
    updated_tickers_pointer = []
    container = st.empty()
    my_bar = st.progress(0)
    for i in range(len(existing_tickers)):
        try:
            ticker = existing_tickers[i]
            progress_percent = float(i / len(existing_tickers))
            st.write('Updated fundamental analysis for: ' + ticker)
            my_bar.progress(progress_percent)
            fundamental_analysis(ticker)
            print('Updated fundamental analysis for', ticker)
            updated_tickers_pointer.append(True)
        except:
            print('Could not update fundamental analysis for', ticker)
            updated_tickers_pointer.append(False)

    my_bar.progress(1.0)
    updated_tickers = pd.Series(updated_tickers_pointer, index=existing_tickers)