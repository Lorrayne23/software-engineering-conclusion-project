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


long_method = df[(df.LOC >= 100) & (df.block_type == 'M')]
total_repositories_long_method = long_method['Repository'].unique()
#print(len(total_repositories_long_method)) # Foram encontrados em 156 repositórios
long_method=long_method.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Long-Method').reset_index() # Conta o número de ocorências de long_method em dado repositório
sum_long_method = int(long_method['Quantity-Long-Method'].sum())


long_method_repositories = long_method['Repository'].unique()
df_multimetric = multimetric[multimetric['Repository'].isin(long_method_repositories)] # Get the metrics of the repositories with long method

df_without_Long_Method =df[~df.loc[:,'Repository'].isin(df_multimetric['Repository'])]
without_long_method_repositories = df_without_Long_Method['Repository'].unique()
df_without_Long_Method = multimetric[multimetric['Repository'].isin(without_long_method_repositories)]


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

new_row = {'Type': 'Long_Method_smell_metrics','Total_Repositories': len(files),'comment_ratio': int(comment_ratio), 'cyclomatic_complexity': int(cyclomatic_complexity), 'fanout_external': int(fanout_external),
           'fanout_internal':  int(fanout_internal), 'halstead_bugprop':int(halstead_bugprop), 'halstead_effort' : int(halstead_effort), 'halstead_difficulty': int(halstead_difficulty),'halstead_timerequired': int(halstead_timerequired),'halstead_volume': int(halstead_volume)}
metrics_Large_Class = metrics_Large_Class.append(new_row, ignore_index=True)

comment_ratio = df_without_Long_Method['comment_ratio'].sum()
cyclomatic_complexity = df_without_Long_Method['cyclomatic_complexity'].sum()
fanout_external = df_without_Long_Method['fanout_external'].sum()
fanout_internal = df_without_Long_Method['fanout_internal'].sum()
halstead_bugprop = df_without_Long_Method['halstead_bugprop'].sum()
halstead_difficulty = df_without_Long_Method['halstead_difficulty'].sum()
halstead_effort = df_without_Long_Method['halstead_effort'].sum()
halstead_timerequired = df_without_Long_Method['halstead_timerequired'].sum()
halstead_volume = df_without_Long_Method['halstead_volume'].sum()

new_row2 = {'Type': 'Without_Long_Method_metrics','Total_Repositories': len(without_long_method_repositories),'comment_ratio': int(comment_ratio), 'cyclomatic_complexity': int(cyclomatic_complexity), 'fanout_external': int(fanout_external),
           'fanout_internal':  int(fanout_internal), 'halstead_bugprop':int(halstead_bugprop), 'halstead_effort' : int(halstead_effort), 'halstead_difficulty': int(halstead_difficulty),'halstead_timerequired': int(halstead_timerequired),'halstead_volume': int(halstead_volume)}
metrics_Large_Class = metrics_Large_Class.append(new_row2, ignore_index=True)

metrics_Large_Class.to_csv("../Questions/Answers/metrics_Long_Method.csv")