import cv2 as CV
import Colour 

def Generate(sample,component):

    ## Creating a circle
    if component["shape"] == "circle":
        sample = CV.circle(sample, component["center"], component["radius"], Colour.Create(component["colour"]), -1)

    else:
        sample = CV.rectangle(sample,component["start"],component["end"],Colour.Create(component["colour"]), -1)

    return sample

