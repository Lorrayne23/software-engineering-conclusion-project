import os
import pathlib
import subprocess
import  glob
import shutil
import pandas as pd

location = os.getcwd() # This will return the Current Working Directory
file = './Collect-repositories/Repositories/Cloned-repositories/' # file location of cloned repositories
file_path = location.replace("Analyse-repositories",file) # Path to file'''


files_py = [f for f in glob.glob(file_path + "**/*.py", recursive=True)] # Search for all python files in the path

for file in files_py:
    f = open(str(file)+"flake8-output.txt", "w") # Define txt with the name of the xxx.py file
    subprocess.run(["flake8", file], stdout=f) # Run library flake8 in the file xxx.py file

for file in files_py:
    m = open(str(file)+"multimetric-output.txt", "w") # Define txt with the name of the xxx.py file
    subprocess.run(["multimetric", file], stdout=m) # Run library multimetric in the file xxx.py file



files = [f for f in glob.glob(file_path + "**/*.txt", recursive=True)] # Get all the txt files generated



path_salve_file_flake8 = os.getcwd()
path_salve_file_flake8 = path_salve_file_flake8.replace("Analyse-repositories","Analyse-repositories/flake8") # Define the path to save flake8 txt's
for file in files:
    if file[-17:] == 'flake8-output.txt':
        shutil.copy(file,path_salve_file_flake8)



path_salve_file_multimetric = os.getcwd()
path_salve_file_multimetric = path_salve_file_multimetric.replace("Analyse-repositories","Analyse-repositories/multimetric/") # Define the path to save multimetric txt's
for file in files:
   if file[-22:] == 'multimetric-output.txt':
        shutil.copy(file,path_salve_file_multimetric)



path_salve_file_radon = os.getcwd()
path_salve_file_radon = path_salve_file_radon.replace("Analyse-repositories","Analyse-repositories/radon/") # Define the path to save radon txt's
radon_command = ["hal","mi","raw","cc"]

for command in radon_command:
    r = open(str(command)+"-radon-output.txt", "w")
    subprocess.run(["radon",str(command), str(file_path)], stdout=r)

for archive in os.listdir(os.getcwd()):
    for command in radon_command:
        if archive.startswith(command):
            shutil.move(archive,path_salve_file_radon)



files = [f for f in glob.glob(file_path + "**/*output.txt", recursive=True)] # Get all the txt files generated

for file in files:
    os.remove(file)

path_salve_file_smelly_python = os.getcwd()
path = 'Collect-repositories/Repositories/' # file location of cloned repositories
file_path = path_salve_file_smelly_python.replace("Analyse-repositories",path) # Path to file

#subprocess.run("ls")

wd = os.getcwd()
os.chdir(file_path)
print(os.getcwd())




subprocess.run(["smelly-python","-d","Cloned-repositories"])
#shutil.move(os.getcwd())

for file in os.listdir():
    if file == 'report':
        path_salve_file_ = os.getcwd()
        file_path = path_salve_file_smelly_python.replace("Collect-repositories/Repositories/","Analyse-repositories/")  # Path to file
        shutil.move(file,file_path)




