import csv

import pandas
import pandas as pd
import numpy as np

df_AD = pd.read_csv('./repositories-autonomous-driving.csv')
df_AV= pd.read_csv('./repositories-autonomous-vehicles.csv')
df_SDC= pd.read_csv('./repositories-self-driving-cars.csv')

concatenated_df = pandas.concat([df_AV, df_AD,df_SDC])
print(concatenated_df.columns)



concatenated_df = concatenated_df.drop_duplicates(subset='Url', keep='first')
concatenated_df['Index'] = range(1, len(concatenated_df) + 1)
concatenated_df = concatenated_df.set_index('Index')
#concatenated_df.pop(concatenated_df.columns.values[0])
print(concatenated_df.shape)
respositories_with_releases = pd.DataFrame()
respositories_without_releases = pd.DataFrame()

respositories_without_releases =  concatenated_df[concatenated_df['Num_of_Releases']==0]
respositories_with_releases = concatenated_df[concatenated_df['Num_of_Releases']>=1]

respositories_without_releases['Index'] = range(1, len(respositories_without_releases) + 1)
respositories_without_releases = respositories_without_releases.set_index('Index')

respositories_with_releases['Index'] = range(1, len(respositories_with_releases) + 1)
respositories_with_releases = respositories_with_releases.set_index('Index')

respositories_without_releases.to_csv("./repositories_with_0_releases.csv")
respositories_with_releases.to_csv("./repositories_with_releases")

print(respositories_with_releases.shape)
print(respositories_without_releases.shape)
print(concatenated_df.columns)


concatenated_df.to_csv("./concatenated_repositories.csv")
print(concatenated_df.shape)
