{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# version 2.0:\n",
    "\n",
    "# Importing Python Libraries:\n",
    "from PIL import Image\n",
    "import requests\n",
    "from io import BytesIO\n",
    "#from tensorflow.python.keras.applications import ResNet50\n",
    "import cv2\n",
    "import numpy as np\n",
    "        \n",
    "# create an overlay image. You can use any image:\n",
    "\n",
    "#response = requests.get('https://static.sport-conrad.com/out/pictures//generated/product/1/247_200_100/98789103_987_891_03.png')\n",
    "#background = Image.open(BytesIO(response.content))\n",
    "    \n",
    "background = cv2.imread('cloth_new.png')\n",
    "  \n",
    "# Open the camera\n",
    "cap = cv2.VideoCapture(0)\n",
    "       \n",
    "# Set initial value of weights\n",
    "alpha = 0.50\n",
    "    \n",
    "while True:\n",
    "       # read the frame\n",
    "        ret, frame = cap.read()\n",
    "        # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()\n",
    "        added_image = cv2.addWeighted(frame[150:350,150:350,:],alpha,background[0:200,0:200,:],1-alpha,0)\n",
    "        \n",
    "        # Change the region with the result\n",
    "        frame[150:350,150:350] = added_image\n",
    "        \n",
    "        # For displaying current value of alpha(weights)\n",
    "        font = cv2.FONT_HERSHEY_SIMPLEX\n",
    "        cv2.putText(frame,'Select S to Save else ESC to Cancel',(20,25), font, 0.7,(0, 0, 255),2,cv2.FONT_HERSHEY_DUPLEX)\n",
    "        cv2.imshow('Try On Window',frame)\n",
    "        k = cv2.waitKey(10)\n",
    "        \n",
    "        # wait for ESC key to exit\n",
    "        if k == 27:\n",
    "            break\n",
    "       \n",
    "      # wait for 's' key to save the image and exit\n",
    "        elif k == ord('s'): \n",
    "            cv2.imwrite('savedimage.png',added_image) \n",
    "            #cv2.putText(frame,'Saving Image...',(10,30), font, 1,(255, 0, 0),2,cv2.FONT_HERSHEY_DUPLEX)\n",
    "            break\n",
    "        \n",
    "        # press a to increase alpha by 0.1\n",
    "        elif k == ord('a'):\n",
    "            alpha +=0.1\n",
    "            if alpha >=1.0:\n",
    "                alpha = 1.0\n",
    "        # press d to decrease alpha by 0.1\n",
    "        elif k== ord('d'):\n",
    "            alpha -= 0.1\n",
    "            if alpha <=0.0:\n",
    "                alpha = 0.0\n",
    "                \n",
    "cloth_image = cv2.imread('cloth_new.png')\n",
    "human_image= cv2.imread('savedimage.png',cv2.IMREAD_UNCHANGED)\n",
    "dst = cv2.addWeighted(cloth_image,0.7,human_image,0.3,0)\n",
    "#dst = cv2.add(cloth_image,human_image)\n",
    "\n",
    "cv2.imshow('dst',dst)\n",
    "cv2.waitKey(20)\n",
    "                \n",
    "                           \n",
    "# Release the camera and destroy all windows         \n",
    "cap.release()\n",
    "cv2.destroyAllWindows() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}