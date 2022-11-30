GRID_LINES = {
    "A" : (0,13),
    "B" : (14,33),
    "C" : (34,53),
    "D" : (54,73),
    "E" : (74,93),
    "F" : (94,113),
    "G" : (114,127)
}

def GetRectangleCoordinates(points):
    yTop = GRID_LINES[points[0][1]][0]
    yBottom = GRID_LINES[points[1][1]][1]
    xLeft = GRID_LINES[points[0][0]][0]
    xRight = GRID_LINES[points[1][0]][1]
    topLeft = (xLeft,yTop)
    bottomRight = (xRight,yBottom)
    return topLeft,bottomRight

def GetCircleCoordinates(points):
    topLeft,bottomRight = GetRectangleCoordinates([points[0],points[0]])
    middleX = bottomRight[0] - (bottomRight[0] - topLeft[0]) // 2
    middleY = bottomRight[1] - (bottomRight[1] - topLeft[1]) // 2
    return (middleX, middleY)

    