import cv2

img = cv2.imread('/home/nilesh/Desktop/Work/OpenCV/watch.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()