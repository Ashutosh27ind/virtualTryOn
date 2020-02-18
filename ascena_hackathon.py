# %%
# version 2.0:

# Importing Python Libraries:
from PIL import Image
import requests
from io import BytesIO
#from tensorflow.python.keras.applications import ResNet50
import cv2
import numpy as np
        
# create an overlay image. You can use any image:

#response = requests.get('https://static.sport-conrad.com/out/pictures//generated/product/1/247_200_100/98789103_987_891_03.png')
#background = Image.open(BytesIO(response.content))
    
background = cv2.imread('cloth_new.png')
  
# Open the camera
cap = cv2.VideoCapture(0)
       
# Set initial value of weights
alpha = 0.50
    
while True:
       # read the frame
        ret, frame = cap.read()
        # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
        added_image = cv2.addWeighted(frame[150:350,150:350,:],alpha,background[0:200,0:200,:],1-alpha,0)
        
        # Change the region with the result
        frame[150:350,150:350] = added_image
        
        # For displaying current value of alpha(weights)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'Select S to Save else ESC to Cancel',(20,25), font, 0.7,(0, 0, 255),2,cv2.FONT_HERSHEY_DUPLEX)
        cv2.imshow('Try On Window',frame)
        k = cv2.waitKey(10)
        
        # wait for ESC key to exit
        if k == 27:
            break
       
      # wait for 's' key to save the image and exit
        elif k == ord('s'): 
            cv2.imwrite('savedimage.png',added_image) 
            #cv2.putText(frame,'Saving Image...',(10,30), font, 1,(255, 0, 0),2,cv2.FONT_HERSHEY_DUPLEX)
            break
        
        # press a to increase alpha by 0.1
        elif k == ord('a'):
            alpha +=0.1
            if alpha >=1.0:
                alpha = 1.0
        # press d to decrease alpha by 0.1
        elif k== ord('d'):
            alpha -= 0.1
            if alpha <=0.0:
                alpha = 0.0
                
cloth_image = cv2.imread('cloth_new.png')
human_image= cv2.imread('savedimage.png',cv2.IMREAD_UNCHANGED)
dst = cv2.addWeighted(cloth_image,0.7,human_image,0.3,0)
#dst = cv2.add(cloth_image,human_image)

cv2.imshow('dst',dst)
cv2.waitKey(20)
                
                           
# Release the camera and destroy all windows         
cap.release()
cv2.destroyAllWindows() 

# %%
