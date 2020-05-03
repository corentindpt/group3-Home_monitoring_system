#! /usr/bin/python3
#########################################################################
#Group 3 - Arnaud JOSIS; Corentin DUPONT; Gerome GOFFIN @ Henallux	#
#Date of the creation : 01/04/2020					#
#Date of the last modification : 01/04/2020				#
#Modifications : 							#
#									#
#Purpose:								#
# Create the VGG model and save it					#
#########################################################################

#Import needed librairies 
from scipy.io import loadmat
from keras.models import Sequential, Model, load_model
from keras.layers import Flatten, Dropout, Activation, Permute
from keras.layers import Convolution2D, MaxPooling2D
from keras import backend as K
K.set_image_data_format( 'channels_last' )

#Function definition
#Create layers Convolution and maxpooling
def convblock(cdim, nb, bits=3):
    L = []
    for k in range(1,bits+1):
        convname = 'conv'+str(nb)+'_'+str(k)
        L.append( Convolution2D(cdim, kernel_size=(3, 3), padding='same', activation='relu', name=convname) )
        #https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/
        #cdim -> The dimensionnality of the output space (number of filter)
        #kernel_size -> Filtre 3x3 -> Assign randomly and adjust with training.
        #Strides -> By default, go head by 1 step
        #padding -> If you instead want to preserve the spatial dimensions of the volume such that the output volume size matches the input volume size, then you would want to supply a value of same  for the padding
        #activation -> Type d'activation. Ici ReLu rectified linear
    L.append( MaxPooling2D((2, 2), strides=(2, 2)) )
    #pool_size - > Filtre 2x2
    #stride -> Avancer de 2
    return L

#Create the model
def vgg_face_blank():
    withDO = True # no effect during evaluation but usefull for fine-tuning
    if True:
        mdl = Sequential() #The model is built layer by layer
        #mdl.add -> ajouter des couches au modèle.
        mdl.add( Permute((1,2,3), input_shape=(224,224,3)) )
        #http://www.robots.ox.ac.uk/~vgg/publications/2015/Parkhi15/parkhi15.pdf
        for l in convblock(64, 1, bits=2):
            mdl.add(l)
        for l in convblock(128, 2, bits=2):
            mdl.add(l)        
        for l in convblock(256, 3, bits=3):
            mdl.add(l)            
        for l in convblock(512, 4, bits=3):
            mdl.add(l)            
        for l in convblock(512, 5, bits=3):
            mdl.add(l)        
        mdl.add( Convolution2D(4096, kernel_size=(7, 7), activation='relu', name='fc6') )
        if withDO:
            mdl.add( Dropout(0.5) )
            #Drop out is a method of randomly ignoring neuron units during training.
        mdl.add( Convolution2D(4096, kernel_size=(1, 1), activation='relu', name='fc7') )
        if withDO:
            mdl.add( Dropout(0.5) )
        mdl.add( Convolution2D(2622, kernel_size=(1, 1), activation='relu', name='fc8') )
        mdl.add( Flatten() )
        #Multiply all and return a scalar value.
        mdl.add( Activation('softmax') )
        #Output activation function
        print(mdl.summary()) #Display the model structure
        return mdl
    
    else:
        raise ValueError('not implemented')

#Load the weight for all connexions
def copy_mat_to_keras(kmodel):
    kerasnames = [lr.name for lr in kmodel.layers]
    prmt = (0,1,2,3)
 
    for i in range(l.shape[1]):
        matname = l[0,i][0,0].name[0]
        if matname in kerasnames:
            kindex = kerasnames.index(matname)
            l_weights = l[0,i][0,0].weights[0,0]
            l_bias = l[0,i][0,0].weights[0,1]
            f_l_weights = l_weights.transpose(prmt)
            assert (f_l_weights.shape == kmodel.layers[kindex].get_weights()[0].shape)
            assert (l_bias.shape[1] == 1)
            assert (l_bias[:,0].shape == kmodel.layers[kindex].get_weights()[1].shape)
            assert (len(kmodel.layers[kindex].get_weights()) == 2)
            kmodel.layers[kindex].set_weights([f_l_weights, l_bias[:,0]])

# CNN model initialization
facemodel = vgg_face_blank()

# Load the pretrained weights into the model
data = loadmat('vgg-face.mat', matlab_compatible=False, struct_as_record=False)
l = data['layers']
description = data['meta'][0,0].classes[0,0].description
 
copy_mat_to_keras(facemodel)

# Final model that can get inputs and generate a prediction as an output
featuremodel = Model(input = facemodel.layers[0].input, output = facemodel.layers[-2].output)

#Save the model into a file
featuremodel.save('VGG_Model.h5')
