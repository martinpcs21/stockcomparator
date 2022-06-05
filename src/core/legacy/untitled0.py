# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 00:00:29 2022

@author: m.perez-chuecos
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


db_name = 'Fundamentals.db'

cwd = os.getcwd()  # current working directory
db_path = os.path.normpath(os.path.join(cwd, '..', '../src/db', db_name))  # build normalized path to access db
conn = sqlite3.connect(db_path)
print(db_path)
cur = conn.cursor()
print(os.path.join('sqlite:///','../db/', db_name))
# instantiate SQLAlchemy engine
engine = create_engine(os.path.join('sqlite:///','../db/', db_name))


FundamentalAnalysisOld = pd.read_sql_query('SELECT * FROM FundamentalAnalysis', conn)