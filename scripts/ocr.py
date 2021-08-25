# export GOOGLE_APPLICATION_CREDENTIALS=brave-drive-314901-a4d9cd4826d8.json
import io
import cv2
from PIL import Image

# Imports the Google Cloud client library
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
    string = ''

    for text in texts:
        string+=' ' + text.description
    return string

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'live.png'
    cv2.imwrite(file,frame)

    # print OCR text
    print(detect_text(file))

    # Display the resulting frame
    cv2.imshow('frame',frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()