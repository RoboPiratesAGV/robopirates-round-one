import time
import cv2


def write_time(image_frame, START_TIME):
    time_lapsed = time.time() - START_TIME
    mins = time_lapsed // 60
    sec = time_lapsed % 60
    mins = mins % 60
    stop_watch_time_now = "{}:{}:{}".format(int(mins), int(sec), int((sec % 1)*1000))

    cv2.putText(image_frame, stop_watch_time_now, (100, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0))

    return image_frame
