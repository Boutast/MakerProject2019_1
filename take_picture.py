#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## Take_picture
## File description:
## Take picture
##

import numpy as np
import cv2
import sys

class Module:
    nb = 3
    def __init__(self):
        return (0)
    def camera_test():
        img = cv2.imread('test_cat.jpg')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def gray_image():
        image = cv2.imread("test_cat4.jpg")
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    Module.camera_test()
    Module.gray_image()

if __name__ == '__main__':
    main();
