import cv2
import sys
import opencv


#return verctor for centring and 
#	size of rectangle for measuring distance as a proportion between distance and size of rectangle
def img_process(frame):

	faces = opencv.detect_faces(frame)

	main_rect = (0, 0)

	sum_sqr_rect = 0
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		main_rect = (main_rect[0] + x + w/2, main_rect[1] + y + h/2)
		sum_sqr_rect += w*h
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	if 0 != len(faces):
		main_rect = (main_rect[0]/len(faces),main_rect[1]/len(faces))
	else:
		return 0
	w, h = frame.shape[:2]
	
	return main_rect[0]-h/2, main_rect[1]-w/2, sum_sqr_rect

#compare two images
def img_compare(frame1, frame2):
	import numpy
	frame1 = cv2.imread('5.jpg')
	frame2 = cv2.imread('4.jpg')
	th, tw = frame2.shape[:2]

	#get array of matching
	result = cv2.matchTemplate(frame1, frame2, cv2.TM_CCORR_NORMED)
	num = 0
	n = 0
	for i in result:
		num += reduce(lambda x, y: x + y, i) / len(i)
		n+=1
	num/=n

	print num

video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
print img_process(frame)
cv2.imwrite('test.jpeg', frame)