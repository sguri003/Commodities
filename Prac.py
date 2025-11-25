import os 
import numpy as np  
import pandas as pd 
import requests
import csv 
import re 
import json
from datetime import datetime

FOUT = 'CPI_Out.csv'
FIN = 'CPI_Test.csv'

def rd_fl():
    #create dataframe from CSV 
    cpi =pd.read_csv('CPI_Test.csv')
    df = pd.DataFrame(data=cpi)
    df['YR'] = (df['Date'][0:4])
    #print(df.sort_values(by='YR' , ascending=True))
    #.loc to slice multipe rows and columns
    print(df.loc[1:33   ,['Series ID', 'Date']])
    df_agg = df.groupby('Series ID').agg({'Annual_Per'
                                          :['max', 'sum'], 'Value': ['min', 'sum']})
    print(df_agg.info())
    print(df.groupby(['Series ID']).agg({'Annual_Per': 'max'}))
    
def df_agg():
    dt = pd.read_csv(FIN)
    df = pd.DataFrame(dt)
    print(df.loc[1:22,['Date', 'Series ID']])
    df_agg = df.groupby('Series ID').agg({'Value' :'min'})
    print(df.loc[1:20,['Series ID', 'Date']])
    #print(df_agg)
    #get all gas/fuel index
    df_g =df[df['Series ID']=='CUSR0000SETB01']
    print(df_g)
    
    
def rd_csv():
    lst = []
    wrtr = open(FOUT, 'w')
    with open(FIN, 'r')as f:
        rd = csv.reader(f)
        for row in rd:
            if row[1].endswith('B01'): 
                lst.append(row)
    wtr = csv.writer(wrtr, lineterminator='\n')
    for x in lst:
        print(x)
        wtr.writerow(x)
        
    
    wrtr.close()


def pr():
    dt = pd.read_csv('CPI_Test.csv')
    df = pd.DataFrame(data=dt)
    df['Yr'] = df['Date'].str[0:4]
    df['Yr']= df['Yr'].astype(int)
    print(df.info())
    df.loc[(df['Yr']>=2020), 'Time_Period']='Covid'
    df.loc[(df['Yr']<2020), 'Time_Period']='Pre-Covid'
    print(df)
    my_d = {}
    my_d = df.to_dict(orient='records')
    print(my_d)
    for idx, row in enumerate(my_d):
        if idx==2:
            break
        print(row)
def rd():
    fout = open('Test_Out.csv', 'w')
    fin = 'CPI_Test.csv'
    lst = []
    wtr = csv.writer(fout, lineterminator='\n')
    with open(fin,'r')as f:
        rdr = csv.DictReader(f=f, lineterminator='\n')
        series = {ky: ky for ky in rdr.fieldnames}
        print(series)
        #print(rdr.fieldnames)
        for row in rdr:
            if row['Series ID']=='CUSR0000SA0':
                row['Date'] = datetime.strptime(row['Date'], '%Y-%m-%d')
                yr = row['Date'].year
                lst.append(row)
                wtr.writerow([row['Series ID'], row['Date'], row['YoY'], yr])
                #print('The {series} has Year over Year of: {yoy}'.format(series=row['Series ID'], yoy=row['YoY']))
    fout.close()

    
    
rd()