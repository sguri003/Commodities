import sqlalchemy as sq
import urllib.parse
import numpy as np 
import pandas as pd  
import xml.etree.ElementTree as ET
import pyodbc as py 

class xml_parser:

    def __init__(self, f_path):
        self.f_path=f_path
        
    def find_node(self, elem, item):
            #if no child node then sinsert into dictionary(). 
        if len(list(elem))==0:
            item[elem.tag]=elem.text     
            #print(elem.text)                              
        else:
            for child in list(elem):
                self.find_node(child, item)
                    
        #parse XML tree with recursive fn() above
    def parse_tree(self)->pd.DataFrame:
        dict_lst = []
        tree = ET.parse(self.f_path)
        root = tree.getroot()
        for child in root:
            items = {} #new dictionary in loop of xml
            self.find_node(child, items) #recursive finde nodes of xml
            dict_lst.append(items) #append dict{} to array<> list
        #print(dict_lst) 
        df = pd.DataFrame(data=dict_lst)
        return df  #return list<dict{}>
            
        #filter list to gasoline only.         
    def gas_only(self, product:str,lst: list):
        gas = 'B01'
        new_lst = []
        for dic_list in lst:
            for k, v in dic_list.items():
                if k=='Series_ID' and v[len(v)-3: len(v)]==gas:
                    new_lst.append(dic_list)
        return new_lst        
    
        #column to dictionary.
    def add_col(self, lst: list):
        new_dict = []
        for dict_list in lst:
            #access dictionary
            #print(dict_list['Series_ID'])
            dict_list["Series_Name"] = 'Gas' 
            new_dict.append(dict_list)    
        #print(dict_list)  
        return dict_list   
    
    def df_lst(self, lst)->pd.DataFrame:
        xml_df = pd.DataFrame(lst)
        print(xml_df)
        return xml_df
    
    def insert_sql(self, lst):
        #cnx = py.connect('DRIVER={SQL SERVER};SERVER=DESKTOP-03RVSDU\SQLEXPRESS;DATABASE=Labor_Stats;')
        #nm = cnx.execute('@@SERVERNAME')
        #print(nm)
        SERVER= "DESKTOP-03RVSDU\SQLEXPRESS"
        DB_NAME = "Labor_Stats"
        conn_str = f"mssql+pyodbc://{SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = sq.create_engine(conn_str)
        cnx = engine.connect()
        #df.to_sql(con=cnx,schema='dbo', name='xml_cpi', if_exists='replace')
        #print(count)
        #df = pd.DataFrame(lst,columns=['Dt'])
        df = pd.DataFrame(lst)
        pd.to_datetime(df['Dt'], format='mixed')
        print(df)
        print(df.columns)
        print(df.info())
        df['Value'] = df['Value'].astype(float)
        df['Value']= df['Value'].round(2)
        #df['Dt'].astype(str)
        #print(df.columns)
        dtypes = {
                'Series_ID': sq.types.VARCHAR(length=100),
                'Dt':sq.types.DATE(),
                'Value': sq.types.DECIMAL(precision=10,decimal_return_scale=2 ),
                'Per_Change': sq.types.DECIMAL(precision=10,decimal_return_scale=2 ),
                'datekey': sq.types.INTEGER()}
        print(df.info())
        df.to_csv('ex_csv.csv', index_label=False, index=False)
        df.to_sql(name='CPI_X', con=cnx, schema='dbo',
                 # dtype=dtypes,
                  index_label=False , index=False,if_exists='replace' 
                   ) 
        cnx.close()
                             #'intfld':  sqlalchemy.types.INTEGER(),
                             #'strfld': sqlalchemy.types.NVARCHAR(length=255)
                             #'floatfld': sqlalchemy.types.Float(precision=3, asdecimal=True)
                             #'booleanfld': sqlalchemy.types.Boolean}))