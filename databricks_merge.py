import yfinance as yf
import pandas as pd
from delta.tables import DeltaTable
from pyspark.sql.functions import year, to_date, try_to_date 
#create merge

#begin to download new data
ticker_lst =['GC=F','SI=F']
dt = yf.download(ticker_lst, start='2022-01-01', group_by='ticker')
#Download historical data for the last year
df = pd.DataFrame(dt)
df_f = df.reset_index()
df_f.head(10)
df_f.columns =  ['_'.join(col).strip() for col in df_f.columns.values]
df_f.columns = ["".join(col).replace('=','_') for col in df_f.columns.values]
df_f["Date_"] = pd.to_datetime(df_f["Date_"], format="%Y-%m-%d")
df_f.head(10)
#read delta table forName with spark session
df_current = DeltaTable.forName(spark, "futures.adf_run_2")
#merge Delta table with new data
df_upsert = df_current.alias("current").merge(spark.createDataFrame(df_f).alias("new"),"current.Date_=new.Date_").whenMatchedUpdate(
    set = { "SI_F_Close": "new.SI_F_Close","GC_F_Close": "new.GC_F_Close", "Date_": "new.Date_", "SI_F_Open": "new.SI_F_Open",
            "SI_F_High": "new.SI_F_High", "SI_F_Low": "new.SI_F_Low", "SI_F_Volume": "new.SI_F_Volume",
             "GC_F_Open": "new.GC_F_Open", "GC_F_High": "new.GC_F_High",  "GC_F_Low": "new.GC_F_Low", "GC_F_Volume": "new.GC_F_Volume"}
    ).whenNotMatchedInsertAll().execute()
df_upsert.write.mode("append").format("delta").option("mergeSchema", "true").saveAsTable("futures.adf_run_2")


#  df = spark.read \
#        .format("sqlanalytics") \
#        .option("fabricWarehouse", "<Warehouse_Name>") \
#        .option("table", "<Table_or_View_Name>") \
#        .load()

# Define the three-part naming convention for your table/view
# Format: <LakehouseName>.<SchemaName>.<TableNameOrViewName>
#table_identifier = "YourLakehouseName.dbo.YourTableName"
# Read data from the SQL Analytics Endpoint into a Spark DataFrame
#df = spark.read.synapsesql(table_identifier)
