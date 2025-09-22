import os 
import numpy as np   
import pandas as pd 
import scipy 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import csv  
import sqlalchemy

df = pd.read_csv('CPI_Data_ML.csv')
df_cpi = pd.DataFrame(data=df)
#y==The next CPI index
#x silver price
df_gld = pd.read_csv('Silver_Price.csv')
gld_df = np.array(df_gld['Gld_Close'])
X = gld_df
print(X)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create and Train the Model
#model = LinearRegression()
#model.fit(X_train, y_train)