""" 
Sector:
-	Banking
-	Automotive
-	REIT
-	IT Consulting
-	E-Commerce
-	Telecom
-	Airport
-	Other Transport
-	Facilities Maintenance
-	Energy
-	Oil and Gas
-	Electronics
-	Software
-	Food 
-	Health
-	Supermarket

 """

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request as u
from sqlalchemy import *
import sqlite3

Price= 1.44
MeanPricePerYear=[1, 1, 1, 1] #[2020, 2019, 2018, 2017]
CompanyName='Reno di Medici'
StockName='RM.MI'
Sector='Packaging'



#from sqlalchemy import create_engine
#from sqlalchemy import insert
conn = sqlite3.connect('Fundamentalsv2.db')
cur = conn.cursor()
engine = create_engine('sqlite:///Fundamentalsv2.db')
#conn = engine.raw_connection()
#cursor = conn.cursor()

queryString="SELECT * FROM CompanyVariables WHERE Company='"+StockName+"';"
query=cur.execute(queryString)
tabledf= pd.read_sql_table('AnnualReports',engine)
tabledfquery=pd.read_sql_query("SELECT * FROM AnnualReports WHERE Company='RM.MI';",engine)
CompanyVariables=pd.read_sql_query("SELECT * FROM CompanyVariables WHERE Company='RM.MI';",engine)

cur.close()
conn.close()


tableinitial=tabledf

tabledf= tabledf.set_index(['Year'])
#tabledf= pd.MultiIndex.from_tuples(tabledf, names=["Year", "KPI"])
tabledf= tabledf.T
#tabledf=tabledf.reset_index(level=0, inplace=True)
#tabledf= tabledf.set_index(['KPI'])
#tabledf= tabledf.set_index('KPI')

tabledfqueryordered=tabledfquery.sort_values(by="Year")

tabledfqueryordered=tabledfqueryordered.drop(["id","Company"],axis=1)
CompanyVariables=CompanyVariables.drop(["id","Company"],axis=1)
CompanyVariables=CompanyVariables.set_index('KPI')
CompanyVariables= CompanyVariables.squeeze()
CompanyVariables=CompanyVariables.apply(pd.to_numeric, errors='ignore')

tabledfqueryordered=tabledfqueryordered.set_index("KPI")


result = pd.pivot_table(tabledfqueryordered, values='Value', index=['KPI'],
                    columns=['Year'])

Statement=result.iloc[:, ::-1] # reverse columns order


##### FUNDAMENTALS ####

FundamentalsIndex= ['EPS', 
                    'Debt-to-Equity Ratio',
                    'Quick ratio / acid test ratio', 
                    'Current ratio', 
                    'Book Value',
                    'Price to Book Value',
                    'Cash/ Current Assets',
                    'Cash per stock', 
                    'Debt to Equity Ratio', 
                    'Debt Quality Ratio',
                    'ROCE Return On Capital Employed', 
                    'ROA Return On Assets', 
                    'ROE Return On Equity', 
                    'PER',
                    'FCFS Free Cash Flow per Stock', 
                    'PayOut DPS/EPS', 
                    'PFCF Price/ Free Cash Flow per Stock', 
                    'EV Enterprise Value',
                    'EV Enterprise Value USD',
                    'EV Entreprise Value at Year Reference Price',
                    'EV Enterprise Value / EBITDA',
                    'EV Entreprise Value / EBITDA at Year Reference Price',
                    'EV Entreprise Value / EBIT'
                    'P/CF Price/ Operating Cash Flow Rate', 
                    'Interest Coverage Ratio EBIT/Interest Expense',
                    'DSCR Asset Coverage Ratio', 
                    'Net Debt to EBITDA', 
                    'EBITDA tendency',
                    'Net income tendency',
                    'Free Cash Flow tendency', 
                    'Operating Cash Flow tendency', 
                    'Equity tendency',
                    'Before Tax Cost of Debt', 
                    'Tax Rate', 
                    'After Tax Cost of Debt', 
                    'ERP Equity Risk Premium',
                    'Cost of Equity CAPM Formula', 
                    'Weighted Average Maturity', 
                    'Market Value of Debt', 
                    'WACC Weighed Average Cost of Capital']

Fundamentals = pd.DataFrame(index=FundamentalsIndex, columns=Statement.columns)

Fundamentals.fillna(0)

## Balance Ratios

try:
    AnnualNetDebt= Statement.loc['annualNetDebt']
except:
    try:
        Statement.loc['annualLongTermDebt']
    except:
        AnnualLongTermDebt= Statement.loc['annualCurrentLiabilities']
        
    AnnualNetDebt= Statement.loc['annualCurrentDebt']+ AnnualLongTermDebt - Statement.loc['annualCashAndCashEquivalents']

Fundamentals.loc['Debt to Equity Ratio']=(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])/Statement.loc['annualStockholdersEquity']

Fundamentals.loc['Quick ratio / acid test ratio']=(Statement.loc['annualAccountsReceivable']+Statement.loc['annualCashAndCashEquivalents'])/Statement.loc['annualStockholdersEquity']

Fundamentals.loc['Current ratio']=Statement.loc['annualCurrentAssets']/Statement.loc['annualCurrentLiabilities']

Fundamentals.loc['Book Value']= Price/Fundamentals.loc['Book Value']

Fundamentals.loc['Price to Book Value']= Statement.loc['annualStockholdersEquity']/CompanyVariables.loc['Shares Outstanding']

Fundamentals.loc['Cash/ Current Assets']= Statement.loc['annualCashAndCashEquivalents']/Statement.loc['annualCurrentAssets']

Fundamentals.loc['Cash per stock']= Statement.loc['annualCashAndCashEquivalents']/CompanyVariables.loc['Shares Outstanding']

Fundamentals.loc['Debt Quality Ratio']= Statement.loc['annualCurrentLiabilities']/(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])

Fundamentals.loc['DSCR Asset Coverage Ratio']=(Statement.loc['annualTotalAssets']-Statement.loc['annualCurrentLiabilities'])/Statement.loc['annualTotalLiabilitiesNetMinorityInterest']

#Income Ratios

Fundamentals.loc['EPS']=Statement.loc['annualNetIncome']/CompanyVariables.loc['Shares Outstanding']

Fundamentals.loc['ROCE Return On Capital Employed']=Statement.loc['annualEBIT']/(Statement.loc['annualTotalAssets']-Statement.loc['annualCurrentLiabilities'])

Fundamentals.loc['ROA Return On Assets']=Statement.loc['annualNetIncome']/(Statement.loc['annualTotalAssets'])

Fundamentals.loc['ROE Return On Equity']=Statement.loc['annualNetIncome']/Statement.loc['annualStockholdersEquity']

Fundamentals.loc['PER']=Price/Fundamentals.loc['EPS']

Fundamentals.loc['FCFS Free Cash Flow per Stock']=  Statement.loc['annualFreeCashFlow']/CompanyVariables.loc['Shares Outstanding']

Fundamentals.loc['PayOut DPS/EPS']=CompanyVariables.loc['Trailing Annual Dividend Rate']/Fundamentals.loc['EPS']

Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock']=Price/Fundamentals.loc['FCFS Free Cash Flow per Stock']

Fundamentals.loc['EV Enterprise Value']= Price*CompanyVariables.loc['Shares Outstanding']+AnnualNetDebt
Fundamentals.loc['EV Enterprise Value / EBITDA']= Fundamentals.loc['EV Enterprise Value']/Statement.loc['annualNormalizedEBITDA']
Fundamentals.loc['EV Enterprise Value / EBIT']= Fundamentals.loc['EV Enterprise Value']/Statement.loc['annualEBIT']

for i in range(len(Fundamentals.loc['EV Enterprise Value'])):
    Fundamentals.loc['EV Entreprise Value at Year Reference Price'][Fundamentals.columns[i]]=MeanPricePerYear[i]*CompanyVariables.loc['Shares Outstanding']+AnnualNetDebt.iloc[i]

Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price']= Fundamentals.loc['EV Entreprise Value at Year Reference Price']/Statement.loc['annualNormalizedEBITDA']

Fundamentals.loc['P/CF Price/ Operating Cash Flow Rate']=Price/Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock']

Fundamentals.loc['Interest Coverage Ratio EBIT/Interest Expense']=Statement.loc['annualEBIT']/Statement.loc['annualInterestExpense']

Fundamentals.loc['Net Debt to EBITDA']=AnnualNetDebt/Statement.loc['annualNormalizedEBITDA']

## Tendency
if len(Statement.columns)==4:
    x=[0,1,2,3]
elif len(Statement.columns)==3: 
    x=[0,1,2]
    
A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, Statement.loc['annualNormalizedEBITDA'][::-1],rcond=-1)[0]
Fundamentals.loc['EBITDA tendency']= m/Statement.loc['annualNormalizedEBITDA'][2017]

m, c = np.linalg.lstsq(A, Statement.loc['annualNetIncome'][::-1],rcond=-1)[0]
Fundamentals.loc['Net income tendency']=m/Statement.loc['annualNetIncome'][2017]

m, c = np.linalg.lstsq(A, Statement.loc['annualFreeCashFlow'][::-1],rcond=-1)[0]
Fundamentals.loc['Free Cash Flow tendency']=m/Statement.loc['annualFreeCashFlow'][2017]

m, c = np.linalg.lstsq(A, Statement.loc['annualOperatingCashFlow'][::-1],rcond=-1)[0]
Fundamentals.loc['Operating Cash Flow tendency']=m/Statement.loc['annualOperatingCashFlow'][2017]

m, c = np.linalg.lstsq(A, Statement.loc['annualStockholdersEquity'][::-1],rcond=-1)[0]
Fundamentals.loc['Equity tendency']=m/Statement.loc['annualStockholdersEquity'][2017]

## Discounted Cash Flows
Fundamentals.loc['Before Tax Cost of Debt']=Statement.loc['annualInterestExpense']/Statement.loc['annualTotalLiabilitiesNetMinorityInterest']
Fundamentals.loc['Tax Rate']=Statement.loc['annualTaxProvision']/(Statement.loc['annualNetIncome']+ Statement.loc['annualTaxProvision'])
Fundamentals.loc['After Tax Cost of Debt']=(1-Fundamentals.loc['Tax Rate'])*Fundamentals.loc['Before Tax Cost of Debt']

RiskFreeReturnTreasuryUSA10YearsInterest=0.0064
HistoricalSP500Return=0.08

Fundamentals.loc['ERP Equity Risk Premium']=CompanyVariables.loc['Beta (5Y Monthly)']*(HistoricalSP500Return-RiskFreeReturnTreasuryUSA10YearsInterest) # Equity Risk Premium(ERP) - Excess return that investing in the stock market provides over a risk-free rate --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return) 
Fundamentals.loc['Cost of Equity CAPM Formula']= RiskFreeReturnTreasuryUSA10YearsInterest+ CompanyVariables.loc['Beta (5Y Monthly)']*(HistoricalSP500Return-RiskFreeReturnTreasuryUSA10YearsInterest) # Cost of equity (CAPM Formula) --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return) 
Fundamentals.loc['Weighted Average Maturity']=1+(1-Fundamentals.loc['Debt Quality Ratio'])*10
Fundamentals.loc['Market Value of Debt']=Statement.loc['annualInterestExpense']*((1-pow(1/(1+Fundamentals.loc['After Tax Cost of Debt']),Fundamentals.loc['Weighted Average Maturity'])))+AnnualNetDebt/(pow((1+Fundamentals.loc['After Tax Cost of Debt']),Fundamentals.loc['Weighted Average Maturity']))
Fundamentals.loc['Market Value of Equity']=Price*CompanyVariables.loc['Shares Outstanding']
WeightOfEquity = Fundamentals.loc['Market Value of Equity']/(Fundamentals.loc['Market Value of Equity']+Fundamentals.loc['Market Value of Debt'])
WeightOfDebt = Fundamentals.loc['Market Value of Debt']/(Fundamentals.loc['Market Value of Equity']+Fundamentals.loc['Market Value of Debt'])
Fundamentals.loc['WACC Weighed Average Cost of Capital']= WeightOfEquity*Fundamentals.loc['Cost of Equity CAPM Formula']+ WeightOfDebt*Fundamentals.loc['After Tax Cost of Debt']

DCFYears=5
WACC=Fundamentals.loc['WACC Weighed Average Cost of Capital'][Statement.columns[0]]

DCFFuture=[]
DCFFuture.append(Statement.loc['annualFreeCashFlow'][Statement.columns[0]]*0.5+Statement.loc['annualFreeCashFlow'][Statement.columns[1]]*0.3+Statement.loc['annualFreeCashFlow'][Statement.columns[2]]*0.15+Statement.loc['annualFreeCashFlow'][Statement.columns[3]]*0.05)

for i in range(DCFYears):
    if DCFFuture[0]>0 and i>0:
        DCFFuture.append(DCFFuture[i-1]*(1+Fundamentals.loc['EBITDA tendency'][Statement.columns[0]]))
        print(DCFFuture[i])
    elif i>0:
        DCFFuture.append(DCFFuture[i-1]*(1-Fundamentals.loc['EBITDA tendency'][Statement.columns[0]]))
        
DCFFuture=np.array(DCFFuture)    
DCFPresent= DCFFuture/((1+WACC)**(i+1))

if Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0)<7.5:
    DCFExitMultiple= (Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0))*(Statement.loc['annualNormalizedEBITDA'][Fundamentals.columns[0]])
else:
    DCFExitMultiple= 7.5*(Statement.loc['annualNormalizedEBITDA'][Fundamentals.columns[0]])

DCFTotalFirmValue=np.sum(DCFPresent)+DCFExitMultiple

DCFResidualValue=DCFTotalFirmValue - Fundamentals.loc['Market Value of Debt'][Fundamentals.columns[0]]+ Fundamentals.loc['Cash per stock'][Fundamentals.columns[0]]
DCFTargetPrice=DCFResidualValue/CompanyVariables.loc['Shares Outstanding']
# Variables to be stored in the database


FundamentalmentalAnalysisDataBase=pd.Series({
    'Ticker': StockName,
    'CompanyName': CompanyName,
    'CurrentPrice': Price,
    'Sector':Sector,
    'CurrentPER': Fundamentals.loc['PER'][Fundamentals.columns[0]],
    'MeanPER': Fundamentals.loc['PER'].mean(axis=0),
    'CurrentEVEBITDA': Fundamentals.loc['EV Enterprise Value / EBITDA'][Fundamentals.columns[0]],
    'MeanEVEBITDA':Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0),
    'CurrentEVEBIT': Fundamentals.loc['EV Enterprise Value / EBIT'][Fundamentals.columns[0]],
    'CurrentPricetoBook':Fundamentals.loc['Price to Book Value'][Fundamentals.columns[0]],
    'CurrentPricetoFreeCashFlowRate':Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][Fundamentals.columns[0]],
    'MeanPricetoFreeCashFlowRate':Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'].mean(axis=0), #this has to be updated with reference price
    'DividendYield':CompanyVariables.loc['Forward Annual Dividend Yield'],
    'PayOut':CompanyVariables.loc['Forward Annual Dividend Rate'],
    'ROE': Fundamentals.loc['ROE Return On Equity'][Fundamentals.columns[0]],
    'ROCE':Fundamentals.loc['ROCE Return On Capital Employed'][Fundamentals.columns[0]],
    'ROA':Fundamentals.loc['ROA Return On Assets'][Fundamentals.columns[0]],
    'Beta':CompanyVariables.loc['Beta (5Y Monthly)'],
    'LiquidityRatio':Fundamentals.loc['Cash/ Current Assets'][Fundamentals.columns[0]],
    'CashperShare': Fundamentals.loc['Cash per stock'][Fundamentals.columns[0]],
    'DebtQualityRatio': Fundamentals.loc['Debt Quality Ratio'][Fundamentals.columns[0]],
    'LiabilitiestoEquityRatio':Fundamentals.loc['Debt to Equity Ratio'][Fundamentals.columns[0]],
    'NetDebttoEBITDA':Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]],
    'MeanNetDebttoEBITDA':Fundamentals.loc['Net Debt to EBITDA'].mean(axis=0),
    'InterestExpensetoEBIT':Fundamentals.loc['Interest Coverage Ratio EBIT/Interest Expense'][Fundamentals.columns[0]],
    'DCFValuewithExitMultiple':DCFTargetPrice,
    'EBITDATendency':Fundamentals.loc['EBITDA tendency'][Fundamentals.columns[0]],
    'FreeCashFlowTendency':Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]],
    'OperatingCashFlowTendency':Fundamentals.loc['Operating Cash Flow tendency'][Fundamentals.columns[0]],
    'NetIncomeTendency':Fundamentals.loc['Net income tendency'][Fundamentals.columns[0]],
    'EquityTendency':Fundamentals.loc['Equity tendency'][Fundamentals.columns[0]],
    })

FundamentalmentalAnalysisDataBase=FundamentalmentalAnalysisDataBase.to_frame().T

try: 
    sqliteConnection = sqlite3.connect('Fundamentals.db')
    cur = sqliteConnection.cursor()
    engine = create_engine('sqlite:///Fundamentals.db', echo=False)
    conn = engine.raw_connection()
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")
    FundamentalmentalAnalysisDataBase.to_sql("FundamentalAnalysis",con=engine, index=False,if_exists='replace')
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






