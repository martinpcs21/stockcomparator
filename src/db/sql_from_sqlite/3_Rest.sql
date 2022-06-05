

-- Table: Currency
DROP TABLE IF EXISTS Currency;

CREATE TABLE Currency (
    id                      INTEGER,
    CurrencyName            VARCHAR(255)    UNIQUE,
    CurrencyConversiontoUSD FLOAT,
    PRIMARY KEY (id)
);

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         1,
                         'USD',
                         1
                     );

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         2,
                         'EUR',
                         0.87
                     );

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         3,
                         'CNY',
                         0.15
                     );

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         4,
                         'CAD',
                         0.77
                     );

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         5,
                         'HKD',
                         0.12
                     );

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         6,
                         'CHF',
                         1.08
                     );

INSERT INTO Currency (
                         id,
                         CurrencyName,
                         CurrencyConversiontoUSD
                     )
                     VALUES (
                         7,
                         'JPY',
                         0.0088
                     );


-- Table: CurrentPrice
DROP TABLE IF EXISTS CurrentPrice;

CREATE TABLE CurrentPrice (
    id     DOUBLE,
    Ticker VARCHAR(255),
    Price  DOUBLE
);

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'UL',
                             49.31
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'BABA',
                             86.71
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'TEF.MC',
                             4.1065
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             '9988.HK',
                             90.8
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'EDF',
                             6.24
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'EDF.PA',
                             8.14
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'GE',
                             96.08
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'BIDU',
                             150.97
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'INTC',
                             47.73
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             '0788.HK',
                             0.93
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             '2168.HK',
                             8.96
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'ORP.PA',
                             40.4
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'KORI.PA',
                             19.85
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'LNA.PA',
                             39.0
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'ORA.PA',
                             10.778
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'MTY.TO',
                             53.46
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'JD.L',
                             188.05
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'AWRD.ST',
                             289.0
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'NWL.MI',
                             7.34
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'GEO',
                             5.25
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'DND.TO',
                             27.15
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'BB.PA',
                             49.36
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'FB',
                             214.72
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'ICP1V.HE',
                             70.1
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'TIXT',
                             26.43
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'CY4.MI',
                             11.06
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'VOLO.ST',
                             193.6
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'D6H.DE',
                             84.2
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'MRL.L',
                             884.0
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'SIS.TO',
                             17.97
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'VCP.L',
                             1000.0
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'BLV.L',
                             254.35
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'EMBRAC-B.ST',
                             83.03
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'MHH',
                             18.35
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'SCK.MI',
                             8.62
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'GREEN.ST',
                             76.6
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'CSAM.OL',
                             80.0
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'ATA.TO',
                             46.75
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             '0762.HK',
                             4.32
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'GOOG',
                             2682.6
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'ECONB.BR',
                             3.69
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             '1044.HK',
                             41.3
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'REP.MC',
                             11.244
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'TTE.PA',
                             45.63
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             '4095.T',
                             997.0
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'SFM',
                             31.96
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'GDI.TO',
                             53.54
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'BOL.PA',
                             4.772
                         );

INSERT INTO CurrentPrice (
                             id,
                             Ticker,
                             Price
                         )
                         VALUES (
                             NULL,
                             'MU',
                             77.89
                         );


-- Table: CurrentPrices
DROP TABLE IF EXISTS CurrentPrices;

CREATE TABLE CurrentPrices (
    id        INTEGER,
    Ticker    VARCHAR(255),
    Year      INTEGER,
    MeanPrice DOUBLE,
    MaxPrice  DOUBLE,
    MinPrice  DOUBLE,
    PRIMARY KEY (id)
);

INSERT INTO CurrentPrices (
                              id,
                              Ticker,
                              Year,
                              MeanPrice,
                              MaxPrice,
                              MinPrice
                          )
                          VALUES (
                              1,
                              'MSFT',
                              2021,
                              275.6677775307307,
                              349.6700134277344,
                              211.94000244140625
                          );

INSERT INTO CurrentPrices (
                              id,
                              Ticker,
                              Year,
                              MeanPrice,
                              MaxPrice,
                              MinPrice
                          )
                          VALUES (
                              2,
                              'MSFT',
                              2020,
                              192.91023706730175,
                              232.86000061035156,
                              132.52000427246094
                          );

INSERT INTO CurrentPrices (
                              id,
                              Ticker,
                              Year,
                              MeanPrice,
                              MaxPrice,
                              MinPrice
                          )
                          VALUES (
                              3,
                              'MSFT',
                              2019,
                              130.33904787093874,
                              159.5500030517578,
                              97.19999694824219
                          );

INSERT INTO CurrentPrices (
                              id,
                              Ticker,
                              Year,
                              MeanPrice,
                              MaxPrice,
                              MinPrice
                          )
                          VALUES (
                              4,
                              'MSFT',
                              2018,
                              101.12235092831799,
                              116.18000030517578,
                              83.83000183105469
                          );

-- Table: HistoricalPrices
DROP TABLE IF EXISTS HistoricalPrices;

CREATE TABLE HistoricalPrices (
    id        INTEGER,
    Ticker    VARCHAR(255),
    Year      INTEGER,
    MeanPrice DOUBLE,
    MaxPrice  DOUBLE,
    MinPrice  DOUBLE,
    PRIMARY KEY (id),
    UNIQUE (
        Ticker,
        Year,
        MeanPrice
    ),
    UNIQUE (
        Ticker,
        Year,
        MaxPrice
    ),
    UNIQUE (
        Ticker,
        Year,
        MinPrice
    )
);

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 1,
                                 'MSFT',
                                 2021,
                                 275.6677775307307,
                                 349.6700134277344,
                                 211.94000244140625
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 2,
                                 'MSFT',
                                 2020,
                                 192.91023706730175,
                                 232.86000061035156,
                                 132.52000427246094
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 3,
                                 'MSFT',
                                 2019,
                                 130.33904787093874,
                                 159.5500030517578,
                                 97.19999694824219
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 4,
                                 'MSFT',
                                 2018,
                                 101.12235092831799,
                                 116.18000030517578,
                                 83.83000183105469
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 5,
                                 'AMZN',
                                 2020,
                                 2681.0041909198985,
                                 3552.25,
                                 1626.030029296875
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 6,
                                 'AMZN',
                                 2019,
                                 1788.7461896623884,
                                 2035.800048828125,
                                 1460.9300537109375
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 7,
                                 'AMZN',
                                 2018,
                                 1644.0727091633466,
                                 2050.5,
                                 1170.510009765625
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 8,
                                 'AMZN',
                                 2017,
                                 950.0,
                                 950.0,
                                 950.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 9,
                                 'T',
                                 2020,
                                 31.09300394774426,
                                 39.54999923706055,
                                 26.07999992370605
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 10,
                                 'T',
                                 2019,
                                 33.90523809099954,
                                 39.70000076293945,
                                 28.29999923706055
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 11,
                                 'T',
                                 2018,
                                 33.3618725400522,
                                 39.29000091552734,
                                 26.79999923706055
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 12,
                                 'UBER',
                                 2020,
                                 35.46980236264557,
                                 56.02000045776367,
                                 13.71000003814697
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 13,
                                 'UBER',
                                 2019,
                                 35.62572991774857,
                                 47.08000183105469,
                                 25.57999992370605
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 15,
                                 'MCD',
                                 2020,
                                 200.78355685147372,
                                 231.91000366210938,
                                 124.2300033569336
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 16,
                                 'MCD',
                                 2019,
                                 198.354246109251,
                                 221.92999267578125,
                                 173.41000366210938
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 17,
                                 'MCD',
                                 2018,
                                 166.11617549577082,
                                 190.8800048828125,
                                 146.83999633789062
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 18,
                                 'ATVI',
                                 2020,
                                 72.92766791181602,
                                 92.98999786376953,
                                 50.5099983215332
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 19,
                                 'ATVI',
                                 2019,
                                 49.13218251485673,
                                 59.75,
                                 39.84999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 20,
                                 'ATVI',
                                 2018,
                                 69.35087649280807,
                                 84.68000030517578,
                                 43.70999908447266
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 21,
                                 'TEF.MC',
                                 2020,
                                 4.19215953489222,
                                 6.57000017166138,
                                 2.71099996566772
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 22,
                                 'TEF.MC',
                                 2019,
                                 7.12022656947374,
                                 7.90000009536743,
                                 5.86100006103516
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 23,
                                 'TEF.MC',
                                 2018,
                                 7.64766929468771,
                                 8.59899997711182,
                                 6.59200000762939
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 24,
                                 'UL',
                                 2020,
                                 57.15956522824736,
                                 63.88999938964844,
                                 44.06000137329102
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 25,
                                 'UL',
                                 2019,
                                 58.78638889676049,
                                 64.83999633789062,
                                 51.31999969482422
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 26,
                                 'UL',
                                 2018,
                                 54.79816743767119,
                                 58.06999969482422,
                                 50.7400016784668
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 27,
                                 'UL',
                                 2017,
                                 53.52705878570301,
                                 60.13000106811523,
                                 40.31000137329102
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 28,
                                 'BABA',
                                 2017,
                                 103.45997921625774,
                                 110.44999694824219,
                                 96.26000213623047
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 29,
                                 'BABA',
                                 2018,
                                 163.2546600341797,
                                 206.1999969482422,
                                 106.76000213623047
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 30,
                                 'BABA',
                                 2019,
                                 171.078904231706,
                                 211.6999969482422,
                                 129.77000427246094
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 31,
                                 'BABA',
                                 2020,
                                 185.06215879652234,
                                 231.13999938964844,
                                 147.9499969482422
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 32,
                                 'BABA',
                                 2021,
                                 249.2795738432987,
                                 319.32000732421875,
                                 185.0399932861328
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 33,
                                 'TEF.MC',
                                 2017,
                                 9.40079997777939,
                                 10.63000011444092,
                                 8.10000038146973
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 46,
                                 'EDF.PA',
                                 2017,
                                 9.50002509679754,
                                 12.47999954223633,
                                 7.33099985122681
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 47,
                                 'EDF.PA',
                                 2018,
                                 12.61232281857588,
                                 15.89000034332275,
                                 9.83199977874756
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 48,
                                 'EDF.PA',
                                 2019,
                                 11.47298824833889,
                                 15.47500038146973,
                                 8.93000030517578
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 49,
                                 'EDF.PA',
                                 2020,
                                 9.67577737011015,
                                 13.60999965667725,
                                 5.97800016403198
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 50,
                                 'GE',
                                 2017,
                                 197.71827324332065,
                                 235.3076934814453,
                                 132.6923065185547
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 51,
                                 'GE',
                                 2018,
                                 99.7267691192627,
                                 149.15383911132812,
                                 51.23077011108398
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 52,
                                 'GE',
                                 2019,
                                 78.129929576737,
                                 94.72000122070312,
                                 57.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 53,
                                 'GE',
                                 2020,
                                 65.94380934276278,
                                 106.08000183105469,
                                 43.84000015258789
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 54,
                                 'BIDU',
                                 2017,
                                 207.0693618449759,
                                 274.9700012207031,
                                 166.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 55,
                                 'BIDU',
                                 2018,
                                 229.87572003173827,
                                 284.2200012207031,
                                 154.61000061035156
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 56,
                                 'BIDU',
                                 2019,
                                 132.53366553925898,
                                 186.22000122070312,
                                 93.38999938964844
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 57,
                                 'BIDU',
                                 2020,
                                 124.69968259902228,
                                 220.60000610351562,
                                 82.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 58,
                                 'INTC',
                                 2017,
                                 37.84323394450735,
                                 47.63999938964844,
                                 33.22999954223633
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 59,
                                 'INTC',
                                 2018,
                                 49.07979998779297,
                                 57.59999847412109,
                                 42.04000091552734
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 60,
                                 'INTC',
                                 2019,
                                 51.28446203588965,
                                 60.47999954223633,
                                 42.86000061035156
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 61,
                                 'INTC',
                                 2020,
                                 54.88880953713069,
                                 69.29000091552734,
                                 43.61000061035156
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 62,
                                 '0788.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 63,
                                 '0788.HK',
                                 2018,
                                 1.20836733555307,
                                 1.57000005245209,
                                 0.99000000953674
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 64,
                                 '0788.HK',
                                 2019,
                                 1.83551020184342,
                                 2.32999992370605,
                                 1.37000000476837
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 65,
                                 '0788.HK',
                                 2020,
                                 1.53251012472006,
                                 2.02999997138977,
                                 1.13999998569489
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 66,
                                 '0788.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 67,
                                 '2168.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 68,
                                 '2168.HK',
                                 2018,
                                 7.66266667048136,
                                 9.42000007629395,
                                 6.17999982833862
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 69,
                                 '2168.HK',
                                 2019,
                                 12.74714286959901,
                                 22.75,
                                 6.30000019073486
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 70,
                                 '2168.HK',
                                 2020,
                                 26.81129554408765,
                                 39.95000076293945,
                                 18.10000038146973
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 71,
                                 '2168.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 72,
                                 'ORP.PA',
                                 2017,
                                 96.05860163801808,
                                 107.3499984741211,
                                 75.4000015258789
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 73,
                                 'ORP.PA',
                                 2018,
                                 106.43255885567253,
                                 125.19999694824219,
                                 86.37999725341797
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 74,
                                 'ORP.PA',
                                 2019,
                                 105.1982744104722,
                                 117.5999984741211,
                                 83.55999755859375
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 75,
                                 'ORP.PA',
                                 2020,
                                 103.79562497138977,
                                 129.0,
                                 69.0999984741211
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 76,
                                 'KORI.PA',
                                 2017,
                                 26.45776258888891,
                                 29.6767692565918,
                                 23.37749862670898
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 77,
                                 'KORI.PA',
                                 2018,
                                 27.2078689139659,
                                 32.60472869873047,
                                 21.09609031677246
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 78,
                                 'KORI.PA',
                                 2019,
                                 32.96940694322773,
                                 39.01483917236328,
                                 27.78329467773438
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 79,
                                 'KORI.PA',
                                 2020,
                                 30.67705488950014,
                                 42.17370986938477,
                                 23.23895263671875
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 80,
                                 'LNA.PA',
                                 2017,
                                 52.94076271380408,
                                 68.5999984741211,
                                 37.09999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 81,
                                 'LNA.PA',
                                 2018,
                                 53.30570859233225,
                                 60.0,
                                 41.5
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 82,
                                 'LNA.PA',
                                 2019,
                                 46.88607841940487,
                                 50.29999923706055,
                                 41.84999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 83,
                                 'LNA.PA',
                                 2020,
                                 46.22910156846046,
                                 53.0,
                                 31.75
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 84,
                                 'ORA.PA',
                                 2017,
                                 14.42036325096065,
                                 15.79500007629395,
                                 13.5
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 85,
                                 'ORA.PA',
                                 2018,
                                 14.28992124993031,
                                 15.25,
                                 13.3149995803833
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 86,
                                 'ORA.PA',
                                 2019,
                                 13.90850982292026,
                                 15.38000011444092,
                                 13.07999992370605
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 87,
                                 'ORA.PA',
                                 2020,
                                 10.75881639122963,
                                 13.54500007629395,
                                 8.63199996948242
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 88,
                                 'MTY.TO',
                                 2017,
                                 48.40352378118606,
                                 55.97999954223633,
                                 44.75
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 89,
                                 'MTY.TO',
                                 2018,
                                 55.40912002563476,
                                 73.19000244140625,
                                 44.97000122070313
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 90,
                                 'MTY.TO',
                                 2019,
                                 60.96888003540039,
                                 71.86000061035156,
                                 51.61000061035156
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 91,
                                 'MTY.TO',
                                 2020,
                                 37.81468001556397,
                                 62.81999969482422,
                                 14.22999954223633
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 92,
                                 'JD.L',
                                 2018,
                                 74.59922118414016,
                                 92.4000015258789,
                                 60.01499938964844
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 93,
                                 'JD.L',
                                 2019,
                                 82.17619051252093,
                                 107.87999725341797,
                                 63.70000076293945
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 94,
                                 'JD.L',
                                 2020,
                                 130.0450792463999,
                                 178.0,
                                 87.30000305175781
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 95,
                                 'JD.L',
                                 2021,
                                 139.5878325568305,
                                 184.63999938964844,
                                 54.93999862670898
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 96,
                                 'AWRD.ST',
                                 2017,
                                 40.37647067799288,
                                 43.90000152587891,
                                 36.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 97,
                                 'AWRD.ST',
                                 2018,
                                 53.56988100021604,
                                 71.0,
                                 38.59999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 98,
                                 'AWRD.ST',
                                 2019,
                                 80.67813762093363,
                                 104.5,
                                 59.40000152587891
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 99,
                                 'AWRD.ST',
                                 2020,
                                 80.4738097720676,
                                 123.0,
                                 41.09999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 100,
                                 'NWL.MI',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 101,
                                 'NWL.MI',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 102,
                                 'NWL.MI',
                                 2019,
                                 6.02538099743071,
                                 6.55999994277954,
                                 5.69000005722046
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 103,
                                 'NWL.MI',
                                 2020,
                                 5.21186275108188,
                                 6.11999988555908,
                                 3.69000005722046
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 104,
                                 'GEO',
                                 2017,
                                 28.52401157891079,
                                 34.31999969482422,
                                 23.05999946594238
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 105,
                                 'GEO',
                                 2018,
                                 23.50455999755859,
                                 28.05999946594238,
                                 18.43000030517578
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 106,
                                 'GEO',
                                 2019,
                                 18.91577682647097,
                                 24.03000068664551,
                                 13.27999973297119
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 107,
                                 'GEO',
                                 2020,
                                 12.08845235809447,
                                 18.42000007629395,
                                 8.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 108,
                                 'DND.TO',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 109,
                                 'DND.TO',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 110,
                                 'DND.TO',
                                 2019,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 111,
                                 'DND.TO',
                                 2020,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 112,
                                 'DND.TO',
                                 2021,
                                 34.82158997667384,
                                 53.68000030517578,
                                 11.25
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 113,
                                 'BB.PA',
                                 2017,
                                 104.22347642628421,
                                 124.3499984741211,
                                 80.38999938964844
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 114,
                                 'BB.PA',
                                 2018,
                                 83.54803139393724,
                                 99.05000305175781,
                                 71.80000305175781
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 115,
                                 'BB.PA',
                                 2019,
                                 70.90313740150602,
                                 92.44999694824219,
                                 56.65000152587891
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 116,
                                 'BB.PA',
                                 2020,
                                 49.4377733618021,
                                 66.05000305175781,
                                 38.5
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 117,
                                 'FB',
                                 2017,
                                 159.32973783401422,
                                 184.25,
                                 130.3000030517578
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 118,
                                 'FB',
                                 2018,
                                 171.62103994750976,
                                 218.6199951171875,
                                 123.0199966430664
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 119,
                                 'FB',
                                 2019,
                                 181.47717096701086,
                                 208.92999267578125,
                                 128.55999755859375
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 120,
                                 'FB',
                                 2020,
                                 234.19928590078203,
                                 304.6700134277344,
                                 137.10000610351562
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 121,
                                 'ICP1V.HE',
                                 2017,
                                 6.10836282029616,
                                 7.19999980926514,
                                 5.3600001335144
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 122,
                                 'ICP1V.HE',
                                 2018,
                                 6.40467999649048,
                                 8.22000026702881,
                                 5.59999990463257
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 123,
                                 'ICP1V.HE',
                                 2019,
                                 13.70323999404907,
                                 23.0,
                                 7.17999982833862
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 124,
                                 'ICP1V.HE',
                                 2020,
                                 14.71784897077651,
                                 21.20000076293945,
                                 8.53231334686279
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 125,
                                 'TIXT',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 126,
                                 'TIXT',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 127,
                                 'TIXT',
                                 2019,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 128,
                                 'TIXT',
                                 2020,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 129,
                                 'CY4.MI',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 130,
                                 'CY4.MI',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 131,
                                 'CY4.MI',
                                 2019,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 132,
                                 'CY4.MI',
                                 2020,
                                 4.812873137531,
                                 10.18000030517578,
                                 3.88050007820129
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 133,
                                 'VOLO.ST',
                                 2017,
                                 68.76973684210526,
                                 86.75,
                                 58.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 134,
                                 'VOLO.ST',
                                 2018,
                                 44.00674592880976,
                                 65.0,
                                 32.09999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 135,
                                 'VOLO.ST',
                                 2019,
                                 41.87429145473218,
                                 48.15000152587891,
                                 32.65000152587891
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 136,
                                 'VOLO.ST',
                                 2020,
                                 51.12288030745491,
                                 97.62268829345703,
                                 28.54999923706055
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 137,
                                 'D6H.DE',
                                 2017,
                                 34.33777107100889,
                                 41.59999847412109,
                                 24.70000076293945
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 138,
                                 'D6H.DE',
                                 2018,
                                 39.53305127301554,
                                 47.20000076293945,
                                 32.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 139,
                                 'D6H.DE',
                                 2019,
                                 38.74379989624023,
                                 49.65000152587891,
                                 28.70000076293945
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 140,
                                 'D6H.DE',
                                 2020,
                                 55.85816733675649,
                                 72.19999694824219,
                                 38.15000152587891
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 141,
                                 'MRL.L',
                                 2017,
                                 340.13157894736844,
                                 401.1000061035156,
                                 305.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 142,
                                 'MRL.L',
                                 2018,
                                 369.71072083735373,
                                 446.0,
                                 278.75
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 143,
                                 'MRL.L',
                                 2019,
                                 434.0058458652421,
                                 570.0,
                                 340.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 144,
                                 'MRL.L',
                                 2020,
                                 438.8309280335196,
                                 515.0,
                                 315.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 145,
                                 'MRL.L',
                                 2021,
                                 542.1100198654901,
                                 730.0,
                                 342.20001220703125
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 146,
                                 'SIS.TO',
                                 2017,
                                 14.76488890329997,
                                 18.46999931335449,
                                 10.18000030517578
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 147,
                                 'SIS.TO',
                                 2018,
                                 16.96232000350952,
                                 20.95000076293945,
                                 11.40999984741211
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 148,
                                 'SIS.TO',
                                 2019,
                                 13.18232000350952,
                                 15.44999980926514,
                                 10.55000019073486
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 149,
                                 'SIS.TO',
                                 2020,
                                 13.28705179358859,
                                 16.42000007629395,
                                 7.30999994277954
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 150,
                                 'VCP.L',
                                 2017,
                                 443.89418978304474,
                                 473.0,
                                 411.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 151,
                                 'VCP.L',
                                 2018,
                                 660.9678208552509,
                                 984.0,
                                 436.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 152,
                                 'VCP.L',
                                 2019,
                                 638.0070677745955,
                                 890.0,
                                 315.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 153,
                                 'VCP.L',
                                 2020,
                                 444.4232017306,
                                 550.0,
                                 136.156005859375
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 154,
                                 'VCP.L',
                                 2021,
                                 435.109126984127,
                                 850.0,
                                 164.10000610351562
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 155,
                                 'BLV.L',
                                 2017,
                                 103.53521242394912,
                                 115.0,
                                 93.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 156,
                                 'BLV.L',
                                 2018,
                                 101.39704350062779,
                                 110.0,
                                 85.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 157,
                                 'BLV.L',
                                 2019,
                                 111.14785706050812,
                                 150.0,
                                 87.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 158,
                                 'BLV.L',
                                 2020,
                                 137.1897233201581,
                                 187.0,
                                 86.9000015258789
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 159,
                                 'EMBRAC-B.ST',
                                 2019,
                                 30.22585915762281,
                                 37.58333206176758,
                                 23.03333282470703
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 160,
                                 'EMBRAC-B.ST',
                                 2020,
                                 38.68161887657352,
                                 55.42499923706055,
                                 30.89999961853027
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 161,
                                 'EMBRAC-B.ST',
                                 2021,
                                 83.17938002014161,
                                 132.5500030517578,
                                 44.59999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 162,
                                 'MHH',
                                 2017,
                                 4.30090708648209,
                                 7.03499984741211,
                                 2.90499997138977
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 163,
                                 'MHH',
                                 2018,
                                 7.38829997825623,
                                 11.48999977111816,
                                 4.70499992370605
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 164,
                                 'MHH',
                                 2019,
                                 6.43908365979138,
                                 11.47999954223633,
                                 4.51000022888184
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 165,
                                 'MHH',
                                 2020,
                                 17.40293647750975,
                                 29.97999954223633,
                                 7.25
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 166,
                                 'SCK.MI',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 167,
                                 'SCK.MI',
                                 2018,
                                 0.94483999967575,
                                 1.17499995231628,
                                 0.71499997377396
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 168,
                                 'SCK.MI',
                                 2019,
                                 0.86603055634196,
                                 1.62999999523163,
                                 0.37999999523163
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 169,
                                 'SCK.MI',
                                 2020,
                                 1.2735294063886,
                                 3.40000009536743,
                                 0.64999997615814
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 170,
                                 'GREEN.ST',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 171,
                                 'GREEN.ST',
                                 2018,
                                 25.90208251205916,
                                 32.5,
                                 19.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 172,
                                 'GREEN.ST',
                                 2019,
                                 32.59392713631696,
                                 39.5,
                                 26.01499938964844
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 173,
                                 'GREEN.ST',
                                 2020,
                                 29.78892373281812,
                                 41.0,
                                 20.39896965026855
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 174,
                                 'CSAM.OL',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 175,
                                 'CSAM.OL',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 176,
                                 'CSAM.OL',
                                 2019,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 177,
                                 'CSAM.OL',
                                 2020,
                                 89.374561510588,
                                 107.0,
                                 72.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 178,
                                 'ATA.TO',
                                 2017,
                                 13.32611115773519,
                                 13.88000011444092,
                                 12.39999961853027
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 179,
                                 'ATA.TO',
                                 2018,
                                 14.41441768048758,
                                 18.03000068664551,
                                 11.22999954223633
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 180,
                                 'ATA.TO',
                                 2019,
                                 18.97023901236485,
                                 24.67000007629395,
                                 13.27999973297119
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 181,
                                 'ATA.TO',
                                 2020,
                                 19.69992026294845,
                                 22.3799991607666,
                                 14.27000045776367
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 182,
                                 'ATA.TO',
                                 2021,
                                 20.83975998306274,
                                 29.88999938964844,
                                 14.85000038146973
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 183,
                                 '0762.HK',
                                 2017,
                                 10.95213637785478,
                                 13.23999977111816,
                                 9.22000026702881
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 184,
                                 '0762.HK',
                                 2018,
                                 9.77379594530378,
                                 11.9399995803833,
                                 8.10000038146973
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 185,
                                 '0762.HK',
                                 2019,
                                 8.43020405866662,
                                 10.69999980926514,
                                 6.51999998092651
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 186,
                                 '0762.HK',
                                 2020,
                                 5.24712553294564,
                                 7.36999988555908,
                                 3.83999991416931
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 187,
                                 'GOOG',
                                 2017,
                                 935.527037753118,
                                 1078.489990234375,
                                 803.3699951171875
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 188,
                                 'GOOG',
                                 2018,
                                 1113.804477294922,
                                 1273.8900146484375,
                                 970.1099853515625
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 189,
                                 'GOOG',
                                 2019,
                                 1186.4397009131444,
                                 1365.0,
                                 1014.0700073242188
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 190,
                                 'GOOG',
                                 2020,
                                 1478.5513310508122,
                                 1847.199951171875,
                                 1013.5360107421875
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 191,
                                 'GOOG',
                                 2021,
                                 2506.6135696471924,
                                 3037.0,
                                 1699.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 192,
                                 'ECONB.BR',
                                 2017,
                                 6.81124221165975,
                                 8.0,
                                 5.75099992752075
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 193,
                                 'ECONB.BR',
                                 2018,
                                 4.3985905515866,
                                 7.29500007629395,
                                 2.28399991989136
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 194,
                                 'ECONB.BR',
                                 2019,
                                 2.99804724107577,
                                 4.09800004959106,
                                 2.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 195,
                                 'ECONB.BR',
                                 2020,
                                 2.20563280582428,
                                 2.88000011444092,
                                 1.37100005149841
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 196,
                                 'FB',
                                 2021,
                                 321.01729076127134,
                                 384.3299865722656,
                                 244.61000061035156
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 197,
                                 'INTC',
                                 2021,
                                 55.90095615766913,
                                 68.48999786376953,
                                 47.86999893188477
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 198,
                                 'ORA.PA',
                                 2021,
                                 9.81951359923248,
                                 10.73600006103516,
                                 8.92599964141846
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 199,
                                 '1044.HK',
                                 2017,
                                 65.85761905851818,
                                 88.69999694824219,
                                 52.79999923706055
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 200,
                                 '1044.HK',
                                 2018,
                                 70.98938783918108,
                                 88.5,
                                 51.79999923706055
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 201,
                                 '1044.HK',
                                 2019,
                                 58.21489804326271,
                                 72.4000015258789,
                                 48.59999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 202,
                                 '1044.HK',
                                 2020,
                                 60.19008095930462,
                                 72.0,
                                 51.34999847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 203,
                                 'DND.TO',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 204,
                                 'DND.TO',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 205,
                                 'DND.TO',
                                 2019,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 206,
                                 'DND.TO',
                                 2020,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 207,
                                 '2168.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 208,
                                 '2168.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 209,
                                 '9988.HK',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 210,
                                 '9988.HK',
                                 2018,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 211,
                                 '9988.HK',
                                 2019,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 212,
                                 '9988.HK',
                                 2020,
                                 203.0564706241383,
                                 227.39999389648438,
                                 167.60000610351562
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 213,
                                 '9988.HK',
                                 2021,
                                 242.06666564941406,
                                 309.3999938964844,
                                 181.10000610351562
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 214,
                                 'GEO',
                                 2021,
                                 7.51561750738744,
                                 11.0,
                                 4.96000003814697
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 215,
                                 'TEF.MC',
                                 2021,
                                 3.90016797743738,
                                 4.32200002670288,
                                 3.23900008201599
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 216,
                                 'REP.MC',
                                 2017,
                                 14.72849007880334,
                                 16.29999923706055,
                                 13.27499961853027
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 217,
                                 'REP.MC',
                                 2018,
                                 15.81498025057344,
                                 17.51000022888184,
                                 13.60499954223633
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 218,
                                 'REP.MC',
                                 2019,
                                 14.43856862760058,
                                 15.66499996185303,
                                 12.36499977111816
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 219,
                                 'REP.MC',
                                 2020,
                                 8.4421093929559,
                                 14.47500038146973,
                                 5.04199981689453
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 220,
                                 'REP.MC',
                                 2021,
                                 10.20575782284141,
                                 11.77999973297119,
                                 7.96000003814697
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 221,
                                 'TTE.PA',
                                 2017,
                                 45.83217815361401,
                                 49.33499908447266,
                                 42.22499847412109
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 222,
                                 'TTE.PA',
                                 2018,
                                 50.642500043854,
                                 56.81999969482422,
                                 43.09000015258789
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 223,
                                 'TTE.PA',
                                 2019,
                                 47.99727458579868,
                                 52.27000045776367,
                                 42.65000152587891
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 224,
                                 'TTE.PA',
                                 2020,
                                 35.00470713526011,
                                 50.93000030517578,
                                 21.1200008392334
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 225,
                                 'TTE.PA',
                                 2021,
                                 39.40984417214004,
                                 45.54999923706055,
                                 33.90999984741211
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 226,
                                 'ECONB.BR',
                                 2021,
                                 3.25768482917014,
                                 3.94000005722046,
                                 2.36999988555908
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 227,
                                 'KORI.PA',
                                 2021,
                                 30.37291828110988,
                                 34.7599983215332,
                                 25.71999931335449
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 228,
                                 'MTY.TO',
                                 2021,
                                 58.88407995605468,
                                 72.0999984741211,
                                 47.15000152587891
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 229,
                                 '4095.T',
                                 2017,
                                 1409.0,
                                 1429.0,
                                 1383.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 230,
                                 '4095.T',
                                 2018,
                                 1719.8599221789884,
                                 2067.0,
                                 1309.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 231,
                                 '4095.T',
                                 2019,
                                 1497.767716535433,
                                 1779.0,
                                 1170.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 232,
                                 '4095.T',
                                 2020,
                                 1196.7333333333333,
                                 1534.0,
                                 863.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 233,
                                 '4095.T',
                                 2021,
                                 1093.8683127572017,
                                 1253.0,
                                 959.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 234,
                                 'SFM',
                                 2017,
                                 22.18963546554248,
                                 25.97999954223633,
                                 17.54999923706055
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 235,
                                 'SFM',
                                 2018,
                                 24.70291999816894,
                                 29.67000007629395,
                                 20.6299991607666
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 236,
                                 'SFM',
                                 2019,
                                 20.49653386119827,
                                 25.31999969482422,
                                 16.45999908447266
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 237,
                                 'SFM',
                                 2020,
                                 21.07904757393731,
                                 28.0,
                                 13.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 238,
                                 'SFM',
                                 2021,
                                 24.65968123660145,
                                 30.61000061035156,
                                 19.1299991607666
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 239,
                                 'GDI.TO',
                                 2017,
                                 NULL,
                                 NULL,
                                 NULL
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 240,
                                 'GDI.TO',
                                 2018,
                                 18.06546208838455,
                                 19.89999961853027,
                                 15.89999961853027
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 241,
                                 'GDI.TO',
                                 2019,
                                 26.8167799987793,
                                 37.25,
                                 18.3799991607666
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 242,
                                 'GDI.TO',
                                 2020,
                                 34.76958168455329,
                                 47.5,
                                 24.19000053405762
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 243,
                                 'GDI.TO',
                                 2021,
                                 51.98992007446289,
                                 60.0,
                                 41.0
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 244,
                                 'BOL.PA',
                                 2017,
                                 4.05094764369945,
                                 4.58699989318848,
                                 3.46300005912781
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 245,
                                 'BOL.PA',
                                 2018,
                                 4.09993700999913,
                                 4.7979998588562,
                                 3.35999989509583
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 246,
                                 'BOL.PA',
                                 2019,
                                 3.87036862653845,
                                 4.34800004959106,
                                 3.41199994087219
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 247,
                                 'BOL.PA',
                                 2020,
                                 3.09139063023031,
                                 3.99600005149841,
                                 2.00999999046326
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 248,
                                 'MU',
                                 2017,
                                 29.63123802911668,
                                 32.95999908447266,
                                 26.36000061035156
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 249,
                                 'MU',
                                 2018,
                                 48.06314737388337,
                                 64.66000366210938,
                                 31.64999961853027
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 250,
                                 'MU',
                                 2019,
                                 39.6943600616455,
                                 52.29999923706055,
                                 28.38999938964844
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 251,
                                 'MU',
                                 2020,
                                 48.91593632185127,
                                 61.18999862670898,
                                 31.1299991607666
                             );

INSERT INTO HistoricalPrices (
                                 id,
                                 Ticker,
                                 Year,
                                 MeanPrice,
                                 MaxPrice,
                                 MinPrice
                             )
                             VALUES (
                                 252,
                                 'MU',
                                 2021,
                                 73.99215135916296,
                                 96.95999908447266,
                                 44.45000076293945
                             );

