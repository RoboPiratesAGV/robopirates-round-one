import time
import cv2
import numpy as np
from arena_detection import detect_arena
from bot_detection import detect_bot
from write_time import write_time


LAST_SAVED_FILE = open("LAST_SAVED.txt", "r")

# VARS
IMAGE_WIDTH = 900
IMAGE_HEIGHT = 800
SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
SOURCE_VIDEO_ADDRESS = "./OBS-OP/4.mkv"
OP_VIDEO_ADDRESS = "./OPENCV-OP"
INDEX = int(LAST_SAVED_FILE.read())

cap = cv2.VideoCapture(SOURCE_VIDEO_ADDRESS)
op = cv2.VideoWriter(f'{OP_VIDEO_ADDRESS}/robo_pirates_{INDEX}.avi',
                     cv2.VideoWriter_fourcc(*'MJPG'), 60,
                     SIZE)

# While loop to continuously fetching data from the Url
START_TIME = time.time()
while True:
    ret, frame = cap.read()

    if ret:
        frame = cv2.resize(frame, SIZE)
        frame = detect_arena(frame)
        frame = detect_bot(frame)
        frame = write_time(frame, START_TIME)
        op.write(frame)
        cv2.imshow("VIDEO", frame)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            LAST_SAVED_FILE = open("LAST_SAVED.txt", "w")
            LAST_SAVED_FILE.write(str(INDEX + 1))
            break

    else:
        LAST_SAVED_FILE = open("LAST_SAVED.txt", "w")
        LAST_SAVED_FILE.write(str(INDEX + 1))
        break

cap.release()
op.release()
cv2.destroyAllWindows()

print("ended")
