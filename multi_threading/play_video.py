import cv2, numpy as np, multiprocessing, math


def getFrame(frame_queue, lock):
    cap = cv2.VideoCapture(0)
    lower_color = np.array([20, 45, 80])
    upper_color = np.array([40, 130, 220])
    while True:
        if not frame_queue.full():
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            blur = cv2.GaussianBlur(hsv, (15, 15), 0)
            mask = cv2.inRange(blur, lower_color, upper_color)
            lock.acquire()
            frame_queue.put(mask)
            lock.release()
        cv2.imshow("frame",frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def drawFrame(frame_queue, lock):
    height = 480
    width = 360
    while True:
        if not frame_queue.empty():
            lock.acquire()
            mask = frame_queue.get()
            lock.release()
            _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours):
                filter(lambda a: cv2.contourArea(a) > 500, contours)
                c = sorted(contours, key=cv2.contourArea)[::-1]
                for contour in c[0:1:]:
                    x, y, w, h = cv2.boundingRect(contour)
                    cxrc = ((2*x+w)/2)-(width/2)
                    cyrc = (height / 2)-((2 * y + h) / 2)
                    dist = math.sqrt(w ** 2 + h ** 2)
                    print(cxrc, cyrc)
                cv2.imshow("frame", mask)
        else:
            pass
        k = cv2.waitKey(1)
        if k == 27:
            break
        else:
            pass
    cv2.destroyAllWindows()


if __name__ == "__main__":
    frame_queue = multiprocessing.Queue(20)
    lock = multiprocessing.Lock()
    getFrameProcess = multiprocessing.Process(target=getFrame, args=(frame_queue, lock))
    drawFrameProcess = multiprocessing.Process(target=drawFrame, args=(frame_queue, lock))
    getFrameProcess.start()
    drawFrameProcess.start()
    getFrameProcess.join()
    drawFrameProcess.join()
