# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 18:06:17 2021

@author: m.perez-chuecos
"""

import yfinance as yf
import pandas as pd
import sqlite3
from sqlalchemy import *

stock_name="VIS.MC"
stock = yf.Ticker(stock_name)

# get stock infos
# stock.info

# get historical market data
hist = stock.history(period="5y")


hist2017=hist.loc['2017-01-01':'2017-12-31']
hist2018=hist.loc['2018-01-01':'2018-12-31']
hist2019=hist.loc['2019-01-01':'2019-12-31']
hist2020=hist.loc['2020-01-01':'2020-12-31']

currency_to_usd_dict={
        'USD': 1,
        'EUR': 0.87,
        'JPY': 0.0088,
        'CNY': 0.15,
        'CAD': 0.77,
        'HKD': 0.12,
        'CHF': 1.08,
    }

report_currency= stock.info['financialCurrency']
stock_currency= stock.info['currency']
price=stock.info['currentPrice']

stock_currency_to_usd_conversion_factor= currency_to_usd_dict[stock_currency]
report_currency_to_usd_conversion_factor= currency_to_usd_dict[report_currency]

price_conversion_factor=stock_currency_to_usd_conversion_factor/report_currency_to_usd_conversion_factor

CompanyPriceDataBase=pd.Series({
        'Ticker': stock_name,
        'CurrentPrice': price*price_conversion_factor,
        'ReportCurrency':report_currency,
        'StockCurrency':stock_currency,

        '2020MeanPrice': (hist2020['Open'].mean())*price_conversion_factor,
        '2020MaxPrice': (hist2020['High'].max())*price_conversion_factor,
        '2020MinPrice': (hist2020['Low'].min())*price_conversion_factor,

        '2019MeanPrice': (hist2019['Open'].mean())*price_conversion_factor,
        '2019MaxPrice': (hist2019['High'].max())*price_conversion_factor,
        '2019MinPrice': (hist2019['Low'].min())*price_conversion_factor,

        '2018MeanPrice': (hist2018['Open'].mean())*price_conversion_factor,
        '2018MaxPrice': (hist2018['High'].max())*price_conversion_factor,
        '2018MinPrice': (hist2018['Low'].min())*price_conversion_factor,

        '2017MeanPrice': (hist2017['Open'].mean())*price_conversion_factor,
        '2017MaxPrice': (hist2017['High'].max())*price_conversion_factor,
        '2017MinPrice': (hist2017['Low'].min())*price_conversion_factor,
        
    })

CompanyPriceDataBase=CompanyPriceDataBase.to_frame().T
#FundamentalmentalAnalysisDataBase=FundamentalmentalAnalysisDataBase.set_index(['Ticker'])

try:
    sqliteConnection = sqlite3.connect('../db/Fundamentals.db')
    cur = sqliteConnection.cursor()
    engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    # print("Database created and Successfully Connected to SQLite")

    try:
        CompanyPricesOld = pd.read_sql_table('CompanyPrices', engine)
    except:
        print('Empty CompanyPrices table')

    try:
        if stock_name in CompanyPricesOld['Ticker'].tolist():
            print(CompanyPricesOld['Ticker'])
            TickerToUpdateIndex = CompanyPricesOld['Ticker'].tolist().index(stock_name)
            CompanyPricesOld.loc[TickerToUpdateIndex] = CompanyPriceDataBase.loc[0]
            CompanyPricesOld.to_sql("CompanyPrices", conn, if_exists='replace', index=False)
        else:
            CompanyPriceDataBase.to_sql("CompanyPrices", conn, if_exists='append', index=False)
    except:
        CompanyPriceDataBase.to_sql("CompanyPrices",conn, if_exists='append', index=False)
    
    

    record = cur.fetchall()
    cur.close()

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
