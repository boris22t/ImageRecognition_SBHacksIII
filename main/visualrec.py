#--------------------------------------------------
#  Project Title: GenderPhotoSorter
#  Authors: Boris Tam, Jason Zhau, Salud Lemus
#  Version: 1/22/17
#
#  Descritipn:
#  This program creates custom classifiers for genders in 
#  a picture
#--------------------------------------------------

import json
import glob, os
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

os.chdir("../sources/mix/female")

visual_recognition = VisualRecognition('2016-05-20', api_key='43c028b896a8000ff57bc2a4d4d0a48619077370')

# delete custom classifier 
# print(json.dumps(visual_recognition.delete_classifier(classifier_id='ManvsWoman_541743446'), indent=2))

# create a classifier between man and woman
# with open(join(dirname(__file__), '../male.zip'), 'rb') as male, \
# 	open(join(dirname(__file__), '../female.zip'), 'rb') as female:
#     print(json.dumps(visual_recognition.create_classifier('ManvsWoman', female_positive_examples=female, negative_examples=male), indent=2))

print(json.dumps(visual_recognition.list_classifiers(), indent=2))

for file in glob.glob("*.jpg"):
	# classify a picture of a woman 
	with open(join(dirname(__file__), file), 'rb') as image_file, \
		open(file.replace(".JPG",".JSON"), 'w') as outfile:
			json.dump(visual_recognition.classify(images_file=image_file, \
				classifier_ids=["ManvsWoman_66993510"]), outfile, indent=2)
			print(image_file)


# generating custom classifiers, inputing negative and positive examples

# with open(join(dirname(__file__), '../resources/trucks.zip'), 'rb') as trucks, \
#       open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars:
#    print(json.dumps(visual_recognition.create_classifier('CarsvsTrucks', \