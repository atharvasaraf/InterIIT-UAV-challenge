import cv2,numpy,qrtools,os


<<<<<<< HEAD
class QrCode:
    def ScanQr(self):
        qr = qrtools.QR()
        thresholdValue = 140;
        print "thresholdValue : 140 (default)"
        cap = cv2.VideoCapture(1)
        i = 1
        while True:
            ret,frame = cap.read()
            grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            retval, threshold = cv2.threshold(grayscaled, thresholdValue, 255, cv2.THRESH_BINARY)
            # th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
            # cv2.imshow('frame',frame)
            # cv2.imshow('th',th)
            cv2.imshow('threshold',frame)
            cv2.imwrite('img.png',frame)
            if qr.decode('img.png'):
                print "data : ",qr.data
                print i
                i += 1
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            k=cv2.waitKey(1)
            if k == 27 :
                break
            elif k == -1 :
                pass
            elif k == 82 :
                if thresholdValue <255 :
                    thresholdValue += 1
                    print "threshold : ",thresholdValue
                else :
                    print "Max threshold"
            elif k == 84 :
                if thresholdValue >0 :
                    thresholdValue -= 1
                    print "threshold : ",thresholdValue
                else :
                    print "Min threshold"
            else :
                # print K
                pass
        cap.release()
        cv2.destroyAllWindows
        os.remove("img.png")
=======

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
>>>>>>> 2a6a446d3f040f7ecf67d87807da479687ae5c09