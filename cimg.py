import cv2
import numpy as np
import random

IMAGE_HEIGHT = 128
IMAGE_WIDTH = 128

def RandInt(start,end):
    return random.randint(start,end)




def CreateLabelFile(filename,content):
    file = open(filename + ".txt","w")
    file.write(content)
    file.close()

def GenerateImage():

    for imageNumber in range(0,10):

        imageName = "output/" + str(imageNumber)
        image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3))

        for x in range(0,IMAGE_HEIGHT):
            for y in range(0,IMAGE_WIDTH):
                image[x][y][0] = RandInt(100,255)

        CreateLabelFile(imageName + ".txt","blue")
        cv2.imwrite((imageName + ".png"),image)


GenerateImage()

#for x in range(0,IMAGE_WIDTH):
#    for y in range(0,IMAGE_HEIGHT):

        
        


    # for x in range(0,IMAGE_WIDTH):
    #     for y in range(0,IMAGE_HEIGHT):

    #         leftBlurOffset = random.randint(0,10)
    #         rightBlurOffset = random.randint(0,10)
    #         pixelX = random.randint(splitX - leftBlurOffset, splitX + rightBlurOffset)

    #         if x > pixelX: 
    #             image[y,x] = 255
