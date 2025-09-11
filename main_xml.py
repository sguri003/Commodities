import numpy as np 
import pandas as pd 
from xml_parser import xml_parser

def main():
    cpi_xml = xml_parser('CPI_Data.xml')
    dict_list = cpi_xml.parse_tree()
    cpi_xml.insert_sql(dict_list)
    #print(dict_list)
    #gas_lst = cpi_xml.gas_only('gas',dict_list)
    #cpi_xml.add_col(gas_lst)   
    #print(gas_lst)
    #df_gas = pd.DataFrame(data=gas_lst)
    #df_gas.to_csv('CPI_Data_exprt.csv')
    
    #cpi_xml.df_lst(dict_list)   

if __name__=="__main__":
    main()