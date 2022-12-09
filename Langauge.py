GRID_LINES = {
    "a" : (0,19),
    "b" : (20,39),
    "c" : (40,59),
    "d" : (60,79),
    "e" : (80,99),
    "f" : (100,119),
    "g" : (120,139)
}

def GetGridPoints(tokens):
    gridPoints = []
    for token in tokens:
        if len(token) == 2 and token[0] >= "a" and token[0] <= "g":
            if token[1] >= "a" and token[1] <= "g":
                gridPoints.append(token)
    return gridPoints

def GetGridCoordinates(topPoint,bottomPoint):
    xLeft = GRID_LINES[topPoint[0]][0]
    yTop = GRID_LINES[topPoint[1]][0]
    xRight = GRID_LINES[bottomPoint[0]][1]
    yBottom = GRID_LINES[bottomPoint[1]][1]
    topLeft = (xLeft,yTop)
    bottomRight = (xRight,yBottom)
    return topLeft,bottomRight

COLOURS = {
    "lavender" : [246,159,227],
    "purple" : [128,0,128],
    "violet" : [147,1,112],
    "mauve" : [122,73,136],
    "mulberry" : [128,0,255],
    "indigo" : [130,0,75],
    "tangerine" : [0,133,242],
    "orange" : [0,165,255],
    "amber" : [0,191,255],
    "bronze" : [13,86,178],
    "marmalade" : [2,96,209],
    "rust" : [57,92,208],
    "darkblue" : [93,30,40],
    "blue" : [255,0,0],
    "turquoise" : [200,213,48],
    "teal" : [128,128,0],
    "cyan" : [255,255,0],
    "navyblue" : [128,0,0],
    "midnightblue" : [112,25,25],
    "red" : [35,11,171],
    "cherry" : [35,11,171],
    "crimson" : [60,60,220],
    "maroon" : [0,0,128],
    "sand" : [99,184,216],
    "cream" : [208,253,255],
    "yellow" : [0,239,255],
    "white" : [255,255,255],
    "black" : [0,0,0],
    "mint" : [195,237,153],
    "emerald" : [120,200,80],
    "olive" : [100,191,152],
    "forest" : [30,120,11],
    "lime" : [89,243,174],
    "seafoam" : [151,237,61],
    "jade" : [107,168,0],
    "green" : [67,176,60],
    "sage" : [105,140,141],
    "strawberry" : [78,76,252],
}

def GetColourScale(token):
    return [0.00390625 * COLOURS[token][channel] for channel in range(0,3)]

def GetColourRGB(token):
    return COLOURS[token]

## Find all the colours in the list of tokens
def GetColours(tokens):
    colours = []
    for token in tokens:
        if token in COLOURS:
            colours.append(token)
    return colours

def Parse(command):

    components = []
    errorMessage = ""
    tokens = command.split(" ")

    if len(tokens) > 0:

        colours = GetColours(tokens)
        gridPoints = GetGridPoints(tokens)

        if len(gridPoints) == 0:

            if len(colours) < 1:
                errorMessage = "Invalid Command."


            ## There are no shapes to create components for
            ## Create a background component
            if len(colours) == 1:

                components.append({
                    "type" : "background",
                    "colour" : colours[0],
                    "colourRGB" : GetColourRGB(colours[0]),
                    "colourScale" : GetColourScale(colours[0]),
                    "startPoint" : "aa",
                    "startCoordinate" : (0,0),
                    "endPoint" : "gg",
                    "endCoordinate" : (139,139)
                })
            
            elif len(colours) > 1:
                errorMessage = "A maximum of one colour must be provided when changing the background."

        elif len(gridPoints) == 1:

            ## Create a single cell square component with a colour
            if len(colours) == 1:

                coordinates = GetGridCoordinates(gridPoints[0],gridPoints[0])

                components.append({
                    "type" : "square",
                    "colour" : colours[0],
                    "colourRGB" : GetColourRGB(colours[0]),
                    "colourScale" : GetColourScale(colours[0]),
                    "startPoint" : gridPoints[0],
                    "startCoordinate" : coordinates[0],
                    "endPoint" : gridPoints[0],
                    "endCoordinate" : coordinates[1]
                })
            
            else:
                errorMessage = "A maximum of one colour must be provided when creating a square."
            

        elif len(gridPoints) == 2:

            ## Create a square component with a colour
            if len(colours) == 1:

                coordinates = GetGridCoordinates(gridPoints[0],gridPoints[1])

                components.append({
                    "type" : "square",
                    "colour" : colours[0],
                    "colourRGB" : GetColourRGB(colours[0]),
                    "colourScale" : GetColourScale(colours[0]),
                    "startPoint" : gridPoints[0],
                    "startCoordinate" : coordinates[0],
                    "endPoint" : gridPoints[1],
                    "endCoordinate" : coordinates[1]
                })
            else:
                errorMessage = "A maximum of one colour must be provided when creating a square."
        
        else:
            errorMessage = "A maximum of two points can be specified when creating a square."

    return components, errorMessage