import numpy as np
import cv2

#add here the location of your file
img = cv2.imread('/home/nilesh/Desktop/Work/OpenCV/loadingImages/watch.jpg',cv2.IMREAD_COLOR)

px = img[55,55]

#now if we want to superimpose our operation on the image we do like

#img[55,55] = [255,255,255]

print(px)

#roi = region of image : gives in output all the pixels that are in the image (coordinates of every pixel in matrix form)

#roi = img[100:150, 100:150] = [255,255,255]

#print(roi) - #uncomment to get all the pixel value coordinates output in the terminal and a 
#filled region of image with white colour with given coordinates position

watch_face = img[37:111, 107:194]

img[0:74, 0:87] = watch_face
 
#above two statement is copying the coordinates mentioned in the region of image (roi)
#matrix and hence pasting it with the help of second line of code :)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
