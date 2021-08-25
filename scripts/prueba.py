#!/usr/bin/env python
# export GOOGLE_APPLICATION_CREDENTIALS=analog-ground-317912-82fc887db980.json
# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\anmrodriguezga\Documents\Pasantia\visual_feedback\analog-ground-317912-82fc887db980.json"
import io
import cv2 as cv
from PIL import Image
import time
import os
from google.cloud import vision
from google.cloud.vision_v1 import types
import rospy
from std_msgs.msg import Float64

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

def axisMove(x, y, z):

    xCoord = (float(x)-255)/1000
    yCoord = (float(y)+175)/1000
    zCoord = float(z)/1000

    x_message.data = xCoord
    y_message.data = yCoord
    z_message.data = zCoord

    x_axis.publish(x_message)
    y_axis.publish(y_message)
    z_axis.publish(z_message)


# try-catch
if __name__ == '__main__':

    cap = cv.VideoCapture('http://admin:Poly15dic@168.176.36.210:8085/video/mjpg.cgi')
    frame_counter = 0
    c = 0;

    # start node 
    rospy.init_node('cnc_move', anonymous=True)

    # publishers
    x_axis = rospy.Publisher('/x_axis_position_controller/command', Float64, queue_size=10)
    y_axis = rospy.Publisher('/y_axis_position_controller/command', Float64, queue_size=10)
    z_axis = rospy.Publisher('/z_axis_position_controller/command', Float64, queue_size=10)

    # messages
    x_message = Float64()
    y_message = Float64()
    z_message = Float64()

    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if c%10 == 0:
            # Region Of Interest(ROI)
            # crop = img[y:y+h, x:x+w]
            crop = cv.rotate(frame[36:267, 25:314], cv.ROTATE_180)
            cv.imshow('frame', crop)
            file = 'live.png'
            cv.imwrite(file,crop)
            # # print OCR text
            # print(detect_text(file))
            data1 = detect_text(file).replace(" ", "")
            data = data1.replace("Ø", "0").replace("の。", "0")
            if len(data)>8:
                x = data.splitlines()[0];
                y = data.splitlines()[1];
                z = data.splitlines()[2];
                axisMove(x, y, z)
                print("\nIteracion", c)
                print("x: ", x, "\ny: ", y, "\nz: ", z)
        c+=1;
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
