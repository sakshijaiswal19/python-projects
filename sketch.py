from email.mime import image
import cv2
image=cv2.imread("./favicom.ico")
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted_img=255-gray_img
blurred=