import json
import glob, os
from pprint import pprint

# change the directory to access source images
os.chdir("../sources/mix/male")

# predefined classifier id obtained via pre-training
classifiers_id = "ManvsWoman_1309697865"

# parsing the json files
with open('1.json') as data_file:    
    data = json.load(data_file)

# only want classification from custom classifier
accessor = data['images'][0]['classifiers'][0]
if( accessor['name'] == classifiers_id):
	pprint(accessor['classes'][0]['class'])
	pprint(accessor['classes'][0]['score'])

