def GetShape(tokens):
    if "circle" in tokens:
        return "circle"
    else:
        return "square"

def GetRadius(tokens):
    for token in tokens:
        if token.isnumeric():
            return token
    return None

def GetPoints(tokens):
    points = []
    for token in tokens:
        if len(token) == 2 and token[0] >= "A" and token[0] <= "G":
            if token[1] >= "A" and token[1] <= "G":
                points.append(token)
    return points


def GetColour(tokens):
    if "red" in tokens:
        return "red"
    elif "green" in tokens: 
        return "green"
    elif "blue" in tokens:
        return "blue"
    elif "cyan" in tokens:
        return "cyan"
    elif "yellow" in tokens:
        return "yellow"
    elif "purple" in tokens:
        return "purple"
    elif "white" in tokens:
        return "white"
    elif "black" in tokens:
        return "black"
    else:
        return None


def IsBackground(tokens):
    if len(tokens) == 1:
        return True

def Parse(description):

    backgroundColour = None
    components = []

    ## Description
    sampleArray = description.strip().split("with")
    
    ## Component Description
    for componentText in sampleArray:
        componentTokens = componentText.strip().split(" ")

        if IsBackground(componentTokens):
            backgroundColour = GetColour(componentTokens)
        else:
            component = {}
            component["shape"] = GetShape(componentTokens)
            component["colour"] = GetColour(componentTokens)

            points = GetPoints(componentTokens)

            ## The component is a circle
            if component["shape"] == "circle":
                if len(points) > 1 or len(points) == 0:
                    raise ValueError("Incorrect Number of Points for Component 'Circle'. Expected: 1, got " + str(len(points)) + ".")
                else:
                    component["points"] = [points[0]]

                radius = GetRadius(componentTokens)
                if radius is None:
                    raise ValueError("Radius Not Provided for Component 'Circle'.")
                else:
                    component["radius"] = int(radius)

            ## The component is a square
            else:

                if len(points) == 2:
                    if points[0] < points[1]:
                        component["points"] = [points[0],points[1]] 
                    else:
                        component["points"] = [points[1],points[0]]

                elif len(points) == 1:
                    component["points"] = [points[0]]
                else:
                    raise ValueError("Incorrect Number of Points for Component 'Square'. Expected 2, got " + str(len(points)) + ".")

            components.append(component)

    return backgroundColour, components

