import numpy as NP
import cv2 as CV
import Language
import Grid

import Colour

def NewSample():
    return NP.zeros((128, 128, 3))

def RenderBackground(sample,backgroundColour):
    for x in range(0,128):
        for y in range(0,128):
            sample[x][y] = Colour.Render(backgroundColour)
    return sample

def RenderComponents(sample,components):

    for component in components:

        if component["shape"] == "square":
            topLeft,topRight = Grid.GetRectangleCoordinates(component["points"])
            sample = CV.rectangle(sample,topLeft,topRight,Colour.Render(component["colour"]),-1)
        else:
            middle = Grid.GetCircleCoordinates(component["points"])
            sample = CV.circle(sample,middle,component["radius"],Colour.Render(component["colour"]),-1)

    return sample

def RenderImage(sample):
    image = NewSample()
    for x in range(0,128):
        for y in range(0,128):
            image[x][y] = Colour.ConvertToRGB(sample[x][y])
    return image

sample = NewSample()
backgroundColour = "black"
components = []

while True:

    description = input("> ")
    if description == "save":
        imageName = input("Save Name > ")
        image = RenderImage(sample)
        CV.imwrite("output/" + imageName + ".png",image)
        sample = NewSample()
        components = []
        backgroundColour = "black"

    else:

        newBackgroundColour, newComponents = Language.Parse(description)
        if newBackgroundColour is not None:
            backgroundColour = newBackgroundColour
        components.extend(newComponents)
        sample = RenderBackground(sample,backgroundColour)
        sample = RenderComponents(sample,components)

    imS = CV.resize(sample, (512, 512))         
    CV.imshow("output", imS)        
    CV.waitKey(300)    


