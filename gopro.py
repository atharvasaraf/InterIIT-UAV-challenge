import cv2
import time


camera = cv2.VideoCapture("udp://10.5.5.9:8554")
time.sleep(5)



while True:
    _, frame = camera.read()
    cv2.imshow("frame", frame)
    if not _:
        print("nothing grabbed")
        break
    else:
        cv2.imshow("frame",frame)