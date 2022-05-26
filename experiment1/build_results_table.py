from os import listdir
from os.path import isfile, join
import json
import csv

mypath='/home/egonzalez/FAIR-Research-Object/results/experiment1/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
dict={}
for file in onlyfiles:
    parameters=file.split('_')
    name_project = parameters[2]
    mode = parameters[3].split('.')[0]
    f = open(mypath+file)
    json_file = json.load(f)
    score = json_file["overall_score"]["score"]
    nComponents = len(json_file["components"])
    nComponents = nComponents - 1
    f.close()
    if name_project in dict:
        project=dict.get(name_project)
        project[mode]=score
        dict[name_project]=project
    else:
        dict[name_project]={mode:score,"components":nComponents}
#print(dict)

f_csv = open('/home/egonzalez/FAIR-Research-Object/results/experiment1.csv','w')
writer=csv.writer(f_csv)
writer.writerow(['project','mode0','mode1','nComponents'])
for project in dict:
    print(project+" "+str(dict.get(project)["mode0"])+" "+str(dict.get(project)["mode1"]))
    values = dict.get(project)
    writer.writerow([project,values["mode0"],values["mode1"],values["components"]])
f_csv.close()
