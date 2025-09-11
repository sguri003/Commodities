import os
import sqlalchemy as sq
import urllib.parse
import pandas as pd            
import numpy as np    
import datetime
import re
from DB_Main import DB_Main

#Calls Parent class
#Uses super() to query. 

class Labor(DB_Main):
    #static variable
   
    def __init__(self):
        super().__init__()
    
    
    def qry_df(self):
        super().qry_df()
        

cpi = Labor()
cpi.qry_df()


