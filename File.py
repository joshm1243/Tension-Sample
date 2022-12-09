import os

def RemoveDirectory(directoryName):
    errorMessage = ""
    if "/" not in directoryName:
        for fileName in os.listdir(directoryName):
            os.remove(directoryName + "/" + fileName)
        os.rmdir(directoryName)
    else:
        errorMessage = "Error: Cannot delete directories outside the Tension Sample space."
    return errorMessage

def CreateDirectory(directoryName):
    if not os.path.exists(directoryName):
        os.mkdir(directoryName)
