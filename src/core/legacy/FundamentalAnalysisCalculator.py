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

import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3


def get_select_query_string(table, stock):
    """
    Generate query string (SELECT)
    :param table: [string] name of the table
    :param stock: [string] stock code of the company
    :return: [string] SQL statement
    """
    query_str = "SELECT * FROM " + table + " WHERE Ticker='" + stock + "';"
    return query_str

def get_company_prices(stock_name, db_name):

    cwd = os.getcwd()  # current working directory
    db_path = os.path.normpath(os.path.join(cwd, '..', '../src/db', db_name))  # build normalized path to access db
    conn = sqlite3.connect(db_path)
    print(db_path)
    cur = conn.cursor()
    print(os.path.join('sqlite:///','../db/', db_name))
    # instantiate SQLAlchemy engine
    engine = create_engine(os.path.join('sqlite:///','../db/', db_name))
    company_prices_query = get_select_query_string(table='CompanyPrices', stock=stock_name)
    print(company_prices_query)
    companyPrices = pd.read_sql_query(company_prices_query, engine)
    return company_prices_query, companyPrices




def run_fundamental_analysis(db_name, company_name, stock_name, sector, price, mean_price_per_year, currency):
    """
    Open DB for a given company and run fundamental analysis calculations.
    :param db_name: name of the .db file (SQLite) to extract the data from
    :param company_name: the name of the company (string)
    :param stock_name: the stock name (string)
    :param sector: the field of activity, from a drop-down list (string)
    :param price: the current price (double)
    :param mean_price_per_year: Mean price of the N-1 to N-4 years [array of doubles]
    :return:
    """

    cwd = os.getcwd()  # current working directory
    db_path = os.path.normpath(os.path.join(cwd, '..', '../src/db', db_name))  # build normalized path to access db

    # check if SQLite .db file exists !
    if not os.path.isfile(db_path):
        raise Exception("DB not found! SQLite .db file does not exist in folder: {0}".format(db_path))

    # connect to SQLite
    conn = sqlite3.connect(db_path)
    print(db_path)
    cur = conn.cursor()
    print(os.path.join('sqlite:///','../db/', db_name))
    # instantiate SQLAlchemy engine
    engine = create_engine(os.path.join('sqlite:///','../db/', db_name))

    company_variables_query = get_select_query_string(table='CompanyVariables', stock=stock_name)
    annual_reports_query = get_select_query_string(table='AnnualReports', stock=stock_name)

    FundamentalAnalysisOld = pd.read_sql_table('FundamentalAnalysis', engine)
    print(FundamentalAnalysisOld)
    tabledfquery = pd.read_sql_query(annual_reports_query, engine)
    CompanyVariables = pd.read_sql_query(company_variables_query, engine)

    try:
        FundamentalAnalysisOld = pd.read_sql_table('FundamentalAnalysis', engine)
    except:
        print('Empty FundamentalAnalysis table')


    cur.close()
    conn.close()

    tabledfqueryordered=tabledfquery.sort_values(by="Year")
    tabledfqueryordered=tabledfqueryordered.drop(["id","Ticker"],axis=1)
    tabledfqueryordered=tabledfqueryordered.set_index("KPI")    
    result = pd.pivot_table(tabledfqueryordered, values='Value', index=['KPI'],
                        columns=['Year'])
    Statement=result.iloc[:, ::-1] # reverse columns order

    CompanyVariables=CompanyVariables.drop(["id","Ticker"],axis=1)
    CompanyVariables=CompanyVariables.set_index('KPI')
    CompanyVariables= CompanyVariables.squeeze()
    CompanyVariables=CompanyVariables.apply(pd.to_numeric, errors='ignore')

    currency_to_usd_dict={
        'USD': 1,
        'EUR': 0.87,
        'JPY': 0.0088,
        'CNY': 0.15,
        'CAD': 0.77,
        'HKD': 0.12,
        'CHF': 1.08,
    }

    currency_to_usd_conversion_factor= currency_to_usd_dict[currency]


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
        AnnualNetDebt = Statement.loc['annualNetDebt']
    except:
        try:
            AnnualLongTermDebt=Statement.loc['annualLongTermDebt']
        except:
            AnnualLongTermDebt= Statement.loc['annualCurrentLiabilities']

        AnnualNetDebt= Statement.loc['annualCurrentDebt'] + AnnualLongTermDebt - Statement.loc['annualCashAndCashEquivalents']
        
    try:
        AnnualEquity= Statement.loc['annualStockholdersEquity']
    except:
        AnnualEquity=Statement.loc['annualCommonStockEquity']

    try:
        AnnualInterestExpense=Statement.loc['annualInterestExpense']
    except:
        AnnualInterestExpense=Statement.loc['annualEBIT']-Statement.loc['annualNetIncome']-Statement.loc['annualTaxProvision']
        

    Fundamentals.loc['Debt to Equity Ratio']=(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])/AnnualEquity

    Fundamentals.loc['Quick ratio / acid test ratio']=(Statement.loc['annualAccountsReceivable']+Statement.loc['annualCashAndCashEquivalents'])/Statement.loc['annualCurrentLiabilities']

    Fundamentals.loc['Current ratio']=Statement.loc['annualCurrentAssets']/Statement.loc['annualCurrentLiabilities']

    Fundamentals.loc['Book Value']= AnnualEquity/Statement.loc['annualOrdinarySharesNumber']

    Fundamentals.loc['Price to Book Value']= price/Fundamentals.loc['Book Value']

    Fundamentals.loc['Cash/ Current Assets']= Statement.loc['annualCashAndCashEquivalents']/Statement.loc['annualCurrentAssets']

    Fundamentals.loc['Cash per stock']= Statement.loc['annualCashAndCashEquivalents']/Statement.loc['annualOrdinarySharesNumber']

    Fundamentals.loc['Debt Quality Ratio']= Statement.loc['annualCurrentLiabilities']/(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])

    Fundamentals.loc['DSCR Asset Coverage Ratio']=(Statement.loc['annualTotalAssets']-Statement.loc['annualCurrentLiabilities'])/Statement.loc['annualTotalLiabilitiesNetMinorityInterest']

    #Income Ratios

    Fundamentals.loc['EPS']=Statement.loc['annualNetIncome']/Statement.loc['annualOrdinarySharesNumber']

    Fundamentals.loc['ROCE Return On Capital Employed']=Statement.loc['annualEBIT']/(Statement.loc['annualTotalAssets']-Statement.loc['annualCurrentLiabilities'])

    Fundamentals.loc['ROA Return On Assets']=Statement.loc['annualNetIncome']/(Statement.loc['annualTotalAssets'])

    Fundamentals.loc['ROE Return On Equity']=Statement.loc['annualNetIncome']/AnnualEquity

    Fundamentals.loc['PER']=price/Fundamentals.loc['EPS']

    Fundamentals.loc['FCFS Free Cash Flow per Stock']=  Statement.loc['annualFreeCashFlow']/Statement.loc['annualOrdinarySharesNumber']

    #Fundamentals.loc['PayOut DPS/EPS']=CompanyVariables.loc['Trailing Annual Dividend Rate']/Fundamentals.loc['EPS']

    Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock']=price/Fundamentals.loc['FCFS Free Cash Flow per Stock']

    Fundamentals.loc['EV Enterprise Value']= price*Statement.loc['annualOrdinarySharesNumber']+AnnualNetDebt
    Fundamentals.loc['EV Enterprise Value USD']= Fundamentals.loc['EV Enterprise Value']*currency_to_usd_conversion_factor
    Fundamentals.loc['EV Enterprise Value / EBITDA']= Fundamentals.loc['EV Enterprise Value']/Statement.loc['annualNormalizedEBITDA']
    Fundamentals.loc['EV Enterprise Value / EBIT']= Fundamentals.loc['EV Enterprise Value']/Statement.loc['annualEBIT']

    for i in range(len(Fundamentals.loc['EV Enterprise Value'])-1):
        Fundamentals.loc['EV Entreprise Value at Year Reference Price'][Fundamentals.columns[i]]=mean_price_per_year[i]*Statement.loc['annualOrdinarySharesNumber'].iloc[i]+AnnualNetDebt.iloc[i]

    Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price']= Fundamentals.loc['EV Entreprise Value at Year Reference Price']/Statement.loc['annualNormalizedEBITDA']

    Fundamentals.loc['P/CF Price/ Operating Cash Flow Rate']=price/Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock']

    Fundamentals.loc['Interest Expense/ EBIT']=AnnualInterestExpense/Statement.loc['annualEBIT']

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

    try:
        m, c = np.linalg.lstsq(A, Statement.loc['annualOperatingCashFlow'][::-1],rcond=-1)[0]
        Fundamentals.loc['Operating Cash Flow tendency']=m/Statement.loc['annualOperatingCashFlow'][2017]
    except:
        Fundamentals.loc['Operating Cash Flow tendency']=0

    m, c = np.linalg.lstsq(A, AnnualEquity[::-1],rcond=-1)[0]
    Fundamentals.loc['Equity tendency']=m/AnnualEquity[2017]

    ## Discounted Cash Flows
    Fundamentals.loc['Before Tax Cost of Debt']=AnnualInterestExpense/Statement.loc['annualTotalLiabilitiesNetMinorityInterest']
    try:
        Fundamentals.loc['Tax Rate']=Statement.loc['annualTaxProvision']/(Statement.loc['annualNetIncome']+ Statement.loc['annualTaxProvision'])
    except: 
        Fundamentals.loc['Tax Rate']= Statement.loc['annualTaxRateForCalcs'] 

    Fundamentals.loc['After Tax Cost of Debt']=(1-Fundamentals.loc['Tax Rate'])*Fundamentals.loc['Before Tax Cost of Debt']

    try:
        if CompanyVariables.loc['Beta (5Y Monthly)']=='N/A':
            Beta = 1
        else:
            Beta = CompanyVariables.loc['Beta (5Y Monthly)']

    except:
        Beta = 1

    RiskFreeReturnTreasuryUSA10YearsInterest=0.0064
    HistoricalSP500Return=0.08 #TO BE CORRECTED with the index tendency for the equity risk premium

    Fundamentals.loc['ERP Equity Risk Premium'] = Beta*(HistoricalSP500Return-RiskFreeReturnTreasuryUSA10YearsInterest) # Equity Risk Premium(ERP) - Excess return that investing in the stock market provides over a risk-free rate --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return)
    Fundamentals.loc['Cost of Equity CAPM Formula'] = RiskFreeReturnTreasuryUSA10YearsInterest + Beta*(HistoricalSP500Return-RiskFreeReturnTreasuryUSA10YearsInterest) # Cost of equity (CAPM Formula) --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return)
    Fundamentals.loc['Weighted Average Maturity']=1+(1-Fundamentals.loc['Debt Quality Ratio'])*10
    Fundamentals.loc['Market Value of Debt']=AnnualInterestExpense*((1-pow(1/(1+Fundamentals.loc['After Tax Cost of Debt']),Fundamentals.loc['Weighted Average Maturity'])))+AnnualNetDebt/(pow((1+Fundamentals.loc['After Tax Cost of Debt']),Fundamentals.loc['Weighted Average Maturity']))
    Fundamentals.loc['Market Value of Equity']=price*Statement.loc['annualOrdinarySharesNumber'].iloc[0]
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
    DCFTargetPrice=DCFResidualValue/Statement.loc['annualOrdinarySharesNumber'].iloc[0]
    # Variables to be stored in the database


    FundamentalmentalAnalysisDataBase=pd.Series({
        'Ticker': stock_name,
        'CompanyName': company_name,
        'CurrentPrice': price,
        'Sector':sector,
        'Currency':currency,
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
        'Beta':Beta,
        'LiquidityRatio':Fundamentals.loc['Cash/ Current Assets'][Fundamentals.columns[0]],
        'CashperShare': Fundamentals.loc['Cash per stock'][Fundamentals.columns[0]],
        'DebtQualityRatio': Fundamentals.loc['Debt Quality Ratio'][Fundamentals.columns[0]],
        'LiabilitiestoEquityRatio':Fundamentals.loc['Debt to Equity Ratio'][Fundamentals.columns[0]],
        'NetDebttoEBITDA':Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]],
        'MeanNetDebttoEBITDA':Fundamentals.loc['Net Debt to EBITDA'].mean(axis=0),
        'InterestExpensetoEBIT':Fundamentals.loc['Interest Expense/ EBIT'][Fundamentals.columns[0]],
        'EntrepriseValueUSD':Fundamentals.loc['EV Enterprise Value USD'][Fundamentals.columns[0]],
        'DCFValuewithExitMultiple':DCFTargetPrice,
        'EBITDATendency':Fundamentals.loc['EBITDA tendency'][Fundamentals.columns[0]],
        'FreeCashFlowTendency':Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]],
        'OperatingCashFlowTendency':Fundamentals.loc['Operating Cash Flow tendency'][Fundamentals.columns[0]],
        'NetIncomeTendency':Fundamentals.loc['Net income tendency'][Fundamentals.columns[0]],
        'EquityTendency':Fundamentals.loc['Equity tendency'][Fundamentals.columns[0]],
        })

    FundamentalmentalAnalysisDataBase=FundamentalmentalAnalysisDataBase.to_frame().T
    #FundamentalmentalAnalysisDataBase=FundamentalmentalAnalysisDataBase.set_index(['Ticker'])

    try: 
        sqliteConnection = sqlite3.connect('../db/Fundamentals.db')
        cur = sqliteConnection.cursor()
        engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
        conn = engine.raw_connection()
        cursor = conn.cursor()
        #print("Database created and Successfully Connected to SQLite")
        try:
            if stock_name in FundamentalAnalysisOld['Ticker'].tolist():
                print(FundamentalAnalysisOld['Ticker'])
                TickerToUpdateIndex=FundamentalAnalysisOld['Ticker'].tolist().index(stock_name)
                FundamentalAnalysisOld.loc[TickerToUpdateIndex] = FundamentalmentalAnalysisDataBase.loc[0]
                FundamentalAnalysisOld.to_sql("FundamentalAnalysis",conn, if_exists='replace', index=False)
            else:
                FundamentalmentalAnalysisDataBase.to_sql("FundamentalAnalysis",conn, if_exists='append', index=False)
        except:
            FundamentalmentalAnalysisDataBase.to_sql("FundamentalAnalysis",conn, if_exists='append', index=False)
        
        
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


if __name__ == '__main__':

    """ EXAMPLE: 
    companyName = 'Econocom'
    stockName = 'ECONB.BR'
    companySector = 'IT Consulting'
    priceToUse = 3.6
    meanPricePerYear = [2, 2.5, 3, 7]  # [2020, 2019, 2018, 2017]
    """

    dbName = 'Fundamentals.db'
    companyName = 'Viscofan'
    stockName = 'VIS.MC'
    companySector = 'Plastic'
    currency = 'EUR'
    currentPrice = 54.7
    meanPricePerYear = [55, 45, 50, 50]  # [2020, 2019, 2018, 2017]

    run_fundamental_analysis(
        db_name=dbName,
        company_name=companyName,
        stock_name=stockName,
        sector=companySector,
        price=currentPrice,
        mean_price_per_year=meanPricePerYear,
        currency=currency)

    hola, adios= get_company_prices(
        stock_name=stockName,
         db_name=dbName,)
