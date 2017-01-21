import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

visual_recognition = VisualRecognition('2016-05-20', api_key='8db55a029e23a6d20c91b8592708fed5f4fe07db')

# classify a picture of a woman 
print(json.dumps(visual_recognition.classify(images_file="file:///C:/Users/Jason/Documents/GitHub/imrec/sources/male/1.jpg"), indent=2))

# detect the face of a picture of a woman
print(json.dumps(visual_recognition.detect_faces(images_url="https://www.ibm.com/ibm/ginni/images\
	/ginni_bio_780x981_v4_03162016.jpg"), indent=2))

# generating custom classifiers, inputing negative and positive examples
'''
with open(join(dirname(__file__), '../resources/trucks.zip'), 'rb') as trucks, \
      open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars:
   print(json.dumps(visual_recognition.create_classifier('CarsvsTrucks', \
'''