import numpy as np 
import pandas as pd 
import sqlalchemy as sq  
import json 
import xml
import pyodbc as py


class DB:
    conn: sq.Connection
    def __init__(self, server, db_nm):
        self.db_nm = db_nm
        self.server = server
        self.conn = self.sql_cnx()
    
    def sql_cnx(self)->sq.Connection:
        conn_str = f"mssql+pyodbc://{self.server}/{self.db_nm}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = sq.create_engine(conn_str)
        cnx = engine.connect()
        dt = pd.read_sql("select * from dbo.Stocks", con=cnx)
        print(dt)
        return cnx
    
    def close_cnx(self): 
        print('Closing Connection to DB')
        self.conn.close()
    
    def qry_df(self):
        conn = self.cnx()
        qry = pd.read_sql_query('select * from dbo.CPI_Data'  ,con=conn)
        df = pd.DataFrame(data=qry)
        print(df.head(5).sort_values(by='Dt', ascending=False))
        #print(['Negative' if x<0.0 else 'Positive' for x in df['Per_Change']])
        df['Mnths'] = [x[5:7] for x in df['Dt']]
        df['Yrs'] = [x[0:4] for x in df['Dt']]
        #df.loc[(df['Courses']=="Spark")&(df['Fee']==23000)|(df['Fee']==25000), 'Discount'] = 1000
        print(df.head(10))  
        conn.close()
        return df
    
    def f_df(self):
        df = self.qry_df()
        df['YR'] = df['Dt'].str[0:4]
        print(df.sort_values(by='YR', ascending=False))
        print(df.info())
    
    def dic_qry(self):
        conn = self.cnx()
        qry = pd.read_sql_query('select * from dbo.CPI_Data', con=conn)
        rec_dict = qry.to_dict('records')
        my_dict = qry.to_dict(orient='tight')
        for index ,(k, v) in enumerate(my_dict.items()):
            print(f"Index {index} Key {k} Values {v}")
        #print(my_dict)
        #print(my_dict['Dt'])
        with open('out_dict.json', 'w') as fl:
            json.dump(my_dict, fp=fl, indent=4)
        
    def old_conn(self):
        print(x)
     
            
x = DB(server='DESKTOP-03RVSDU\SQLEXPRESS', db_nm='Labor_Stats')
cnx = x.sql_cnx()
    