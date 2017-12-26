import zbar
import Image
import cv2

# create a reader
scanner = zbar.ImageScanner()
# configure the reader
scanner.parse_config('enable')
#create video capture feed
cap = cv2.VideoCapture(0)

while(True):
    ret, cv = cap.read()
    cv = cv2.cvtColor(cv, cv2.COLOR_BGR2GRAY, dstCn=0)
    pil = Image.fromarray(cv)
    width, height = pil.size
    raw = pil.tobytes()
    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)
    cv2.imshow('frame',cv)
    # extract results
    for symbol in image:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
print "/n ...Done"