# from kraken import binarization
# from PIL import Image
# from pyzbar.pyzbar import decode
# from pyzbar.pyzbar import ZBarSymbol
# import cv2
# image_path = "20220707_130314.jpg"
# # img =cv2.imread("20220707_130314.jpg")
# # image_path='download.png'
# # binarization using kraken
# im = Image.open(image_path)
# bw_im = binarization.nlbin(im)
# # zbar
# dec = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
# print('decode',dec)

import cv2
import numpy as np

# Load image, grayscale, median blur, sharpen image
# image = cv2.imread('20220707_130314.jpg')
# image = cv2.imread('download.jpeg')
img = cv2.imread('crop.jpg')

# res = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.imread('download1.jpeg')
res = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)

gray_img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for cnt in cnts:
    approx = cv2.contourArea(cnt)
    # print(approx)

blur = cv2.medianBlur(gray, 5)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

# Threshold and morph close
thresh = cv2.threshold(sharpen, 160, 255, cv2.THRESH_BINARY_INV)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# Find contours and filter using threshold area
cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 100
max_area = 1500
image_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area and area < max_area:
        x,y,w,h = cv2.boundingRect(c)
        ROI = img[y:y+h, x:x+w]
        cv2.imwrite('ROI_{}.png'.format(image_number), ROI)
        cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
        image_number += 1

cv2.imshow('sharpen', sharpen)
cv2.imshow('close', close)
cv2.imshow('thresh', thresh)
# cv2.imshow('image', img)
cv2.imshow('image', res)
cv2.imshow('Binary',thresh_img)
cv2.waitKey()


# import cv2
# import numpy as np

# fileName = ['9','8','7','6','5','4','3','2','1','0']

# # img = cv2.imread('20220707_130314.jpg')

# # img = cv2.imread('download1.jpeg')
# img = cv2.imread('crop.jpg')

# # res = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.bilateralFilter(gray, 11, 17, 17)

# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(gray,kernel,iterations = 2)
# kernel = np.ones((4,4),np.uint8)
# dilation = cv2.dilate(erosion,kernel,iterations = 2)

# edged = cv2.Canny(dilation, 30, 200)

# contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# rects = [cv2.boundingRect(cnt) for cnt in contours]
# rects = sorted(rects,key=lambda  x:x[1],reverse=True)

# i = -1
# j = 1
# y_old = 5000
# x_old = 5000
# for rect in rects:
#     x,y,w,h = rect
#     area = w * h

#     if area > 47000 and area < 70000:

#         if (y_old - y) > 200:
#             i += 1
#             y_old = y

#         if abs(x_old - x) > 300:
#             x_old = x
#             x,y,w,h = rect

#             out = img[y+10:y+h-10,x+10:x+w-10]
#             # res = cv2.resize(out, (0, 0), fx = 0.1, fy = 0.1)
            
#             cv2.imwrite('/cropped/' + fileName[i] + '_' + str(j) + '.jpg', out)
#             j+=1
            
# cv2.imshow('edged',edged)
# cv2.imshow('erosion', erosion)
# cv2.imshow('res', img)

# cv2.waitKey()
