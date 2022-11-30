CONVERTION_RATE = 0.00390625

def ConvertToScale(blue,green,red):
    return [CONVERTION_RATE * blue, 
            CONVERTION_RATE * green,
            CONVERTION_RATE * red]

def ConvertToRGB(sample):
    return [
        int(sample[0] // CONVERTION_RATE),
        int(sample[1] // CONVERTION_RATE),
        int(sample[2] // CONVERTION_RATE)
    ]

def Render(colourName):

    if colourName == "lavender":
        return ConvertToScale(246,159,227)
    elif colourName == "purple":
        return ConvertToScale(128,0,128)
    elif colourName == "violet":
        return ConvertToScale(147,1,113)
    elif colourName == "mauve":
        return ConvertToScale(122,73,136)
    elif colourName == "mulberry":
        return ConvertToScale(128,0,255)
    elif colourName == "indigo":
        return ConvertToScale(130,0,75)
    elif colourName == "white":
        return ConvertToScale(255,255,255)
    elif colourName == "black":
        return ConvertToScale(0,0,0)
    elif colourName == "tangerine":
        return ConvertToScale(0,133,242)
    elif colourName == "orange":
        return ConvertToScale(0,165,255)
    elif colourName == "amber":
        return ConvertToScale(0,191,255)
    elif colourName == "bronze":
        return ConvertToScale(13,86,178)
    elif colourName == "marmalade":
        return ConvertToScale(2,96,209)
    elif colourName == "rust":
        return ConvertToScale(57,92,208)
    elif colourName == "darkblue":
        return ConvertToScale(93,30,40)
    elif colourName == "blue":
        return ConvertToScale(255,0,0)
    elif colourName == "turquoise":
        return ConvertToScale(200,213,48)
    elif colourName == "teal":
        return ConvertToScale(128,128,0)
    elif colourName == "cyan":
        return ConvertToScale(255,255,0)
    elif colourName == "navyblue":
        return ConvertToScale(128,0,0)
    elif colourName == "midnightblue":
        return ConvertToScale(112,25,25)
    elif colourName == "red":
        return ConvertToScale(0,36,255)
    elif colourName == "cherry":
        return ConvertToScale(35,11,171)
    elif colourName == "crimson":
        return ConvertToScale(60,60,220)
    elif colourName == "maroon":
        return ConvertToScale(0,0,128)
    elif colourName == "sand":
        return ConvertToScale(99,184,216)
    elif colourName == "cream":
        return ConvertToScale(208,253,255)
    elif colourName == "yellow":
        return ConvertToScale(0,239,255)
    elif colourName == "strawberry":
        return ConvertToScale(78,76,252)
    elif colourName == "sage":
        return ConvertToScale(105,140,114)
    elif colourName == "green":
        return ConvertToScale(67,176,60)
    elif colourName == "jade":
        return ConvertToScale(107,168,0)
    elif colourName == "seafoam":
        return ConvertToScale(151,237,61)
    elif colourName == "lime":
        return ConvertToScale(89,243,174)
    elif colourName == "forest":
        return ConvertToScale(30,120,11)
    elif colourName == "olive":
        return ConvertToScale(100,191,152)
    elif colourName == "emerald":
        return ConvertToScale(120,200,80)
    elif colourName == "mint":
        return ConvertToScale(195,237,153)
    elif colourName == "black":
        return ConvertToScale(0,0,0)
    elif colourName == "white":
        return ConvertToScale(255,255,255)
