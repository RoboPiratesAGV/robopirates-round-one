import cv2
import numpy as np


def detect_bot(img_frame):
    hsv_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)

    # obtaining red mask
    red_lower = np.array([175, 87, 81], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsv_frame, red_lower, red_upper)

    # obtaining pink mask
    pink_lower = np.array([140, 57, 121], np.uint8)
    pink_upper = np.array([175, 255, 255], np.uint8)
    pink_mask = cv2.inRange(hsv_frame, pink_lower, pink_upper)

    # obtaining blue mask
    blue_lower = np.array([100, 150, 1], np.uint8)
    blue_upper = np.array([160, 255, 235], np.uint8)
    blue_mask = cv2.inRange(hsv_frame, blue_lower, blue_upper)

    # obtaining green mask
    green_lower = np.array([67, 45, 5], np.uint8)
    green_upper = np.array([70, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsv_frame, green_lower, green_upper)

    kernal = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(img_frame, img_frame, mask=red_mask)

    # For green color 
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(img_frame, img_frame, mask=green_mask)

    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(img_frame, img_frame, mask=blue_mask)

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img_frame = cv2.rectangle(img_frame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.putText(img_frame, "Bot 2", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img_frame = cv2.rectangle(img_frame, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)

            cv2.putText(img_frame, "Bot 3", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

    # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img_frame = cv2.rectangle(img_frame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)

            cv2.putText(img_frame, "Bot 4", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))

    # Creating contour to track pink color
    contours, hierarchy = cv2.findContours(pink_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img_frame = cv2.rectangle(img_frame, (x, y),
                                      (x + w, y + h),
                                      (255, 0, 0), 2)

            cv2.putText(img_frame, "Bot 1", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))

    return img_frame
