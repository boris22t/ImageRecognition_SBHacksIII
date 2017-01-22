import json
import glob, os
from pprint import pprint

# object that keeps track of category and count
def ClassCounter:
	
	def __init__(self, name):
		self.name = name
		self.count = 0

	def inc():
		self.count = self.count + 1

# updates the list elements
def update_class(obj, listobj):
	if (obj in listobj):
		list[obj].inc()
	else:
		list.append(obj)


# change the directory to access source images
os.chdir("../sources/mix/male")

# predefined classifier id obtained via pre-training
classifiers_id = "ManvsWoman"


# parsing the json files
for file in glob.glob("*.json"):
	with open(file) as data_file:    
    	data = json.load(data_file)

		# only want classification from custom classifier
		accessor = data['images'][0]['classifiers'][0]
		if( classifiers_id in accessor['name']):
			pprint(accessor['classes'][0]['class'])
			pprint(accessor['classes'][0]['score'])

arraylist of objects
object counter = {
	name = 'male',
	count = 0
}

# for every male found 
# 	count increments

# in the arraylist, many categories, for example (male, female, cat, orange) 
# 	sort the arraylist with comparator of the count

# select the top 5 categories

# display these categories
# and allow the user to choose them

# make folders of the choices
# put photo files that fall under these classifications into the folders
