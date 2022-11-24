import cv2




import numpy as np
import cv2
import random
import os

IMAGE_HEIGHT = 128
IMAGE_WIDTH = 128

def CreateDirectory(directoryName):
    os.mkdir(directoryName)
    

def CreateLabelFile(filename,content):
    file = open(filename + ".txt","w")
    file.write(content)
    file.close()
#6
def GetLabelOpening():
    label = "a "
    label += random.choice(["slightly blurry ","","blurry ","faded ","slightly faded "]) 
    label += random.choice(["bright ","white "])
    return label

## Generates an image of stage left
def GetStageLeftImage():
    image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH))
    splitX = random.randint(40,90)

    label = GetLabelOpening()
    label += random.choice(["left side of stage ","stage left ", "left side of the stage "])

    print(splitX)


    if splitX > 85:
        label += "with a substantially narrow acting space"
    elif splitX > 80:
        label += "with a very narrow acting space"
    elif splitX > 75:
         label += "with quite a narrow acting space"
    elif splitX > 70:
         label += "with a slightly narrow size acting space"
    elif splitX > 65:
        label += "with a normal size acting space"
    elif splitX > 60:
        label += "with a slightly wide acting space"
    elif splitX > 55:
        label += "with quite a wide acting space"
    elif splitX > 50:
        label += "with a very wide acting space"
    else:
        label += "with a substantially wide acting space"

    for x in range(0,IMAGE_WIDTH):
        for y in range(0,IMAGE_HEIGHT):

            leftBlurOffset = random.randint(0,10)
            rightBlurOffset = random.randint(0,10)
            pixelX = random.randint(splitX - leftBlurOffset, splitX + rightBlurOffset)

            if x > pixelX: 
                image[y,x] = 255

    return image,label


## Generates an image of stage right
def GetStageRightImage():
    image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH))
    splitX = random.randint(40,90)

    label = GetLabelOpening()
    label += random.choice(["right side of stage ","stage right ", "right side of the stage "])

    if splitX < 50:
        label += "with an substantially narrow acting space"
    elif splitX < 55:
        label += "with a very narrow acting space"
    elif splitX < 60:
        label += "with quite a narrow acting space"
    elif splitX < 65:
        label += "with a slightly narrow size acting space"
    elif splitX < 70:
        label += "with a normal size acting space"
    elif splitX < 75:
        label += "with a slightly wide acting space"
    elif splitX < 80:
        label += "with quite a wide acting space"
    elif splitX < 85:
        label += "with a very wide acting space"
    else:
        label += "with a substantially wide acting space"

    for x in range(0,IMAGE_WIDTH):
        for y in range(0,IMAGE_HEIGHT):

            leftBlurOffset = random.randint(0,10)
            rightBlurOffset = random.randint(0,10)
            pixelX = random.randint(splitX - leftBlurOffset, splitX + rightBlurOffset)

            if x < pixelX: 
                image[y,x] = 255

    return image,label

## Generates an image of center stage
def GetCenterStageImage():
    image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH))
    leftSplitX = random.randint(20,40)
    rightSplitX = random.randint(80,100)

    label = GetLabelOpening()

    label += random.choice(["center spot ","spot in the middle of the stage ", "spot in the center of the stage "])

    distance = rightSplitX - leftSplitX
    

    if distance < 40:
        label += "with an substantially narrow acting space"
    elif distance < 45:
        label += "with a very narrow acting space"
    elif distance < 50:
        label += "with quite a narrow acting space"
    elif distance < 55:
        label += "with a slightly narrow size acting space"
    elif distance < 60:
        label += "with a normal size acting space"
    elif distance < 65:
        label += "with a slightly wide acting space"
    elif distance < 70:
        label += "with quite a wide acting space"
    elif distance < 75:
        label += "with a very wide acting space"
    else:
        label += "with a substantially wide acting space"
    
    for x in range(0, IMAGE_WIDTH):
        for y in range(0, IMAGE_HEIGHT):

            leftBlurLeftOffset = random.randint(0,10)
            leftBlurRightOffset = random.randint(0,10)

            rightBlurLeftOffset = random.randint(0,10)
            rightBlurRightOffset = random.randint(0,10)

            leftPixelX = random.randint(leftSplitX - leftBlurLeftOffset, leftSplitX + leftBlurRightOffset)
            rightPixelX = random.randint(rightSplitX - rightBlurLeftOffset, rightSplitX + rightBlurRightOffset)

            if x > leftPixelX and x < rightPixelX:
                image[y,x] = 255

    return image,label

## Generates an image of the center spot
def GetCenterSpotImage():

    image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH))
    leftSplitX = random.randint(20,40)
    rightSplitX = random.randint(80,100)
    topSplitY = random.randint(80,100)
    bottomSplitY = random.randint(20,40)

    distance = rightSplitX - leftSplitX


    label = GetLabelOpening()
    label += random.choice(["center stage ","stage center ", "the center of the stage "])

    if distance < 40:
        label += "with an substantially narrow acting space"
    elif distance < 45:
        label += "with a very narrow acting space"
    elif distance < 50:
        label += "with quite a narrow acting space"
    elif distance < 55:
        label += "with a slightly narrow size acting space"
    elif distance < 60:
        label += "with a normal size acting space"
    elif distance < 65:
        label += "with a slightly wide acting space"
    elif distance < 70:
        label += "with quite a wide acting space"
    elif distance < 75:
        label += "with a very wide acting space"
    else:
        label += "with a substantially wide acting space"

    
    for x in range(0, IMAGE_WIDTH):
        for y in range(0, IMAGE_HEIGHT):

            ## Generating the X values

            leftBlurLeftOffset = random.randint(0,10)
            leftBlurRightOffset = random.randint(0,10)

            rightBlurLeftOffset = random.randint(0,10)
            rightBlurRightOffset = random.randint(0,10)

            leftPixelX = random.randint(leftSplitX - leftBlurLeftOffset, leftSplitX + leftBlurRightOffset)
            rightPixelX = random.randint(rightSplitX - rightBlurLeftOffset, rightSplitX + rightBlurRightOffset)


            ## Generating the Y values

            topBlurTopOffset = random.randint(0,10)
            topBlurBottomOffset = random.randint(0,10)

            bottomBlurTopOffset = random.randint(0,10)
            bottomBlurBottomOffset = random.randint(0,10)

            topPixelY = random.randint(topSplitY - topBlurBottomOffset, topSplitY + topBlurTopOffset)
            bottomPixelY = random.randint(bottomSplitY - bottomBlurBottomOffset, bottomSplitY + bottomBlurTopOffset)
            
            if x > leftPixelX and x < rightPixelX and y < topPixelY and y > bottomPixelY:
                image[y,x] = 255

    return image,label

directoryName = "./../dalle_test/igc_stage_samples/"

START_OFFSET = 3000

CreateDirectory(directoryName)
    
for i in range(0,500):
    image,label = GetStageRightImage()
    filename = str(i + START_OFFSET)
    CreateLabelFile(directoryName + filename,label)    
    cv2.imwrite(directoryName + filename + ".png",image)
