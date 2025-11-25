import json  
import numpy as np 
import pandas as pd 
import os 
import csv

def delta_json_format():
    with open('Delta_log_2.json', 'r')as d_in:
        dt = json.load(d_in)
    with open('delta_log_11-23.json', 'w') as d_format:
        json.dump(d_format, indent=4)

def js():
    with open('CPI_QA.json', 'r')as f:
        dt = json.load(f)
        print(dt)
    with open('CPI_OUT.json', 'w') as f1:
        json.dump(dt, f1,indent=4)
    
def rd_fl():
    f_out = open('test.csv', 'w') 
    with open('CPI_Data_ML.csv')as f:
        header = next(f)
        reader = csv.DictReader(f, fieldnames=header)
        for row in reader:
            print(row)

def rd():
    fout = open('CPI_OUT.csv', 'w')
    wtr = csv.writer(fout, lineterminator='\n')
    lst = []
    with open('CPI_Data_ML.csv', 'r') as f:
        for i, row in enumerate(f):
            row.split(',')[1]
            wtr.writerow([row.split(',')[1],row.split(',')[2]])
        fout.close()
            
            

#rd()
delta_json_format()   