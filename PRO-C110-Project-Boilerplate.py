# import the opencv library
import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5')

  

vid = cv2.VideoCapture(0)
  
while(True):
      
   
    ret, frame = vid.read()
    prediction = model.predict(frame)
    print("prediction", prediction)
  
    
    cv2.imshow('frame', frame)
      
    
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  

vid.release()

cv2.destroyAllWindows()