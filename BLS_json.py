import json  
import numpy as np 
import pandas as pd 
import os 
import csv

def js():
    with open('out_dict.json','r') as js:
        orign_data = json.load(js)
        
    with open('BLS_OG.json', 'w')as fpl:
        json.dump(orign_data, fp=fpl, indent=4)
        
def rd_fl():
    f_out = open('test.csv', 'w') 
    with open('CPI_Data_ML.csv')as f:
        header = next(f)
        reader = csv.DictReader(f, fieldnames=header)
        for row in reader:
            print(row)

rd_fl()

    