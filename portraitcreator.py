import numpy as np
import cv2
from turtle import *
import random
turtle = Turtle()
screen = Screen()

turtle.speed(5000)

#Capturing image

#vid = cv2.VideoCapture(0)
#ret, frame = vid.read()


path = "doraemon.jpg"





#############################BACK GROUND REMOVAL################################################

#fgbg = cv2.createBackgroundSubtractorMOG2()

#frame = fgbg.apply(frame)



###########################################    PROCESSING IMAGE       ###############################################

#imgray = frame
imgray = cv2.imread(path,0)

p = 0.4
w = imgray.shape[1]
h = imgray.shape[0]
nw = int(w*p)
nh = int(h*p)

#print(w,h)



screen.setworldcoordinates(0, 0, nw+100, nh+100)

imgray = cv2.resize(imgray, (nw,nh))
imgray = cv2.rotate(imgray, cv2.ROTATE_180)

#imgray = cv2.GaussianBlur(imgray, (3,3), 0) #Blurring
#imgray = cv2.Canny(image=imgray, threshold1=100, threshold2=200) # Canny Edge Detection

graynot = cv2.bitwise_not(imgray)
imgrayblur = cv2.GaussianBlur(graynot, (21,21), sigmaX = 0, sigmaY = 0)
imgray = cv2.divide(imgray, 255 - imgrayblur, scale = 256)


################################  VISULISATION IMAGE     ######################################
#c = frame
c = cv2.imread(path)
c = cv2.resize(c, (nw, nh))



######################################         CONTOURS     #####################


ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)




#cv2.drawContours(c, contours, 1, (0, 255, 0), 3)


prev = cv2.rotate(imgray, cv2.ROTATE_180)
cv2.imshow('Image', prev)
#cv2.imshow('Image', frame)


cv2.waitKey(0)
cv2.destroyAllWindows()

def draw(arr):
    turtle.penup()
    for i in range(len(arr)):
        
        turtle.goto(arr[i][0],arr[i][1])
        turtle.pendown()



for j in range(len(contours)):
    arr = []
    for i in contours[j]:
        
        arr.append(i[0])
        #print(i[0])

    draw(arr)









 






