import os
import subprocess
import  glob
import shutil
import subprocess
from pathlib import Path

import pandas as pd


class Treats_files:
    def __init__(self):
        self.directory = self.define_directory()

    def define_directory(self):
        path_read_files = os.getcwd()
        path = 'Codigos/Analyse-repositories'  # file location of cloned repositories
        file_path = path_read_files.replace("Codigos/Treats-analyzes", path)
        wd = os.getcwd()
        os.chdir(file_path)
        directory = os.getcwd()
        return directory

    def read_files_directory(self):
         directory = self.define_directory()
         librarys_directory = ["flake8", "multimetric","radon", "report"]
         for library in librarys_directory:
             if library == 'flake8':
                 files_flake8 = [f for f in glob.glob(directory+str("/")+library+ "**/*.txt", recursive=True)] # Get all the txt files generated
                 self.treat_files_flake8(files_flake8)
             if library == 'report':
                 file_smelly_python = [f for f in glob.glob(directory + str("/") + library+"/smelly_python" + "**/*.txt", recursive=True)]
                 self.treat_files_smelly_python(file_smelly_python)
             if library == 'multimetric':
                 files_multimetric = [f for f in glob.glob(directory + str("/") + library+ "**/*.txt", recursive=True)]
                 self.treat_files_multimetric(files_multimetric)
             if library == 'radon':
                files_radon = [f for f in glob.glob(directory + str("/") + library + "**/*.txt", recursive=True)]
                self.treat_files_radon(files_radon)


    def treat_files_radon(self,files_radon):

        mi = {'Repository': [], 'Classification': []}
        df_mi= pd.DataFrame(mi)

        hal = {'Repository': [], 'h1': [], 'h2': [], 'N1': [],
             'N2': [], 'vocabulary': [],
             'length': [], 'calculated_length': [], 'volume': [],
             'difficulty': [], 'effort': [], 'time': [], 'bugs': []}
        df_hal = pd.DataFrame(hal)

        raw = {'Repository': [], 'LOC': [],
                   'LLOC': [],'SLOC': [], 'Comments': [],
                   'Single Comments': [],
                   'Multi': [], 'Blank': [],
                   '(C%L)': [],
                   '(C%S)': [], '(C+M%L)': []}

        df_raw = pd.DataFrame(raw)

        cc = {'Repository': [],'block_type':[] ,'Classification': []}
        df_cc = pd.DataFrame(cc)

        for file in files_radon:
            if file.endswith("raw-radon-output.txt"):
                f = open(file)
                for line in f.readlines():
                    if line.startswith("/"):
                        list_line = list(line.split("/"))
                        repository = list_line[14]
                    if line.startswith(" "):
                        line = line.replace(" ", "")
                        list_line = list(line.split(":"))
                        if list_line[0] == '-CommentStats':
                            list_line.remove(list_line[0])
                        if list_line[0] == 'LOC':
                            LOC = list_line[1].replace("\n", "")
                        if list_line[0] == 'LLOC':
                            LLOC = list_line[1].replace("\n", "")
                        if list_line[0] == 'SLOC':
                            SLOC = list_line[1].replace("\n", "")
                        if list_line[0] == 'Comments':
                            comments = list_line[1].replace("\n", "")
                        if list_line[0] == 'Singlecomments':
                            single_comments = list_line[1].replace("\n", "")
                        if list_line[0] == 'Multi':
                            multi = list_line[1].replace("\n", "")
                        if list_line[0] == 'Blank':
                            blank = list_line[1].replace("\n", "")
                        if list_line[0] == '(C%L)':
                            c_l = list_line[1].replace("\n", "")
                        if list_line[0] == '(C%S)':
                            c_s = list_line[1].replace("\n", "")
                        if list_line[0] == '(C+M%L)':
                            c_m_l = list_line[1].replace("\n", "")

                            new_row = {'Repository': repository, 'LOC': LOC,
                                       'LLOC': LLOC,
                                       'SLOC': SLOC, 'Comments': comments,
                                       'Single Comments': single_comments,
                                       'Multi': multi, 'Blank': blank,
                                       '(C%L)': c_l,
                                       '(C%S)': c_s, '(C+M%L)': c_m_l }

                            df_raw= df_raw.append(new_row, ignore_index=True)
                    df_raw.to_csv('raw-radon.csv')

            if file.endswith("mi-radon-output.txt"):
                f = open(file)
                for line in f.readlines():

                    if line.startswith("/"):
                        classification = line.split("-")[-1]
                        list_line = list(line.split("/"))
                        repository = list_line[14]
                        classification = str(classification)
                        classification= classification.replace("\n", "")
                        classification = classification.replace('"', '')

                        new_row = {'Repository': repository, 'Classification': classification}
                        # append row to the dataframe
                        df_mi= df_mi.append(new_row, ignore_index=True)

            df_mi.to_csv("mi-radon.csv")

            if file.endswith("cc-radon-output.txt"):
                f = open(file)
                for line in f.readlines():
                    if line.startswith("/"):
                        list_line = list(line.split("/"))
                        repository = list_line[14]
                    if line.startswith(" "):
                        list_line = list(line.split(" "))
                        block_type = list_line[4]
                        classification = list_line[-1].replace("\n","")
                        new_row = {'Repository': repository, 'block_type': block_type, 'Classification': classification}
                        # append row to the dataframe
                        df_cc = df_cc.append(new_row, ignore_index=True)
                df_cc.to_csv('cc-radon.csv')


            if file.endswith("hal-radon-output.txt"):
                f = open(file)
                for line in f.readlines():
                    if line.startswith("/"):
                        list_line = list(line.split("/"))
                        repository = list_line[14]
                    if line.startswith(" "):
                        line = line.replace(" ","")
                        list_line = list(line.split(":"))
                        if list_line[0] == 'h1':
                            h1 = list_line[1].replace("\n","")
                        if list_line[0] == 'h2':
                            h2 = list_line[1].replace("\n","")
                        if list_line[0] == 'N1':
                             N1 = list_line[1].replace("\n","")
                        if list_line[0] == 'N2':
                             N2 = list_line[1].replace("\n","")
                        if list_line[0] == 'vocabulary':
                            vocabulary = list_line[1].replace("\n","")
                        if list_line[0] == 'length':
                            length = list_line[1].replace("\n","")
                        if list_line[0] == 'calculated_length':
                            calculated_length = list_line[1].replace("\n","")
                        if list_line[0] == 'volume':
                            volume = list_line[1].replace("\n","")
                        if list_line[0] == 'difficulty':
                            difficulty = list_line[1].replace("\n","")
                        if list_line[0] == 'effort':
                            effort = list_line[1].replace("\n","")
                        if list_line[0] == 'time':
                            time = list_line[1].replace("\n","")
                        if list_line[0] == 'bugs':
                            bugs = list_line[1].replace("\n","")


                            new_row = {'Repository': repository, 'h1': h1,
                                   'h2': h2,
                                   'N1': N1, 'N2': N2,
                                   'vocabulary': vocabulary,
                                   'length': length, 'calculated_length': calculated_length,
                                   'volume': volume,
                                   'difficulty': difficulty, 'effort': effort, 'time': time, 'bugs': bugs}


                            df_hal = df_hal.append(new_row, ignore_index=True)
            df_hal.to_csv('hal-radon.csv')

    def treat_files_multimetric(self,files_multimetric):
        d = {'Repository' : [],'comment_ratio': [], 'cyclomatic_complexity': [], 'fanout_external': [],
                'fanout_internal': [], 'halstead_bugprop': [],
                'halstead_difficulty': [], 'halstead_effort': [], 'halstead_timerequired': [],
                'halstead_volume': []}
        df = pd.DataFrame(d)

        for file in files_multimetric:
            path = Path(file)
            if path.stat().st_size == 0:
                os.remove(file)  # remove empty txt files
            else:
                with open(file) as f:
                    data = f.readlines()[2:48]
            repository = data[0]
            repository = repository.split("/")[14]
            data = data[21:48]

            for line in data:
                line = line.split(":")
                chars = "'[]' {}" " "
                line = str(line)
                line = line.translate(str.maketrans('', '', chars))
                line = line.replace("\\n", "")
                line = line.replace('"', '')
                if line.startswith('comment_ratio'):
                    comment_ratio = line.split(',')[1]
                if line.startswith('cyclomatic_complexity'):
                    cyclomatic_complexity = line.split(',')[1]
                if line.startswith('fanout_external'):
                    fanout_external = line.split(',')[1]
                if line.startswith('fanout_internal'):
                    fanout_internal = line.split(',')[1]
                if line.startswith('halstead_bugprop'):
                    halstead_bugprop = line.split(',')[1]
                if line.startswith('halstead_difficulty'):
                    halstead_difficulty = line.split(',')[1]
                if line.startswith('halstead_effort'):
                    halstead_effort = line.split(',')[1]
                if line.startswith('halstead_timerequired'):
                    halstead_timerequired = line.split(',')[1]
                if line.startswith('halstead_volume'):
                    halstead_volume = line.split(',')[1]
            new_row = {'Repository': repository ,'comment_ratio': comment_ratio, 'cyclomatic_complexity': cyclomatic_complexity,
                       'fanout_external': fanout_external, 'fanout_internal': fanout_internal,
                       'halstead_bugprop': halstead_bugprop,
                       'halstead_difficulty': halstead_difficulty, 'halstead_effort': halstead_effort,
                       'halstead_timerequired': halstead_timerequired,
                       'halstead_volume': halstead_volume}
            df = df.append(new_row, ignore_index=True)

        print(df.head(5))
        df.to_csv('multimetric.csv')

    def treat_files_smelly_python(self,file_smelly_python):
        data = {'Repository': [], 'Smell Type': [], 'Information': []}
        df = pd.DataFrame(data)

        for file in file_smelly_python:
            f = open(file)
            for line in f.readlines():
                if line.startswith("Cloned-repositories"):
                    chars = "'.:,![]' " " "
                    information = line.split(" ")[-1]
                    repository = line.split("/")[1:2]
                    information = information.replace("\n","")
                    repository = str(repository)
                    repository = repository.translate(str.maketrans('', '', chars))
                    smell_type = line.split(" ")[1]
                    smell_type = smell_type.translate(str.maketrans('', '', chars))
                    new_row = {'Repository': repository, 'Smell Type': smell_type, 'Information': information}
                    # append row to the dataframe
                    df = df.append(new_row, ignore_index=True)
        df_remove = df.loc[(df['Information'] == 'files')]
        df = df.drop(df_remove.index)
        df.to_csv('smelly_python.csv')

    def treat_files_flake8(self,files_fkake8):
        data = {'Repository': [],'Smell Type':[],'Information': []}
        df = pd.DataFrame(data)

        for file in files_fkake8:
            path = Path(file)
            if path.stat().st_size == 0:
                os.remove(file)            # remove empty txt files
            else:
                f = open(file)
                for line in f.readlines():
                    repository = line.split("/")[15]
                    smell = line.split("/")[-1]
                    information = smell.split(" ")[2:-1]
                    smell_type = smell.split(" ")[1]

                    new_row = {'Repository': repository, 'Smell Type': smell_type,'Information':information}
                    # append row to the dataframe
                    df = df.append(new_row, ignore_index=True)
        df.to_csv("flake8.csv")

#arrumar flake8

if __name__ == "__main__":
    crawler = Treats_files()
    crawler.read_files_directory()