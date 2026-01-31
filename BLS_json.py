import json  
import numpy as np 
import pandas as pd 
import os 
import csv
import azure.storage.blob
from azure.storage.blob import BlobServiceClient, ContainerClient


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

def read_blob():
    blob_path = "abfss://bronze@greedysotre.dfs.core.windows.net/"
    blob_token = "sp=rcw&st=2025-11-30T14:42:15Z&se=2025-11-30T22:57:15Z&sv=2024-11-04&sr=c&sig=sENzYgcCYxggpsFBCkjxxudQCN2GXGYPJZJTjhEOweg%3D"
    blob_url= "https://greedystore.blob.core.windows.net/bronze?sp=rcw&st=2025-11-30T14:42:15Z&se=2025-11-30T22:57:15Z&sv=2024-11-04&sr=c&sig=sENzYgcCYxggpsFBCkjxxudQCN2GXGYPJZJTjhEOweg%3D"
    bronze = BlobServiceClient(blob_url)
    bronze_client = bronze.get_blob_client(container='bronzze', blob='greedystore')
    print(bronze_client)


#rd()
read_blob()
#delta_json_format()   