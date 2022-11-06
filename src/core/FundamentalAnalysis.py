import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3
import datetime

def fundamental_analysis (ticker_name, expected_growth):
    def get_select_query_string(table, ticker):
        """
        Generate query string (SELECT)
        :param table: [string] name of the table
        :param stock: [string] stock code of the company
        :return: [string] SQL statement
        """
        query_str = "SELECT * FROM " + table + " WHERE Ticker='" + ticker + "';"
        return query_str

    def calculate_tendency(kpi, kpi_tendency, x_axis_matrix):
        slope, c = np.linalg.lstsq(x_axis_matrix, Statement.loc[kpi][::-1], rcond=-1)[0]
        try:
            if Statement.loc[kpi].values[-1] > 0:
                Fundamentals.loc[kpi_tendency] = slope / Statement.loc[kpi].values[-1]
            else:
                Fundamentals.loc[kpi_tendency] = slope / Statement.loc[kpi].mean()
        except:
            Fundamentals.loc[kpi_tendency] = 0

    def df_to_exisiting_sql_db(df_old, df_to_db, table):
        try:
            if ticker_name in df_old['Ticker'].tolist():
                print(df_old['Ticker'])
                TickerToUpdateIndex = df_old['Ticker'].tolist().index(ticker_name)
                df_old.loc[TickerToUpdateIndex] = df_to_db.loc[0]
                df_old.to_sql(table, conn, if_exists='replace', index=False)
            else:
                df_to_db.to_sql(table, conn, if_exists='append', index=False)
        except:
            print('Could not connect to db')

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
        engine = create_engine('sqlite:////app/stockcomparator/src/db/Fundamentals.db')

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    ## company variables: country, beta, sector ...

    company_variables_query = get_select_query_string(table='Companies', ticker=ticker_name)
    CompanyVariables = pd.read_sql_query(company_variables_query, engine)
    CompanyVariables = CompanyVariables.drop(["Ticker"], axis=1)
    CompanyVariables = CompanyVariables.squeeze()
    CompanyVariables = CompanyVariables.apply(pd.to_numeric, errors='ignore')

    # currency
    currency_to_usd_dict = {
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
        'TWD': 0.033,
        'INR': 0.012
    }

    currency_to_usd_conversion_factor = currency_to_usd_dict[CompanyVariables['ReportCurrency']]
    stock_currency_to_usd_conversion_factor = currency_to_usd_dict[CompanyVariables['StockCurrency']]
    report_currency_to_usd_conversion_factor = currency_to_usd_dict[CompanyVariables['ReportCurrency']]

    price_conversion_factor = stock_currency_to_usd_conversion_factor / report_currency_to_usd_conversion_factor

    ## current price
    current_prices_query = get_select_query_string(table='CurrentPrice', ticker=ticker_name)
    current_price = pd.read_sql_query(current_prices_query, engine)
    price = current_price['Price'][0] * price_conversion_factor

    ## historical price
    company_prices_query = get_select_query_string(table='HistoricalPrices', ticker=ticker_name)
    companyPrices = pd.read_sql_query(company_prices_query, engine)
    companyPrices = companyPrices.T
    companyPrices.columns = companyPrices.loc['Year']
    companyPrices = companyPrices.drop(['Ticker', 'id', 'Year'])
    companyPrices.loc['MeanPrice'] = companyPrices.loc['MeanPrice'] * price_conversion_factor
    years_in_historical_price = companyPrices.columns.tolist()

    ## sector industry multiples analysis
    industry_query = "SELECT EVEBITDAMultiple, cyclical FROM Industry WHERE Industry='" + CompanyVariables[
        'Industry'] + "';"
    industry_multiple = pd.read_sql_query(industry_query, engine)
    cyclical = bool(industry_multiple['cyclical'][0])

    ## ordenary_shares_alternative
    shares_alternative_query = get_select_query_string(table='OrdinarySharesAlternative', ticker=ticker_name)
    shares_alternative_df = pd.read_sql_query(shares_alternative_query, engine)
    try:
        ordinary_shares_alternative = bool(shares_alternative_df['Alternative'][0])
    except:
        ordinary_shares_alternative = False

    ## previous existing fundamental analyis
    try:
        FundamentalAnalysisOld = pd.read_sql_table('FundamentalAnalysis', engine)
        simpleAnalysisOld = pd.read_sql_table('SimpleAnalysis', engine)
        expectedGrowthOld = pd.read_sql_table('ExpectedGrowth', engine)
        # FundamentalAnalysisOld = pd.read_sql_query('SELECT * FROM FundamentalAnalysis', conn)
    except:
        print('Empty FundamentalAnalysis table')

    ## annual report
    annual_reports_query = get_select_query_string(table='AnnualReports', ticker=ticker_name)
    tabledfquery = pd.read_sql_query(annual_reports_query, engine)
    tabledfqueryordered = tabledfquery.sort_values(by="Year")
    tabledfqueryordered = tabledfqueryordered.drop(["Ticker", "id"], axis=1)
    tabledfqueryordered = tabledfqueryordered.set_index("kpi")
    result = pd.pivot_table(tabledfqueryordered, values='Value', index=['kpi'], columns=['Year'])
    Statement = result.iloc[:, ::-1]  # reverse columns order
    statement_years = Statement.columns.tolist()

    # adapt years between historical prices and annual report to match dataframes
    if len(years_in_historical_price) < len(statement_years):
        Statement = Statement.loc[:, Statement.columns.isin(years_in_historical_price)]

    elif len(statement_years) < len(years_in_historical_price):
        companyPrices = companyPrices.loc[:, companyPrices.columns.isin(statement_years)]

    companyPrices = companyPrices.loc[:, ~companyPrices.columns.duplicated()]
    mean_price_per_year = (companyPrices.loc['MeanPrice'][::-1]).tolist()

    #####  FUNDAMENTAL ANALYSIS ####

    FundamentalsIndex = ['EPS',
                         'FFO Funds From Operations per share',
                         'Debt-to-Equity Ratio',
                         'Quick ratio / acid test ratio',
                         'Current ratio',
                         'Book Value',
                         'Price to Book Value',
                         'Price to Book Value at Year Reference Price',
                         'Cash/ Total Assets',
                         'Cash per stock',
                         'Debt Quality Ratio',
                         'Liabilities to Assets',
                         'Liabilities to Equity',
                         'ROCE Return On Capital Employed',
                         'ROA Return On Assets',
                         'ROE Return On Equity',
                         'ROIC Return On Invested Capital',
                         'PER',
                         'PFFO',  # Price / Funds From Operations per share --> For REIT Valuations
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
                         'Net Debt to Operating Cash Flow',
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
        Statement.loc['annualOrdinarySharesNumber'] = CompanyVariables.loc['SharesOutstanding']

    try:
        if CompanyVariables['Sector'] == 'Financial Services':
            AnnualNetDebt = 0 * Statement.loc['annualTotalDebt']
        else:
            AnnualNetDebt = Statement.loc['annualTotalDebt'] - Statement.loc['annualCashAndCashEquivalents']
    except:
        try:
            AnnualLongTermDebt = Statement.loc['annualLongTermDebt']
            AnnualCurrentTermDebt = Statement.loc['annualCurrentDebt']
            AnnualNetDebt = AnnualCurrentTermDebt + AnnualLongTermDebt - Statement.loc['annualCashAndCashEquivalents']
        except:
            try:
                AnnualNetDebt = Statement.loc['annualNetDebt']
            except:
                AnnualCurrentTermDebt = Statement.loc['annualCurrentLiabilities']
                AnnualLongTermDebt = Statement.loc['annualCurrentLiabilities']
                AnnualNetDebt = AnnualCurrentTermDebt + AnnualLongTermDebt - Statement.loc[
                    'annualCashAndCashEquivalents']

    try:
        AnnualEquity = Statement.loc['annualStockholdersEquity']
    except:
        AnnualEquity = Statement.loc['annualCommonStockEquity']

    Statement.loc['annualStockholdersEquity'] = AnnualEquity

    # Fundamentals.loc['Debt to Equity Ratio']=(Statement.loc['annualCurrentLiabilities']+Statement.loc['annualTotalNonCurrentLiabilitiesNetMinorityInterest'])/AnnualEquity

    Fundamentals.loc['Book Value'] = AnnualEquity / Statement.loc['annualOrdinarySharesNumber']

    Fundamentals.loc['Price to Book Value'] = price / Fundamentals.loc['Book Value']
    Fundamentals.loc['Price to Book Value at Year Reference Price'] = mean_price_per_year / Fundamentals.loc[
        'Book Value']

    Fundamentals.loc['Cash/ Total Assets'] = Statement.loc['annualCashAndCashEquivalents'] / Statement.loc[
        'annualTotalAssets']

    Fundamentals.loc['Cash per stock'] = Statement.loc['annualCashAndCashEquivalents'] / Statement.loc[
        'annualOrdinarySharesNumber']
    try:
        AnnualInterestExpense = Statement.loc['annualInterestExpense']
    except:
        AnnualInterestExpense = Statement.loc['annualEBIT'] - Statement.loc['annualNetIncome'] - Statement.loc[
            'annualTaxProvision']

    try:

        Fundamentals.loc['Debt Quality Ratio'] = Statement.loc['annualCurrentLiabilities'] / (
                Statement.loc['annualCurrentLiabilities'] + Statement.loc[
            'annualTotalNonCurrentLiabilitiesNetMinorityInterest'])
        Fundamentals.loc['DSCR Asset Coverage Ratio'] = (Statement.loc['annualTotalAssets'] - Statement.loc[
            'annualCurrentLiabilities']) / Statement.loc['annualTotalLiabilitiesNetMinorityInterest']
        Fundamentals.loc['Current ratio'] = Statement.loc['annualCurrentAssets'] / Statement.loc[
            'annualCurrentLiabilities']
        Fundamentals.loc['Liabilities to Assets'] = Statement.loc['annualTotalLiabilitiesNetMinorityInterest'] / \
                                                    Statement.loc['annualTotalAssets']
        Fundamentals.loc['Liabilities to Equity'] = Statement.loc[
                                                        'annualTotalLiabilitiesNetMinorityInterest'] / AnnualEquity

        try:
            Fundamentals.loc['Quick ratio / acid test ratio'] = (Statement.loc['annualAccountsReceivable'] +
                                                                 Statement.loc[
                                                                     'annualCashAndCashEquivalents']) / Statement.loc[
                                                                    'annualCurrentLiabilities']
        except:
            Fundamentals.loc['Quick ratio / acid test ratio'] = (Statement.loc['annualCashAndCashEquivalents']) / \
                                                                Statement.loc['annualCurrentLiabilities']
    except:
        pass
    # Income Ratios

    Fundamentals.loc['EPS'] = Statement.loc['annualNetIncome'] / Statement.loc['annualOrdinarySharesNumber']

    Fundamentals.loc['ROA Return On Assets'] = Statement.loc['annualNetIncome'] / (Statement.loc['annualTotalAssets'])
    Fundamentals.loc['ROE Return On Equity'] = Statement.loc['annualNetIncome'] / AnnualEquity
    Fundamentals.loc['ROIC Return On Invested Capital'] = Statement.loc['annualNetIncome'] / (
                AnnualEquity + AnnualNetDebt)
    Fundamentals.loc['Net Income Margin'] = Statement.loc['annualNetIncome'] / Statement.loc['annualOperatingRevenue']
    try:
        Fundamentals.loc['ROCE Return On Capital Employed'] = Statement.loc['annualEBIT'] / (
                Statement.loc['annualTotalAssets'] - Statement.loc['annualCurrentLiabilities'])
        Fundamentals.loc['EBITDA Margin'] = Statement.loc['annualNormalizedEBITDA'] / Statement.loc[
            'annualOperatingRevenue']
    except:
        pass

    Fundamentals.loc['PER'] = price / Fundamentals.loc['EPS']
    Fundamentals.loc['PER at Year Reference Price'] = mean_price_per_year / Fundamentals.loc['EPS']

    for i in range(len(Fundamentals.loc['PER'])):
        if Fundamentals.loc['PER'][Fundamentals.columns[i]] < 0:
            Fundamentals.loc['PER'][Fundamentals.columns[i]] = 100
            Fundamentals.loc['PER at Year Reference Price'][Fundamentals.columns[i]] = 100

    try:
        Fundamentals.loc['FFO Funds From Operations per share'] = (Statement.loc['annualNetIncome'] \
                                                                   + Statement.loc['annualDepreciationAndAmortization'] \
                                                                   + Statement.loc[
                                                                       'annualEarningsLossesFromEquityInvestments']) / \
                                                                  Statement.loc['annualOrdinarySharesNumber']
        Fundamentals.loc['PFFO'] = price / Fundamentals.loc['FFO Funds From Operations per share']
        Fundamentals.loc['PFFO at Year Reference Price'] = mean_price_per_year / Fundamentals.loc[
            'FFO Funds From Operations per share']
    except:
        pass

    Fundamentals.loc['FCFS Free Cash Flow per Stock'] = Statement.loc['annualFreeCashFlow'] / Statement.loc[
        'annualOrdinarySharesNumber']

    # Fundamentals.loc['PayOut DPS/EPS']=CompanyVariables.loc['Trailing Annual Dividend Rate']/Fundamentals.loc['EPS']

    Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'] = price / Fundamentals.loc['FCFS Free Cash Flow per Stock']
    Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'] = mean_price_per_year / \
                                                                                       Fundamentals.loc[
                                                                                           'FCFS Free Cash Flow per Stock']

    for i in range(len(Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'])):
        if Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][Fundamentals.columns[i]] < 0:
            Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][Fundamentals.columns[i]] = 100

    for i in range(len(Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'])):
        if Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'][
            Fundamentals.columns[i]] < 0:
            Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock at Year Reference Price'][
                Fundamentals.columns[i]] = 100

    Fundamentals.loc['EV Enterprise Value'] = price * Statement.loc['annualOrdinarySharesNumber'] + AnnualNetDebt
    Fundamentals.loc['EV Enterprise Value USD'] = Fundamentals.loc[
                                                      'EV Enterprise Value'] * currency_to_usd_conversion_factor

    try:
        Fundamentals.loc['EV Enterprise Value / EBITDA'] = Fundamentals.loc['EV Enterprise Value'] / Statement.loc[
            'annualNormalizedEBITDA']
        Fundamentals.loc['EV Enterprise Value / EBIT'] = Fundamentals.loc['EV Enterprise Value'] / Statement.loc[
            'annualEBIT']

        for i in range(len(Fundamentals.loc['EV Enterprise Value'])):
            Fundamentals.loc['EV Enterprise Value at Year Reference Price'][Fundamentals.columns[i]] = \
            mean_price_per_year[
                i] * \
            Statement.loc[
                'annualOrdinarySharesNumber'].iloc[
                i] + \
            AnnualNetDebt.iloc[i]

        Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'] = Fundamentals.loc[
                                                                                       'EV Enterprise Value at Year Reference Price'] / \
                                                                                   Statement.loc[
                                                                                       'annualNormalizedEBITDA']
        Fundamentals.loc['EV Enterprise Value / EBIT at Year Reference Price'] = Fundamentals.loc[
                                                                                     'EV Enterprise Value at Year Reference Price'] / \
                                                                                 Statement.loc['annualEBIT']

        Fundamentals.loc['P/CF Price/ Operating Cash Flow Rate'] = price / Fundamentals.loc[
            'PFCF Price/ Free Cash Flow per Stock']
        Fundamentals.loc['Interest Expense/ EBIT'] = AnnualInterestExpense / Statement.loc['annualEBIT']
        Fundamentals.loc['Net Debt to EBITDA'] = AnnualNetDebt / Statement.loc['annualNormalizedEBITDA']
        Fundamentals.loc['Net Debt to Operating Cash Flow'] = AnnualNetDebt / Statement.loc['annualOperatingCashFlow']

    except:
        pass

    ## TENDENCY ##
    # enum years [0,n] to generate x axis for tendency
    x = []
    for i in range(0, len(Statement.columns)):
        x.append(i)

    x_axis_matrix = np.vstack([x, np.ones(len(x))]).T

    tendency_dict = {
        'Net income tendency': 'annualNetIncome',
        'Free Cash Flow tendency': 'annualFreeCashFlow',
        'Operating Revenue tendency': 'annualOperatingRevenue',
        'Equity tendency': 'annualStockholdersEquity',
        'Operating Cash Flow tendency': 'annualOperatingCashFlow',
        'EBITDA tendency': 'annualNormalizedEBITDA'
    }

    if CompanyVariables['Sector'] == 'Financial Services': tendency_dict.popitem()

    for key in tendency_dict:
        calculate_tendency(tendency_dict[key], key, x_axis_matrix)

    ## Discounted Cash Flows

    RiskFreeReturnTreasuryUSA10YearsInterest = 0.05  # 5% US 10 years bond yield
    HistoricalSP500Return = 0.08
    DCFYears = 5

    Fundamentals.loc['Before Tax Cost of Debt'] = AnnualInterestExpense / AnnualNetDebt

    try:
        Fundamentals.loc['Tax Rate'] = Statement.loc['annualTaxRateForCalcs']
    except:
        Fundamentals.loc['Tax Rate'] = Statement.loc['annualTaxProvision'] / (
                Statement.loc['annualNetIncome'] + Statement.loc['annualTaxProvision'])

    for i in range(len(Fundamentals.loc['Tax Rate']) - 1):
        if Fundamentals.loc['Tax Rate'][Fundamentals.columns[i]] < 0 or Fundamentals.loc['Tax Rate'][
            Fundamentals.columns[i]] > 1:
            Fundamentals.loc['Tax Rate'][Fundamentals.columns[i]] = 0.25

    Fundamentals.loc['After Tax Cost of Debt'] = (1 - Fundamentals.loc['Tax Rate']) * Fundamentals.loc[
        'Before Tax Cost of Debt']
    # Rates adjustements to gouvernment interest rates
    for i in range(len(Fundamentals.loc['After Tax Cost of Debt']) - 1):
        if Fundamentals.loc['After Tax Cost of Debt'][
            Fundamentals.columns[i]] < RiskFreeReturnTreasuryUSA10YearsInterest:
            Fundamentals.loc['After Tax Cost of Debt'][
                Fundamentals.columns[i]] = RiskFreeReturnTreasuryUSA10YearsInterest

    try:
        Beta = CompanyVariables.loc['Beta']
    except:
        Beta = 1

    try:
        dividend_yield = float(CompanyVariables.loc['DividendYield'])
    except:
        dividend_yield = 0

    Fundamentals.loc['ERP Equity Risk Premium'] = Beta * (
            HistoricalSP500Return - RiskFreeReturnTreasuryUSA10YearsInterest)  # Equity Risk Premium(ERP) - Excess return that investing in the stock market provides over a risk-free rate --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return)
    Fundamentals.loc['Cost of Equity CAPM Formula'] = RiskFreeReturnTreasuryUSA10YearsInterest + Beta * (
            HistoricalSP500Return - RiskFreeReturnTreasuryUSA10YearsInterest)  # Cost of equity (CAPM Formula) --> Free Risk Rate + Beta * (Market Rate of Return - Risk Free Rate of Return)
    Fundamentals.loc['Weighted Average Maturity'] = 1 + (1 - Fundamentals.loc['Debt Quality Ratio']) * 10
    Fundamentals.loc['Market Value of Debt'] = AnnualInterestExpense * ((
            1 - pow(1 / (1 + Fundamentals.loc['After Tax Cost of Debt']),
                    Fundamentals.loc['Weighted Average Maturity']))) + AnnualNetDebt / (
                                                   pow((1 + Fundamentals.loc['After Tax Cost of Debt']),
                                                       Fundamentals.loc['Weighted Average Maturity']))
    Fundamentals.loc['Market Value of Equity'] = price * Statement.loc['annualOrdinarySharesNumber'].iloc[0]
    WeightOfEquity = Fundamentals.loc['Market Value of Equity'] / (
            Fundamentals.loc['Market Value of Equity'] + Fundamentals.loc['Market Value of Debt'])
    WeightOfDebt = Fundamentals.loc['Market Value of Debt'] / (
            Fundamentals.loc['Market Value of Equity'] + Fundamentals.loc['Market Value of Debt'])

    if CompanyVariables['Sector'] == 'Financial Services':
        Fundamentals.loc['WACC Weighed Average Cost of Capital'] = Fundamentals.loc['Cost of Equity CAPM Formula']
    else:
        Fundamentals.loc['WACC Weighed Average Cost of Capital'] = WeightOfEquity * Fundamentals.loc[
            'Cost of Equity CAPM Formula'] + WeightOfDebt * Fundamentals.loc['After Tax Cost of Debt']

    WACC = Fundamentals.loc['WACC Weighed Average Cost of Capital'][Fundamentals.columns[0]]

    DCFFuture = []
    # DCF initial value and tendency

    try:
        expected_growth = float(expected_growth) * 0.01
        if isinstance(expected_growth, float):
            expectedGrowthDataBase = pd.Series({
                'Ticker': ticker_name,
                'ExpectedGrowth': expected_growth * 100
            })
            expectedGrowthDataBase = expectedGrowthDataBase.to_frame().T
            df_to_exisiting_sql_db(expectedGrowthOld, expectedGrowthDataBase, 'ExpectedGrowth')
    except:
        pass

    if CompanyVariables['Sector'] == 'Financial Services':  # banking, insurance ...
        DCFFuture.append(Statement.loc['annualNetIncome'].mean() * 0.5)
        if isinstance(expected_growth, float):
            tendency = expected_growth
        else:
            tendency = np.minimum(Fundamentals.loc['Equity tendency'].iloc[0], 0.4)
    elif cyclical:  # oil and gas, mining ...
        DCFFuture.append(Statement.loc['annualFreeCashFlow'].mean())

        if isinstance(expected_growth, float):
            tendency = expected_growth
        else:
            tendency = np.minimum(Fundamentals.loc['Equity tendency'].iloc[0], 0.3)
    else:
        DCFFuture.append(Statement.loc['annualFreeCashFlow'].iloc[0])
        if isinstance(expected_growth, float):
            tendency = expected_growth
        else:
            tendency = np.minimum(Fundamentals.loc['EBITDA tendency'].iloc[0], 0.5)

    for i in range(DCFYears):
        if DCFFuture[0] > 0 and i > 0:
            DCFFuture.append(DCFFuture[i - 1] * (1 + tendency))
            print(DCFFuture[i])
        elif i > 0:
            DCFFuture.append(DCFFuture[i - 1] * (1 - tendency))

    DCFFuture = np.array(DCFFuture)
    DCFPresent = DCFFuture / ((1 + WACC) ** DCFYears)

    if CompanyVariables['Sector'] == 'Financial Services':
        if Fundamentals.loc['Price to Book Value at Year Reference Price'].mean(axis=0) < 0.6:
            exit_multiple = 0.7
            DCFExitValue = exit_multiple * (
                Fundamentals.loc['Price to Book Value at Year Reference Price'].mean(axis=0)) * \
                           AnnualEquity.iloc[0]
        else:
            exit_multiple = 0.7
            DCFExitValue = exit_multiple * 0.6 * AnnualEquity.iloc[0]

    else:
        if cyclical:
            exit_multiple = Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0)
            DCFExitValue = exit_multiple * Statement.loc['annualNormalizedEBITDA'].mean(axis=0)

        elif Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0) < 7.5:
            exit_multiple = Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0)
            DCFExitValue = exit_multiple * (Statement.loc['annualNormalizedEBITDA'][Fundamentals.columns[0]])

        elif (Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0) > 9 and
              Fundamentals.loc['ROA Return On Assets'][Fundamentals.columns[0]] > 0.15 and
              Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]] < 1):
            # premium for highly profitable companies: High ROA > 15% AND Low debt (Net debt to Ebitda< 1)
            exit_multiple = 9
            DCFExitValue = exit_multiple * (Statement.loc['annualNormalizedEBITDA'][Fundamentals.columns[0]])
        else:
            exit_multiple = 7.5
            DCFExitValue = exit_multiple * (Statement.loc['annualNormalizedEBITDA'][Fundamentals.columns[0]])

    DCFTotalFirmValue = np.sum(DCFPresent) + DCFExitValue - AnnualNetDebt.iloc[0]  # Risk of COMPLEX Number
    DCFTargetPrice = DCFTotalFirmValue / Statement.loc['annualOrdinarySharesNumber'].iloc[0]

    # Multiple valuation weights

    if CompanyVariables['PercentInsidersHold'] > 0.3:
        insiders_weight = 1.03
    else:
        insiders_weight = 1

    if (CompanyVariables['Country'] == 'China' or
            CompanyVariables['Country'] == 'Hong Kong' or
            CompanyVariables['Country'] == 'Rusia'):
        country_transparency_weight = 0.95
    else:
        country_transparency_weight = 1

    if (any(cashflow < 0 for cashflow in Statement.loc['annualFreeCashFlow']) == False and
            Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]] > 0.07):
        # constant positive cash flows  and tendency that beats inflation
        cash_flow_stability_weight = 1.03
    elif (any(cashflow < 0 for cashflow in Statement.loc['annualFreeCashFlow']) == True and
          (np.std(Statement.loc['annualFreeCashFlow']) / Statement.loc['annualFreeCashFlow'][
              Statement.columns[0]]) > 0.5):
        cash_flow_stability_weight = 0.95
    else:
        cash_flow_stability_weight = 1

    if Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]] > 3:
        net_debt_to_ebitda_weight = 0.92
    elif Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]] > 2:
        net_debt_to_ebitda_weight = 0.97
    else:
        net_debt_to_ebitda_weight = 1

    if Fundamentals.loc['Interest Expense/ EBIT'][Fundamentals.columns[0]] > 0.7:
        debt_coverage_weight = 0.9
    else:
        debt_coverage_weight = 1

    if Fundamentals.loc['Price to Book Value'][Fundamentals.columns[0]] < 0.5:
        price_to_book_weight = 1.03
    else:
        price_to_book_weight = 1

    if Fundamentals.loc['EV Enterprise Value USD'][Fundamentals.columns[0]] < 1e9:
        enterprise_size_weight = 0.97
    else:
        enterprise_size_weight = 1

    target_price = DCFTargetPrice * cash_flow_stability_weight * net_debt_to_ebitda_weight * debt_coverage_weight * price_to_book_weight * enterprise_size_weight

    # SCORES

    # Debt score [0-1] #TODO make dependent on sector
    debt_score = \
        0.34 * (3 - np.minimum(3, Fundamentals.loc['Net Debt to EBITDA'].iloc[0])) / 3 + \
        0.33 * (6 - np.minimum(6, Fundamentals.loc['Net Debt to Operating Cash Flow'].iloc[0])) / 6 + \
        0.33 * (0.7 - np.minimum(0.7, Fundamentals.loc['Interest Expense/ EBIT'].iloc[0])) / 0.7

    # Growth score [0-1] -- 25% optimal growth
    growth_score = ( \
                               0.2 * np.maximum(-0.25, np.minimum(0.25, Fundamentals.loc['EBITDA tendency'].iloc[0])) + \
                               0.15 * np.maximum(-0.25,
                                                 np.minimum(0.25,
                                                            Fundamentals.loc['Free Cash Flow tendency'].iloc[0])) + \
                               0.15 * np.maximum(-0.25, np.minimum(0.25,
                                                                   Fundamentals.loc[
                                                                       'Operating Cash Flow tendency'].iloc[
                                                                       0])) + \
                               0.15 * np.maximum(-0.25,
                                                 np.minimum(0.25, Fundamentals.loc['Net income tendency'].iloc[0])) + \
                               0.15 * np.maximum(-0.25, np.minimum(0.25, Fundamentals.loc['Equity tendency'].iloc[0])) \
                       ) / 0.25

    # Earnings multiple score #TODO make dependent on sector
    earnigns_score = \
        0.3 * (30 - np.maximum(0, np.minimum(25, Fundamentals.loc['PER'].iloc[0] - 5))) / 25 + \
        0.4 * (30 - np.maximum(0,
                               np.minimum(25,
                                          Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'].iloc[0] - 5))) / 25 + \
        0.4 * (15 - np.maximum(0, np.minimum(15, Fundamentals.loc['EV Enterprise Value / EBITDA'].iloc[0] - 3))) / 15

    # Value score
    value_score = \
        np.minimum(1, target_price / price - 1)

    # Profitability score #TODO make dependent on sector
    profitability_score = \
        0.2 * np.minimum(0.3, (Fundamentals.loc['ROE Return On Equity'].iloc[0])) / 0.3 + \
        0.1 * np.minimum(0.3, (Fundamentals.loc['ROCE Return On Capital Employed'].iloc[0])) / 0.3 + \
        0.2 * np.minimum(0.2, (Fundamentals.loc['ROA Return On Assets'].iloc[0])) / 0.2 + \
        0.1 * np.minimum(0.2, (Fundamentals.loc['ROIC Return On Invested Capital'].iloc[0])) / 0.2 + \
        0.2 * np.minimum(0.2, (Fundamentals.loc['Net Income Margin'].iloc[0])) / 0.3 + \
        0.2 * np.minimum(0.2, (Fundamentals.loc['EBITDA Margin'].iloc[0])) / 0.4

    # Variables to be stored in the database

    FundamentalmentalAnalysisDataBase = pd.Series({
        'Ticker': ticker_name,
        'CompanyName': CompanyVariables['CompanyName'],
        'CurrentPrice': price,
        'Country': CompanyVariables['Country'],
        'Sector': CompanyVariables['Industry'],
        'LastReportDate': CompanyVariables['BalanceSheetDate'],
        'StockCurrency': CompanyVariables['StockCurrency'],
        'ReportCurrency': CompanyVariables['ReportCurrency'],
        'CurrentPER': Fundamentals.loc['PER'][Fundamentals.columns[0]],
        'MeanPER': Fundamentals.loc['PER at Year Reference Price'].mean(axis=0),
        'CurrentPricetoBook': Fundamentals.loc['Price to Book Value'][Fundamentals.columns[0]],
        'MeanPricetoBook': Fundamentals.loc['Price to Book Value at Year Reference Price'].mean(axis=0),
        'CurrentEVEBITDA': Fundamentals.loc['EV Enterprise Value / EBITDA'][Fundamentals.columns[0]],
        'MeanEVEBITDA': Fundamentals.loc['EV Enterprise Value / EBITDA at Year Reference Price'].mean(axis=0),
        'CurrentEVEBIT': Fundamentals.loc['EV Enterprise Value / EBIT'][Fundamentals.columns[0]],
        'CurrentPricetoFreeCashFlowRate': Fundamentals.loc['PFCF Price/ Free Cash Flow per Stock'][
            Fundamentals.columns[0]],
        'MeanPricetoFreeCashFlowRate': Fundamentals.loc[
            'PFCF Price/ Free Cash Flow per Stock at Year Reference Price'].mean(axis=0),
        # this has to be updated with reference price
        'ROE': Fundamentals.loc['ROE Return On Equity'][Fundamentals.columns[0]],
        'ROCE': Fundamentals.loc['ROCE Return On Capital Employed'][Fundamentals.columns[0]],
        'ROA': Fundamentals.loc['ROA Return On Assets'][Fundamentals.columns[0]],
        'ROIC': Fundamentals.loc['ROIC Return On Invested Capital'][Fundamentals.columns[0]],
        'Beta': Beta,
        'WACC': WACC,
        'CashToTotalAssets': Fundamentals.loc['Cash/ Total Assets'][Fundamentals.columns[0]],
        'CashOverStockPrice': Fundamentals.loc['Cash per stock'][Fundamentals.columns[0]] / price,
        'DebtQualityRatio': Fundamentals.loc['Debt Quality Ratio'][Fundamentals.columns[0]],
        'LiabilitiestoEquityRatio': Fundamentals.loc['Liabilities to Equity'][Fundamentals.columns[0]],
        'NetDebttoEBITDA': Fundamentals.loc['Net Debt to EBITDA'][Fundamentals.columns[0]],
        'MeanNetDebttoEBITDA': Fundamentals.loc['Net Debt to EBITDA'].mean(axis=0),
        'InterestExpensetoEBIT': Fundamentals.loc['Interest Expense/ EBIT'][Fundamentals.columns[0]],
        'EntrepriseValueUSD': Fundamentals.loc['EV Enterprise Value USD'][Fundamentals.columns[0]],
        'DCFValuewithExitMultiplePotential': (target_price / price - 1),
        'EBITDATendency': Fundamentals.loc['EBITDA tendency'][Fundamentals.columns[0]],
        'FreeCashFlowTendency': Fundamentals.loc['Free Cash Flow tendency'][Fundamentals.columns[0]],
        'OperatingCashFlowTendency': Fundamentals.loc['Operating Cash Flow tendency'][Fundamentals.columns[0]],
        'NetIncomeTendency': Fundamentals.loc['Net income tendency'][Fundamentals.columns[0]],
        'EquityTendency': Fundamentals.loc['Equity tendency'][Fundamentals.columns[0]],
        'DividendYield': dividend_yield,
        'NetIncomeMargin': Fundamentals.loc['Net Income Margin'][Fundamentals.columns[0]],
        'EBITDAMargin': Fundamentals.loc['EBITDA Margin'][Fundamentals.columns[0]],
        'TargetPrice': target_price,
        'PFFO': Fundamentals.loc['PFFO'][Fundamentals.columns[0]],
        'MeanPFFO': Fundamentals.loc['PFFO at Year Reference Price'].mean(axis=0),
        'LastUpdate': datetime.datetime.now().strftime("%Y-%m-%d"),
        'FirstYearReport': str(Statement.columns[-1])
    })

    simpleAnalysisDataBase = pd.Series({
        'Ticker': ticker_name,
        'CompanyName': CompanyVariables['CompanyName'],
        'Sector': CompanyVariables['Industry'],
        'Potential': (target_price / price - 1),
        'TargetPrice': target_price,
        'EarningsScore': earnigns_score,
        'DebtQualityScore': debt_score,
        'GrowthScore': growth_score
    })

    FundamentalmentalAnalysisDataBase = FundamentalmentalAnalysisDataBase.to_frame().T
    simpleAnalysisDataBase = simpleAnalysisDataBase.to_frame().T

    ## save fundamental analysis into the database

    df_to_exisiting_sql_db(FundamentalAnalysisOld, FundamentalmentalAnalysisDataBase, 'FundamentalAnalysis')
    df_to_exisiting_sql_db(simpleAnalysisOld, simpleAnalysisDataBase, 'SimpleAnalysis')

    # try:
    #     if ticker_name in FundamentalAnalysisOld['Ticker'].tolist():
    #         print(FundamentalAnalysisOld['Ticker'])
    #         TickerToUpdateIndex = FundamentalAnalysisOld['Ticker'].tolist().index(ticker_name)
    #         FundamentalAnalysisOld.loc[TickerToUpdateIndex] = FundamentalmentalAnalysisDataBase.loc[0]
    #         FundamentalAnalysisOld.to_sql("FundamentalAnalysis", conn, if_exists='replace', index=False)
    #     else:
    #         FundamentalmentalAnalysisDataBase.to_sql("FundamentalAnalysis", conn, if_exists='append', index=False)
    # except:
    #     print('Could not connect to db')
    #
    # if ticker_name in simpleAnalysisOld['Ticker'].tolist():
    #     print(simpleAnalysisOld['Ticker'])
    #     TickerToUpdateIndex = simpleAnalysisOld['Ticker'].tolist().index(ticker_name)
    #     simpleAnalysisOld.loc[TickerToUpdateIndex] = simpleAnalysisDataBase.loc[0]
    #     simpleAnalysisOld.to_sql("SimpleAnalysis", conn, if_exists='replace', index=False)
    # else:
    #     simpleAnalysisDataBase.to_sql("SimpleAnalysis", conn, if_exists='append', index=False)

    record = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()

    print("The SQLite connection is closed")
    print(ticker_name, '-  TARGET PRICE : ', target_price)

    return target_price