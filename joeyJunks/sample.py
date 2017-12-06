import qrtools
qr = qrtools.QR()
if qr.decode('./../index.jpeg'):
    print "data : ",qr.data
