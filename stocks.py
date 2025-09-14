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
        usd_fred = f.get_series('DTWEXBGS', observation_start='2015-01-01'
                                ,observation_end=self.get_today())
        print(type(usd_fred))
        usd_srs = pd.Series(usd_fred, name=['Dt','USD'])
        fed =usd_fred.to_frame()
        print(usd_fred)
        
    def ticks_plt(self)->pd.DataFrame:
        ticker_lst =['PL=F', 'GC=F','SI=F','HG=F','PA=F','DXY']
        dt = yf.download(ticker_lst, start='2015-01-01', group_by='ticker')
        #Download historical data for the last year
        dt = pd.DataFrame(data=dt)
        #dt_dt = dt.reset_index()
        return dt

    def ticks_sql(self)->pd.DataFrame:
        ticker_lst =['PL=F', 'GC=F','SI=F','HG=F','PA=F','DXY']
        dt = yf.download(ticker_lst, start='2010-01-01', group_by='ticker')
        #Download historical data for the last year
        dt = pd.DataFrame(data=dt)
        dt_f = dt.reset_index()
        dt_f.columns = ['_'.join(col).strip() for col in dt_f.columns.values]
        print(dt_f.columns)
        return dt_f    
        
        
    def plotting(self, dt: pd.DataFrame):
        y1= dt['GC=F']['Close']
        y2 = dt['PL=F']['Close']
        y3 = dt['DXY']['Close']
        #y4 = dt['RTX']['Close']
        cmap = plt.cm.RdYlGn #tooltip
        plt.figure(figsize=(12, 8))
        plt.plot(y1, label='Gold Price', color='gold')
        plt.plot(y2, label='Platinum', color='gray')
        plt.plot(y3, label='USD', color='green')
        #plt.plot(y4, label='Raytheon', color='orange')
        plt.title('Precious Metals to USD Index Yahoo Finance')
        plt.xlabel('Date')
        plt.ylabel('US Dollar')
        #plt.ylabel('Raytheon')
        y_tick_locations = np.arange(500, 4000, 500) #start, stop, step
        plt.yticks(y_tick_locations)
        plt.legend()
        plt.grid(True)
        plt.show()
        #print(dt.head(10))

    def insert_db(self,df:pd.DataFrame):
        SERVER= "DESKTOP-03RVSDU\SQLEXPRESS"
        DB_NAME = "Labor_Stats"
        conn_str = f"mssql+pyodbc://{SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = sq.create_engine(conn_str)
        cnx = engine.connect()
        df.to_sql(name='Stocks_Py', schema='dbo'
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
#df = st.ticks_plt()
df = st.ticks_sql()
#st.plotting(df)
st.insert_db(df=df)
