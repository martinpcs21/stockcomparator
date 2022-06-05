
-- Table: Variables
DROP TABLE IF EXISTS Variables;

CREATE TABLE Variables (
    Ticker                  VARCHAR(255),
    CompanyName             VARCHAR(255),
    StockCurrency           VARCHAR(255),
    ReportCurrency          VARCHAR(255),
    Country                 VARCHAR(255),
    Industry                VARCHAR(255),
    Sector                  VARCHAR(255),
    Beta                    DOUBLE,
    BalanceSheetDate        VARCHAR(255),
    LastYearReport          INTEGER,
    DividendYield           DOUBLE,
    PercentInsidersHold     DOUBLE,
    PercentInstitutionsHold DOUBLE,
    SharesOutstanding       DOUBLE
);

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'UBER',
                          'Uber Technologies, Inc.',
                          'USD',
                          'USD',
                          'United States',
                          'Software�Application',
                          'Technology',
                          1.312725,
                          '2020-12-31',
                          2020,
                          0.0,
                          0.00441,
                          0.7403,
                          NULL
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'MSFT',
                          'Microsoft Corporation',
                          'USD',
                          'USD',
                          'United States',
                          'Software�Infrastructure',
                          'Technology',
                          0.862138,
                          '2021-06-30',
                          2021,
                          0.008,
                          0.00062,
                          0.71826,
                          NULL
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'MCD',
                          'McDonald''s Corporation',
                          'USD',
                          'USD',
                          'United States',
                          'Restaurants',
                          'Consumer Cyclical',
                          0.59706,
                          '2020-12-31',
                          2020,
                          0.0214,
                          0.00046,
                          0.69064003,
                          NULL
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'ATVI',
                          'Activision Blizzard, Inc',
                          'USD',
                          'USD',
                          'United States',
                          'Electronic Gaming & Multimedia',
                          'Communication Services',
                          0.697415,
                          '2020-12-31',
                          2020,
                          0.0057,
                          0.00727,
                          0.88164,
                          NULL
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'TEF.MC',
                          'TELEFONICA,S.A.',
                          'EUR',
                          'EUR',
                          'Spain',
                          'Telecom Services',
                          'Communication Services',
                          0.840085,
                          '2021-12-31',
                          2020,
                          0.0867,
                          0.09126,
                          0.19181,
                          5779049984.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'UL',
                          'Unilever PLC',
                          'USD',
                          'EUR',
                          'United Kingdom',
                          'Household & Personal Products',
                          'Consumer Defensive',
                          0.167658,
                          '2020-12-31',
                          2020,
                          0.041199997,
                          0.000010000001,
                          0.09834,
                          NULL
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'BABA',
                          'Alibaba Group Holding Limited',
                          'USD',
                          'CNY',
                          'China',
                          'Internet Retail',
                          'Consumer Cyclical',
                          0.881397,
                          '2021-03-31',
                          2020,
                          0.0,
                          0.00021,
                          0.18978001,
                          2687500032.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          '9988.HK',
                          'BABA-SW',
                          'HKD',
                          'CNY',
                          'China',
                          'Internet Retail',
                          'Consumer Cyclical',
                          0.881397,
                          '2021-03-31',
                          2020,
                          0.0,
                          0.30688998,
                          0.16529,
                          21500000256.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'EDF',
                          'Stone Harbor Emerging Markets I',
                          'USD',
                          'USD',
                          'United States',
                          'Asset Management',
                          'Financial Services',
                          1.0,
                          '2020-11-30',
                          2020,
                          0.1154,
                          0.00442,
                          0.1159,
                          16843900.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'EDF.PA',
                          'EDF',
                          'EUR',
                          'EUR',
                          'France',
                          'Utilities�Diversified',
                          'Utilities',
                          0.888588,
                          '2020-12-31',
                          2019,
                          0.0617,
                          0.82986,
                          0.039049998,
                          3237499904.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'GE',
                          'General Electric Company',
                          'USD',
                          'USD',
                          'United States',
                          'Specialty Industrial Machinery',
                          'Industrials',
                          1.035478,
                          '2020-12-31',
                          2019,
                          0.0033000002,
                          0.00242,
                          0.72029,
                          1098140032.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'BIDU',
                          'Baidu, Inc.',
                          'USD',
                          'CNY',
                          'China',
                          'Internet Content & Information',
                          'Communication Services',
                          1.016725,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.00361,
                          0.57787,
                          348059008.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'INTC',
                          'Intel Corporation',
                          'USD',
                          'USD',
                          'United States',
                          'Semiconductors',
                          'Technology',
                          0.535554,
                          '2021-12-31',
                          2020,
                          0.0301,
                          0.0007,
                          0.64913005,
                          4072000000.
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          '0788.HK',
                          'CHINA TOWER',
                          'HKD',
                          'CNY',
                          'China',
                          'Telecom Services',
                          'Communication Services',
                          0.111382,
                          '2020-12-31',
                          2019,
                          0.028299998,
                          0.0,
                          0.24531001,
                          46663901184.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          '2168.HK',
                          'KAISA PROSPER',
                          'HKD',
                          'CNY',
                          'China',
                          'DOUBLE Estate Services',
                          'DOUBLE Estate',
-                         0.097794,
                          '2020-12-31',
                          2019,
                          0.0757,
                          0.67179,
                          0.04046,
                          154110000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'ORP.PA',
                          'ORPEA',
                          'EUR',
                          'EUR',
                          'France',
                          'Medical Care Facilities',
                          'Healthcare',
                          0.803136,
                          '2020-12-31',
                          2019,
                          0.0163,
                          0.050780002,
                          0.53564,
                          64587500.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'KORI.PA',
                          'KORIAN',
                          'EUR',
                          'EUR',
                          'France',
                          'Medical Care Facilities',
                          'Healthcare',
                          0.9371,
                          '2021-12-31',
                          2020,
                          0.015,
                          0.31996,
                          0.27038,
                          103618000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'LNA.PA',
                          'LNA SANTE',
                          'EUR',
                          'EUR',
                          'France',
                          'Medical Care Facilities',
                          'Healthcare',
                          0.749053,
                          '2020-12-31',
                          2019,
                          0.0047,
                          0.42157,
                          0.14863,
                          9624550.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'ORA.PA',
                          'ORANGE',
                          'EUR',
                          'EUR',
                          'France',
                          'Telecom Services',
                          'Communication Services',
                          0.210021,
                          '2021-12-31',
                          2020,
                          0.064899996,
                          0.13397,
                          0.39042,
                          2657819904.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'MTY.TO',
                          'MTY FOOD GROUP INC',
                          'CAD',
                          'CAD',
                          'Canada',
                          'Restaurants',
                          'Consumer Cyclical',
                          2.071474,
                          '2021-11-30',
                          2020,
                          0.0155,
                          0.19436,
                          0.32878,
                          24669900.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'JD.L',
                          'JD SPORTS FASHION PLC ORD 0.05P',
                          'GBp',
                          'GBP',
                          'United Kingdom',
                          'Specialty Retail',
                          'Consumer Cyclical',
                          1.517036,
                          '2021-01-31',
                          2020,
                          0.0015,
                          0.52131003,
                          0.26132,
                          5158139904.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'AWRD.ST',
                          'Awardit AB',
                          'SEK',
                          'SEK',
                          'Sweden',
                          'Advertising Agencies',
                          'Communication Services',
                          1.204054,
                          '2020-12-31',
                          2019,
                          0.0072000003,
                          0.55974,
                          0.04606,
                          8335520.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'NWL.MI',
                          'NEWLAT FOOD',
                          'EUR',
                          'EUR',
                          'Italy',
                          'Packaged Foods',
                          'Consumer Defensive',
                          0.413756,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.61658,
                          0.16518,
                          41299500.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'GEO',
                          'Geo Group Inc (The) REIT',
                          'USD',
                          'USD',
                          'United States',
                          'REIT�Healthcare Facilities',
                          'DOUBLE Estate',
                          0.68996,
                          '2021-12-31',
                          2020,
                          0.0,
                          0.04188,
                          0.77585,
                          122518000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'DND.TO',
                          'DYE AND DURHAM LIMITED',
                          'CAD',
                          'CAD',
                          'Canada',
                          'Software�Infrastructure',
                          'Technology',
                          1.0,
                          '2021-06-30',
                          2020,
                          0.0028,
                          0.18621999,
                          0.71689004,
                          69140000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'BB.PA',
                          'BIC',
                          'EUR',
                          'EUR',
                          'France',
                          'Household & Personal Products',
                          'Consumer Defensive',
                          0.676041,
                          '2020-12-31',
                          2019,
                          0.0356,
                          0.46300998,
                          0.15515,
                          44580800.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'FB',
                          'Meta Platforms, Inc.',
                          'USD',
                          'USD',
                          'United States',
                          'Internet Content & Information',
                          'Communication Services',
                          1.28543,
                          '2021-12-31',
                          2020,
                          0.0,
                          0.00529,
                          0.79033,
                          2309080064.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'ICP1V.HE',
                          'Incap Corporation',
                          'EUR',
                          'EUR',
                          'Finland',
                          'Electronic Components',
                          'Technology',
                          1.855382,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.46078,
                          0.22506,
                          5849330.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'TIXT',
                          'TELUS International (Cda) Inc. ',
                          'USD',
                          'USD',
                          'Canada',
                          'Software�Infrastructure',
                          'Technology',
                          1.0,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.10094,
                          0.97533,
                          66000000.
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'CY4.MI',
                          'CY4GATE',
                          'EUR',
                          'EUR',
                          'Italy',
                          'Software�Infrastructure',
                          'Technology',
                          1.0,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.5529,
                          0.20201999,
                          15000000.
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'VOLO.ST',
                          'Volati AB',
                          'SEK',
                          'SEK',
                          'Sweden',
                          'Conglomerates',
                          'Industrials',
                          1.500803,
                          '2020-12-31',
                          2019,
                          0.0061000003,
                          0.78423,
                          0.19218999,
                          79406600.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'D6H.DE',
                          'DATAGROUP SE  INH. O.N.',
                          'EUR',
                          'EUR',
                          'Germany',
                          'Information Technology Services',
                          'Technology',
                          1.055704,
                          '2020-09-30',
                          2019,
                          0.0119,
                          0.582,
                          0.131,
                          8331000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'MRL.L',
                          'MARLOWE PLC ORD 50P',
                          'GBp',
                          'GBP',
                          'United Kingdom',
                          'Security & Protection Services',
                          'Industrials',
                          1.083556,
                          '2021-03-31',
                          2020,
                          0.0,
                          0.22850999,
                          0.49255002,
                          95833904.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'SIS.TO',
                          'SAVARIA CORP.',
                          'CAD',
                          'CAD',
                          'Canada',
                          'Specialty Industrial Machinery',
                          'Industrials',
                          0.669432,
                          '2020-12-31',
                          2019,
                          0.0278,
                          0.24454,
                          0.24611999,
                          64210200.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'VCP.L',
                          'VICTORIA PLC ORD 5P',
                          'GBp',
                          'GBP',
                          'United Kingdom',
                          'Furnishings, Fixtures & Appliances',
                          'Consumer Cyclical',
                          1.6797,
                          '2021-03-31',
                          2020,
                          0.0,
                          0.32931998,
                          0.48031,
                          116852000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'BLV.L',
                          'BELVOIR GROUP PLC ORD 1P',
                          'GBp',
                          'GBP',
                          'United Kingdom',
                          'DOUBLE Estate Services',
                          'DOUBLE Estate',
                          1.257632,
                          '2020-12-31',
                          2019,
                          0.0343,
                          0.18603,
                          0.62520003,
                          37292100.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'EMBRAC-B.ST',
                          'Embracer Group AB ser. B',
                          'SEK',
                          'SEK',
                          'Sweden',
                          'Electronic Gaming & Multimedia',
                          'Communication Services',
                          0.136047,
                          '2021-03-31',
                          2020,
                          0.0,
                          0.36078998,
                          0.31596002,
                          1017489984.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'MHH',
                          'Mastech Digital, Inc',
                          'USD',
                          'USD',
                          'United States',
                          'Staffing & Employment Services',
                          'Industrials',
                          0.533068,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.79907,
                          0.14385,
                          11438000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'SCK.MI',
                          'SCIUKER FRAMES',
                          'EUR',
                          'EUR',
                          'Italy',
                          'Building Products & Equipment',
                          'Industrials',
                          3.55668,
                          '2020-12-31',
                          2019,
                          0.041199997,
                          0.0,
                          0.06181,
                          21451400.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'GREEN.ST',
                          'Green Landscaping Group AB',
                          'SEK',
                          'SEK',
                          'Sweden',
                          'Specialty Business Services',
                          'Industrials',
                          0.454183,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.53205,
                          0.2455,
                          52944200.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'CSAM.OL',
                          'CSAM HEALTH GROUP',
                          'NOK',
                          'NOK',
                          'Norway',
                          'Health Information Services',
                          'Healthcare',
                          1.0,
                          '2020-12-31',
                          2019,
                          0.0,
                          0.41777,
                          0.30488002,
                          20967400.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'ATA.TO',
                          'ATS AUTOMATION',
                          'CAD',
                          'CAD',
                          'Canada',
                          'Specialty Industrial Machinery',
                          'Industrials',
                          1.514358,
                          '2021-03-31',
                          2020,
                          0.0,
                          0.0062599997,
                          0.56783,
                          92260200.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          '0762.HK',
                          'CHINA UNICOM',
                          'HKD',
                          'CNY',
                          'Hong Kong',
                          'Telecom Services',
                          'Communication Services',
                          0.988752,
                          '2020-12-31',
                          2019,
                          0.0791,
                          0.79934,
                          0.01719,
                          30598100992.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'GOOG',
                          'Alphabet Inc.',
                          'USD',
                          'USD',
                          'United States',
                          'Internet Content & Information',
                          'Communication Services',
                          1.069617,
                          '2021-12-31',
                          2020,
                          0.0,
                          0.00035,
                          0.66629,
                          315639008.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'ECONB.BR',
                          'ECONOCOM GROUP',
                          'EUR',
                          'EUR',
                          'France',
                          'Information Technology Services',
                          'Technology',
                          1.480277,
                          '2021-12-31',
                          2020,
                          0.0339,
                          0.4027,
                          0.20319,
                          183827008.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          '1044.HK',
                          'HENGAN INT''L',
                          'HKD',
                          'CNY',
                          'China',
                          'Household & Personal Products',
                          'Consumer Defensive',
                          0.418853,
                          '2020-12-31',
                          2019,
                          0.0668,
                          0.48178002,
                          0.25983,
                          1162119936.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'REP.MC',
                          'REPSOL,  S.A.',
                          'EUR',
                          'EUR',
                          'Spain',
                          'Oil & Gas Integrated',
                          'Energy',
                          1.416844,
                          '2021-12-31',
                          2020,
                          0.051599998,
                          0.06311,
                          0.33977002,
                          1474070016.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'TTE.PA',
                          'TOTALENERGIES',
                          'EUR',
                          'USD',
                          'France',
                          'Oil & Gas Integrated',
                          'Energy',
                          1.084754,
                          '2021-12-31',
                          2020,
                          0.0579,
                          0.06485,
                          0.41869,
                          2596460032.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          '4095.T',
                          'NIHON PARKERIZING CO',
                          'JPY',
                          'JPY',
                          'Japan',
                          'Specialty Chemicals',
                          'Basic Materials',
                          0.559168,
                          '2021-03-31',
                          2020,
                          0.026099999,
                          0.12231,
                          0.39086,
                          117623000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'SFM',
                          'Sprouts Farmers Market, Inc.',
                          'USD',
                          'USD',
                          'United States',
                          'Grocery Stores',
                          'Consumer Defensive',
                          0.296259,
                          '2021-12-31',
                          2020,
                          0.0,
                          0.0072600003,
                          1.1025901,
                          110906000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'GDI.TO',
                          'GDI INTEGRATED FACILITY SERVICE',
                          'CAD',
                          'CAD',
                          'Canada',
                          'Specialty Business Services',
                          'Industrials',
                          0.980855,
                          '2021-12-31',
                          2020,
                          0.0,
                          0.0029,
                          0.47457,
                          14280000.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'BOL.PA',
                          'BOLLORE SE',
                          'EUR',
                          'EUR',
                          'France',
                          'Entertainment',
                          'Communication Services',
                          0.813432,
                          '2020-12-31',
                          2019,
                          0.0127,
                          0.69319,
                          0.14186,
                          2932120064.0
                      );

INSERT INTO Variables (
                          Ticker,
                          CompanyName,
                          StockCurrency,
                          ReportCurrency,
                          Country,
                          Industry,
                          Sector,
                          Beta,
                          BalanceSheetDate,
                          LastYearReport,
                          DividendYield,
                          PercentInsidersHold,
                          PercentInstitutionsHold,
                          SharesOutstanding
                      )
                      VALUES (
                          'MU',
                          'Micron Technology, Inc.',
                          'USD',
                          'USD',
                          'United States',
                          'Semiconductors',
                          'Technology',
                          1.0,
                          '2021-08-31',
                          2020,
                          0.0023999999,
                          0.00193,
                          0.82128996,
                          1119779968.0
                      );