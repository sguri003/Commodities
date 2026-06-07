import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fredapi as fred
from datetime import date
import sqlalchemy as sq
from DB import DB


class Stocks:

    def __init__(self):
        f_key = pd.read_csv('/src/API_KEY.csv')
        self._fred_key = f_key['Fred_key'][0]

    def get_today(self) -> str:
        return date.today().strftime('%Y-%m-%d')

    def get_fed(self) -> pd.DataFrame:
        f = fred.Fred(api_key=self._fred_key)
        usd_fred = f.get_series('DTWEXBGS', observation_start='2015-01-01',
                                observation_end=self.get_today())
        return usd_fred.to_frame(name='USD')

    def _download_tickers(self, tickers: list, start: str) -> pd.DataFrame:
        dt = yf.download(tickers, start=start, group_by='ticker').reset_index()
        dt.columns = ['_'.join(col).strip().replace('=', '_') 
                      for col in dt.columns.values]
        return np.round(dt, decimals=2)

    def ticks_plt(self) -> pd.DataFrame:
        tickers = ['PL=F', 'GC=F', 'SI=F', 'HG=F', 'PA=F', 'CL=F', 'BZ=F', 'DXY']
        return yf.download(tickers, start='2015-01-01', group_by='ticker')

    def ticks_sql(self) -> pd.DataFrame:
        tickers = ['PL=F', 'GC=F', 'SI=F', 'HG=F', 'PA=F', 'CL=F', 'BZ=F',
                   'NDX', 'XEL', 'CVX', 'B', 'MP', 'DJI']
        return self._download_tickers(tickers, start='2010-01-01')

    def plotting(self, dt: pd.DataFrame):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(dt['GC=F']['Close'], label='Gold Price', color='gold')
        ax.plot(dt['PL=F']['Close'], label='Platinum', color='gray')
        ax.plot(dt['SI=F']['Close'], label='Silver', color='green')
        ax.set_title('Precious Metals to USD Index — Yahoo Finance')
        ax.set_xlabel('Date')
        ax.set_ylabel('US Dollar')
        ax.set_yticks(np.arange(500, 4000, 500))
        ax.legend()
        ax.grid(True)
        plt.show()

    def sql_insert(self, df: pd.DataFrame):
        db = DB(server=r"DESKTOP-03RVSDU\SQLEXPRESS", db_nm="Labor_Stats")
        cnx = db.sql_cnx()
        df = df.rename(columns={'Date_': 'Dt'})
        df['Dt'] = pd.to_datetime(df['Dt']).dt.date
        df['datekey'] = pd.to_datetime(df['Dt']).dt.strftime('%Y%m%d').astype(int)
        df.to_sql(name='Commodity', schema='dbo', con=cnx,
                  if_exists='replace', index=False)
        db.close_cnx()

    def csv_x(self, df: pd.DataFrame):
        (df[['Date_', 'GC=F_Close']]
            .rename(columns={'GC=F_Close': 'Gld_Close'})
            .round(2)
            .to_csv('Silver_Price.csv', index=False))


if __name__ == '__main__':
    st = Stocks()
    df = st.ticks_sql()
    st.plotting(dt=df)
    #st.sql_insert(df=df)
