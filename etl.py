import os   
import numpy as np    
import pandas as pd    
import sqlalchemy as sq
from sqlalchemy import create_engine
import json 
import csv         
import urllib

#engine = create_engine("mssql+pyodbc://username:password@servername/dbname?driver=ODBC+Driver+17+for+SQL+Server").
def run_sql():
    server = 'DESKTOP-03RVSDU\\SQLEXPRESS'  # to specify an alternate port
    database = 'AdventureWorksDW2019'
    trusted = "trusted_connection=yes"
    params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};{trusted}")
    engine = sq.create_engine(f"mssql+pyodbc:///?odbc_connect=%s" % params).connect()
    conn = engine.connect()
    dt_cursor =pd.read_sql('select * from dbo.FactCallCenter', conn)
    df = pd.DataFrame(dt_cursor)
    print(df.iloc[0:10,0:5])
    #rows 0-4 and Data and Calls
    print(df.loc[0:4 ,['Date','Calls', 'DateKey']])
    print(df.columns)
    print(df[df['Shift']=='AM'].sort_values(by='Date', ascending=False))
    df_am = df[df['Shift']=='AM']
    #print(df_am.sort_values(by='Calls', ascending=False))
    #print(df_am['Calls'].sum())
    df_agg = df_am[['Calls', 'Orders']].agg({'sum','mean', 'max', 'min' })
    print(df_agg)

def test():
    #x = ("y" "z")
    x = np.array([1, 2,4,6,7])
    for i, v in np.ndenumerate(x):
        if v%2==0:
            print(x[i])
        else:
            print("Not Even")
            
            
test()
#run_sql()