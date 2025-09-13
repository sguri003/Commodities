import yfinance  as yf 
import requests 
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import fredapi as fred    
from datetime import date
import sqlalchemy as sq
import pyodbc as py
from DB import DB


class Stocks:
    
    def __init__(self):
         self
      
    def get_ky(self):
        f_key = pd.read_csv('API_KEY.csv')
        ky = f_key['Fred_key'][0]
        formatted_date_1 = str(date.today().strftime("%d-%m-%Y"))
        print(formatted_date_1)
        return ky
    
    def get_today(self):
        formatted_date_1 = str(date.today().strftime("%d-%m-%Y"))
        return formatted_date_1
    
    def dt_ky(self, dt:date):
        print()
    
    def get_fed(self):
        f = fred.Fred(api_key=self.get_ky())
        usd_fred = f.get_series('JTSHIR', observation_start='2015-01-01' ,observation_end='2025-07-01')
                                #,observation_end=self.get_today())
        #usd_jobs = f.get_series('JTSJOB', observation_start='2015-01-01' ,observation_end='2025-08-01')
        print(type(usd_fred))
        usd_fred = pd.Series(usd_fred, name=['Dt','Hires'])
        #fed =usd_fred.to_frame()
        #combined = pd.concat(usd_fred, usd_jobs)
        usd_fred.to_csv('Hires.csv')
        print(usd_fred)
        
   
    def insert_db(self,df:pd.DataFrame):
        SERVER= "DESKTOP-03RVSDU\SQLEXPRESS"
        DB_NAME = "Labor_Stats"
        conn_str = f"mssql+pyodbc://{SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = sq.create_engine(conn_str)
        cnx = engine.connect()
        df.to_sql(name='Stocks_Test', schema='dbo'
            , con=cnx, if_exists='replace', index=False,index_label=False)
        cnx.close()
        
    def sql_insert(self,df:pd.DataFrame):
        SERVER= "DESKTOP-03RVSDU\SQLEXPRESS"
        DB_NAME = "Labor_Stats"
        #Call DB class with server and name parameters
        db = DB(server=SERVER, db_nm=DB_NAME)
        cnx = db.sql_cnx()
        df.to_sql(name='Stock_QA', schema='dbo'
            , con=cnx, if_exists='replace', index=False,index_label=False)
        #close connection DB:Close()
        print(sq.inspect(cnx).has_table('Stocks_Test'))
        db.close_cnx()    

st = Stocks()
st.get_fed()
#df = st.ticks_plt()
#df = st.test_dt()
#st.plotting(df)
#st.insert_db(df=df)
