import os
import pandas as pd


cc = pd.read_csv("../Analyse-repositories/Analyzed-files/cc-radon.csv")
raw = pd.read_csv("../Analyse-repositories/Analyzed-files/raw-radon.csv")
cc = cc[['Repository', 'block_type']]


df = pd.merge(cc, raw, on='Repository', how='inner')
#df = pd.merge(df, multimetric, on='Repository', how='inner')
df = df.drop('Unnamed: 0', axis=1)
total_analyzed_repositories = df['Repository'].unique()


large_class = df[(df.LOC >= 200) & (df.block_type == 'C')]
total_repositories_large_class = large_class['Repository'].unique()
print(len(total_repositories_large_class)) # Foram encontrados em 133 repositórios
large_class=large_class.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Large-Class').reset_index() # Conta o número de ocorências de long class em dado repositório
sum_large_class = int(large_class['Quantity-Large-Class'].sum())


long_method = df[(df.LOC >= 100) & (df.block_type == 'M')]
total_repositories_long_method = long_method['Repository'].unique()
#print(len(total_repositories_long_method)) # Foram encontrados em 156 repositórios
long_method=long_method.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Long-Method').reset_index() # Conta o número de ocorências de long_method em dado repositório
sum_long_method = int(long_method['Quantity-Long-Method'].sum())

df['Total_Comments'] = df['Comments'] + df['Single Comments'] + df['Multi']
df['Total_Comments_LOC'] = df['Total_Comments'] / df['LOC']
df['Percentage_LOC'] = df['LOC']/100

comments = df[df.Total_Comments_LOC >= df.Percentage_LOC]
total_repositories_comments = comments['Repository'].unique()
comments=comments.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Comments').reset_index() # Conta o número de ocorências de long_method em dado repositório
sum_comments = int(comments['Quantity-Comments'].sum())

COLUMNS=['Smell Type',
          'Total Occurrences']

df_smells = pd.DataFrame(columns=COLUMNS)
new_row = {'Smell Type': 'Large Class', 'Total Occurrences': int(sum_large_class)}
df_smells = df_smells.append(new_row ,ignore_index=True)
new_row2 = {'Smell Type': 'Long Method', 'Total Occurrences': int(sum_long_method)}
df_smells =  df_smells.append(new_row2 ,ignore_index=True)
new_row3 = {'Smell Type': 'Comments', 'Total Occurrences': int(sum_comments)}
df_smells = df_smells.append(new_row3 ,ignore_index=True)
df_smells.to_csv('./Answers/smell_ocurrences.csv')