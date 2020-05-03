#! /usr/bin/python3
#########################################################################
#Group 3 - Arnaud JOSIS; Corentin DUPONT; Gerome GOFFIN @ Henallux	#
#Date of the creation : 01/05/2020					#
#Date of the last modification : 03/05/2020				#
#Modifications : 							#
#									#
#Purpose:								#
# Manage the function call						#
#########################################################################

#Import the needed libraries
import numpy as np
import cv2
from scipy.spatial.distance import cosine as dcos
from scipy.io import loadmat
from keras.models import Sequential, Model, load_model
from keras.layers import Flatten, Dropout, Activation, Permute
from keras.layers import Convolution2D, MaxPooling2D
from keras import backend as K
K.set_image_data_format( 'channels_last' )
import os
from imutils.video import VideoStream
import time
import imutils
from multiprocessing.dummy import Pool
import matplotlib.pyplot as plt
import pickle
from facialRecognitionFunction import *
import subprocess


print("[Info] : Loading the model ...")
featuremodel_load = load_model('createModel/VGG_Model.h5')
print("[Info] : model loaded")

print("[Info] : Loading the dataset ...")
f = open('dataset/dataset.txt','rb')
db_Load = pickle.load(f)
f.close()
print("[Info] : dataset loaded")

# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
	#Wait for a command
	print("[Info] : Wait for command")
	#nb = int(input("[Action required] : 0-Exit; 1-Predict in live; 2-Add a new person with piCamera; 3-Add a new person with downloaded pictures; 4-Delete a person of the dataset\n"))
	nb = int(subprocess.check_output("mosquitto_sub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/option -C 1", shell = True))
	if nb == 0:
		#exit the program
		exit()
	elif nb == 1:
		#Live prediction
		print("[Info] : option chosen - Predict in live")
		print("[INFO] starting video stream...")
		
		#Start the video stream
		vs = VideoStream(usePiCamera=True, rotation=180).start()
		time.sleep(2.0)

		# loop over the frames from the video stream
		while True:
			# grab the frame from the threaded video stream, clone it, (just
			# in case we want to write it to disk), and then resize the frame
			# so we can apply face detection faster
			frame = vs.read()
			orig = frame.copy()
			frame = imutils.resize(frame, width=400)
			
			# detect faces in the grayscale frame
			rects = detector.detectMultiScale(
			cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
			minNeighbors=5, minSize=(30, 30))
			
			# loop over the face detections and draw them on the frame
			crpim, image, (x, y, w, h)  = auto_crop_image(frame)
			if crpim is not None:
				name, distance = find_closest(crpim,db_Load,0.23,featuremodel=featuremodel_load)
				print("Person detected : ", name)
				if name == "Unknown":
					os.system("mosquitto_pub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/recognition -m 0")
				else:
					os.system("mosquitto_pub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/recognition -m 1")
				cv2.putText(image, name, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2)
				cv2.imwrite("lastPredictPerson.png",image)
			
			# show the output frame
			cv2.imshow("q -> exit", image)
			key = cv2.waitKey(1000) & 0xFF

			# if the `q` key was pressed, break from the loop
			if key == ord("q"):
				break

		# do a bit of cleanup
		print("[INFO] cleaning up...")
		cv2.destroyAllWindows()
		vs.stop()
		
		#crpim, image, (x, y, w, h)  = auto_crop_image(img_)
		#if crpim is not None:
		#	print(find_closest(crpim,db_Load,featuremodel=featuremodel_load))

	elif nb == 2:
		#Add a new person with the pi camera
		print("[Info] : option chosen - Add a new person with piCamera")
		#Get the firstname and the name of the person to be added
		#firstname = input("[Action required] : Enter the firstname of the new person (first letter in capital)\n")
		print("[Info] : Enter the first name of the person")
		firstname = subprocess.check_output("mosquitto_sub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/prenom -C 1", shell = True)
		firstname = firstname.decode("utf-8")
		firstname = firstname[:firstname.find('\n')] 
		#name = input("[Action required] : Enter the name of the person (first letter in capital)\n")
		print("[Info] : Enter the last name of the person")
		name = subprocess.check_output("mosquitto_sub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/nom -C 1", shell = True)
		name = name.decode("utf-8")
		name = name[:name.find('\n')]
		
		#Call the program to create the dataset with pictures
		cmd = "python createDataset/buildFaceDataset.py --name " + firstname + "_" + name + " --output dataset/"
		os.system(cmd)
		
		#Rename the picture with a jpeg format and resize to a max size
		print("[Info] : Resize and rename the picture of the person")
		pathResize = "dataset/" + firstname + "_" + name
		cmd = "python createDataset/resizePictures.py -p " + pathResize + " -o " + pathResize + " -c " + "1"
		os.system(cmd)
		
		#Delete the old pictures png from the picamera
		cmd = "rm dataset/" + firstname + "_" + name + "/*.png"
		os.system(cmd)
		
		#Update the dataset and store it
		print("[Info] : Update of the dataset")
		db_Load = generate_database("dataset/" + firstname + "_" + name, featuremodel_load, db_Load)
		print("[Info] Save the new dataset")
		f = open('dataset/dataset.txt','wb')
		pickle.dump(db_Load,f)
		f.close()
		print("[Info] : New dataset saved")

	elif nb == 3:
		#Add a new person with downloaded pictures
		print("[Info] : option chosen - Add a new person with downloaded pictures")
		#pathIN = input("Indicate the absolute path of pictures a the person to import. The path must be contain the name of the person in the format Firstname_Name\n")
		#Precise the path to the downloaded pictures
		print("[Info] : Add the path to the downloaded pictures")
		pathIN = subprocess.check_output("mosquitto_sub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/chemin -C 1", shell = True)
		pathIN = pathIN.decode("utf-8")
		pathIN = pathIN[:pathIN.find('\n')]
		
		#Create the directory with the new person
		if not os.path.exists("dataset/"+pathIN[pathIN.rfind('/')+1:]):
			os.makedirs("dataset/"+pathIN[pathIN.rfind('/')+1:])
		cmd = "python createDataset/resizePictures.py -p " + pathIN  + " -o dataset/" + pathIN[pathIN.rfind('/')+1:] + " -c " + "1"
		os.system(cmd)
		
		#Delete the downloaded pictures on the RaspberryPi
		cmd = "rm -r " + pathIN 
		os.system(cmd)

		#Update the dataset and store it
		print("[Info] : Update of the dataset")
		db_Load = generate_database("dataset/" + pathIN[pathIN.rfind('/')+1:], featuremodel_load, db_Load)
		print("[Info] Save the new dataset")
		f = open('dataset/dataset.txt','wb')
		pickle.dump(db_Load,f)
		f.close()
		print("[Info] : New dataset saved")

	elif nb == 4:
		#Delete a person of the dataset
		print("[Info] : option chosen - Delete a person from the dataset.")
		#Display the name of the person in the dataset
		print(os.system("ls dataset/"))
		#Ask the name of the person to be deleted
		#personName = input("Enter the name of the person to be deleted in the format FirstName_LastName\n")
		print("[Info] : Enter the name of the person to be deleted Firstname_Lastname")
		personName = subprocess.check_output("mosquitto_sub -h maqiatto.com -u etu30673@henallux.be -P HenalluxFlower -t etu30673@henallux.be/si/suppression -C 1", shell = True)
		personName = personName.decode("utf-8")
		personName = personName[:personName.find('\n')]
		
		#Delete the folder of picture in the dataset
		cmd = "rm -r " + "dataset/" + personName
		os.system(cmd)
		
		#Delete the person in the dictionnary
		del db_Load[personName]
		f = open('dataset/dataset.txt','wb')
		pickle.dump(db_Load,f)
		f.close()
		print("[Info] : ", personName, " delete from the dataset")

