import numpy as np
import cv2


def edgeDetector(img):
    img = cv2.GaussianBlur(img,(13,13),4)
    cv2.imshow('img',img)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    result = cv2.Canny(img_gray,65,30,11)
    cv2.imshow('result',result)
