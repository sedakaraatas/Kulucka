from textwrap import fill
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype="uint8")
cv.imshow("Blank",blank)
#içindeki görselin boyutunu gösteren bu köşeli parantez içindeki değerler




cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=1)

cv.imshow("Text",blank)
cv.waitKey(0)