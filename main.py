# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import argparse

arg_parser = argparse.ArgumentParser(description="Launches robopirates-round-one server.")
arg_parser.add_argument('url',
                       metavar='url',
                       type=str,
                       help='url of the launched IP Webcam')
args = arg_parser.parse_args()

# assigning args to vars
url = args.url

# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Data_Input", img)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()