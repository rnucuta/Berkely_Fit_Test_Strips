import numpy as np 
import cv2
import math

def drawMarkers(filename, color):
	#reading default image
	rgb = cv2.imread(filename)

	#changing color space to hsv
	hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

	#storing the value of pink
	pink = np.uint8([[color]])


	#filtering out everything that isn't pink and greating a binary mask
	hsv_pink = cv2.cvtColor(pink, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, np.array([hsv_pink[0][0][0]-10, 100, 100]), np.array([hsv_pink[0][0][0]+10, 255, 255]))
	#applying the mask to the rgb image
	res_rgb = cv2.bitwise_and(rgb,rgb, mask= mask)
	#applying the mask to the hsv image
	res_hsv = cv2.bitwise_and(hsv,hsv, mask= mask)

	b=[]
	g=[]
	r=[]
	h=[]
	s=[]
	v=[]

	#iterating through the masked rgb image
	for i in range(res_rgb.shape[0]):
		for j in range(res_rgb.shape[1]):
			if(res_rgb[i][j][0]!=0 and res_rgb[i][j][1]!=0 and res_rgb[i][j][2]!=0):
				b.append(res_rgb[i][j][0])
				g.append(res_rgb[i][j][1])
				r.append(res_rgb[i][j][2])
	#iterating through the masked hsv image
	for i in range(res_hsv.shape[0]):
		for j in range(res_hsv.shape[1]):
			if(res_hsv[i][j][0]!=0 and res_hsv[i][j][1]!=0 and res_hsv[i][j][2]!=0):
				h.append(res_hsv[i][j][0])
				s.append(res_hsv[i][j][1])
				v.append(res_hsv[i][j][2])

	#takes average of the rgb color
	print("R: {}".format(np.average(r)))
	print("G: {}".format(np.average(g)))
	print("B: {}".format(np.average(b)))

	#takes average of the hsv values and converts them from OpenCV's way of storing them (H: 0 - 180, S: 0 - 255, V: 0 - 255) 
	#to the conventional way (H = 0-360, S = 0-100 and V = 0-100)
	print("H: {}".format(np.average(h)*2))
	print("S: {}".format(np.average(s)*0.39215686274))
	print("V: {}".format(np.average(v)*0.39215686274))

	#cv2.imshow("hsv", hsv)
	#cv2.imshow("mask", mask)
	cv2.imshow("res", res_rgb)
	cv2.waitKey(0)


drawMarkers("PATH_TO_IMAGE", COLOR_VALUES)	

#pink color value: (170, 161, 203)
#yellow color value: (60, 156, 164)