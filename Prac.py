import os 
import numpy as np  
import pandas as pd 
import requests
import csv 
import re 
import json

FOUT = 'CPI_Out.csv'
FIN = 'CPI_Test.csv'

def rd_fl():
    #create dataframe from CSV 
    cpi =pd.read_csv('CPI_Test.csv')
    df = pd.DataFrame(data=cpi)
    df['YR'] = (df['Date'][0:4])
    #print(df.sort_values(by='YR' , ascending=True))
    #.loc to slice multipe rows and columns
    print(df.loc[1:33,['Series ID', 'Date']])
    df_agg = df.groupby('Series ID').agg({'Annual_Per'
                                          :['max', 'sum'], 'Value': ['min', 'sum']})
    print(df_agg.info())
    print(df.groupby(['Series ID']).agg({'Annual_Per': 'max'}))
    
def df_agg():
    dt = pd.read_csv(FIN)
    df = pd.DataFrame(dt)
    print(df.loc[1:22,['Date', 'Series ID']])
    df_agg = df.groupby('Series ID').agg({'Value' :'min'})
    print(df_agg)
    df_g =df[df['Series ID']=='CUSR0000SETB01']
    print(df_g)
def rd_csv():
    lst = []
    with open(FIN, 'r')as f:
        for row in f:
            #print(row.strip())
            lst.append(row.strip())
        i=0
        for x in lst:
            print(x.strip(','))
    
df_agg()