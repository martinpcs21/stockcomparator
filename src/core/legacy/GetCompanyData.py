import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
from urllib.request import Request, urlopen
import numpy as np
from sklearn.linear_model import LinearRegression
import sqlite3
from sqlalchemy import *
from socket import timeout

#from sqlalchemy import *
#from sqlalchemy import insert
#conn = sqlite3.connect('Fundamentalsv2.db')
#cur = conn.cursor()
conn = sqlite3.connect('../db/Fundamentals.db')
cur = conn.cursor()
engine = create_engine('sqlite:///../db/Fundamentals.db')
conn = engine.raw_connection()
cursor = conn.cursor()

#disk_engine = create_engine('sqlite:///Fundamentals.db')

#cur.execute("INSERT INTO Adios (Company,Year,KPI,Value) VALUES ('Martin', 32, 'California', 20000.00 )")

""" try:
    sqliteConnection = sqlite3.connect('Fundamentals.db')
    cur = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cur.execute("INSERT INTO Adios (Company,Year,KPI,Value) VALUES ('Martin', 32, 'California', 20000.00 )")
    record = cur.fetchall()
    print("SQLite Database Version is: ", record)
    cur.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed") """

# Enter a stock symbol
StockName = 'MSFT'
Columns = 5
CurrentYear = True

# URL link
url_is = 'https://finance.yahoo.com/quote/' + \
    StockName + '/financials?p=' + StockName
url_bs = 'https://finance.yahoo.com/quote/' + \
    StockName + '/balance-sheet?p=' + StockName
url_cf = 'https://finance.yahoo.com/quote/' + \
    StockName + '/cash-flow?p=' + StockName
url_st = 'https://finance.yahoo.com/quote/' + \
    StockName + '/key-statistics?p=' + StockName
if Columns == 5:
    YearsList = ['ttm', '2019', '2018', '2017', '2016']
    YearListNoTTM=['2020', '2019', '2018', '2017']
elif Columns == 4 and CurrentYear == True:
    YearsList = ['ttm', '2019', '2018', '2017']
    YearListNoTTM=['2020', '2019', '2018']
else:
    YearsList = ['ttm', '2018', '2017', '2016']

##### CASH FLOW ######

req = Request(url_cf, headers={'User-Agent': 'Mozilla/5.0'})
read_data = ur.urlopen(req, timeout=50).read()
soup_cf = read_data.decode("utf-8")

soup_cf = soup_cf.split(',')
ls = []
lt = []
Token = False
Counter = 0
# print(soup_cf)
for i, l in enumerate(soup_cf):
    if l.startswith('"annual'):
        ls.append(l)
        Token = True
        Counter = 0
    elif Token == True and '{"raw":' in l and Counter < (Columns-1):
        ls.append(l)
        Counter += 1
        if Counter == (Columns-1):
            Token = False
            Counter = 0
# cashflowls=ls
CashFlowList = []
for i, l in enumerate(ls):
    if l.startswith('"annual') and ls[i+1].startswith('"reportedValue"') and ls[i+2].startswith('"reportedValue"') and ls[i+3].startswith('"reportedValue"') and ls[i+4].startswith('"reportedValue"'):
        CashFlowList.append(ls[i][:-17])
        CashFlowList.append(ls[i+4].lstrip('"reportedValue":{"raw":'))
        CashFlowList.append(ls[i+3].lstrip('"reportedValue":{"raw":'))
        CashFlowList.append(ls[i+2].lstrip('"reportedValue":{"raw":'))
        CashFlowList.append(ls[i+1].lstrip('"reportedValue":{"raw":'))
    elif l.startswith('"annual') and ls[i+1].startswith('"reportedValue"') and ls[i+2].startswith('"reportedValue"') and ls[i+3].startswith('"reportedValue"') and Columns == 4:
        CashFlowList.append(ls[i][:-17])
        CashFlowList.append(ls[i+3].lstrip('"reportedValue":{"raw":'))
        CashFlowList.append(ls[i+2].lstrip('"reportedValue":{"raw":'))
        CashFlowList.append(ls[i+1].lstrip('"reportedValue":{"raw":'))
        

YearIndex=0
ListIndex=0
KPIName=[]
CashFlowDataBaseKPIIndexList=[]
CashFlowDataBaseKPIValueList=[]
CashFlowDataBaseKPIYearList=[]
CashFlowDataBaseStockNameList=[]
for i,l in enumerate(CashFlowList):
    if l.startswith('"annual'):
        TokenDataBase=True
        KPIName=l
        YearIndex=0
    else:
        TokenDataBase=False
    if TokenDataBase==False  and YearIndex<len(YearListNoTTM):
        CashFlowDataBaseKPIIndexList.append(KPIName)
        CashFlowDataBaseKPIValueList.append(l)
        CashFlowDataBaseKPIYearList.append(YearListNoTTM[YearIndex])
        CashFlowDataBaseStockNameList.append(StockName)
        YearIndex=YearIndex+1
        ListIndex=ListIndex+1

CashFlowDFDataBase=pd.DataFrame({
    'Ticker':CashFlowDataBaseStockNameList,
    'Year':CashFlowDataBaseKPIYearList,
    'KPI':CashFlowDataBaseKPIIndexList,
    'Value':CashFlowDataBaseKPIValueList
    })

CashFlowDFDataBase=CashFlowDFDataBase.apply(pd.to_numeric, errors='ignore')
CashFlowDFDataBase=CashFlowDFDataBase.replace('"', '', regex=True)
#CashFlowDFDataBase.to_sql('EconomicIndicators', disk_engine, index=True, if_exists='append')

CashFlowList = YearsList + CashFlowList
is_data = list(zip(*[iter(CashFlowList)]*(Columns)))
# print(is_data)



CashFlow_st = pd.DataFrame(is_data[0:])
# Name columns to first row of dataframe
CashFlow_st.columns = CashFlow_st.iloc[0]
CashFlow_st = CashFlow_st.iloc[1:, ]
CashFlow_st.set_index('ttm', inplace=True, drop=True)
#CashFlow_st.rename(index={'"annualStockholdersEquity"': '12/31/2019'}, inplace=True)
CashFlow_st = CashFlow_st.replace('"', '', regex=True)
CashFlow_st = CashFlow_st.apply(pd.to_numeric, errors='ignore')
print(CashFlow_st)

##### INCOME ######

req = Request(url_is, headers={'User-Agent': 'Mozilla/5.0'})
read_data = ur.urlopen(req, timeout=50).read()
soup_is = read_data.decode("utf-8")
# print(soup_is) HASTA AQUI OK
#soup_is = BeautifulSoup(read_data, features="lxml")

soup_is = soup_is.split(',')
# print(soup_is)  # HASTA AQUI OK
ls = []
lt = []
Token = False
Counter = 0
for i, l in enumerate(soup_is):
    if l.startswith('"annual'):
        ls.append(l)
        Token = True
        Counter = 0
    elif Token == True and '{"raw":' in l and Counter < (Columns-1):
        ls.append(l)
        Counter += 1
        if Counter == (Columns-1):
            Token = False
            Counter = 0
# print(ls)
IncomeList = []
for i, l in enumerate(ls):
    if l.startswith('"annual') and ls[i+1].startswith('"reportedValue"') and ls[i+2].startswith('"reportedValue"') and ls[i+3].startswith('"reportedValue"') and ls[i+4].startswith('"reportedValue"'):
        IncomeList.append(ls[i][:-17])
        IncomeList.append(ls[i+4].lstrip('"reportedValue":{"raw":'))
        IncomeList.append(ls[i+3].lstrip('"reportedValue":{"raw":'))
        IncomeList.append(ls[i+2].lstrip('"reportedValue":{"raw":'))
        IncomeList.append(ls[i+1].lstrip('"reportedValue":{"raw":'))
    elif l.startswith('"annual') and ls[i+1].startswith('"reportedValue"') and ls[i+2].startswith('"reportedValue"') and ls[i+3].startswith('"reportedValue"') and Columns == 4:
        IncomeList.append(ls[i][:-17])
        IncomeList.append(ls[i+3].lstrip('"reportedValue":{"raw":'))
        IncomeList.append(ls[i+2].lstrip('"reportedValue":{"raw":'))
        IncomeList.append(ls[i+1].lstrip('"reportedValue":{"raw":'))
        

YearIndex=0
ListIndex=0
KPIName=[]
IncomeDataBaseKPIIndexList=[]
IncomeDataBaseKPIValueList=[]
IncomeDataBaseKPIYearList=[]
IncomeDataBaseStockNameList=[]

for i,l in enumerate(IncomeList):
    if l.startswith('"annual'):
        TokenDataBase=True
        KPIName=l
        YearIndex=0
    else:
        TokenDataBase=False
    if TokenDataBase==False and YearIndex<len(YearListNoTTM):
        IncomeDataBaseKPIIndexList.append(KPIName)
        IncomeDataBaseKPIValueList.append(l)
        IncomeDataBaseKPIYearList.append(YearListNoTTM[YearIndex])
        IncomeDataBaseStockNameList.append(StockName)
        YearIndex=YearIndex+1
        ListIndex=ListIndex+1

IncomeDFDataBase=pd.DataFrame({
    'Ticker':IncomeDataBaseStockNameList,
    'Year':IncomeDataBaseKPIYearList,
    'KPI':IncomeDataBaseKPIIndexList,
    'Value':IncomeDataBaseKPIValueList
    })

IncomeDFDataBase=IncomeDFDataBase.apply(pd.to_numeric, errors='ignore')
IncomeDFDataBase=IncomeDFDataBase.replace('"', '', regex=True)
#IncomeDFDataBase.to_sql('EconomicIndicators', disk_engine, index=True, if_exists='append')

IncomeList = YearsList + IncomeList
is_data = list(zip(*[iter(IncomeList)]*(Columns)))
# print(is_data)

Income_st = pd.DataFrame(is_data[0:])
# Name columns to first row of dataframe
Income_st.columns = Income_st.iloc[0]
Income_st = Income_st.iloc[1:, ]
Income_st.set_index('ttm', inplace=True, drop=True)
#Income_st.rename(index={'"annualStockholdersEquity"': '12/31/2019'}, inplace=True)
Income_st = Income_st.replace('"', '', regex=True)
Income_st = Income_st.apply(pd.to_numeric, errors='ignore')
print(Income_st)

##### BALANCE ######

req = Request(url_bs, headers={'User-Agent': 'Mozilla/5.0'})
read_data = ur.urlopen(req, timeout=50).read()
soup_bs = read_data.decode("utf-8")
# print(soup_bs) HASTA AQUI OK
#soup_bs = BeautifulSoup(read_data, features="lxml")

soup_bs = soup_bs.split(',')
# print(soup_bs)  # HASTA AQUI OK
ls = []
lt = []
Token = False
Counter = 0
for i, l in enumerate(soup_bs):
    if l.startswith('"annual'):
        ls.append(l)
        Token = True
        Counter = 0
    elif Token == True and '{"raw":' in l and Counter < (Columns-1):
        ls.append(l)
        Counter += 1
        if Counter == (Columns-1):
            Token = False
            Counter = 0
# print(ls)
BalanceList = []
for i, l in enumerate(ls):
    if l.startswith('"annual') and ls[i+1].startswith('"reportedValue"') and ls[i+2].startswith('"reportedValue"') and ls[i+3].startswith('"reportedValue"') and ls[i+4].startswith('"reportedValue"'):
        BalanceList.append(ls[i][:-17])
        BalanceList.append(ls[i+4].lstrip('"reportedValue":{"raw":'))
        BalanceList.append(ls[i+3].lstrip('"reportedValue":{"raw":'))
        BalanceList.append(ls[i+2].lstrip('"reportedValue":{"raw":'))
        BalanceList.append(ls[i+1].lstrip('"reportedValue":{"raw":'))
    elif l.startswith('"annual') and ls[i+1].startswith('"reportedValue"') and ls[i+2].startswith('"reportedValue"') and ls[i+3].startswith('"reportedValue"') and Columns == 4:
        BalanceList.append(ls[i][:-17])
        BalanceList.append(ls[i+3].lstrip('"reportedValue":{"raw":'))
        BalanceList.append(ls[i+2].lstrip('"reportedValue":{"raw":'))
        BalanceList.append(ls[i+1].lstrip('"reportedValue":{"raw":'))

YearIndex=0
ListIndex=0
KPIName=[]
BalanceDataBaseKPIIndexList=[]
BalanceDataBaseKPIValueList=[]
BalanceDataBaseKPIYearList=[]
BalanceDataBaseStockNameList=[]
for i,l in enumerate(BalanceList):
    if l.startswith('"annual'):
        TokenDataBase=True
        KPIName=l
        YearIndex=0
    else:
        TokenDataBase=False
    if TokenDataBase==False and YearIndex<len(YearListNoTTM):
        BalanceDataBaseKPIIndexList.append(KPIName)
        BalanceDataBaseKPIValueList.append(l)
        BalanceDataBaseKPIYearList.append(YearListNoTTM[YearIndex])
        BalanceDataBaseStockNameList.append(StockName)
        YearIndex=YearIndex+1
        ListIndex=ListIndex+1

BalanceDFDataBase=pd.DataFrame({
    'Ticker':BalanceDataBaseStockNameList,
    'Year':BalanceDataBaseKPIYearList,
    'KPI':BalanceDataBaseKPIIndexList,
    'Value':BalanceDataBaseKPIValueList
    })

BalanceDFDataBase=BalanceDFDataBase.apply(pd.to_numeric, errors='ignore')
BalanceDFDataBase=BalanceDFDataBase.replace('"', '', regex=True)
#BalanceDFDataBase.to_sql('EconomicIndicators', disk_engine, index=True, if_exists='append')

BalanceList = YearsList + BalanceList
bs_data = list(zip(*[iter(BalanceList)]*(Columns)))
# print(bs_data)

Balance_st = pd.DataFrame(bs_data[0:])
# Name columns to first row of dataframe
Balance_st.columns = Balance_st.iloc[0]
Balance_st = Balance_st.iloc[1:, ]
Balance_st.set_index('ttm', inplace=True, drop=True)
#Income_st.rename(index={'"annualStockholdersEquity"': '12/31/2019'}, inplace=True)
Balance_st = Balance_st.replace({'"': ''}, regex=True)
Balance_st = Balance_st.apply(pd.to_numeric, errors='ignore')

Balance_st= Balance_st.T
Balance_st.index.rename='Year'
Balance_st.insert(0,'Ticker',StockName) #insert a column with the company name in the dataframe
#Balance_st.set_index(0, inplace=True, drop=True)
#Balance_st.MultiIndex.from_product('Year', StockName)
print(Balance_st.columns)
print(Balance_st)

BalanceTableName= StockName+'_Balance'
#Balance_st.to_sql(BalanceTableName, disk_engine, if_exists='append', index=True)

##### STATISTICS ######

req = Request(url_st, headers={'User-Agent': 'Mozilla/5.0'})
read_data = ur.urlopen(req, timeout=50).read()

soup_st = BeautifulSoup(read_data, 'lxml')
# Creating a BeautifulSoup object of the HTML page for easy extraction of data.

ls = []
clm = []  # Create empty list
StatisticsListIndex = []  # listofindex
StatisticsListValue = []  # list of values transformed into real numbers
pointer = False

for l in soup_st.find_all('td'):
    # Find all data structure that is ‘div'
    # print(l)
    reference = l.find('span')
    if pointer == True:
        ls.append(l.string)
        pointer = False
    if reference and reference != None and reference.string != 'N/A':  # that means that the list is not empty
        # add each element one by one to the StatisticsListIndexst
        StatisticsListIndex.append(reference.string)
        pointer = True


for i, l in enumerate(ls):
    if l == None:
        ls.pop(i)
        StatisticsListIndex.pop(i)

#
# newls = new_ls[9:]

# for l in soup_st.find_all('span'):
#     # Find all data structure that is ‘div’
#     clm.append(l.string)  # add each element one by one to the list

""" currency = ''
for l in clm:
    if type(l) == str:
        if l.startswith('Currency'):
            currency = l.lstrip('Currency in ')
            print(currency)
            break """

# new_clm = [e for e in clm if e not in (
#     'Share Statistics', 'Dividends & Splits', 'Balance Sheet', 'Stock Price History', 'Income Statement',
#     'Management Effectiveness', 'Financial Highlights', 'Profitability', 'Cash Flow Statement', 'Fiscal Year', 'N/A')]

# newclm = new_clm[25:75]


for i, l in enumerate(ls):
        if l.endswith('T'):
            # Removing last characters
            l = l[:-1]
            l = float(l)*1e12
            StatisticsListValue.append(l)
        elif l.endswith('B'):
            # Removing last characters
            l = l[:-1]
            l = float(l)*1e9
            StatisticsListValue.append(l)
        elif l.endswith('M'):
            l = l[:-1]
            l = float(l)*1e6
            StatisticsListValue.append(l)
        elif l.endswith('k'):
            l = l[:-1]
            l = float(l)*1e3
            StatisticsListValue.append(l)
        elif l.endswith('%'):
            l = l[:-1]
            l = float(l)*0.01
            StatisticsListValue.append(l)
        else:
            StatisticsListValue.append(l)

#newls.append(currency)

#StatisticsDataBaseKPIYearList=[]
StatisticsDataBaseStockNameList=[]
for i,l in enumerate(StatisticsListValue):
        #StatisticsDataBaseKPIYearList.append(YearListNoTTM[0])
        StatisticsDataBaseStockNameList.append(StockName)

StatisticsDFDataBase=pd.DataFrame({
    'Ticker':StatisticsDataBaseStockNameList,
    'KPI':StatisticsListIndex,
    'Value':StatisticsListValue
    })


StatisticsDFDataBase=StatisticsDFDataBase.apply(pd.to_numeric, errors='ignore')
StatisticsDFDataBase=StatisticsDFDataBase.replace('"', '', regex=True)
#BalanceDFDataBase.to_sql('EconomicIndicators', disk_engine, index=True, if_exists='append')


#li.append('Currency in')
#Statistics_st = pd.Series(StatisticsListValue, index=StatisticsListIndex)
#Statistics_st = Statistics_st.apply(pd.to_numeric, errors='ignore')
#print(Statistics_st)
#StatisticsDFDataBase.to_sql('EconomicIndicators', disk_engine, index=True, if_exists='append')

try:
    sqliteConnection = sqlite3.connect('../db/Fundamentals.db')
    cur = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    
    
    for i in range(len(BalanceDFDataBase)):
        try:
            BalanceDFDataBase.iloc[i:i+1].to_sql("AnnualReports",conn, index=False,if_exists='append')
        except sqlite3.Error:
            print('Data already in database')
            print(sqlite3.Error)
            pass #or any other action
    for i in range(len(IncomeDFDataBase)):
        try:
            IncomeDFDataBase.iloc[i:i+1].to_sql("AnnualReports",conn, index=False,if_exists='append')
        except sqlite3.Error:
            print('Data already in database')
            print(sqlite3.Error)
            pass #or any other action
    for i in range(len(CashFlowDFDataBase)):
        try:
            CashFlowDFDataBase.iloc[i:i+1].to_sql("AnnualReports",conn, index=False,if_exists='append')
        except sqlite3.Error:
            print('Data already in database')
            print(sqlite3.Error)
            pass #or any other action
    for i in range(len(StatisticsDFDataBase)):
        try:
            StatisticsDFDataBase.iloc[i:i+1].to_sql("CompanyVariables",conn, index=False,if_exists='append')
        except sqlite3.Error:
            print('Data already in database')
            print(sqlite3.Error)
            pass #or any other action

    #BalanceDFDataBase.to_sql('AnnualReports', conn, index=False, if_exists='append')
    #StatisticsDFDataBase.to_sql('CompanyVariables', conn, index=False, if_exists='append')    
    #IncomeDFDataBase.to_sql('AnnualReports', conn, index=False, if_exists='append')
    #CashFlowDFDataBase.to_sql('AnnualReports', conn, index=False, if_exists='append')
    record = cur.fetchall()
    print("SQLite Database Version is: ", record)
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

