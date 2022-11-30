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

        if token == "l":
            points.extend(["AA","DG"])
        elif token == "l1":
            points.extend(["AA","BG"])
        elif token == "l2":
            points.extend(["AA","CG"])

        elif token == "r":
            points.extend(["DA","GG"])
        elif token == "r1":
            points.extend(["FA","GG"])
        elif token == "r2":
            points.extend(["EA","GG"])
 
    return points

def GetColour(tokens):


    if "lavender" in tokens:
        return "lavender"
    elif "purple" in tokens:
        return "purple"
    elif "violet" in tokens:
        return "violet"
    elif "mauve" in tokens:
        return "mauve"
    elif "mulberry" in tokens:
        return "mulberry"
    elif "indigo" in tokens:
        return "indigo"
    elif "white" in tokens:
        return "white"
    elif "black" in tokens:
        return "black"
    elif "tangerine" in tokens:
        return "tangerine"
    elif "orange" in tokens:
        return "orange"
    elif "amber" in tokens:
        return "amber"
    elif "bronze" in tokens:
        return "bronze"
    elif "marmalade" in tokens:
        return "marmalade"
    elif "rust" in tokens:
        return "rust"
    elif "darkblue" in tokens:
        return "darkblue"
    elif "blue" in tokens:
        return "blue"
    elif "turquoise" in tokens:
        return "turquoise"
    elif "teal" in tokens:
        return "teal"
    elif "cyan" in tokens:
        return "cyan"
    elif "skyblue" in tokens:
        return "skyblue"
    elif "navyblue" in tokens:
        return "navyblue"
    elif "midnightblue" in tokens:
        return "midnightblue"
    elif "burgundy" in tokens:
        return "burgundy"
    elif "red" in tokens:
        return "red"
    elif "cherry" in tokens:
        return "cherry"
    elif "crimson" in tokens:
        return "crimson"
    elif "maroon" in tokens:
        return "maroon"
    elif "sand" in tokens:
        return "sand"
    elif "cream" in tokens:
        return "cream"
    elif "yellow" in tokens:
        return "yellow"
    elif "strawberry" in tokens:
        return "strawberry"
    elif "sage" in tokens:
        return "sage"
    elif "green" in tokens:
        return "green"
    elif "jade" in tokens:
        return "jade"
    elif "seafoam" in tokens:
        return "seafoam"
    elif "lime" in tokens:
        return "lime"
    elif "forest" in tokens:
        return "forest"
    elif "olive" in tokens:
        return "olive"
    elif "emerald" in tokens:
        return "emerald"
    elif "mint" in tokens:
        return "mint"
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
                    component["points"] = [points[0],points[0]]
                else:
                    raise ValueError("Incorrect Number of Points for Component 'Square'. Expected 2, got " + str(len(points)) + ".")

            components.append(component)

    return backgroundColour, components

