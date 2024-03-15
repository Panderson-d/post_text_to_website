import os
import requests
#  edit os.chdir to where txt files are located
os.chdir('/data/feedback')
filedir = os.listdir()
Data_Dict = {}
Txt_files = []
for items in filedir:
         if items.endswith('.txt'):  
                   Txt_files.append(items)   
for files in Txt_files:
        with open(files, "r") as file:
            line1 = file.readline()
            line2 = file.readline()
            line3 = file.readline()
            all_other_lines = file.read()
            Data_Dict['title'] = line1
            Data_Dict['name'] = line2
            Data_Dict['date'] = line3
            Data_Dict['feedback'] = all_other_lines
            #  change ip address to webpage
            response = requests.post("http://34.133.15.121/feedback/", data=Data_Dict)
