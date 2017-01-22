mport json
import glob, os
from os.path import join, dirname
from pprint import pprint

# object that keeps track of category and count
class ClassCounter(object):
    def __init__(self, name):
        self.name = name
        self.count = 0

    def inc(self):
        self.count += 1

# updates the list elements
def update_class(obj, listobj):
    #if len(listobj) == 0:
    listobj.append(obj)
    #for x in listobj:
        #if (x.name == obj.name):
    x.count += 1

    # else:
    #     listobj.append(obj)


# change the directory to access source images
os.chdir("../sources/mix/male")

# predefined classifier id obtained via pre-training
classifiers_id = "ManvsWoman"


# parsing the json files
for file in glob.glob("*.json"):
    with open(join(dirname(__file__), file), 'r') as data_file:    
        data = json.load(data_file)
# only want classification from custom classifier
        accessor = data['images'][0]['classifiers'][0]
        if( classifiers_id in accessor['name']):
            myList = []
            myObj = ClassCounter(accessor['classes'][0]['class'])
            update_class(myObj, myList)

for p in myList:
    print(p.name)
    print(p.count)

# arraylist of objects
# object counter = {
#     name = 'male',
#     count = 0
# }

# for every male found
#     count increments

# in the arraylist, many categories, for example (male, female, cat, orange)
#     sort the arraylist with comparator of the count

# select the top 5 categories

# display these categories
# and allow the user to choose them

# make folders of the choices
# put photo files that fall under these classifications into the folders