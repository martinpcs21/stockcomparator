import streamlit as st
import sqlite3
from sqlalchemy import *
import os
import pandas as pd
import matplotlib

st.set_page_config(
    page_title="Easy Stock Comparator",
    page_icon="👋",
    layout="wide",
)

#get data
def get_select_query_string(table):
    query_str = "SELECT * FROM " + table
    return query_str

db_name = 'Fundamentals.db'

### READ TABLES AND REFRAME ###

cwd = os.getcwd()  # current working directory
db_path = os.path.normpath(os.path.join(cwd, '../db', db_name))  # build normalized path to access db
db_path = '/app/stockcomparator/src/db/Fundamentals.db'
# check if SQLite .db file exists !
if not os.path.isfile(db_path):
    raise Exception("DB not found! SQLite .db file does not exist in folder: {0}".format(db_path))

try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    engine = create_engine('sqlite:///app/stockcomparator/src/db/Fundamentals.db')

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

fundamental_analysis_query = get_select_query_string(table='SimpleAnalysis')
fundamental_analysis_df = pd.read_sql_query(fundamental_analysis_query, engine)
fundamental_analysis_df=fundamental_analysis_df.set_index('CompanyName')




#Add sidebar to the app
st.sidebar.markdown("### Stock Comparator")
st.sidebar.markdown("Welcome stock comparator app. Select the sector you are interested in and the company. Enjoy the best value stocks!")
st.sidebar.markdown("")

#Add title and subtitle to the main interface of the app



mapper= {
    'Potential': '{:.1%}',
    'EarningsScore': '{:.1%}',
    'DebtQualityScore': '{:.1%}',
    'GrowthScore': '{:.1%}',
}


sector = fundamental_analysis_df['Sector'].unique()

#ticker_choice = st.sidebar.selectbox('', ticker)
st.sidebar.header("Select sector(s):")
sector_choice = st.sidebar.multiselect('', sector)
st.sidebar.markdown("")
st.sidebar.markdown("")
if sector_choice == []:
    pass
else:
    fundamental_analysis_df = fundamental_analysis_df[fundamental_analysis_df['Sector'].isin(sector_choice)]

ticker = fundamental_analysis_df['Ticker']
st.sidebar.header("Select company(s):")
ticker_choice = st.sidebar.multiselect('', ticker)


if ticker_choice == [] and sector_choice == []:
    pass
elif ticker_choice != [] and sector_choice == []: #only ticker choice
    fundamental_analysis_df = fundamental_analysis_df[fundamental_analysis_df['Ticker'].isin(ticker_choice)]

elif ticker_choice == [] and sector_choice != []: #only sector choice
    fundamental_analysis_df = fundamental_analysis_df[fundamental_analysis_df['Sector'].isin(sector_choice)]
    # ticker = fundamental_analysis_df['Ticker']
    # ticker_choice = st.sidebar.multiselect('', ticker)
else:
    fundamental_analysis_df = fundamental_analysis_df[fundamental_analysis_df['Sector'].isin(sector_choice)]
    # ticker = fundamental_analysis_df['Ticker']
    # ticker_choice = st.sidebar.multiselect('', ticker)
    fundamental_analysis_df = fundamental_analysis_df[fundamental_analysis_df['Ticker'].isin(ticker_choice)]


# st.write('You selected:', ticker_choice)
# st.write('You selected:', sector_choice)

# col1, col2, col3, col4, col5 = st.columns(5)
# col1.markdown("Google")
# col2.metric("Debt Quality Score", "98%")
# col3.metric("Debt Quality Score", "98%")
# col4.metric("Debt Quality Score", "98%")
# col5.metric("Debt Quality Score", "98%")
# col1, col2, col3, col4, col5 = st.columns(5)
# col1.markdown("Google Dice hola porque le da la gana")
# col2.metric("Debt Quality Score", "98%")
# col3.metric("Debt Quality Score", "98%")
# col4.metric("Debt Quality Score", "98%")
# col5.metric("Debt Quality Score", "98%")


#ontainer.dataframe(fundamental_analysis_df)
st.dataframe(fundamental_analysis_df.style.format(mapper)\
                                            .background_gradient(cmap='RdYlGn',subset=['Potential'], vmin=-0.5, vmax=1)\
                                            .background_gradient(cmap='RdYlGn',subset=['EarningsScore'], vmin=0.1, vmax=0.9)\
                                            .background_gradient(cmap='RdYlGn',subset=['DebtQualityScore'], vmin=0.1, vmax=0.9)\
                                            .background_gradient(cmap='RdYlGn',subset=['GrowthScore'], vmin=0.1, vmax=0.9)
             )



#st.markdown("Where are the hottest housing markets in the U.S.? Select the housing market metrics you are interested in and your insights are just a couple clicks away. Hover over the map to view more details.")

