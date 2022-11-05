# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:49:22 2022
@author: m.perez-chuecos
"""

from yahooquery import Ticker
import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import *

ticker_name = 'BKT.MC'


def df_to_database(ticker_name, df):
    df = df.dropna(axis=1, how='any', thresh=4)
    df = df.dropna(axis=0, how='any', thresh=len(df.columns))
    years = df.columns.to_list()
    index = pd.MultiIndex.from_product([[ticker_name], df.index, years], names=['Ticker', 'KPI', 'Year'])
    data = df.values.tolist()
    flat_list = []
    for sublist in data:
        for item in sublist:
            flat_list.append(item)

    df_db = pd.DataFrame(index=index, data=flat_list, columns=['Value'])

    for i in range(2, -1, -1):
        df_db.reset_index(level=i, inplace=True)
    return df_db


def get_years(df):
    dates = df.loc['asOfDate'].values.tolist()
    years = []
    report_dates = []
    for date in dates:
        years.append(date.year)
        report_dates.append(date.date().strftime("%Y-%m-%d"))
    return years, report_dates


tickers = Ticker(ticker_name)

summary_profile = tickers.summary_profile

# all_financial_data= tickers.all_financial_data('a')

# CASH FLOW

cash_flow = tickers.cash_flow('a', True)
cash_flow = cash_flow[cash_flow.periodType.ne('TTM')]
cash_flow = cash_flow.T
report_currency = cash_flow.loc['currencyCode'][1:2].values[0]
years, report_dates = get_years(cash_flow)

# years
# years[-1]='TTM'
yearsTTM = years + ['TTM']
yearsTTM = yearsTTM[::-1]
# years=years[::-1]

cash_flow.columns = years

cash_flow = cash_flow.iloc[:, ::1]
cash_flow_intermediate = cash_flow

filter_cash_flow = [
    'AmortizationCashFlow',
    'CapitalExpenditure',
    'CashDividendsPaid',
    'CashFlowFromContinuingFinancingActivities',
    'CashFlowFromContinuingInvestingActivities',
    'CashFlowFromContinuingOperatingActivities',
    'CommonStockDividendPaid',
    'CommonStockPayments',
    'DeferredIncomeTax',
    'DeferredTax',
    'Depreciation',
    'DepreciationAndAmortization',
    'FinancingCashFlow',
    'FreeCashFlow',
    'InvestingCashFlow',
    'IssuanceOfDebt',
    'NetCommonStockIssuance',
    'NetIncome',
    'NetIssuancePaymentsOfDebt',
    'OperatingCashFlow']

cash_flow = cash_flow[cash_flow.index.isin(filter_cash_flow)]
# cash_flow.drop(columns=cash_flow.columns[0], axis=1, inplace=True)

# BALANCE SHEET

balance_sheet = tickers.balance_sheet('a', True)
balance_sheet = balance_sheet[balance_sheet.periodType.ne('TTM')]
balance_sheet = balance_sheet.T
list = balance_sheet.loc['asOfDate'].values.tolist()

balance_years, balance_report_dates = get_years(balance_sheet)
balance_sheet.columns = balance_years
balance_sheet = balance_sheet.iloc[:, ::-1]

filter_balance_sheet = [
    'AccountsPayable',
    'AccountsReceivable',
    'AccumulatedDepreciation',
    'CashAndCashEquivalents',
    'CashCashEquivalentsAndShortTermInvestments',
    'CommonStockEquity',
    'CurrentAssets',
    'CurrentCapitalLeaseObligation',
    'CurrentDebt',
    'CurrentDebtAndCapitalLeaseObligation',
    'CurrentDeferredLiabilities',
    'CurrentDeferredRevenue',
    'CurrentLiabilities',
    'CurrentProvisions',
    'Goodwill',
    'IncomeTaxPayable',
    'Inventory',
    'InvestedCapital',
    'LoansReceivable',
    'LongTermCapitalLeaseObligation',
    'LongTermDebt',
    'LongTermDebtAndCapitalLeaseObligation',
    'MinorityInterest',
    'NetDebt',
    'NetPPE',
    'NetTangibleAssets',
    'NonCurrentAccountsReceivable',
    'OrdinarySharesNumber',
    'Payables',
    'PrepaidAssets',
    'Receivables',
    'RetainedEarnings',
    'StockholdersEquity',
    'TaxesReceivable',
    'TotalAssets',
    'TotalDebt',
    'TotalEquityGrossMinorityInterest',
    'TotalLiabilitiesNetMinorityInterest',
    'TotalNonCurrentAssets',
    'TotalNonCurrentLiabilitiesNetMinorityInterest',
    'TotalTaxPayable']

balance_sheet = balance_sheet[balance_sheet.index.isin(filter_balance_sheet)]

# INCOME STATEMENT
income_statement = tickers.income_statement('a', True)
income_statement = income_statement[income_statement.periodType.ne('TTM')]
income_statement = income_statement.T
list = income_statement.loc['asOfDate'].values.tolist()

income_years, income_report_dates = get_years(income_statement)
income_statement.columns = income_years
income_statement = income_statement.iloc[:, ::-1]

filter_income_statement = [
    'Amortization',
    'AmortizationOfIntangiblesIncomeStatement',
    'BasicAverageShares',
    'CostOfRevenue',
    'DepreciationAmortizationDepletionIncomeStatement',
    'DepreciationAndAmortizationInIncomeStatement',
    'DepreciationIncomeStatement',
    'DilutedAverageShares',
    'EBIT',
    'GainOnSaleOfPPE',
    'GainOnSaleOfSecurity',
    'InterestExpense',
    'InterestIncome',
    'NetIncome',
    'NetIncomeCommonStockholders',
    'NetIncomeContinuousOperations',
    'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NetInterestIncome',
    'NormalizedEBITDA',
    'NormalizedIncome',
    'OperatingExpense',
    'OperatingIncome',
    'OperatingRevenue',
    'PretaxIncome',
    'ReconciledCostOfRevenue',
    'SellingGeneralAndAdministration',
    'TaxProvision',
    'TaxRateForCalcs',
    'TotalExpenses',
    'TotalRevenue']

income_statement = income_statement[income_statement.index.isin(filter_income_statement)]

# statement to database
cash_flow_db = df_to_database(ticker_name, cash_flow)
cash_flow_db['KPI'] = 'annual' + cash_flow_db['KPI']

income_statement_db = df_to_database(ticker_name, income_statement)
income_statement_db['KPI'] = 'annual' + income_statement_db['KPI']

balance_sheet_db = df_to_database(ticker_name, balance_sheet)
balance_sheet_db['KPI'] = 'annual' + balance_sheet_db['KPI']

# Current Price
current_price = [tickers.price[ticker_name]['regularMarketPrice']]
current_price_db = pd.DataFrame({'Ticker': ticker_name, 'Price': current_price})

# Mean Price
prices = tickers.history(period='5y', interval='1d')
prices.reset_index(level=1, inplace=True)
prices['date'] = pd.to_datetime(prices['date'])  # IMP

year_mean_price = []
year_max_price = []
year_min_price = []

"""or year in years[1::]:    
    year_prices=prices[prices['date'].dt.year == year]
    year_mean_price.append(year_prices['open'].mean())
    year_max_price.append(year_prices['high'].max())
    year_min_price.append(year_prices['low'].min())"""

# report_dates=[]
# report_dates.pop() #remove ttm date
last_report_year = int(report_dates[0][0:4])  # report date
report_dates = report_dates[::-1]
backwards_years = 2
years_prices_db = []

for i in range(backwards_years):
    report_early_year = last_report_year - i - 1
    report_early_date = str(report_early_year) + report_dates[0][4::]
    report_dates.append(report_early_date)
report_dates = report_dates[::-1]  # revert order for the next for loop

for i in (range(len(report_dates) - 1)):
    year_prices = prices[(prices['date'] > report_dates[i]) & (prices['date'] < report_dates[i + 1])]
    year_mean_price.append(year_prices['open'].mean())
    year_max_price.append(year_prices['high'].max())
    year_min_price.append(year_prices['low'].min())
    years_prices_db.append(report_dates[i + 1][0:4])

prices_db = pd.DataFrame(
    {'Ticker': ticker_name, 'Year': years_prices_db, 'MeanPrice': year_mean_price, 'MaxPrice': year_max_price,
     'MinPrice': year_min_price})

try:
    dividend_yield = tickers.summary_detail[ticker_name]['dividendYield']
except:
    dividend_yield = 0

try:
    beta = tickers.key_stats[ticker_name]['beta']
except:
    beta = 1

# COMPANY VARIABLES

company_variables = {
    'Ticker': ticker_name,
    'CompanyName': tickers.quote_type[ticker_name]['shortName'],
    'StockCurrency': tickers.summary_detail[ticker_name]['currency'],
    'ReportCurrency': report_currency,
    'Country': tickers.summary_profile[ticker_name]['country'],
    'Industry': tickers.summary_profile[ticker_name]['industry'],
    'Sector': tickers.summary_profile[ticker_name]['sector'],
    'Beta': beta,
    'BalanceSheetDate': report_dates[-1],
    'LastYearReport': years[1],
    'DividendYield': dividend_yield,
    'PercentInsidersHold': tickers.key_stats[ticker_name]['heldPercentInsiders'],
    'PercentInstitutionsHold': tickers.key_stats[ticker_name]['heldPercentInstitutions'],
    'SharesOutstanding': tickers.key_stats[ticker_name]['sharesOutstanding']
}

company_variables = pd.Series(company_variables).to_frame().T

# # TO DATABASE
#
# try:
#     sqliteConnection = sqlite3.connect('../db/Fundamentals.db')
#     cur = sqliteConnection.cursor()
#     engine = create_engine('sqlite:///../db/Fundamentals.db', echo=False)
#     conn = engine.raw_connection()
#     cursor = conn.cursor()
#     # print("Database created and Successfully Connected to SQLite")
#
#     # Current prices
#     try:
#         CurrentPriceOld = pd.read_sql_table('CurrentPrice', engine)
#     except:
#         print('Empty CurrentPrice table')
#
#     try:
#         if ticker_name in CurrentPriceOld['Ticker'].tolist():
#             print(CurrentPriceOld['Ticker'])
#             TickerToUpdateIndex = CurrentPriceOld['Ticker'].tolist().index(ticker_name)
#             CurrentPriceOld.loc[TickerToUpdateIndex] = current_price_db.loc[0]
#             CurrentPriceOld.to_sql("CurrentPrice", conn, if_exists='replace', index=False)
#         else:
#             current_price_db.to_sql("CurrentPrice", conn, if_exists='append', index=False)
#     except:
#         current_price_db.to_sql("CurrentPrice", conn, if_exists='append', index=False)
#
#     # Company Historical Prices
#
#     for i in range(len(prices_db)):
#         try:
#             prices_db.iloc[i:i + 1].to_sql("HistoricalPrices", conn, index=False, if_exists='append')
#         except sqlite3.Error:
#             print('Data already in HistoricalPrices database')
#             print(sqlite3.Error)
#             pass  # or any other action
#
#     # Company Variables
#
#     try:
#         CompanyVariablesOld = pd.read_sql_table('Variables', engine)
#     except:
#         print('Empty Variables table')
#
#     try:
#         if ticker_name in CompanyVariablesOld['Ticker'].tolist():
#             print(CompanyVariablesOld['Ticker'])
#             TickerToUpdateIndex = CompanyVariablesOld['Ticker'].tolist().index(ticker_name)
#             CompanyVariablesOld.loc[TickerToUpdateIndex] = company_variables.loc[0]
#             CompanyVariablesOld.to_sql("Variables", conn, if_exists='replace', index=False)
#         else:
#             company_variables.to_sql("Variables", conn, if_exists='append', index=False)
#     except:
#         company_variables.to_sql("Variables", conn, if_exists='append', index=False)
#
#     # Balance Sheet
#     for i in range(len(balance_sheet_db)):
#         try:
#             balance_sheet_db.iloc[i:i + 1].to_sql("AnnualReports", conn, index=False, if_exists='append')
#         except sqlite3.Error:
#             print('Data already in Balance Sheet database')
#             print(sqlite3.Error)
#             pass  # or any other action
#
#     # Income Statement
#     for i in range(len(income_statement_db)):
#         try:
#             income_statement_db.iloc[i:i + 1].to_sql("AnnualReports", conn, index=False, if_exists='append')
#         except sqlite3.Error:
#             print('Data already in Income database')
#             print(sqlite3.Error)
#             pass  # or any other action
#
#     # Cash Flow
#     for i in range(len(cash_flow_db)):
#         try:
#             cash_flow_db.iloc[i:i + 1].to_sql("AnnualReports", conn, index=False, if_exists='append')
#         except sqlite3.Error:
#             print('Data already in Cash Flow database')
#             print(sqlite3.Error)
#             pass  # or any other action
#
#     record = cur.fetchall()
#     cur.close()
#
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")
#
# # Save (commit) the changes
# conn.commit()
#
# # Just be sure any changes have been committed or they will be lost.
# conn.close()









