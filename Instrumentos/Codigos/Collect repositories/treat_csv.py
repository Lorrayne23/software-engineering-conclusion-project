import csv

import pandas
import pandas as pd

df_AD = pd.read_csv('./repositories-autonomous-driving.csv')
df_AV= pd.read_csv('./repositories-autonomous-vehicles.csv')
df_SDC= pd.read_csv('./repositories-self-driving-cars.csv')


concatenated_df = pandas.concat([df_AV, df_AD,df_SDC],ignore_index=True)
concatenated_df.pop(concatenated_df.columns.values[0])
print(concatenated_df.columns)
print(concatenated_df.shape)
concatenated_df = concatenated_df.drop_duplicates(subset='Url', keep='first')
print(concatenated_df.shape)
concatenated_df.to_csv("./concatenated_repositories.csv")