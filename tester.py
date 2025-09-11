import pyodbc
import numpy as np   
import pandas as pd 


def cnx():
    conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=DESKTOP-03RVSDU\SQLEXPRESS;DATABASE=Labor_Stats;')
    cursor = conn.cursor()
    cur = cursor.execute('select * from dbo.CPI_Data')
    #print(x.fetchall())
    #df = pd.read_sql('select * from dbo.CPI_Data', con=conn)
    #df_1 = pd.DataFrame(data=df)
    #print(df_1.head(4))
    lst = []
    print(cur.description)
    cols = [columns[0] for columns in cur.description]
    for i, row in enumerate(cur.fetchall()):
        lst.append(row)        
        #print(type(row))
        #print(row)
    #row_dict = dict(zip(cols, x))
    #for k, v in row_dict.items():
    #    print(f'{k} {v}')  
        
    #print([key for key, value in x.fetchall().items()])
    #rec_sz = len(lst)
    #print(rec_sz)
    conn.close()
cnx()

