import numpy as np
import os
import cv2
from tkinter import *
from tkinter import filedialog
import PIL
import imutils

def loadimage(path):
    original = cv2.imread(path)
    cv2.imwrite('final.png',original)
    cv2.imwrite('final.png',original)
    cv2.imwrite('copy.png',original)
    return original


def blackandwhite(temp) :
    grayImage = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('blackandwhite.png',grayImage)
    cv2.imwrite('final.png',grayImage)
    return grayImage
    

    



def negative(temp) :
    img_neg = cv2.bitwise_not(temp)
    cv2.imwrite('negative.png',img_neg)
    cv2.imwrite('final.png',img_neg)
    return img_neg





def clockwise_rotate(temp):
    rotated1=imutils.rotate_bound(temp,-90)
    cv2.imwrite('clockwise rotated.png',rotated1)
    cv2.imwrite('final.png',rotated1)
    return rotated1
    




def anticlockwise_rotate(temp):
    rotated2=imutils.rotate_bound(temp,90,)
    cv2.imwrite('rotated.png',rotated2)
    cv2.imwrite('final.png',rotated2)
    return rotated2 
    




def flip(temp):
    flipped=cv2.flip(temp,1)
    cv2.imwrite('flipped.png',flipped)
    cv2.imwrite('final.png',flipped)
    return flipped
    
    




def denoise(temp):
    dst = cv2.fastNlMeansDenoisingColored(temp,None,10,10,5,21)
    cv2.imwrite('denoise.png',dst)
    cv2.imwrite('final.png',dst)
    return dst
    


    
def canny_edge(temp):
    cv2.imwrite('forcanny.jpg',temp)
    forcanny=cv2.imread('forcanny.jpg')
    img = cv2.cvtColor(forcanny, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(img,100,200)
    cv2.imwrite('canny_edge.jpg',edge)
    cv2.imwrite('final.png',edge)
    return edge

    
def resize(temp,width):
    resized = imutils.resize(temp, width)
    cv2.imwrite('final.png',resized)
    return resized
    

def undo(temp):
    cv2.imwrite('final.png',temp)
    
    
    
def save(path):
    save=cv2.imread('final.png')
    cv2.imwrite(path,save)
    return 0
    
    


