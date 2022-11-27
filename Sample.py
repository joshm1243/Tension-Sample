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
            print(middle)
            sample = CV.circle(sample,middle,component["radius"],Colour.Render(component["colour"]),-1)

    return sample

sample = NewSample()
backgroundColour = "black"
components = []
while True:
    description = input("> ")
    newBackgroundColour, newComponents = Language.Parse(description)
    if newBackgroundColour is not None:
        backgroundColour = newBackgroundColour
    components.extend(newComponents)
    sample = RenderBackground(sample,backgroundColour)
    sample = RenderComponents(sample,components)
    CV.imshow("image",sample)
    CV.waitKey(33)



# print("# Background Colour:",backgroundColour)
# print("--------------------------")

# for component in components:
#     print("# Component")
#     print("Shape:",component["shape"])
#     print("Colour:",component["colour"])
#     if component["shape"] == "circle":
#         print("Point:",component["points"][0])
#         print("Radius:",component["radius"])
#     else:
#         print("Start Point:",component["points"][0])
#         print("End Point:",component["points"][1])
#     print("--------------------------")