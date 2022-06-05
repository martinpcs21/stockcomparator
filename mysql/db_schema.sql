-- ====================================
-- Script to restart the whole db schema from scratch
-- Date: 27/12/2021
-- Version: 1.0
-- ====================================

DROP SCHEMA IF EXISTS `Fundamentals`;

CREATE SCHEMA IF NOT EXISTS `Fundamentals`;

USE `Fundamentals`;

CREATE TABLE IF NOT EXISTS `Sectors` (
    `Sector` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`Sector`)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `Companies` (
    `Ticker` VARCHAR(10) NOT NULL,
    `Name` VARCHAR(255) DEFAULT NULL,
    `Sector` VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (`Ticker`),
    -- CONSTRAINTS
    CONSTRAINT `fk_Companies_Sectors`
        FOREIGN KEY (`Sector`)
        REFERENCES `Sectors`(`Sector`)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `KPIs` (
    `KPI` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`KPI`)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `Variables` (
    `Variable` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`Variable`)
) ENGINE=INNODB;

CREATE TABLE `Currency` (
    `CurrencyName` VARCHAR(255) NOT NULL,
    `CurrencyConversiontoUSD` DOUBLE,
    PRIMARY KEY (`CurrencyName`)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `AnnualReports` (
    `Company` VARCHAR(255) NOT NULL,
    `Year` INTEGER NOT NULL,
    `KPI` VARCHAR(255) NOT NULL,
    `Value` DOUBLE DEFAULT NULL,
    PRIMARY KEY (`Company`, `KPI`, `Year`),
    -- CONSTRAINTS
    CONSTRAINT `fk_AnnualReports_Companies`
        FOREIGN KEY (`Company`)
        REFERENCES `Companies`(`Ticker`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT `fk_AnnualReports_KPIs`
        FOREIGN KEY (`KPI`)
        REFERENCES `KPIs`(`KPI`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `CompanyMetaData` (
    `Company` VARCHAR(255) NOT NULL,
    `KPI` VARCHAR(255) NOT NULL,
    `Value` TEXT NOT NULL,
    PRIMARY KEY (`Company`, `KPI`),
    -- CONSTRAINTS
    CONSTRAINT `fk_CompanyMetaData_Companies`
        FOREIGN KEY (`Company`)
        REFERENCES `Companies`(`Ticker`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT `fk_CompanyMetaData_KPIs`
        FOREIGN KEY (`KPI`)
        REFERENCES `KPIs`(`KPI`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `CompanyVariables` (
    `Company` VARCHAR(255) NOT NULL,
    `KPI` VARCHAR(255) NOT NULL,
    `Value` VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (`Company`, `KPI`),
    CONSTRAINT `fk_CompanyVariables_Companies`
        FOREIGN KEY (`Company`)
        REFERENCES `Companies`(`Ticker`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT `fk_CompanyVariables_Variables`
        FOREIGN KEY (`KPI`)
        REFERENCES `Variables`(`Variable`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=INNODB;

CREATE TABLE `FundamentalAnalysis` (
    `Ticker` VARCHAR(255) NOT NULL,
    -- `CompanyName` TEXT,
    `CurrentPrice` DOUBLE,
    -- `Sector` TEXT,
    `StockCurrency` VARCHAR(255) NOT NULL,
    `ReportCurrency` VARCHAR(10),
    `LastReportDate` DATE,
    `CurrentPER` DOUBLE,
    `MeanPER` DOUBLE,
    `CurrentEVEBITDA` DOUBLE,
    `MeanEVEBITDA` DOUBLE,
    `CurrentEVEBIT` DOUBLE,
    `CurrentPricetoBook` DOUBLE,
    `CurrentPricetoFreeCashFlowRate` DOUBLE,
    `MeanPricetoFreeCashFlowRate` DOUBLE,
    `DividendYield` DOUBLE,
    `PayOut` DOUBLE,
    `ROE` DOUBLE,
    `ROCE` DOUBLE,
    `ROA` DOUBLE,
    `Beta` DOUBLE,
    `LiquidityRatio` DOUBLE,
    `CashOverStockPrice` DOUBLE,
    `DebtQualityRatio` DOUBLE,
    `LiabilitiestoEquityRatio` DOUBLE,
    `NetDebttoEBITDA` DOUBLE,
    `MeanNetDebttoEBITDA` DOUBLE,
    `InterestExpensetoEBIT` DOUBLE,
    `EntrepriseValueUSD` DOUBLE,
    `DCFValuewithExitMultiplePotential` DOUBLE,
    `EBITDATendency` DOUBLE,
    `FreeCashFlowTendency` DOUBLE,
    `OperatingCashFlowTendency` DOUBLE,
    `NetIncomeTendency` DOUBLE,
    `EquityTendency` DOUBLE,
    `TargetPrice` DOUBLE,
    PRIMARY KEY (`Ticker`),
    CONSTRAINT `fk_FundamentalAnalysis_Companies`
        FOREIGN KEY (`Ticker`)
        REFERENCES `Companies`(`Ticker`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT `fk_FundamentalAnalysis_Currency`
        FOREIGN KEY (`Currency`)
        REFERENCES `Currency`(`CurrencyName`)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=INNODB;
