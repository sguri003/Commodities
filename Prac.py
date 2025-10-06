import os 
import numpy as np  
import pandas as pd 
import requests
import csv 
import re 
import json

def json_prac():
    lst = [] 
    with open('CPI_QA.json', 'r') as f:
        my_dict = json.load(fp=f)
        for x in my_dict['Results']['series']:
            for data in x['data']:
                print(data['calculations'])
                lst.append(data['calculations'])   
                print(data['calculations']['net_changes'])
    
        for calcs in lst:
            print(calcs['pct_changes']['12'])
        for k in my_dict.keys():
            print(k)
        
def csv_prac():
    lst = []
    file_nm = 'test_BLS.csv'
    out_fl = open('test.csv', 'w')
    with open(file_nm, 'r') as f:
        rdr = csv.reader(f)
        hdr = next(rdr)
        d_wtr =csv.writer(out_fl, lineterminator='\n')
        d_wtr.writerow([hdr[1] ,hdr[2], 'Year', hdr[4]])
        for row in rdr:
            print(row)
            s_id = row[1]
            dt = row[2]
            yr = row[2].split('-')[0] #split into array get first element. 
            print(yr)
            yoy = row[4]
            if dt[0:4]>='2024':
                d_wtr.writerow([s_id, dt, yr, yoy])
    out_fl.close()
        

def p_csv():
    df_c = pd.read_csv('Silver_Price.csv')
    df = pd.DataFrame(data=df_c)
    df_c.sort_values(by='Date_', ascending=False)
    dy = df_c['Date_'].str.split('-',).str[2]
    #derived column
    df_c.loc[df_c['Gld_Close']>2500, 'Price_Category']='High'
    df_c.loc[(df_c['Gld_Close']<2500) & (df_c['Gld_Close']>1200), 'Price_Category']='Mid'
    print(df_c[df_c['Price_Category']=='Mid'])

csv_prac()