import cv2 as cv
import numpy as np

def CreateScaleSquare(sample,component):
    sample = cv.rectangle(sample,component["startCoordinate"],component["endCoordinate"],component["colourScale"],-1)
    return sample

def CreateRGBSquare(sample,component):
    sample = cv.rectangle(sample,component["startCoordinate"],component["endCoordinate"],component["colourRGB"],-1)
    return sample

def Display(components):

    sample = np.zeros((140,140,3))

    for component in components:
        if component["type"] == "background":
            sample = CreateScaleSquare(sample,component)
    
    for component in components:
        if component["type"] == "square":
            sample = CreateScaleSquare(sample,component)

    sample = cv.resize(sample, (512, 512))   
    cv.imshow("Tension Sample",sample)
    cv.waitKey(300)


def Save(components,filePath):

    errorMessage = ""

    sample = np.zeros((140,140,3))

    for component in components:
        if component["type"] == "background":
            sample = CreateRGBSquare(sample,component)
    
    for component in components:
        if component["type"] == "square":
            sample = CreateRGBSquare(sample,component)

    cv.imwrite(filePath,sample)

    return errorMessage