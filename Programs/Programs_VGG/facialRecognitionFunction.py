#! /usr/bin/python3
#########################################################################
#Group 3 - Arnaud JOSIS; Corentin DUPONT; Gerome GOFFIN @ Henallux	#
#Date of the creation : 04/05/2020					#
#Date of the last modification : 04/05/2020				#
#Modifications : 							#
#									#
#Purpose:								#
#  This file contains the functions for the mainProgram.py		#
#########################################################################

#Import the needed libraries
import os
import cv2
import pickle
from scipy.spatial.distance import cosine as dcos
import numpy as np

#Function declaration
#This function allows to generate the dataset
#Input parameters :
#	folder_dataset: where the dataset is store with the name of the person
#	featuremodel: the vgg model loaded
#	database: the dataset loaded
#Output parameter :
#	database: the database with the new added person (with the other one)
def generate_database(folder_dataset = "dataset/Corentin_Dupont", featuremodel = " ", database = " "):
	print()
	name = folder_dataset[folder_dataset.rfind('/')+1:]
	print("[Info]",name)
	tab = []
	for the_file in os.listdir(folder_dataset):
		print("[Info]",the_file, end='')
		try:
			if os.path.isfile(folder_dataset + '/' + the_file):
				img = cv2.imread(folder_dataset + '/' + the_file)
				crpim, srcimg, (x, y, w, h) = auto_crop_image(img)
				vector_image = crpim[None,...] #...->Add none at the begining. Before : 224x224x3; After 1x224x224x3
				tab.append(featuremodel.predict(vector_image)[0,:]) #-> Return 2622 values
		except Exception as e:
			print(e)
		database[name] = tab
	return database

#This function allow to resize the picture to 224 224 3
#This function can just return one person on the picture. If there are more than one person, the up-left side person is the first
#Input parameter :
#	image: the image from the piCamera
#Output parameters :
#	if a person if detected on the picture, 
#		crpim: the 224x224x3 picture of the face found on the picture
#		image: the original image plus a rectangle near around the face
#		(x,y,w,h): the x,y,w,h coordonates
#	if a person is not detected on the picture
#		none: no image
#		image : the original image
#		(0,0,0,0) : no coordonate
def auto_crop_image(image):
    if image is not None:
        im = image.copy()
        # Load HaarCascade from the file with OpenCV
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Read the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        #faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        if len(faces) > 0:
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  

            (x, y, w, h) = faces[0]
            center_x = x+w/2
            center_y = y+h/2
            height, width, channels = im.shape
            b_dim = min(max(w,h)*1.2,width, height) #Take a little bit than the rectangle on the picture.
            box = [center_x-b_dim/2, center_y-b_dim/2, center_x+b_dim/2, center_y+b_dim/2]
            #Inside box there are 4 values
            box = [int(x) for x in box] #-> Convert all x values in the variables box to int
            # Crop Image
            #Cut the image if the size to cut is lower than the size of the picture.
            if box[0] >= 0 and box[1] >= 0 and box[2] <= width and box[3] <= height:
                crpim = im[box[1]:box[3],box[0]:box[2]] #Cut the image.
                crpim = cv2.resize(crpim, (224,224), interpolation = cv2.INTER_AREA) #Resize the picture in 224x224.
                #https://chadrick-kwag.net/cv2-resize-interpolation-methods/
                print(" Found {0} face(s)!".format(len(faces)))
                return crpim, image, (x, y, w, h)
    return None, image, (0,0,0,0)

#This function display the predict person
#Input parameters
#	img: the image 224 224 3 format
#	database: the loaded dataset
#	featuremodel: the loaded dataset
#Output parameters
#	name: the name of the predict person
#	dmin: value of the cos of the find_closest function
def recognize_image(img, database, featuremodel):
    print("******** PROCEDING FACIAL RECOGNITION ********")
    name, dmin = find_closest(img ,database, 0.35, featuremodel)   
    print("******** RESUME ANALYSIS ********")
    return name, dmin, True

#This function search the matching beween the person to predict and the dataset
#Input parameters
#       img: the image 224 224 3 format
#       database: the loaded dataset
#	min_detection: a trigger level between the known and unknown person
#       featuremodel: the loaded dataset
#Output parameters
#       umin: the name of the predict person
#       dmin: value of the cos of the find_closest function
def find_closest(img, database, min_detection=0.35, featuremodel=" "):
    imarr1 = np.asarray(img)
    imarr1 = imarr1[None,...]
    #Prediction
    fvec1 = featuremodel.predict(imarr1)[0,:]
    #Closest person in DB
    dmin = 0.0
    umin = ""
    for key, person in database.items():
        #Inside key, there are the name of people from the dataset
        #Inside person, there are x * 2622 values that define the person. Where x = number of pitures of the person inside the dataset
        for value in person:
            #Inside value, there are the 2622 values that define a person.
            fvec2 = value
            dcos_1_2 = dcos(fvec1, fvec2)
            if umin == "":
                dmin = dcos_1_2
                umin = key
            elif dcos_1_2 < dmin:
                dmin = dcos_1_2
                umin = key
    if dmin > min_detection:
        umin = "Unknown"
    return umin, dmin


