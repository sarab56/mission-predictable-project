import pandas as pd 
data=pd.read_csv("dataset.csv")
country_wise=data.groupby("Country_Region").sum()