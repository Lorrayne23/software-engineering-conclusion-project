import csv
import os
import pandas
import pandas as pd
import numpy as np
import git
import shutil

location = os.getcwd() # This will return the Current Working Directory
file_path = 'concatenated_repositories.csv' # csv location
file_path = location.replace("Repositories",file_path) # Path to csv
path_to_cloned_respositories = os.getcwd() + "/Cloned-repositories"
print(path_to_cloned_respositories)
print(file_path)

#Instrumentos/Codigos/Collect-repositories/concatenated_repositories.csv


df = pd.read_csv(file_path)

df.sort_values("Url", inplace=True)

# dropping ALL duplicate values
df.drop_duplicates(subset="Url",
                     keep=False, inplace=True)

df.sort_values("Name", inplace=True)

# dropping ALL duplicate values
df.drop_duplicates(subset="Name",
                     keep=False, inplace=True)

repositories = df['Url'][0:100]
repositories = df['Url'][101:200]
repositories = df['Url'][201:300]
repositories = df['Url'][301:400]
repositories = df['Url'][401:500]
repositories = df['Url'][501:600]
repositories = df['Url'][601:700]
repositories = df['Url'][701:800]
repositories = df['Url'][801:900]
repositories = df['Url'][901:1000]



for i in repositories:
 #git.Git(path_to_dulicated_respositories).clone(i)







