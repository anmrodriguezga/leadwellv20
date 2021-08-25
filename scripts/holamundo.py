# export GOOGLE_APPLICATION_CREDENTIALS=analog-ground-317912-82fc887db980.json
# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\anmrodriguezga\Documents\Pasantia\visual_feedback\analog-ground-317912-82fc887db980.json"
import io
import cv2 as cv
from PIL import Image
import time
import os
from google.cloud import vision
from google.cloud.vision_v1 import types

# Instantiates a client
client = vision.ImageAnnotatorClient()
def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = texts[0].description

    return string

# cap = cv.VideoCapture('http://admin:Poly15dic@168.176.36.210:8085/video/mjpg.cgi')
cap = cv.VideoCapture('https://drive.google.com/file/d/14FHQ7pBNDVbCjhBdjMeNjS2MkHuG5baI/view?usp=sharing')
# cap = cv.VideoCapture("pantalla.mkv")
frame_counter = 0
c = 0

while cap.isOpened():
    ret, frame = cap.read()
    # frame_counter += 1
    # #If the last frame is reached, reset the capture and the frame_counter
    # if frame_counter == cap.get(cv.CAP_PROP_FRAME_COUNT):
    #     frame_counter = 0 #Or whatever as long as it is the same as next line
    #     cap.set(cv.CAP_PROP_POS_FRAMES, 0)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if c%20==0:
        # Region Of Interest(ROI)
        # crop = img[y:y+h, x:x+w]
        crop = cv.rotate(frame[140:327, 54:238], cv.ROTATE_180)
        cv.imshow('frame', frame)
        file = 'live.png'
        cv.imwrite(file,crop)
        # # print OCR text
        print(detect_text(file))
        # data = detect_text(file).replace(" ", "")
        # print(float(data.splitlines()[1]))
    c+=1;
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

