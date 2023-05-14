import os
import pandas as pd


cc = pd.read_csv("../Analyse-repositories/Analyzed-files/cc-radon.csv")
raw = pd.read_csv("../Analyse-repositories/Analyzed-files/raw-radon.csv")
multimetric = pd.read_csv("../Analyse-repositories/Analyzed-files/multimetric.csv")
cc = cc[['Repository', 'block_type']]
df_releases = pd.read_csv("../Collect-repositories/repositories_with_relases.csv")


df = pd.merge(cc, raw, on='Repository', how='inner')
#df = pd.merge(df, multimetric, on='Repository', how='inner')
df = df.drop('Unnamed: 0', axis=1)
total_analyzed_repositories = df['Repository'].unique()



repositories_releases = df_releases['Name']
df_filter_releases = df[df['Repository'].isin(repositories_releases)] # Get the repositories of 0 releases are in the collect repositories

print(df_filter_releases)
large_class = df_filter_releases[(df_filter_releases.LOC >= 200) & (df_filter_releases.block_type == 'C')]
total_repositories_large_class = large_class['Repository'].unique()
print(len(total_repositories_large_class)) # Foram encontrados em 133 repositórios
large_class=large_class.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Large-Class').reset_index() # Conta o número de ocorências de long class em dado repositório
sum_large_class = int(large_class['Quantity-Large-Class'].sum())


long_method = df_filter_releases[(df_filter_releases.LOC >= 100) & (df_filter_releases.block_type == 'M')]
total_repositories_long_method = long_method['Repository'].unique()
#print(len(total_repositories_long_method)) # Foram encontrados em 156 repositórios
long_method=long_method.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Long-Method').reset_index() # Conta o número de ocorências de long_method em dado repositório
sum_long_method = int(long_method['Quantity-Long-Method'].sum())

df_filter_releases['Total_Comments'] = df_filter_releases['Comments'] + df_filter_releases['Single Comments'] + df_filter_releases['Multi']
df_filter_releases['Total_Comments_LOC'] = df_filter_releases ['Total_Comments'] / df_filter_releases['LOC']
df_filter_releases['Percentage_LOC'] = df_filter_releases['LOC']/100

comments = df_filter_releases[df_filter_releases.Total_Comments_LOC >= df_filter_releases.Percentage_LOC]
total_repositories_comments = comments['Repository'].unique()
comments=comments.groupby(["Repository", "block_type"])["Repository"].count().rename('Quantity-Comments').reset_index() # Conta o número de ocorências de long_method em dado repositório
sum_comments = int(comments['Quantity-Comments'].sum())

repositories_releases_multimetric = df_filter_releases['Repository']
df_filter_releases = multimetric[multimetric['Repository'].isin(repositories_releases_multimetric)]
df_filter_releases= df_filter_releases.drop('Unnamed: 0', axis=1)
print(len(df_filter_releases))

files = df_filter_releases['Repository'].unique()
comment_ratio = df_filter_releases['comment_ratio'].sum()
cyclomatic_complexity = df_filter_releases['cyclomatic_complexity'].sum()
fanout_external = df_filter_releases['fanout_external'].sum()
fanout_internal = df_filter_releases['fanout_internal'].sum()
halstead_bugprop = df_filter_releases['halstead_bugprop'].sum()
halstead_difficulty = df_filter_releases['halstead_difficulty'].sum()
halstead_effort = df_filter_releases['halstead_effort'].sum()
halstead_timerequired = df_filter_releases['halstead_timerequired'].sum()
halstead_volume = df_filter_releases['halstead_volume'].sum()

COLUMNS= ['repositories',
    'Total_Large_Class',
    'Total_Long_Method',
    'Total_Comments',
    'comment_ratio',
    'cyclomatic_complexity',
    'fanout_external',
    'fanout_internal',
    'halstead_bugprop',
    'halstead_difficulty',
    'halstead_effort',
    'halstead_timerequired',
    'halstead_volume']

multimetric_releaes = pd.DataFrame(columns=COLUMNS
    )

new_row = {'repositories': 'repositories_with_releases','Total_Long_Method': sum_long_method,'Total_Large_Class':sum_large_class,'Total_Comments': sum_comments,'comment_ratio': int(comment_ratio), 'cyclomatic_complexity': int(cyclomatic_complexity), 'fanout_external': int(fanout_external),
           'fanout_internal':  int(fanout_internal), 'halstead_bugprop':int(halstead_bugprop), 'halstead_effort' : int(halstead_effort), 'halstead_difficulty': int(halstead_difficulty),'halstead_timerequired': int(halstead_timerequired),'halstead_volume': int(halstead_volume)}
multimetric_0_releaes = multimetric_releaes.append(new_row, ignore_index=True)

multimetric_0_releaes.to_csv("../Questions/Answers/metrics_releases.csv")