# from pyzbar import pyzbar
# import argparse
# import cv2

# # Build a parameter parser and parse the parameters
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#  help="path to input image")
# args = vars(ap.parse_args())

# # Load input image
# image = cv2.imread(args["image"])

# # Locate the barcode in the image and decode it
# barcodes = pyzbar.decode(image)

# # Cycle detected barcodes
# for barcode in barcodes:
#  # The location of the bounding box from which the barcode is extracted
#  # Draw the bounding box of the barcode in the image
#     (x, y, w, h) = barcode.rect
#     x,y,w,h = cv.boundingRect(cnt)
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#     crop = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     print("crop", crop)
#     # The barcode data is a byte object, so if we want to print it on the output image
#     # To draw it, you need to convert it into a string first
#     barcodeData = barcode.data.decode("utf-8")
#     barcodeType = barcode.type

#     # Draw the barcode data and barcode type on the image
#     text = "{} ({})".format(barcodeData, barcodeType)
#     cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
#     0.5, (0, 0, 255), 2)

#     # Print barcode data and barcode type to the terminal
#     print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

# # Show output image
# im = cv2.resize(image)
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# from pyzbar import pyzbar
# import numpy as np
# import cv2

# img =cv2.imread("20220707_130314.jpg")

# # resize image
# half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
# x,y,w,h = cv.boundingRect(cnt)
# cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# # thresholds image to white in back then invert it to black in white
# #   try to just the BGR values of inRange to get the best result
# mask = cv2.inRange(half,(0,0,0),(200,200,200))
# thresholded = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
# inverted = 255-thresholded # black-in-white
# # barcodes = pyzbar.decode(inverted)
# # print (barcodes)
# cv2.imshow("inverted", inverted)
# cv2.waitKey(0)

import numpy as np
import cv2
from pyzbar.pyzbar import decode

# img =cv2.imread("20220707_130314.jpg")
# img =cv2.imread("download.png")
# img =cv2.imread("crop.jpg")
img =cv2.imread("front.png")

for barcode in decode(img):
    print(barcode.data)
    myData = barcode.data.decode('utf-8')
    print(myData)
    rect_pts = barcode.rect
    if myData:
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts], True,(255,0,255), 3)
cv2.imshow('img',img)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

# while True:
#     success, img = cap.read()
    
#     for barcode in decode(img):
#         print(barcode.data)
#         myData = barcode.data.decode('utf-8')
#         print(myData)
        
#         rect_pts = barcode.rect
               
#         if myData:
#             pts = np.array([barcode.polygon], np.int32)
#             pts = pts.reshape((-1,1,2))
#             cv2.polylines(img,[pts], True,(255,0,255), 3)
#     cv2.imshow('img',img)
#     cv2.waitKey(1)
# cv2.release()

# half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
# print("code",code)
# mask = cv2.inRange(half,(0,0,0),(200,200,200))
# thresholded = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
# inverted = 255-thresholded # black-in-white