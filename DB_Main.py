import numpy as np 
import pandas as pd 
import sqlalchemy as sq  
import json 
import xml


class DB_Main:
    
    def __init__(self):
        self.DB_NAME = "Labor_Stats"
        self.SERVER = "DESKTOP-03RVSDU\SQLEXPRESS"
        
    
    def cnx(self):
        conn=None
        engine=None
        conn_str = f'mssql+pyodbc://{self.SERVER}/{self.DB_NAME}?driver=ODBC+Driver+SQL+Server+17'
        try: 
        #f"mssql+pyodbc:///?odbc_connect={conn_str}"
            engine = sq.create_engine(conn_str)
            conn  = engine.connect()
            print(f"Connection to Server {self.SERVER} and {self.DB_NAME} successful")
        except:
            print(f"Failed to connect  {self.SERVER} and {self.DB_NAME}")
        qry = pd.read_sql_query('select * from dbo.CPI_Data'  ,con=conn)
        df = pd.DataFrame(data=qry)
        print(df.head(5).sort_values(by='Dt', ascending=False))
        #print(my_dict.keys())
        #conn.close()
        return conn
     
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
     
            
x = DB_Main()
x.cnx()
    