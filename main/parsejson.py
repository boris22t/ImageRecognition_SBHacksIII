#--------------------------------------------------
#  Project Title: GenderPhotoSorter
#  Authors: Boris Tam, Jason Zhau, Salud Lemus
#  Version: 1/22/17
#
#  Descritipn:
#  This program aims to classify and organize photos into 
#  clear, user-friendly folders with the use of IBM Watson's 
#  image recognition functionality.
#--------------------------------------------------

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

   #not used, keep for reference
   # def appendFile(self, filename):
      # print(filename)
      # print(len(self.filenames))
      # self.filnames = self.filenames + [filename]
      # list = ['' for x in range(len(self.filenames)+1)]
      list = copy.copy(self.filenames)
      # for i in range(len(self.filenames)):
         # list[i] = self.filenames[i]
      # list[len(list)-1] = filename
      # print(list[len(list)-1])
      # self.filenames = copy.copy(list)
      # return self.filenames
      
   def setFileNames(self, list):
      self.filenames=list
      
# updates the list elements
def update_class(obj_class, listobj):
   for x in listobj:
      if (x.name == obj_class.name):
         x.inc()
         return
   listobj.append(obj_class)

def findClass(file):
   file = file.replace('.JPG','') + '.json'
   with open(join(dirname(__file__), file), 'r') as data_file:    
      data = json.load(data_file)   
      className = data['images'][0]['classifiers'][0]['classes'][0]['class']
      fileName = data['images'][0]['image']
      return className
      
# change the directory to access source images
os.chdir("../sources/mix/both")

# predefined classifier id obtained via pre-training
classifiers_id = "ManvsWoman"

# Parse the JSON files and count the number of files for each category
myList = []
name = ''
for file in glob.glob("*.json"):
    with open(join(dirname(__file__), file), 'r') as data_file:    
        data = json.load(data_file)
        # only want classification from custom classifier
        accessor = data['images'][0]['classifiers'][0]
        
        if( classifiers_id in accessor['name']):
            myObj = ClassCounter(accessor['classes'][0]['class'])
            update_class(myObj, myList)

   #remove
ans = input("Do you want to sort the categories? (yes/no) ")
doSort = ans.lower() in ("yes", "true", "t", "1")
if (doSort):
   print ("Sorting")
   sorted(myList, key=lambda obj: obj.count)
else:
   print("not sorting")


#Create a list for each category that the photos will be sorted into
for p in myList: #male or female
   p.setListSize(p.count)

#Compare class name in each JSON file with object's name, and put them into the corresponding list
for file in glob.glob("*.json"):
    with open(join(dirname(__file__), file), 'r') as data_file:    
        data = json.load(data_file)
         
        className = data['images'][0]['classifiers'][0]['classes'][0]['class']
        fileName = data['images'][0]['image']
        for p in myList:
            if className == p.name:
               p.filenames[p.index] = fileName
               break

#Copy files into folders for each category
destination = ''
directory = input('Enter destination directory to copy photos: ')
print(directory)     
for p in myList: #male or female   
   folderName = p.name
   destination = directory + '\\' +folderName
   if not os.path.exists(destination): #create or open directory
      os.makedirs(destination)
   for pic in glob.glob(os.path.join('', '*.JPG')):
      cat = findClass(pic)
      if cat == folderName:
         shutil.copy(pic, destination)
   #print('Done! Successfully created files for ', p.name, ' in the directory: ', destination)
print('Done! Successfully created files!!')
# TO DO:
# for every male found
#     count increments

# in the arraylist, many categories, for example (male, female, cat, orange)
#     sort the arraylist with comparator of the count

# select the top 5 categories

# display these categories
# and allow the user to choose them

# make folders of the choices
# put photo files that fall under these classifications into the folders