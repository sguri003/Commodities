import os 
import numpy as np   
import pandas as pd 
from sklearn.tree import plot_tree
import scipy
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import csv  
import sqlalchemy

def greadient():
    df_e = pd.read_csv('ML_Vacation.csv')
    print(df_e)
    df_v  = df_e.dropna()
    df_v = df_v.drop('DOB_Yr')
    df_v = pd.DataFrame(data=df_v)
    df_v = df_v.dropna()
    column_to_encode = ['Gender', 'D_Name']
    for col in column_to_encode:
        le = LabelEncoder()
        df_v[col] = le.fit_transform(df_v[col])
    # Remove Vacation hours from the model
    X, y = df_v.drop('VacationHours', axis=1), df_v['VacationHours']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, shuffle=False)
    v_clf = GradientBoostingRegressor(criterion='squared_error', learning_rate=0.1, random_state=42)
    #fit the model
    v_clf.fit(X_train, y_train)
    for i, tree_idx in enumerate([0, 2, 24, 49]):
        plt.subplot(4, 1, i+1)
        plot_tree(v_clf.estimators_[tree_idx,0], 
                feature_names=X_train.columns,
                impurity=False,
                filled=True, 
                rounded=True,
                precision=2,
                fontsize=12)
    plt.title(f'Tree {tree_idx + 1}')

    plt.suptitle('Decision Trees from GradientBoosting', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
        #Predict Sick time
    y_pred = v_clf.predict(X_test)

    #Create dataframe with predicted values
    # Create DataFrame with actual and predicted values
    results_df = pd.DataFrame({
            'Actual': y_test,
            'Predicted': y_pred
    })
    print(results_df)
    #print root mean square error
    rmse = mean_squared_error(y_test, y_pred)
    print(f"\nModel Accuracy: {rmse:.4f}")
greadient()