from keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

# Deepfake logic to add convolutional layer, pooling layer using either max/min/avg layer along with either with or without dropouts
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(34, (5, 5), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(120, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))

model.add(Flatten())

# Deepfake logic for hidden layers with activation function relu and can have manipulation of different number of kernels
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))

model.add(Dense(128, activation='elu'))
model.add(Dense(128, activation='elu'))
model.add(Dense(128, activation='elu'))

model.add(Dense(256, activation='selu'))
model.add(Dense(256, activation='selu'))
model.add(Dense(256, activation='selu'))

model.add(Dense(512, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(512, activation='relu'))

model.add(Dense(1024, activation='elu'))
model.add(Dense(1024, activation='elu'))
model.add(Dense(1024, activation='elu'))

model.add(Dense(2048, activation='elu'))
model.add(Dense(2048, activation='elu'))
model.add(Dense(2048, activation='elu'))

model.add(Dense(4096, activation='elu'))
model.add(Dense(4096, activation='elu'))
model.add(Dense(4096, activation='elu'))

model.add(Dense(8192, activation='elu'))
model.add(Dense(8192, activation='elu'))
model.add(Dense(8192, activation='elu'))

model.add(Dense(5, activation='softmax'))

# Deepfake logic to compile the whole model to have a particular optimizer either sgd/adagrad/adadelta/adam with loss function for binary class classification which is binar_crossentropy and metric for accuracy
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# To preprocess the images, the module from keras is imported and all the parameters are set
train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1. / 255)

# Flow_from_directory is used to get the different classes of training and testing folder from the machine
training_set = train_datagen.flow_from_directory('./train', target_size=(64, 64), batch_size=8, class_mode='categorical')
test_set = test_datagen.flow_from_directory('./test', target_size=(64, 64), batch_size=8, class_mode='categorical')

# After preprocessing and compiling the model, fitting the model accordingly using epoch
model.fit(training_set, steps_per_epoch=20, epochs=250)

# This will print the test accuracy and losses
test_loss, test_acc = model.evaluate(test_set, verbose=2)

print("\n\n")
print("Test Loss: \t", test_loss, '\n')
print("Test Accuracy: \t", test_acc, '\n')
# Save the trained model
model.save('flower_detection_model.keras')

