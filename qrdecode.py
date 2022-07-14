# pip install pypng

# import pyqrcode
# qr = pyqrcode.create("Icard")
# qr.png("stuid156.jpg", scale=6)

# from PIL import Image
# from pyzbar.pyzbar import decode
# data = decode(Image.open('stuid156.jpg'))
# # data = decode(Image.open('download.jpeg'))
# print(data)

# pip install id-card-extractor


import cv2
# # Name of the QR Code Image file
# filename = "download.png"
# # read the QRCODE image
# image = cv2.imread(filename)
# # initialize the cv2 QRCode detector
# detector = cv2.QRCodeDetector()
# # detect and decode
# data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
# # if there is a QR code
# # print the data
# if vertices_array is not None:
#   print("QRCode data:")
#   print(data)
# else:
#   print("There was some error") 

import os
import pytesseract
import re
from PIL import Image
import ftfy

def data_extraction_with_cleaning(path,file_name,threshold,preprocess_resize,filtering):
    """This function will do data extraction along with image preprocessing"""
    image = cv2.imread(path+file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # check to see if we should apply thresholding to preprocess the
    # image
    if threshold == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    elif threshold == "adaptive":
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
   
    if preprocess_resize == "linear":
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    
    elif preprocess_resize == "cubic":
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # make a check to see if blurring should be done to remove noise, first is default median blurring
    
    
    if filtering == "blur":
        gray = cv2.medianBlur(gray, 3)
    
    elif filtering == "bilateral":
        gray = cv2.bilateralFilter(gray, 9, 75, 75)
    
    elif filtering == "gauss":
        gray = cv2.GaussianBlur(gray, (5,5), 0)
    else:
        pass
    
    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')
    text = re.sub(r'[^\da-zA-Z0-9_() \n]+', '', text)
    # text = text.replace('\n', ' ')
    
    # add +hin after eng within the same argument to extract hindi specific text - change encoding to utf-8 while writing
    os.remove(filename)
    # print(text)
    
    # show the output images
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)
    
    # writing extracted data into a text file
    text_output = open('outputbase1.txt', 'w', encoding='utf-8')
    text_output.write(text)
    text_output.close()
    
    file = open('outputbase1.txt', 'r', encoding='utf-8')
    text = file.read()
    # print(text)
    
    # Cleaning all the gibberish text
    text = ftfy.fix_text(text)
    text = ftfy.fix_encoding(text)
    return text

text_passport_can = data_extraction_with_cleaning('/home/mr-computer/ML/I_card_detection/QRdecode/','stuid156.jpg','thresh','linear','blur')