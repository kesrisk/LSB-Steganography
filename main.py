from PIL import Image
import binascii
import cv2
import numpy
import math
import os
import shutil
import hashlib





def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def hex2rgb(hexcode):
    h = hexcode.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def str2bin(message):
    message = message.encode("ASCII")
    binary = bin(int(binascii.hexlify(message), 16))
    return binary[2:]


def bin2str(binary):
    message = binascii.unhexlify('%x'%(int('0b' + binary, 2)))
    return message.decode("ASCII")



def encode(hexcode, digit):
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        hexcode = hexcode[:-1] + digit
        return hexcode
    else:
        return None


def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    else:
        return None


def hide(filename):
    root_dir = os.getcwd()
    os.chdir(os.getcwd()+"/Input")
    if filename not in os.listdir():
        return filename + " Not found"

    os.chdir(os.getcwd() + "/"+ filename)
    img = Image.open(filename+".png")
    file = open("message.txt", "r")
    message = file.read()
    # print(type(message))
    binary = str2bin(message) + '1111111111111110'
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()    # this will store RGBA of each pixel in a list object

        new_data = []
        message_bit_count = 0
        temp = ''
        for item in datas:
            if message_bit_count < len(binary):
                newpixel = encode(rgb2hex(item[0], item[1], item[1]), binary[message_bit_count])

                if newpixel == None:
                    new_data.append(item)
                else:
                    r, g, b = hex2rgb(newpixel)
                    new_data.append((r, g, b, 255))
                    message_bit_count += 1
            else:
                
                new_data.append(item)
        img.putdata(new_data)
        # new_filename = str(filename[:-4] + "_new" + ".png")
        os.chdir(root_dir + "/Output")

        new_dir = os.getcwd() + "/"+filename
        if filename in os.listdir():
            shutil.rmtree(new_dir)
        os.mkdir(new_dir)
        os.chdir(new_dir)
        img.save(filename+".png", "PNG")

        # print(sum([ord(c) for c in message]))

        f = open("log.txt", "w+")
        # h=hash(message)
        h =  hashlib.sha256(message.encode())

        f.write(h.hexdigest())
        f.close()
        return "Completed"
    return "Incorrect image mode, couldn't hide"


def retrive_message(filename):
    os.chdir(os.getcwd() + "/Output")
    if filename not in os.listdir():
        return ("No message is hidden in the "+ filename + " or log.txt is missing")
    # if "log.txt" not in os.listdir():
    #     return "log.txt not found"
    os.chdir(os.getcwd()+"/"+filename)
    f = open("log.txt", "r")            #Reads the log file for the comparishion
    hashed_message = f.read()
    f.close()
    # print(hashed_message)
    img = Image.open(filename+".png")
    binary = ''

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        for item in datas:
            message_bit = decode(rgb2hex(item[0], item[1], item[2]))
            if message_bit == None:
                pass
            else:
                binary = binary + message_bit
                if binary[-16:] == '1111111111111110':
                    # print ("Success")
                    message = bin2str(binary[:-16])

                    # print(h)
                    # os.chdir(os.getcwd() + "/Output")
                    # message = bin2str(binary)
                    # sum(bytearray(message))

                    # print(sum([ord(c) for c in message]))

                    fl = open('result.txt', 'w+')
                    fl.write(message)
                    fl.close()
                    ##### data from result.txt in output folder
                    f_out = open('result.txt', 'r')
                    f_out_data = f_out.read()
                    f_out.close()
                    f_out_data_hash = hashlib.sha256(f_out_data.encode())
                    if f_out_data_hash.hexdigest() == hashed_message:
                        print("Data Integrity is confirmed")
                    else:
                        print("Data Integrity is not confirmed")
                    return "Hidden message is => "+message
        # os.chdir(os.getcwd()+"/Output")
        message = bin2str(binary)
        # numpy.frombuffer(message, "uint8").sum()
        # print(sum([ord(c) for c in message]))
        fl = open('result.txt', 'w+')
        fl.write(message)
        fl.close()
        ##### data from result.txt in output folder
        f_out = open('result.txt', 'r')
        f_out_data = f_out.read()
        f_out.close()
        f_out_data_hash = hashlib.sha256(f_out_data.encode())
        if f_out_data_hash.hexdigest() == hashed_message:
            print("Data Integrity is confirmed")
        else:
            print("Data Integrity is not confirmed")
        return "Hidden message is => " + message
    return ("Incorrect Image mode, Couldn't retrieve.")


def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))




# hide('picture.png', 'shivam')
# print (rgb2hex(255, 255, 255))
def main():
	
    root_directory_main = os.getcwd()
    print ("#####################################")
    print ("Hello! Welcome to LSB Steganography..")
    print ("##################################### \n \n \n")
    print ("Available options: \n 1) Hide message in Image \n 2) Decode message from the Image \n 3) Calculate PSNR\n 4) Project advisor   \n 5) submitted by")
    case = int(input("Select one option: "))
    print ("\n \n")
    if case == 1:
        if "Output" not in os.listdir():
            os.mkdir(os.getcwd() + "/Output")
        filename = input("Enter filename: ")
        # message = input("Enter message: ")
        print (hide(filename))

    elif case == 2:
        filename = input("Enter filename: ")
        # print (filename)
        print( end = "")
        print(retrive_message(filename))

    elif case == 4:
        print ("Project Advisor: \n Miss Shikha Goswami \n Assistant professor, \n Dept. of Information Technology \n College of Technology, GBPUA&T")

    elif case == 3:
        img = input("Please Enter the name of original picture: ")
        # new_img = input("Please Enter the name of new image: ")

        os.chdir(root_directory_main + "/Input")
        if img not in os.listdir():
            print("File is not present in Input folder")
            print(" \n")
            print("######################################")
            print("               THANK YOU")
            print("######################################")
            exit()
        else:
            os.chdir(os.getcwd()+"/"+img)
            original = cv2.imread(img+".png")

        os.chdir(root_directory_main + "/Output")
        if img not in os.listdir():
            print("File is not present in output folder")
            print(" \n")
            print("######################################")
            print("               THANK YOU")
            print("######################################")
            exit()
        os.chdir(os.getcwd() + "/" + img)
        newImg = cv2.imread(img+".png", 1)

        print("The PSNR ration between original vs new photo is : " + str(psnr(original,newImg)))

    elif case == 5:
        print ("Submitted by: \n 1) Nitin Pal           49136 \n 2) Shivam Kesarwani    49110 \n 3) Aman Singh Rautella 50684\n 4) Gaurav Joshi        48678")

    else:
        print ("You have entered a wrong input. \n Restart the program and Enter Correct option.")

    print (" \n")
    print ("######################################")
    print ("               THANK YOU")
    print ("######################################")




if __name__ == '__main__':
    main()
    # filename = 'picture.png'
    # text = 'pal is good'
    # print(retrive_message(filename))

