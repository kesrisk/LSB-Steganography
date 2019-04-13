import numpy
import math
import cv2

def psnr(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    try:
        mse = numpy.mean((img1 - img2) ** 2 )
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return "\n \n PSNR of both the image is: "+str(20 * math.log10(PIXEL_MAX / math.sqrt(mse)))
    except:
        return "\n \n PSNR can be calculated between the images having same shape and pixel count \n" \
               "please try again with pictures with same shape."



print("\n \n##############################################")
print("         Welcome to PSNR Caluclator")
print("##############################################\n \n")
print("save both the image in the root folder before calculating the psnr ratio")
img1 = input("Enter name of 1st Image : ")
img2 = input("Enter name of 2nd Image : ")
if len(img1) != 0 and len(img2) != None:
    print(psnr(img1,img2))
else:
    print("Name of Image cannot be left Empty. Please try again.")