import csv
import os
import pandas
import pandas as pd
import numpy as np
import git

location = os.getcwd() # This will return the Current Working Directory
file_path = 'concatenated_repositories.csv' # csv location
file_path = location.replace("Repositories",file_path) # Path to csv
path_to_cloned_respositories = os.getcwd() + "/Cloned-repositories"
print(path_to_cloned_respositories)
print(file_path)

#Instrumentos/Codigos/Collect-repositories/concatenated_repositories.csv


df = pd.read_csv(file_path)
head_url = df['Url'].head(10)


for i in head_url:
    git.Git(path_to_cloned_respositories).clone(i)
