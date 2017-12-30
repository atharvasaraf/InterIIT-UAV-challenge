import cv2,numpy,qrtools,os



def ScanQr():
    qr = qrtools.QR()
    print "thresholdValue : 140 (default)"
    cap = cv2.VideoCapture(1)
    i = 1
    while True:
        _, frame = cap.read()
        cv2.imshow('frame',frame)
        cv2.imwrite('img.png',frame)
        if qr.decode('img.png'):
            print "data : ", qr.data
            print i
            i += 1
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        k=cv2.waitKey(1)
        if k == 27 :
            break
        else:
            pass
    cap.release()
    cv2.destroyAllWindows()
    os.remove("img.png")


ScanQr()