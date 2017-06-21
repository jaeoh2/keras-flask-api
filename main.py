from flask import Flask, render_template, request
#from skimage.io import imread, imsave
#from skimage.transform import resize
from scipy.misc import imsave, imread, imresize
import numpy as np
from keras.models import model_from_json
import tensorflow as tf
import re
import sys
import os
import base64
    

app = Flask(__name__)

def model_init():
    with open("model.json","r") as json_file:
        loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    print("Loaded Model from disk")
    
    loaded_model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=['accuracy'])
    graph = tf.get_default_graph()
    
    return loaded_model, graph

def convertImage(imgData1):
    imgstr = re.search(r'base64,(.*)', imgData1).group(1)
    with open('output.png', 'wb') as output:
        #output.write(imgstr.decode('base64'))
        output.write(base64.b64decode(imgstr))

model, graph = model_init()
        
@app.route('/')
#def hello_world():
#    return "Deep learning based lung cancer analyzer Flask API repository"
def index():
    return render_template("index.html")

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)

@app.route('/predict/', methods=['GET','POST'])
#def hell_world():
#    return "Hell World!"
def predict():
    imgData = request.get_data()
    convertImage(imgData)
    print("debug")
    
    #x = imread('output.png', as_grey=True)
    #x = np.invert(x.astype(np.uint8))
    #x = resize(x,(28,28))
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))
    x = x.reshape(1,28,28,1)
    
    print("debug2")
    print(x)
    
    with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out, axis=1))
        print("debug3")
        
        response = np.array_str(np.argmax(out, axis=1))
        return response

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000, debug=True)
