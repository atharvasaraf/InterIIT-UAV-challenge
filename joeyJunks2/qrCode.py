import cv2
import Image
import zbar
import sys

class ImageSource(object):
    def __init__(self,source):
        self.is_camera = type(source)==int
        if self.is_camera:
            self.source = cv2.VideoCapture(source)
        else:
            self.source = cv2.imread(source,1)

    def get_size(self):
        if self.is_camera:
            return (int(self.source.get(3)),int(self.source.get(4)))
        else:
            return (self.source.shape[1],self.source.shape[0])

    def get_next(self):
        if self.is_camera:
            return self.source.read()[1]
        else:
            return self.source

    def release(self):
        if self.is_camera:
            self.source.release()

class QRScanner(object):
    def __init__(self, width, height):
        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config('enable')
        self.width = width
        self.height = height

    def get_qrcodes(self, image):
        zbar_img = self.cv2_to_zbar_image(image)
        self.scanner.scan(zbar_img)
        result=[]
        for symbol in zbar_img:
            if symbol.type!=zbar.Symbol.QRCODE: continue
            fixed_data = symbol.data.decode("utf8").encode("shift_jis").decode("utf8")

            result.append((fixed_data,symbol.location))
        del(zbar_img)
        return result

    def cv2_to_zbar_image(self, cv2_image):
        return zbar.Image(self.width, self.height, 'Y800',cv2_image.tostring())

pil = Image.open(sys.argv[1]).convert('L')
width, height = pil.size
scanner = QRScanner(width,height)
print scanner.get_qrcodes(pil)