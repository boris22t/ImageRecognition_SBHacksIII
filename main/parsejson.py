import json
import glob, os
from pprint import pprint

os.chdir("../sources/mix/male")

classifiers_id = "ManvsWoman_1309697865"

with open('1.json') as data_file:    
    data = json.load(data_file)

accessor = data['images'][0]['classifiers'][0]
if( accessor['name'] == classifiers_id):
	pprint(accessor['classes'][0]['class'])
	pprint(accessor['classes'][0]['score'])

