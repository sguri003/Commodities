import os 
import numpy as np  
import pandas as pd 
import requests
import csv 
import re 
import json

def rd_fl():
    dt = pd.read_csv('CPI_Test.csv')
    df = pd.DataFrame(data=dt)
    print(df.info())
    print(df.head(10))