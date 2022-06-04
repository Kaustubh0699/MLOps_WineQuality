import json
from datetime import datetime

with open("runs.json",'r') as file:
    data = json.load(file)
    date = datetime.now().strftime("%d-%m-%y")
    data.append({'Run_name':"Trial",'Retrain_TBName':'XYZ',"Retrain_DateTime": str(date)})

with open("runs.json",'w') as w_file:
    json.dump(data,w_file,indent=3)