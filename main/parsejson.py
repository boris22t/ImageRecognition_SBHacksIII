import json
import glob, os, shutil
from os.path import join, dirname
from pprint import pprint
import copy

# object that keeps track of category and count
class ClassCounter(object):
   def __init__(self, name):
      self.name = name
      self.count = 0
      self.filenames = []
      self.index = 0
      
   def inc(self):
      self.count += 1
   
   def incIndex(self):
      self.index +=1
      
   def setListSize(self, size):
      list = ['' for x in range(size)]
      self.filenames = copy.copy(list)
   def appendFile(self, filename):
      print(filename)
      print(len(self.filenames))
      #self.filnames = self.filenames + [filename]
      list = ['' for x in range(len(self.filenames)+1)]
      #list = copy.copy(self.filenames)
      for i in range(len(self.filenames)):
         list[i] = self.filenames[i]
      list[len(list)-1] = filename
      print(list[len(list)-1])
      self.filenames = copy.copy(list)
      #self.filenames.append(filename)
      
      print(len(self.filenames))
      return self.filenames
      
   def setFileNames(self, list):
      self.filenames=list
      
# updates the list elements
def update_class(obj_class, listobj):
   for x in listobj:
      #print(x.name)
      if (x.name == obj_class.name):
         x.inc()
         return
   listobj.append(obj_class)

   
   # else:
   #    listobj.append(obj)

#def add_file(obj_class, filename):  
#   obj_class.setFileNames(obj_class.filenames.append(filename))

def findClass(file):
   #print(json)
   file = file.replace('.JPG','') + '.json'
   print('class ', file)
   #for file in glob.glob(json+'.json'):
   with open(join(dirname(__file__), file), 'r') as data_file:    
      data = json.load(data_file)   
      className = data['images'][0]['classifiers'][0]['classes'][0]['class']
      fileName = data['images'][0]['image']
      return className
      
# change the directory to access source images
os.chdir("../sources/mix/both")

# predefined classifier id obtained via pre-training
classifiers_id = "ManvsWoman"

# parsing the json files

myList = []
name = ''
for file in glob.glob("*.json"):
    with open(join(dirname(__file__), file), 'r') as data_file:    
        data = json.load(data_file)
# only want classification from custom classifier
        accessor = data['images'][0]['classifiers'][0]
        #myObj = ClassCounter(accessor['classes'][0]['class'])
        
        if( classifiers_id in accessor['name']):
            myObj = ClassCounter(accessor['classes'][0]['class'])
            update_class(myObj, myList)
            #name = data['images'][0]['image'] #@@
            #myObj.appendFile(name)
        else:
            print('false')
            #add name of picture to list


   

#for class
for p in myList: #male or female
   p.setListSize(p.count)
   print ('list length: ', len(p.filenames))

for file in glob.glob("*.json"):
    with open(join(dirname(__file__), file), 'r') as data_file:    
        data = json.load(data_file)
# only want classification from custom classifier
        className = data['images'][0]['classifiers'][0]['classes'][0]['class']
        fileName = data['images'][0]['image']
        #myObj = ClassCounter(accessor['classes'][0]['class'])
        for p in myList:
            if className == p.name:
               p.filenames[p.index] = fileName
               
               break

            
print(p.name + ' ')
print(p.count)
print(len(p.filenames))
print('length', len(p.filenames))
               
#src+filename = src
#directory + folderName+filename
destination = ''
source = 'C:\\Users\\Boris\\Documents\\imrec\\sources\\mix\\both\\'
directory = input('Enter destination directory to copy photos: ')
print(directory)     
for p in myList: #male or female   
   folderName = p.name
   destination = directory + '\\' +folderName
   print(destination)
   if not os.path.exists(destination): #create or open directory
      os.makedirs(destination)
   for pic in glob.glob(os.path.join('', '*.JPG')):
      cat = findClass(pic)
      if cat == folderName:
         shutil.copy(pic, destination)
      

   #for pic in p.filenames:
#      print(pic)
 #     print(len(p.filenames))
  

  #shutil.copy(source + pic, destination)
   #for file in p.filenames:
      #print(file)
      #destination = directory + folderName + file
   #print('next')
#print(len(myList)) ////////////
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