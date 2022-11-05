import streamlit as st
import sqlite3
from sqlalchemy import *
import os
import pandas as pd
import matplotlib
import sys
sys.path.insert(0,'../')
#from src.core import GetCompanyData, FundamentalAnalysis
# noinspection PyUnresolvedReferences
from GetCompanyData import get_company_data
# noinspection PyUnresolvedReferences
from FundamentalAnalysis import fundamental_analysis

st.set_page_config(
    page_title="Get Company Data",
    page_icon="",
)

#Add sidebar to the app
st.sidebar.markdown("### Stock Comparator")
st.sidebar.markdown("Welcome stock comparator app. Select the sector you are interested in and the company. Enjoy the best value stocks!")

#Add title and subtitle to the main interface of the app


container= st.empty()
ticker= st.text_input('Ticker', placeholder='GOOG')
expected_growth= st.text_input('Expected Growth', placeholder='2%')
if st.button('Calculate'):
    st.write(ticker)
    st.write(expected_growth)
    get_company_data(ticker)
    target_price=fundamental_analysis(ticker, expected_growth)
    st.write('Target price '+ str(target_price))

