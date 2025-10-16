# DATA: 2025-06-21
# NOTES: Retrieving Data from BLS to understand key labor sectors. 
# To use this LABOR_US class, each use must provide their own BLS API Version 2
# registration key from here: https://data.bls.gov/registrationEngine/

#NOTE: OPEN SOURCE PROJECT @https://github.com/sguri003/Labor_Stats_Dev

# To use the c_bls_data class, create an instance with below parameter in constructor:
import os 
import json
import csv
import requests
import numpy as np                
import pandas as pd  
import sqlalchemy as sq
             
#new comming
class BLS_CPI:
    #CONSTRUCTOR APsI KEY, OUTPUT FILE, START AND END YEAR
    def __init__(self, reg_key, out_file_nm, series_id, start_year, end_year):        # Set the file name variable and create the parameters for the API request.
        #instance variables of CPI_Puller classs
        self.out_file_nm = out_file_nm
        headers = {'Content-type': 'application/json'}
        parameters = json.dumps({'seriesid' : series_id, 'startyear' : start_year, 'endyear' : end_year, 'calculations' : True , 'registrationkey' : reg_key})
        # Get data in JSON format and then write it to a CSV file.
        json_data = self.get_cpi(headers, parameters)
        with open('CPI_QA.json' , 'w') as qa:
            json.dump(json_data, fp=qa, indent=4)
        df = self.data_to_csv(json_data)
        self.insert_sql(df=df)
        
    #retrive cpi data from BLS AP
    def get_cpi(self, headers, parameters):
        #Fire Post to end point BLS Grab Json
        post = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data = parameters, headers = headers)
        json_data = json.loads(post.text)
        return json_data

    def data_to_csv(self, json_data):
        # Convert the data from JSON format to CSV records. Write
        # each record to the specified output file.
        if os.path.exists(self.out_file_nm):
            os.remove(self.out_file_nm)
            print(f"File '{self.out_file_nm}' deleted successfully.")
        else:
            print(f"File '{self.out_file_nm}' does not exist.")    
        #open file to be written to CSV. 
        with open(self.out_file_nm, mode = 'w', newline = '') as data_file:
            #Series ID is category such as Gasoline, Groceries. 
            fieldnames = ['Series ID', 'Date', 'Value', 'Annual_Per','Monhtly' ,'3_Months', 'Half-Year', 'Yoy %']
            d_wrtr = csv.writer(data_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            #Place Headers
            d_wrtr.writerow(fieldnames)
            # Write each record to the output file.
            for series in json_data['Results']['series']:
                series_id = series['seriesID']
                for item in series['data']:
                    # Get the basic data
                    year = item['year']
                    period_name = item['periodName']
                    value = item['value']
                    # Get the 12-month change
                    calculations = item['calculations']
                    pct_changes = calculations['pct_changes']
                    #get the 12th month in the JSON:
                    annual_pct_chg = pct_changes['12']
                    mnthly = pct_changes['1']
                    mth_3 = pct_changes['3']
                    half_yr = pct_changes['6']
                    yoy = pct_changes['12']
                    # Create a month field in the format of a date for 
                    # the first day of each month (for example: January 1, 2022).
                    month = period_name + ' 1 ' + year
                    #Write the CSV record to the output file.
                    d_wrtr.writerow([series_id, month, value,annual_pct_chg  
                                 ,mnthly,mth_3,half_yr, yoy])
        #place in dataframe format from
        dt = pd.read_csv(self.out_file_nm)
        df_cpi = pd.DataFrame(data=dt)
        df_cpi['Date'] = pd.to_datetime(dt['Date'], format="mixed")
        df_cpi.to_csv("CPI_Data_ML.csv")
        print(df_cpi)
        return df_cpi

    def insert_sql(self, df:pd.DataFrame):
        SERVER= "DESKTOP-03RVSDU\SQLEXPRESS"
        DB_NAME = "Labor_Stats"
        conn_str = f"mssql+pyodbc://{SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = sq.create_engine(conn_str)
        #cast to date yyyy-mm-dd
        cnx = engine.connect()
        df.to_sql(name='BLS_Test_Run', schema='dbo'
            , con=cnx, if_exists='replace', index=False,index_label=False)
        cnx.close()
        
        
        
df_ky = pd.read_csv('src/API_KEY.csv')
BLS_API_KEY = df_ky['BLS_API'][0]         
#CPI_Data = CPI_BLS(BLS_API_KEY, 'CPI_QA.csv',
#                       ['CUSR0000SETB01', 'CUSR0000SAF1', 'CUSR0000SETA02']
#                         ,2010, 2025)
CPI_Data = BLS_CPI(BLS_API_KEY, 'CPI.csv',
                        ['CUSR0000SA0','CUSR0000SETB01', 'CUSR0000SAF1', 'CUSR0000SETA02']
                         ,2010, 2025)