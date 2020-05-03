#! /usr/bin/python3
#########################################################################
#Group 3 - Arnaud JOSIS; Corentin DUPONT; Gerome GOFFIN @ Henallux	#
#Date of the creation : 17/04/2020					#
#Date of the last modification : 17/04/2020				#
#Modifications : 							#
#									#
#									#
#Purpose:								#
# Resized images from a folder to a maximum size (width and height)	#
# Inputs arguments 							#
#	-p or --path to specify the path of all the picture to resize it#
#	-o or --output to specify where the resized pictures will be	#
#			stored.						#
#	-w or --width the maximum width of pictures. By default = 600	#
#	-H or --height the maximum height of pictures. By default = 500 #
#	-c or --change the format of all resized pictures. By default 0 #
#	-f or --format of pictures to be stores .png or .jpg		#
#									#
# Output argument							#
#	none								#
#									#
# The program calculate the ratio to reduce the size of pictures to the	# 
# maximum size. The pictures will not be distorted			#
# This program also rename the picture like CoCo.png -> 000.png		#
# This program can also change the format of the picture (e.g. .png ->	#
# .jpeg									#
#########################################################################

#Import libraries#
from imutils import paths
import cv2
import argparse
import os

#Get input arguments#
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to input directory of faces + images")
ap.add_argument("-o", "--output", required=True, help="path to store the directory with resized images")
ap.add_argument("-w", "--width", type=int, default="600", help="maximal width of pictures")
ap.add_argument("-H", "--height", type=int, default="500", help="maximal height of pictures")
ap.add_argument("-c", "--change", default="0", help="Change the format of the picture")
ap.add_argument("-f", "--format", default=".jpeg", help="Format of the picture. .png .jpeg")
args = vars(ap.parse_args())

#Create the folder where the resized pictures will be stored#
#path = args["output"]
#if not os.path.exists(path):
#	os.makedirs(path)

#Get the pictures via the path#
imagePaths = list(paths.list_images(args["path"]))
#Get the maximum width and height#
W_MAX=args["width"]
H_MAX=args["height"]

#Initialize the counter for the name of the pictures
cpt = 0

#For each picture, check if it is below the max size#
for (i, imagePath) in enumerate(imagePaths):

	path = args["output"] + "/"

	#print("[INFO] processing image {}/{} - {}".format(i+1, len(imagePaths), imagePath)) #debog
	
	#Read the picture
	img_RGB = cv2.imread(imagePath)

	#Get the picture's size
	img_H = img_RGB.shape[0]
	img_W = img_RGB.shape[1]

	print("[Info] : Size before - H: {} - W: {}".format(img_H, img_W))

	#Check if the size of the picture is below the max size
	if((img_H > H_MAX)|(img_W > W_MAX)):
		H_Factor = H_MAX/img_H
		W_Factor = W_MAX/img_W

		#print("Factor : H {}".format(H_Factor))
		#print("Factor : W {}".format(W_Factor))

		if(H_Factor <= W_Factor):
			img_new = cv2.resize(img_RGB,(0,0), fx = H_Factor, fy = H_Factor)
			#print("Resize via H")
		else:
			img_new = cv2.resize(img_RGB,(0,0), fx = W_Factor, fy = W_Factor)
			#print("Resize via W")
	else:
		img_new = img_RGB

	print("[Info] : Size after - H: {} - W: {}".format(img_new.shape[0], img_new.shape[1]))
	
	#Store the resized image with the old name but in the folder precise in parameter
	if(args["change"] == "1"):
		path = path + str(cpt).zfill(3) + args["format"]
		#print(path)
	else:
		path = path + str(cpt).zfill(3) + imagePath[imagePath.find('.'):]
		#print(path)
	print("[Info] :", path)
	cv2.imwrite(path,img_new)
	
	#Update the counter for the name of the picture
	cpt = cpt + 1

