         
# Name:     run_get_bls_data.py
# Date:     2025-06-20
# Author:   STEVEN M. GURIDI
#
# Description:
# Use the c_bls_data class to obtain series of data
# from the US Bureau of Labor Statistics (BLS) API.
import csv
import numpy as np
import pandas as pd
import BLS_CPI

# @params API Key, Export_File, Series ID, start year, and year
# CUSR0000SA0 - All items in U.S. city average, all urban consumers, seasonally adjusted
# CUSR0000SETB01 - Gasoline (all types) in U.S. city average, all urban consumers, seasonally adjusted
# CUSR0000SAF1 - Food in U.S. city average, all urban consumers, seasonally adjusted
# CUSR0000SETA02 - Used cars and trucks in U.S. city average, all urban consumers, seasonally adjusted
df_ky = pd.read_csv('API_KEY.csv')
BLS_API_KEY = df_ky['BLS_API'][0]
#OUTPUT DEFLATOR ID: IPUCN2211__T051000000, REAL SECTOR OUTPUT ID: IPUCN2211__T011000000
#bls_dt = labor_US(BLS_API_KEY, 'POWER DELIVER SG.CSV' , ['IPUCN2211__T051000000', 'IPUCN2211__T011000000'], 2000, 2022 )
#CPI for Gas, Groceries, necessities. 
#CPI-->CUSR0000SA0 ALL URBAN AREAS
cpi = BLS_CPI(BLS_API_KEY, 'CPI_2011-MTD.csv',
                        ['CUSR0000SA0', 'CUSR0000SETB01', 'CUSR0000SAF1', 'CUSR0000SETA02']
                        , 2011, 2025)
#pd = BLS(BLS_API_KEY, 'POWER_OUTPUT_2015-MTD.csv'
#                                ,['IPUCN2211__T051000000', 'IPUCN2211__T011000000']
#                                , 2015, 2025 )
