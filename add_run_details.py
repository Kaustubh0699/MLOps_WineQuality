import json
with open("runs.json",'r') as file:
    data = json.load(file)
    data['Test'] = {'Run_name':"Trial",'Retrain_TBName':'XYZ'}
    print(data)

with open("runs.json",'w') as w_file:
    json.dump(data,w_file,indent=3)