#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## Take_picture
## File description:
## Take picture
##

import numpy as np
import cv2

class Module:
    nb = 3
    def __init__(self):
        return (0)
    def camera_test():
        img = cv2.imread('test_cat.jpg')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
print(Module.nb)
Module.camera_test()
