# Task 3 : Training the ML model with the train data and later testing the model with the test data


# Importing the models and layers and ImageDataGenerator from Keras
# Keras uses Tensorflow as its backend.
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# Sequential model is selected for this Task
classifier = Sequential()

# Steps in building a CNN
# Step 1 : Convolution
# Step 2 : Pooling
# Step 3 : Flattening
# Step 4 : Full Connection

# First convolutional layer.
'''
This will modulate the image input tensor and result in convoluted matrices. 
The matrices produced will be merged and amalgamated into a single matrix. 
This basically consists of mathematical operands, each of which serves as a node. 
The operands are decided on the basis of image size, colour and characteristics. 
After the convolution, we will be Max-Pooling the matrix, 
so that the size of the matrix is reduced, and it will help in efficient determination.
'''

classifier.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Second Convolutional Layer.
'''
This is added in order to increase the efficiency of detection. 
However, we cannot add infinite number of layers, as it would decrease the speed and also, 
can result in wrong detections. Please note that we are not passing
the input shape again, as the image array has been already been manipulated
'''
classifier.add(Convolution2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))


classifier.add(Flatten())  # This is done to change to array from 2D to a 1Da array.

# Dense layers are added. These are hidden layers.
# Dense() is the function to add a fully connected layer.
# Units is where we define the number of nodes that should be present in this hidden layer,
# these units value will be always between the number of input nodes and the output nodes but
# the art of choosing the most optimal number of nodes can be achieved only through experimental tries.
# Though it’s a common practice to use a power of 2 and the activation function will be a rectifier function.
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=6, activation='softmax'))

# Compiling the model
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# Defining the Data Generators for the test and train data individually
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# accessing the training dataset
training_set = train_datagen.flow_from_directory('data/train',
                                                 target_size=(64, 64),
                                                 batch_size=5,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')
# accessing the test dataset
test_set = test_datagen.flow_from_directory('data/test',
                                            target_size=(64, 64),
                                            batch_size=5,
                                            color_mode='grayscale',
                                            class_mode='categorical') 

# fitting the dataset to the model
# Epoch is the number of passes of the entire training dataset the machine learning algorithm has completed.
classifier.fit_generator(training_set, epochs=10, validation_data=test_set)

# Saving the model in the form of hierarchical data-model.
model_json = classifier.to_json()
with open("model-bw.json", "w") as json_file:
    json_file.write(model_json)
classifier.save_weights('model-bw.h5')

