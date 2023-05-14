import os
import pandas as pd


cc = pd.read_csv("../Analyse-repositories/Analyzed-files/cc-radon.csv")
raw = pd.read_csv("../Analyse-repositories/Analyzed-files/raw-radon.csv")
cc = cc[['Repository', 'block_type']]
multimetric = pd.read_csv("../Analyse-repositories/Analyzed-files/multimetric.csv")


df = pd.merge(cc, raw, on='Repository', how='inner')
#df = pd.merge(df, multimetric, on='Repository', how='inner')
df = df.drop('Unnamed: 0', axis=1)
total_analyzed_repositories = df['Repository'].unique()


large_class = df[(df.LOC >= 200) & (df.block_type == 'C')]
total_repositories_large_class = large_class['Repository'].unique()
#print(len(total_repositories_large_class)) # Foram encontrados em 133 repositórios
large_class=large_class.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Large-Class').reset_index() # Conta o número de ocorências de long class em dado repositório
sum_large_class = int(large_class['Quantity-Large-Class'].sum())

large_class_repositories = large_class['Repository'].unique()
df_multimetric = multimetric[multimetric['Repository'].isin(large_class_repositories)] # Get the metrics of the repositories with large class

df_without_Large_Class =df[~df.loc[:,'Repository'].isin(df_multimetric['Repository'])]
without_large_class_repositories = df_without_Large_Class['Repository'].unique()
df_without_Large_Class = multimetric[multimetric['Repository'].isin(without_large_class_repositories)]



df['Total_Comments'] = df['Comments'] + df['Single Comments'] + df['Multi']
df['Total_Comments_LOC'] = df['Total_Comments'] / df['LOC']
df['Percentage_LOC'] = df['LOC']/100

comments = df[df.Total_Comments_LOC >= df.Percentage_LOC]
total_repositories_comments = comments['Repository'].unique()
comments=comments.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Comments').reset_index() # Conta o número de ocorências de long_method em dado repositório
sum_comments = int(comments['Quantity-Comments'].sum())

files = df_multimetric['Repository'].unique()
comment_ratio = df_multimetric['comment_ratio'].sum()
cyclomatic_complexity = df_multimetric['cyclomatic_complexity'].sum()
fanout_external = df_multimetric['fanout_external'].sum()
fanout_internal = df_multimetric['fanout_internal'].sum()
halstead_bugprop = df_multimetric['halstead_bugprop'].sum()
halstead_difficulty = df_multimetric['halstead_difficulty'].sum()
halstead_effort = df_multimetric['halstead_effort'].sum()
halstead_timerequired = df_multimetric['halstead_timerequired'].sum()
halstead_volume = df_multimetric['halstead_volume'].sum()

COLUMNS= ['Type',
    'Total_Repositories',
    'comment_ratio',
    'cyclomatic_complexity',
    'fanout_external',
    'fanout_internal',
    'halstead_bugprop',
    'halstead_difficulty',
    'halstead_effort',
    'halstead_timerequired',
    'halstead_volume']

metrics_Large_Class = pd.DataFrame(columns=COLUMNS
    )

new_row = {'Type': 'Large_Class_smell_metrics','Total_Repositories': len(files),'Total_Large_Class':sum_large_class,'comment_ratio': int(comment_ratio), 'cyclomatic_complexity': int(cyclomatic_complexity), 'fanout_external': int(fanout_external),
           'fanout_internal':  int(fanout_internal), 'halstead_bugprop':int(halstead_bugprop), 'halstead_effort' : int(halstead_effort), 'halstead_difficulty': int(halstead_difficulty),'halstead_timerequired': int(halstead_timerequired),'halstead_volume': int(halstead_volume)}
metrics_Large_Class = metrics_Large_Class.append(new_row, ignore_index=True)

comment_ratio = df_without_Large_Class['comment_ratio'].sum()
cyclomatic_complexity = df_without_Large_Class['cyclomatic_complexity'].sum()
fanout_external = df_without_Large_Class['fanout_external'].sum()
fanout_internal = df_without_Large_Class['fanout_internal'].sum()
halstead_bugprop = df_without_Large_Class['halstead_bugprop'].sum()
halstead_difficulty = df_without_Large_Class['halstead_difficulty'].sum()
halstead_effort = df_without_Large_Class['halstead_effort'].sum()
halstead_timerequired = df_without_Large_Class['halstead_timerequired'].sum()
halstead_volume = df_without_Large_Class['halstead_volume'].sum()

new_row2 = {'Type': 'Without_Large_Class_metrics','Total_Repositories': len(without_large_class_repositories),'comment_ratio': int(comment_ratio), 'cyclomatic_complexity': int(cyclomatic_complexity), 'fanout_external': int(fanout_external),
           'fanout_internal':  int(fanout_internal), 'halstead_bugprop':int(halstead_bugprop), 'halstead_effort' : int(halstead_effort), 'halstead_difficulty': int(halstead_difficulty),'halstead_timerequired': int(halstead_timerequired),'halstead_volume': int(halstead_volume)}
metrics_Large_Class = metrics_Large_Class.append(new_row2, ignore_index=True)

metrics_Large_Class.to_csv("../Questions/Answers/metrics_Large_Class.csv")

