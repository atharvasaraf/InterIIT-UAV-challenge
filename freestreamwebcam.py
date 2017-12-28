import cv2
cap=cv2.VideoCapture(1)
while(True):
	ret, frame =cap.read()
	cv2.imshow('frame',frame)
	k=cv2.waitKey(1)
	if k==27 :
		break
	else:
		pass
cap.release()
cv2.destroyAllWindows()
