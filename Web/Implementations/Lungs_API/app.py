# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:34:20 2020

@author: Krish Naik
"""

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
#from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions


from tensorflow.keras.models import load_model
#from tensorflow.keras.preprocessing import image
import os
#import tensorflow 
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from tensorflow.keras.applications.efficientnet import preprocess_input
from efficientnet.tfkeras import EfficientNetB4



# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
model = load_model(r'D:/Projects/KU Seventh Semester/Health App [AI Project]/Health-Application/Modelling/Lungs/Chest_Xray_Ef.h5')





def model_predict(img_path, model):
    img = load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255.0
    my_image = x
    #x = np.expand_dims(x, axis=0)
   

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    #x = preprocess_input(x)

    #preds = model.predict(x)
    #preds=np.argmax(preds, axis=1)

    my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))
    
    my_image = preprocess_input(my_image)
    prediction = model.predict(my_image)
    prediction = np.around(prediction, decimals=3)
    prediction = list(prediction[0])
    final = {'COVID':prediction[0], 'Lungs Opacity': prediction[1], 'Normal':prediction[2], 'Viral Pneumonia': prediction[3]}
    Keymax = max(final, key= lambda x: final[x])
    print(Keymax)
    return Keymax



@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        print(file_path)
        #file_path = file_path.replace('\\','\\')

        f.save(file_path)
        #f.close()

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        print(result)
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7646)
