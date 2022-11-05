import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3
import datetime


ticker_name = 'DND.TO'
ordinary_shares_alternative=False

def get_select_query_string(table, stock):
    """
    Generate query string (SELECT)
    :param table: [string] name of the table
    :param stock: [string] stock code of the company
    :return: [string] SQL statement
    """
    query_str = "SELECT * FROM " + table + " WHERE Ticker='" + stock + "';"
    return query_str

def calcutate_tendency(kpi, kpi_tendency, x_axis_matrix):
    slope, c = np.linalg.lstsq(x_axis_matrix, Statement.loc[kpi][::-1], rcond=-1)[0]
    try:
        if Statement.loc[kpi].values[-1] > 0:
            Fundamentals.loc[kpi_tendency] = slope / Statement.loc[kpi].values[-1]
        else:
            Fundamentals.loc[kpi_tendency] = slope / Statement.loc[kpi].mean()
    except:
        Fundamentals.loc[kpi_tendency]=0

db_name = 'Fundamentals.db'

### READ TABLES AND REFRAME ###

cwd = os.getcwd()  # current working directory
db_path = os.path.normpath(os.path.join(cwd, '../src', '../src/db', db_name))  # build normalized path to access db
# check if SQLite .db file exists !
if not os.path.isfile(db_path):
    raise Exception("DB not found! SQLite .db file does not exist in folder: {0}".format(db_path))

try:
    conn = sqlite3.connect(db_path)
    print(db_path)
    cur = conn.cursor()
    print(os.path.join('sqlite:///', '../src/db/', db_name))
    engine = create_engine(os.path.join('sqlite:///', '../src/db/', db_name))

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

## company variables: country, beta, sector ...

company_variables_query = get_select_query_string(table='Companies', stock=ticker_name)
CompanyVariables = pd.read_sql_query(company_variables_query, engine)
CompanyVariables=CompanyVariables.drop(["Ticker"],axis=1)
CompanyVariables= CompanyVariables.squeeze()
CompanyVariables=CompanyVariables.apply(pd.to_numeric, errors='ignore')

#currency
currency_to_usd_dict={
    'USD': 1,
    'EUR': 0.87,
    'GBP': 134,
    'GBp': 1.34,
    'JPY': 0.0088,
    'CNY': 0.15,
    'CAD': 0.77,
    'HKD': 0.12,
    'CHF': 1.08,
    'SEK': 0.11,
    'KRW': 0.00081,
    'CHF': 0.9,
    'TWD':0.033,
}

currency_to_usd_conversion_factor= currency_to_usd_dict[CompanyVariables['ReportCurrency']]
stock_currency_to_usd_conversion_factor= currency_to_usd_dict[CompanyVariables['StockCurrency']]
report_currency_to_usd_conversion_factor= currency_to_usd_dict[CompanyVariables['ReportCurrency']]

price_conversion_factor=stock_currency_to_usd_conversion_factor/report_currency_to_usd_conversion_factor

## current price
current_prices_query = get_select_query_string(table='CurrentPrice', stock=ticker_name)
current_price = pd.read_sql_query(current_prices_query, engine)
price=current_price['Price'][0]*price_conversion_factor


## historical price
company_prices_query = get_select_query_string(table='HistoricalPrices', stock=ticker_name)
companyPrices = pd.read_sql_query(company_prices_query, engine)
companyPrices=companyPrices.T
companyPrices.columns=companyPrices.loc['Year']
companyPrices=companyPrices.drop(['Ticker','id','Year'])
companyPrices.loc['MeanPrice']=companyPrices.loc['MeanPrice']*price_conversion_factor
years_in_historical_price=companyPrices.columns.tolist()


## previous existing fundamental analyis
try:
    FundamentalAnalysisOld = pd.read_sql_table('FundamentalAnalysis', engine)
    # FundamentalAnalysisOld = pd.read_sql_query('SELECT * FROM FundamentalAnalysis', conn)
except:
    print('Empty FundamentalAnalysis table')

## annual report
annual_reports_query = get_select_query_string(table='AnnualReports', stock=ticker_name)
tabledfquery = pd.read_sql_query(annual_reports_query, engine)
tabledfqueryordered=tabledfquery.sort_values(by="Year")
tabledfqueryordered=tabledfqueryordered.drop(["Ticker","id"],axis=1)
tabledfqueryordered=tabledfqueryordered.set_index("kpi")
result = pd.pivot_table(tabledfqueryordered, values='Value', index=['kpi'], columns=['Year'])
Statement=result.iloc[:, ::-1] # reverse columns order
statement_years=Statement.columns.tolist()

# adapt years between historical prices and annual report to match dataframes
if len(years_in_historical_price) < len(statement_years):
    Statement = Statement.loc[:, Statement.columns.isin(years_in_historical_price)]

elif len(statement_years) < len(years_in_historical_price):
    companyPrices = companyPrices.loc[:, companyPrices.columns.isin(statement_years)]

companyPrices = companyPrices.loc[:,~companyPrices.columns.duplicated()]
mean_price_per_year = (companyPrices.loc['MeanPrice'][::-1]).tolist()

##### FUNDAMENTAL ANALYSIS ####

FundamentalsIndex= ['EPS',
                    'FFO Funds From Operations per share',
                    'Debt-to-Equity Ratio',
                    'Quick ratio / acid test ratio',
                    'Current ratio',
                    'Book Value',
                    'Price to Book Value',
                    'Price to Book Value at Year Reference Price',
                    'Cash/ Total Assets',
                    'Cash per stock',
                    'Debt to Equity Ratio',
                    'Debt Quality Ratio',
                    'ROCE Return On Capital Employed',
                    'ROA Return On Assets',
                    'ROE Return On Equity',
                    'ROIC Return On Invested Capital',
                    'PER',
                    'PFFO', #Price / Funds From Operations per share --> For REIT Valuations
                    'PER at Year Reference Price',
                    'PFFO at Year Reference Price',
                    'FCFS Free Cash Flow per Stock',
                    'PayOut DPS/EPS',
                    'PFCF Price/ Free Cash Flow per Stock',
                    'PFCF Price/ Free Cash Flow per Stock at Year Reference Price',
                    'EV Enterprise Value',
                    'EV Enterprise Value USD',
                    'EV Enterprise Value at Year Reference Price',
                    'EV Enterprise Value / EBITDA',
                    'EV Enterprise Value / EBITDA at Year Reference Price',
                    'EV Enterprise Value / EBIT',
                    'EV Enterprise Value / EBIT at Year Reference Price',
                    'P/CF Price/ Operating Cash Flow Rate',
                    'Interest Coverage Ratio EBIT/Interest Expense',
                    'Interest Expense/ EBIT',
                    'DSCR Asset Coverage Ratio',
                    'Net Debt to EBITDA',
                    'EBITDA tendency',
                    'Net income tendency',
                    'Free Cash Flow tendency',
                    'Operating Cash Flow tendency',
                    'Equity tendency',
                    'Operating Revenue tendency',
                    'Before Tax Cost of Debt',
                    'Tax Rate',
                    'After Tax Cost of Debt',
                    'ERP Equity Risk Premium',
                    'Cost of Equity CAPM Formula',
                    'Weighted Average Maturity',
                    'Market Value of Debt',
                    'WACC Weighed Average Cost of Capital',
                    'EBITDA Margin',
                    'NetIncomeMargin']

Fundamentals = pd.DataFrame(index=FundamentalsIndex, columns=Statement.columns)

Fundamentals.fillna(0)

## Balance Ratios

if ordinary_shares_alternative:
    Statement.loc['annualOrdinarySharesNumber']=CompanyVariables.loc['SharesOutstanding']

try:
    AnnualNetDebt =  Statement.loc['annualTotalDebt']- Statement.loc['annualCashAndCashEquivalents']
except:
    try:
        AnnualLongTermDebt=Statement.loc['annualLongTermDebt']
        AnnualCurrentTermDebt = Statement.loc['annualCurrentDebt']
        AnnualNetDebt = AnnualCurrentTermDebt + AnnualLongTermDebt - Statement.loc['annualCashAndCashEquivalents']
    except:
        try:
            AnnualNetDebt = Statement.loc['annualNetDebt']
        except:
            AnnualCurrentTermDebt = Statement.loc['annualCurrentLiabilities']
            AnnualLongTermDebt = Statement.loc['annualCurrentLiabilities']
            AnnualNetDebt = AnnualCurrentTermDebt + AnnualLongTermDebt - Statement.loc['annualCashAndCashEquivalents']

try:
    AnnualEquity= Statement.loc['annualStockholdersEquity']
except:
    AnnualEquity=Statement.loc['annualCommonStockEquity']

Statement.loc['annualStockholdersEquity'] = AnnualEquity

try:
    AnnualInterestExpense=Statement.loc['annualInterestExpense']
except:
    AnnualInterestExpense=Statement.loc['annualEBIT']-Statement.loc['annualNetIncome']-Statement.loc['annualTaxProvision']


#Fundamentals.loc['Debt to Equity Ratio']=(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])/AnnualEquity

try:
    Fundamentals.loc['Quick ratio / acid test ratio']=(Statement.loc['annualAccountsReceivable']+Statement.loc['annualCashAndCashEquivalents'])/Statement.loc['annualCurrentLiabilities']
except:
    Fundamentals.loc['Quick ratio / acid test ratio']=(Statement.loc['annualCashAndCashEquivalents'])/Statement.loc['annualCurrentLiabilities']


Fundamentals.loc['Current ratio']=Statement.loc['annualCurrentAssets']/Statement.loc['annualCurrentLiabilities']

Fundamentals.loc['Book Value']= AnnualEquity/Statement.loc['annualOrdinarySharesNumber']

Fundamentals.loc['Price to Book Value']= price/Fundamentals.loc['Book Value']
Fundamentals.loc['Price to Book Value at Year Reference Price']= mean_price_per_year/Fundamentals.loc['Book Value']

Fundamentals.loc['Cash/ Total Assets']= Statement.loc['annualCashAndCashEquivalents']/Statement.loc['annualTotalAssets']

Fundamentals.loc['Cash per stock']= Statement.loc['annualCashAndCashEquivalents']/Statement.loc['annualOrdinarySharesNumber']

Fundamentals.loc['Debt Quality Ratio']= Statement.loc['annualCurrentLiabilities']/(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])

Fundamentals.loc['DSCR Asset Coverage Ratio']=(Statement.loc['annualTotalAssets']-Statement.loc['annualCurrentLiabilities'])/Statement.loc['annualTotalLiabilitiesNetMinorityInterest']

#Income Ratios

Fundamentals.loc['EPS']=Statement.loc['annualNetIncome']/Statement.loc['annualOrdinarySharesNumber']



Fundamentals.loc['ROCE Return On Capital Employed']=Statement.loc['annualEBIT']/(Statement.loc['annualTotalAssets']-Statement.loc['annualCurrentLiabilities'])
Fundamentals.loc['ROA Return On Assets']=Statement.loc['annualNetIncome']/(Statement.loc['annualTotalAssets'])
Fundamentals.loc['ROE Return On Equity']=Statement.loc['annualNetIncome']/AnnualEquity
Fundamentals.loc['ROIC Return On Invested Capital']=Statement.loc['annualNetIncome']/(AnnualEquity+AnnualNetDebt)

Fundamentals.loc['PER']=price/Fundamentals.loc['EPS']
Fundamentals.loc['PER at Year Reference Price']=mean_price_per_year/Fundamentals.loc['EPS']

try:
    Fundamentals.loc['FFO Funds From Operations per share']= (Statement.loc['annualNetIncome']\
                                                            + Statement.loc['annualDepreciationAndAmortization']\
                                                            + Statement.loc['annualEarningsLossesFromEquityInvestments'])/\
                                                            Statement.loc['annualOrdinarySharesNumber']
    Fundamentals.loc['PFFO'] = price / Fundamentals.loc['FFO Funds From Operations per share']
    Fundamentals.loc['PFFO at Year Reference Price'] = mean_price_per_year / Fundamentals.loc[
        'FFO Funds From Operations per share']
except:
    pass

Fundamentals.loc['EBITDA Margin']= Statement.loc['annualNormalizedEBITDA']/Statement.loc['annualOperatingRevenue']
Fundamentals.loc['Net Income Margin']= Statement.loc['annualNetIncome']/Statement.loc['annualOperatingRevenue']

for i in range(len(Fundamentals.loc['PER'])):
    if Fundamentals.loc['PER'][Fundamentals.columns[i]]<0:
        Fundamentals.loc['PER'][Fundamentals.columns[i]]=100
        Fundamentals.loc['PER at Year Reference Price'][Fundamentals.columns[i]]=100

Fundamentals.loc['FCFS Free Cash Flow per Stock']=  Statement.loc['annualFreeCashFlow']/Statement.loc['annualOrdinarySharesNumber']

#Fundamentals.loc['PayOut DPS/EPS']=CompanyVariables.loc['Trailing Annual Dividend Rate']/Fundamentals.loc['EPS']

Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock']=price/Fundamentals.loc['FCFS Free Cash Flow per Stock']
Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price']=mean_price_per_year/Fundamentals.loc['FCFS Free Cash Flow per Stock']

for i in range(len(Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'])):
    if Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][Fundamentals.columns[i]]<0:
        Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][Fundamentals.columns[i]]=100

for i in range(len(Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'])):
    if Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'][Fundamentals.columns[i]]<0:
        Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'][Fundamentals.columns[i]]=100

Fundamentals.loc['EV Enterprise Value']= price*Statement.loc['annualOrdinarySharesNumber']+AnnualNetDebt
Fundamentals.loc['EV Enterprise Value USD']= Fundamentals.loc['EV Enterprise Value']*currency_to_usd_conversion_factor
Fundamentals.loc['EV Enterprise Value / EBITDA']= Fundamentals.loc['EV Enterprise Value']/Statement.loc['annualNormalizedEBITDA']
Fundamentals.loc['EV Enterprise Value / EBIT']= Fundamentals.loc['EV Enterprise Value']/Statement.loc['annualEBIT']

for i in range(len(Fundamentals.loc['EV Enterprise Value'])):
    Fundamentals.loc['EV Enterprise Value at Year Reference Price'][Fundamentals.columns[i]]=mean_price_per_year[i]*Statement.loc['annualOrdinarySharesNumber'].iloc[i]+AnnualNetDebt.iloc[i]

Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price']= Fundamentals.loc['EV Enterprise Value at Year Reference Price']/Statement.loc['annualNormalizedEBITDA']
Fundamentals.loc['EV Enterprise Value / EBIT at Year Reference Price']= Fundamentals.loc['EV Enterprise Value at Year Reference Price']/Statement.loc['annualEBIT']

Fundamentals.loc['P/CF Price/ Operating Cash Flow Rate']=price/Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock']
Fundamentals.loc['Interest Expense/ EBIT']=AnnualInterestExpense/Statement.loc['annualEBIT']
Fundamentals.loc['Net Debt to EBITDA']=AnnualNetDebt/Statement.loc['annualNormalizedEBITDA']

## TENDENCY ##
# enum years [0,n] to generate x axis for tendency
x=[]
for i in range(0,len(Statement.columns)):
    x.append(i)

x_axis_matrix = np.vstack([x, np.ones(len(x))]).T

tendency_dict={
    'EBITDA tendency':'annualNormalizedEBITDA',
    'Net income tendency':'annualNetIncome',
    'Free Cash Flow tendency':'annualFreeCashFlow',
    'Operating Revenue tendency':'annualOperatingRevenue',
    'Equity tendency':'annualStockholdersEquity',
    'Operating Cash Flow tendency':'annualOperatingCashFlow'
}

for key in tendency_dict:
    calcutate_tendency(tendency_dict[key], key, x_axis_matrix)

## Discounted Cash Flows

RiskFreeReturnTreasuryUSA10YearsInterest=0.035 #3.5% US 10 years bond yield
HistoricalSP500Return=0.08
DCFYears=5

Fundamentals.loc['Before Tax Cost of Debt']=AnnualInterestExpense/AnnualNetDebt

try:
    Fundamentals.loc['Tax Rate'] = Statement.loc['annualTaxRateForCalcs']
except:
    Fundamentals.loc['Tax Rate']=Statement.loc['annualTaxProvision']/(Statement.loc['annualNetIncome']+ Statement.loc['annualTaxProvision'])

for i in range(len(Fundamentals.loc['Tax Rate'])-1):
    if Fundamentals.loc['Tax Rate'][Fundamentals.columns[i]]<0 or Fundamentals.loc['Tax Rate'][Fundamentals.columns[i]]>1:
        Fundamentals.loc['Tax Rate'][Fundamentals.columns[i]]=0.25

Fundamentals.loc['After Tax Cost of Debt']=(1-Fundamentals.loc['Tax Rate'])*Fundamentals.loc['Before Tax Cost of Debt']
#Rates adjustements to gouvernment interest rates
for i in range(len(Fundamentals.loc['After Tax Cost of Debt'])-1):
    if Fundamentals.loc['After Tax Cost of Debt'][Fundamentals.columns[i]]<RiskFreeReturnTreasuryUSA10YearsInterest:
        Fundamentals.loc['After Tax Cost of Debt'][Fundamentals.columns[i]]=RiskFreeReturnTreasuryUSA10YearsInterest

try:
    Beta=CompanyVariables.loc['Beta']
except:
    Beta = 1

try:
    dividend_yield=float(CompanyVariables.loc['DividendYield'])
except:
    dividend_yield=0


Fundamentals.loc['ERP Equity Risk Premium'] = Beta*(HistoricalSP500Return-RiskFreeReturnTreasuryUSA10YearsInterest) # Equity Risk Premium(ERP) - Excess return that investing in the stock market provides over a risk-free rate --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return)
Fundamentals.loc['Cost of Equity CAPM Formula'] = RiskFreeReturnTreasuryUSA10YearsInterest + Beta*(HistoricalSP500Return-RiskFreeReturnTreasuryUSA10YearsInterest) # Cost of equity (CAPM Formula) --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return)
Fundamentals.loc['Weighted Average Maturity']=1+(1-Fundamentals.loc['Debt Quality Ratio'])*10
Fundamentals.loc['Market Value of Debt']=AnnualInterestExpense*((1-pow(1/(1+Fundamentals.loc['After Tax Cost of Debt']),Fundamentals.loc['Weighted Average Maturity'])))+AnnualNetDebt/(pow((1+Fundamentals.loc['After Tax Cost of Debt']),Fundamentals.loc['Weighted Average Maturity']))
Fundamentals.loc['Market Value of Equity']=price*Statement.loc['annualOrdinarySharesNumber'].iloc[0]
WeightOfEquity = Fundamentals.loc['Market Value of Equity']/(Fundamentals.loc['Market Value of Equity']+Fundamentals.loc['Market Value of Debt'])
WeightOfDebt = Fundamentals.loc['Market Value of Debt']/(Fundamentals.loc['Market Value of Equity']+Fundamentals.loc['Market Value of Debt'])
Fundamentals.loc['WACC Weighed Average Cost of Capital']= WeightOfEquity*Fundamentals.loc['Cost of Equity CAPM Formula']+ WeightOfDebt*Fundamentals.loc['After Tax Cost of Debt']

WACC=Fundamentals.loc['WACC Weighed Average Cost of Capital'][Fundamentals.columns[0]]

DCFFuture=[]
if Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]]>0.2 and Fundamentals.loc['EBITDA tendency'][Fundamentals.columns[0]]>0.2:
    #DCF for high growth stocks
    DCFFuture.append(Statement.loc['annualFreeCashFlow'][Statement.columns[0]])
elif len(statement_years)>=4:
    DCFFuture.append(Statement.loc['annualFreeCashFlow'][Statement.columns[0]]*0.5+Statement.loc['annualFreeCashFlow'][Statement.columns[1]]*0.3+Statement.loc['annualFreeCashFlow'][Statement.columns[2]]*0.15+Statement.loc['annualFreeCashFlow'][Statement.columns[3]]*0.05)
elif len(statement_years)==3:
    DCFFuture.append(Statement.loc['annualFreeCashFlow'][Statement.columns[0]]*0.6+Statement.loc['annualFreeCashFlow'][Statement.columns[1]]*0.3+Statement.loc['annualFreeCashFlow'][Statement.columns[2]]*0.1)

for i in range(DCFYears):
    if DCFFuture[0]>0 and i>0:

        DCFFuture.append(DCFFuture[i-1]*(1+growth_rate))
        print(DCFFuture[i])
    elif i>0:
        DCFFuture.append(DCFFuture[i-1]*(1-growth_rate))

DCFFuture=np.array(DCFFuture)
DCFPresent= DCFFuture/((1+WACC) ** DCFYears)

if Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0)<7.5:
    EBITDAExitMultiple= Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0)
elif (Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0)>9 and
       Fundamentals.loc['ROA Return On Assets'][Fundamentals.columns[0]]>0.15 and
       Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]]<1) :
    # premium for highly profitable companies: High ROA > 15% AND Low debt (Net debt to Ebitda< 1)
    EBITDAExitMultiple=9
else:
    EBITDAExitMultiple=7.5


DCFExitMultiple= EBITDAExitMultiple*(Statement.loc['annualNormalizedEBITDA'][Fundamentals.columns[0]])

DCFTotalFirmValue=np.sum(DCFPresent)+DCFExitMultiple #Risk of COMPLEX Number

DCFResidualValue=DCFTotalFirmValue - AnnualNetDebt[AnnualNetDebt.index[0]]
DCFTargetPrice=DCFResidualValue/Statement.loc['annualOrdinarySharesNumber'].iloc[0]

# Multiple valuation weights

if CompanyVariables['PercentInsidersHold']>0.3:
    insiders_weight = 1.03
else:
    insiders_weight = 1

if (CompanyVariables['Country']=='China' or
    CompanyVariables['Country']=='Hong Kong' or
    CompanyVariables['Country']=='Rusia'):
    country_transparency_weight = 0.95
else:
    country_transparency_weight = 1

if (any(cashflow<0 for cashflow in Statement.loc['annualFreeCashFlow']) == False and
    Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]]>0.07):
    # constant positive cash flows  and tendency that beats inflation
    cash_flow_stability_weight = 1.03
elif (any(cashflow<0 for cashflow in Statement.loc['annualFreeCashFlow']) == True and
      (np.std(Statement.loc['annualFreeCashFlow'])/Statement.loc['annualFreeCashFlow'][Statement.columns[0]])>0.5):
    cash_flow_stability_weight = 0.95
else:
    cash_flow_stability_weight = 1

if Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]]>3:
    net_debt_to_ebitda_weight = 0.92
elif Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]]>2:
    net_debt_to_ebitda_weight = 0.97
else:
    net_debt_to_ebitda_weight = 1

if Fundamentals.loc['Interest Expense/ EBIT'][Fundamentals.columns[0]]>0.7:
    debt_coverage_weight = 0.92
else:
    debt_coverage_weight = 1

if Fundamentals.loc['Price to Book Value'][Fundamentals.columns[0]]<0.5:
    price_to_book_weight = 1.03
else:
    price_to_book_weight = 1

if Fundamentals.loc['EV Enterprise Value USD'][Fundamentals.columns[0]]< 1e9:
    enterprise_size_weight = 0.97
else:
    enterprise_size_weight = 1


saleTargetPrice = DCFTargetPrice*cash_flow_stability_weight*net_debt_to_ebitda_weight*debt_coverage_weight*price_to_book_weight*enterprise_size_weight

# Variables to be stored in the database

FundamentalmentalAnalysisDataBase=pd.Series({
    'Ticker': ticker_name,
    'CompanyName': CompanyVariables['CompanyName'],
    'CurrentPrice': price,
    'Country':CompanyVariables['Country'],
    'Sector':CompanyVariables['Industry'],
    'LastReportDate':CompanyVariables['BalanceSheetDate'],
    'StockCurrency':CompanyVariables['StockCurrency'],
    'ReportCurrency':CompanyVariables['ReportCurrency'],
    'CurrentPER': Fundamentals.loc['PER'][Fundamentals.columns[0]],
    'MeanPER': Fundamentals.loc['PER at Year Reference Price'].mean(axis=0),
    'CurrentPricetoBook':Fundamentals.loc['Price to Book Value'][Fundamentals.columns[0]],
    'MeanPricetoBook':Fundamentals.loc['Price to Book Value at Year Reference Price'].mean(axis=0),
    'CurrentEVEBITDA':Fundamentals.loc['EV Enterprise Value / EBITDA'][Fundamentals.columns[0]],
    'MeanEVEBITDA':Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0),
    'CurrentEVEBIT':Fundamentals.loc['EV Enterprise Value / EBIT'][Fundamentals.columns[0]],
    'CurrentPricetoFreeCashFlowRate':Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][Fundamentals.columns[0]],
    'MeanPricetoFreeCashFlowRate':Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'].mean(axis=0), #this has to be updated with reference price
    'ROE': Fundamentals.loc['ROE Return On Equity'][Fundamentals.columns[0]],
    'ROCE':Fundamentals.loc['ROCE Return On Capital Employed'][Fundamentals.columns[0]],
    'ROA':Fundamentals.loc['ROA Return On Assets'][Fundamentals.columns[0]],
    'ROIC':Fundamentals.loc['ROIC Return On Invested Capital'][Fundamentals.columns[0]],
    'Beta':Beta,
    'WACC':WACC,
    'CashToTotalAssets':Fundamentals.loc['Cash/ Total Assets'][Fundamentals.columns[0]],
    'CashOverStockPrice': Fundamentals.loc['Cash per stock'][Fundamentals.columns[0]]/price,
    'DebtQualityRatio': Fundamentals.loc['Debt Quality Ratio'][Fundamentals.columns[0]],
    'LiabilitiestoEquityRatio':Fundamentals.loc['Debt to Equity Ratio'][Fundamentals.columns[0]],
    'NetDebttoEBITDA':Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]],
    'MeanNetDebttoEBITDA':Fundamentals.loc['Net Debt to EBITDA'].mean(axis=0),
    'InterestExpensetoEBIT':Fundamentals.loc['Interest Expense/ EBIT'][Fundamentals.columns[0]],
    'EntrepriseValueUSD':Fundamentals.loc['EV Enterprise Value USD'][Fundamentals.columns[0]],
    'DCFValuewithExitMultiplePotential':(saleTargetPrice/price-1),
    'EBITDATendency':Fundamentals.loc['EBITDA tendency'][Fundamentals.columns[0]],
    'FreeCashFlowTendency':Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]],
    'OperatingCashFlowTendency':Fundamentals.loc['Operating Cash Flow tendency'][Fundamentals.columns[0]],
    'NetIncomeTendency':Fundamentals.loc['Net income tendency'][Fundamentals.columns[0]],
    'EquityTendency':Fundamentals.loc['Equity tendency'][Fundamentals.columns[0]],
    'DividendYield':dividend_yield,
    'NetIncomeMargin': Fundamentals.loc['Net Income Margin'][Fundamentals.columns[0]],
    'EBITDAMargin': Fundamentals.loc['EBITDA Margin'][Fundamentals.columns[0]],
    'TargetPrice':saleTargetPrice,
    'PFFO':Fundamentals.loc['PFFO'][Fundamentals.columns[0]],
    'MeanPFFO':Fundamentals.loc['PFFO at Year Reference Price'].mean(axis=0),
    'LastUpdate':datetime.datetime.now().strftime("%Y-%m-%d")
    })

FundamentalmentalAnalysisDataBase=FundamentalmentalAnalysisDataBase.to_frame().T
#FundamentalmentalAnalysisDataBase=FundamentalmentalAnalysisDataBase.set_index(['Ticker'])


## save fundamental analysis into the database
try:
    if ticker_name in FundamentalAnalysisOld['Ticker'].tolist():
        print(FundamentalAnalysisOld['Ticker'])
        TickerToUpdateIndex=FundamentalAnalysisOld['Ticker'].tolist().index(ticker_name)
        FundamentalAnalysisOld.loc[TickerToUpdateIndex] = FundamentalmentalAnalysisDataBase.loc[0]
        FundamentalAnalysisOld.to_sql("FundamentalAnalysis",conn, if_exists='replace', index=False)
    else:
        FundamentalmentalAnalysisDataBase.to_sql("FundamentalAnalysis",conn, if_exists='append', index=False)
except:
    FundamentalmentalAnalysisDataBase.to_sql("FundamentalAnalysis",conn, if_exists='append', index=False)
    print('Could not connect to db')

record = cur.fetchall()
cur.close()
conn.commit()
conn.close()
print("The SQLite connection is closed")
