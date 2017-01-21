import json
import glob, os
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

os.chdir("../sources/mix/male")

visual_recognition = VisualRecognition('2016-05-20', api_key='8db55a029e23a6d20c91b8592708fed5f4fe07db')

# delete custom classifier 

# create a classifier between man and woman
# with open(join(dirname(__file__), '../sources/mix/male.zip'), 'rb') as male, \
# 	open(join(dirname(__file__), '../sources/mix/female.zip'), 'rb') as female:
#     print(json.dumps(visual_recognition.create_classifier('ManvsWoman', male_positive_examples=male, negative_examples=female), indent=2))

print(json.dumps(visual_recognition.list_classifiers(), indent=2))

for file in glob.glob("*.jpg"):
	# classify a picture of a woman 
	with open(join(dirname(__file__), file), 'rb') as image_file, \
		open(file.replace(".JPG",".JSON"), 'w') as outfile:
			json.dump(visual_recognition.classify(images_file=image_file, \
				classifier_ids=["ManvsWoman_1309697865", "default"]), outfile, indent=2)
			print(image_file)


# detect the face of a picture of a woman
# print(json.dumps(visual_recognition.detect_faces(images_url='https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'), indent=2))

# generating custom classifiers, inputing negative and positive examples

# with open(join(dirname(__file__), '../resources/trucks.zip'), 'rb') as trucks, \
#       open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars:
#    print(json.dumps(visual_recognition.create_classifier('CarsvsTrucks', \
