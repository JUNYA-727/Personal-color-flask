from flask import Flask,render_template, request
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.python.keras.saving.saved_model.load import load
import image
from datetime import datetime
import os
import cv2
import pandas as pd

app=Flask(__name__)

model=load_model('personal_color_model1.h5')

@app.route("/",methods=["GET","POST"])
def upload_file():
    if request.method=="GET":
        return render_template("index.html")
    
    if request.method=="POST":
        f=request.files['file']
        filepath='./static/'+datetime.now().strftime('%Y%m%d%H%M%S')+'.png'
        f.save(filepath)
        face_image=image.face(filepath)
        predict_image=image.image_create(face_image)
        scores=model.predict(predict_image)[0]
        predict=[]
        score=0
        for j,k in enumerate(scores):
            predict.append(100*k)
            if score<k:
                score=k
                ans=j
            else:
                continue
        #predict[0]は秋､predict[1]は春､predict[2]は夏､predict[3]は冬
        return render_template('index.html',filepath=filepath,autumn=predict[0],spring=predict[1],summer=predict[2],winter=predict[3],ans=ans)
    
if __name__=="__main__":
    app.debug=True
    app.run(host="localhost",port=5000)