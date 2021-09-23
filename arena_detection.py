import cv2
import numpy as np


def detect_arena(image_frame):
    hsv_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)

    # obtaining white mask
    white_lower = np.array([0, 0, 32], dtype=np.uint8)
    white_upper = np.array([160, 136, 106], dtype=np.uint8)
    white_mask = cv2.inRange(hsv_frame, white_lower, white_upper)

    kernal = np.ones((5, 5), "uint8")

    # For white color
    white_mask = cv2.dilate(white_mask, kernal)
    res_white = cv2.bitwise_and(image_frame, image_frame, mask=white_mask)

    # Creating contour to track white color
    contours, hierarchy = cv2.findContours(white_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    index = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        print(area)
        if index == 0:
            largest = area
            index += 1
        if area >= largest:
            largest = area
        else:
            continue

        if area > 25000:
            x, y, w, h = cv2.boundingRect(contour)
            # image_frame = image_frame[y:y+h, x:x+w]
            # image_frame = cv2.rectangle(image_frame, (x, y),
            #                            (x + w, y + h),
            #                            (0, 0, 255), 2)
            #
            # cv2.putText(image_frame, "Arena", (x, y),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1.0,
            #             (0, 0, 255))

    return image_frame
