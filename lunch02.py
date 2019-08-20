import requests
import json
import input_data

# dictに変換
jdata = json.loads(input_data.past_lunches)

inputdate = input()
print('date=' + inputdate)

inputcost = input()
print('cost=' + inputcost)

new_lunches = {"date": inputdate,"cost": inputcost}

url = 'http://ec2-18-208-114-164.compute-1.amazonaws.com/lunches'
headers = {'content-type': 'application/json'}
response = requests.post(url, json.dumps(new_lunches), headers=headers)
