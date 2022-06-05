import streamlit as st
import sqlite3
from sqlalchemy import *
import os
import pandas as pd
import matplotlib


#get data
def get_select_query_string(table):
    query_str = "SELECT * FROM " + table
    return query_str

db_name = 'Fundamentals.db'

### READ TABLES AND REFRAME ###

cwd = os.getcwd()  # current working directory
db_path = os.path.normpath(os.path.join(cwd, 'src/db', db_name))  # build normalized path to access db
print(db_path)
# check if SQLite .db file exists !
if not os.path.isfile(db_path):
    raise Exception("DB not found! SQLite .db file does not exist in folder: {0}".format(db_path))

try:
    conn = sqlite3.connect(db_path)
    print(db_path)
    cur = conn.cursor()
    print(os.path.join('sqlite:///','src/db/', db_name))
    engine = create_engine(os.path.join('sqlite:///','src/db/', db_name))

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

fundamental_analysis_query = get_select_query_string(table='FundamentalAnalysis')
fundamental_analysis_df = pd.read_sql_query(fundamental_analysis_query, engine)
fundamental_analysis_df=fundamental_analysis_df.set_index('CompanyName')
fundamental_analysis_df= fundamental_analysis_df[['CurrentPrice','TargetPrice','DCFValuewithExitMultiplePotential','CurrentPER','CurrentEVEBITDA', 'NetDebttoEBITDA',\
                         'CurrentPricetoFreeCashFlowRate','CurrentEVEBIT','CurrentPricetoBook',\
                         'MeanPER','MeanEVEBITDA','MeanNetDebttoEBITDA','MeanPricetoFreeCashFlowRate',\
                         'Sector','Ticker',\
                         'ROE','ROCE','ROA','Beta',\
                         'CashOverStockPrice','InterestExpensetoEBIT', 'EntrepriseValueUSD',\
                         'EBITDATendency', 'FreeCashFlowTendency', 'OperatingCashFlowTendency', 'NetIncomeTendency','EquityTendency',\
                         'LiquidityRatio','DebtQualityRatio','LiabilitiestoEquityRatio','DividendYield']]



st.set_page_config(layout="wide")

#Add sidebar to the app
st.sidebar.markdown("### Stock Comparator")
st.sidebar.markdown("Welcome stock comparator app. Select the sector you are interested in and the company. Enjoy the best value stocks!")
st.sidebar.markdown("")

#Add title and subtitle to the main interface of the app
st.title("Stock Comparator")


mapper= {
    'CurrentPrice': '{:.1f}',
    'CurrentPER': '{:.1f}',
    'MeanPER': '{:.1f}',
    'CurrentEVEBITDA': '{:.1f}',
    'MeanEVEBITDA': '{:.1f}',
    'CurrentEVEBIT': '{:.1f}',
    'CurrentPricetoBook': '{:.1f}',
    'CurrentPricetoFreeCashFlowRate': '{:.1f}',
    'MeanPricetoFreeCashFlowRate': '{:.1f}',
    'ROE': '{:.2%}',
    'ROCE': '{:.2%}',
    'ROA': '{:.2%}',
    'Beta': '{:.1f}',
    'LiquidityRatio': '{:.1f}',
    'CashOverStockPrice': '{:.2%}',
    'DebtQualityRatio': '{:.1f}',
    'LiabilitiestoEquityRatio': '{:.1f}',
    'NetDebttoEBITDA': '{:.1f}',
    'MeanNetDebttoEBITDA': '{:.1f}',
    'InterestExpensetoEBIT': '{:.2%}',
    'EntrepriseValueUSD': '{:.2g}',
    'DCFValuewithExitMultiplePotential': '{:.2%}',
    'EBITDATendency': '{:.1%}',
    'FreeCashFlowTendency': '{:.2%}',
    'OperatingCashFlowTendency': '{:.2%}',
    'NetIncomeTendency': '{:.2%}',
    'EquityTendency': '{:.2%}',
    'DividendYield': '{:.2%}',
    'TargetPrice': '{:.1f}',
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

container= st.empty()
container.dataframe(fundamental_analysis_df.style.format(mapper)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['MeanPER'], vmin=2, vmax=25)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['CurrentPER'], vmin=2, vmax=25)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['CurrentEVEBITDA'], vmin=2, vmax=15)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['MeanEVEBITDA'], vmin=2, vmax=15)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['CurrentEVEBIT'], vmin=2, vmax=20)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['CurrentPricetoBook'], vmin=0.7, vmax=3)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['CurrentPricetoFreeCashFlowRate'], vmin=5, vmax=20)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['MeanPricetoFreeCashFlowRate'], vmin=5, vmax=20)\
                                            .background_gradient(cmap='RdYlGn',subset=['ROE'], vmin=0.05, vmax=0.3)\
                                            .background_gradient(cmap='RdYlGn',subset=['ROCE'], vmin=0.05, vmax=0.3)\
                                            .background_gradient(cmap='RdYlGn',subset=['ROA'], vmin=0.03, vmax=0.25)\
                                            .background_gradient(cmap='Reds_r',subset=['LiquidityRatio'], vmin=-1, vmax=0.4)\
                                            .background_gradient(cmap='RdYlGn',subset=['CashOverStockPrice'], vmin=0.05, vmax=0.4)\
                                            .background_gradient(cmap='Reds_r',subset=['DebtQualityRatio'], vmin=2, vmax=20, text_color_threshold=0.1)\
                                            .background_gradient(cmap='Reds_r',subset=['LiabilitiestoEquityRatio'], vmin=2, vmax=20, text_color_threshold=0.1)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['NetDebttoEBITDA'], vmin=0.2, vmax=4)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['MeanNetDebttoEBITDA'], vmin=0.2, vmax=4)\
                                            .background_gradient(cmap='RdYlGn_r',subset=['InterestExpensetoEBIT'], vmin=0.1, vmax=0.8)\
                                            .background_gradient(cmap='RdYlGn',subset=['DCFValuewithExitMultiplePotential'], vmin=-0.2, vmax=0.4)\
                                            .background_gradient(cmap='RdYlGn',subset=['EBITDATendency'], vmin=-0.2, vmax=0.5)\
                                            .background_gradient(cmap='RdYlGn',subset=['FreeCashFlowTendency'], vmin=-0.2, vmax=0.5)\
                                            .background_gradient(cmap='RdYlGn',subset=['OperatingCashFlowTendency'], vmin=-0.2, vmax=0.5)\
                                            .background_gradient(cmap='RdYlGn',subset=['NetIncomeTendency'], vmin=-0.2, vmax=0.5)\
                                            .background_gradient(cmap='RdYlGn',subset=['EquityTendency'], vmin=-0.2, vmax=0.5)\
                                            ,width=None,height=700
             )



#st.markdown("Where are the hottest housing markets in the U.S.? Select the housing market metrics you are interested in and your insights are just a couple clicks away. Hover over the map to view more details.")

