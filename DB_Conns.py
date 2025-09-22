import os
import sqlalchemy as sq
import urllib.parse
import pandas as pd            
import numpy as np    
import datetime
import re

class DB_Conns:
    #static variable
    DB_NAME = "Labor_Stats"
    SERVER = "DESKTOP-03RVSDU\SQLEXPRESS"
    def __init__(self, xlsx_fl):
        self.xlsx_fl = xlsx_fl
        self.DB_NAME = "Labor_Stats"
        self.SERVER = "DESKTOP-03RVSDU\SQLEXPRESS"
        
    def conn_s(self):
        conn_str = (
        "DRIVER={SQL Server};"+
        "SERVER={};".format(self.SERVER)+
        "DATABASE={};".format(self.DB_NAME)+
        "Trusted_Connection=yes;"
        )
        print(type(conn_str))
        
    def qry_db(self):
        x = urllib.parse.quote("{ODBC Driver SQL Server 17}")
        print(x)
        conn_str = (
        "DRIVER={SQL Server};"+
        "SERVER={};".format(self.SERVER)+
        "DATABASE={};".format(self.DB_NAME)+
        "Trusted_Connection=yes;"
        )
        #params = urllib.parse.quote_plus(conn_str)
        engine = sq.create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")
        conn = engine.connect()
        print(conn.connection)
        df = pd.read_sql_query("select * from dbo.CPI_Data", con=conn)
        df_1 = pd.DataFrame(data=df)
        print(df_1)
        df_1.to_xml(self.xlsx_fl)
        
        
    def read_xml(self):
        xm  = pd.read_xml(self.xlsx_fl)
        df = pd.DataFrame(data=xm)
        print(df.head(4).sort_values(by="Value", ascending=False))
        
        
    def quick_cnx(self):
        conn_str = f"mssql+pyodbc://{self.SERVER}/{self.DB_NAME}?driver=SQL+Server"
        engine = sq.create_engine(conn_str)
        conn = engine.connect()
        result = pd.read_sql("select * from dbo.CPI_Data",con=conn)
        #print(result)
        df = pd.DataFrame(data=result)
        df_high = df.loc[df['Per_Change']>25.0]
        df_high = df_high.loc[df_high['Dt'].str[0:4]=='2022']
        df_high['YR'] = df_high["Dt"].str[0:4]
        #df_high.loc[df_high["Dt"].str[5:7]]
        print(str(df_high['Dt'].str[5:7]) + df_high["Dt"])
        print(df_high.info())
        print(df.head(5))
        conn.close()
        
 
        
        
cpi_test = DB_Pull("exprt.xml")
cpi_test.conn_s()
#cpi_test.qry_db()
#cpi_test.read_xml()
cpi_test.quick_cnx()

#    def main():
#        cpi_test = CPI('exprt.xlm')
#        cpi_test.qry_db()

#if __name__=="__main__":
#   CPI.main()
    
