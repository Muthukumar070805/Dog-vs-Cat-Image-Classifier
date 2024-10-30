from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import cv2 as cv
import random
import matplotlib.pyplot as plt
import os 
import pandas as pd 
size=100
DIREC=r'C:\Users\admin\Documents\dogs-vs-cats\train'
data=[]
CATE=['cat','dog']
for cag in CATE:
    fold = os.path.join(DIREC, cag)
    labels=CATE.index(cag)
    for img in os.listdir(fold):
        img_path = os.path.join(fold, img)
        img_arr = cv.imread(img_path)
        if img_arr is not None:
            img_arr =cv.resize(img_arr,(size,size))
            data.append([img_arr,labels])
x=[];y=[]
for feature, label in data:
        x.append(feature)
        y.append(label)
x=np.array(x)
y=np.array(y)
x=x/255
model=Sequential()
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(128,input_shape=x.shape[1:],activation='relu'))
model.add(Dense(2,activation='softmax'))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x,y,epochs=5,validation_split=0.1)
def predict_image(model, image_path):
    img = cv.imread(image_path)
    img = cv.resize(img, (size, size))  
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    if np.argmax(prediction) == 0:
        return "Cat"
    else:
        return "Dog"
value = input("Enter the image number: ")
image_path = f"C:\\Users\\admin\\Documents\\AI_project\\dogs-vs-cats\\test1\\test1\\{value}.jpg"
result = predict_image(model, image_path)
print(f"The image is predicted to be a: {result}")