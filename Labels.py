def CreateLabelFile(filename,content):
    file = open(filename + ".txt","w")
    file.write(content)
    file.close()

endImageNumber = 100
imageNumber = int(input("Start Image > "))

while imageNumber <= endImageNumber:
    print(imageNumber)
    print("Create Label For",imageNumber)
    label = input("> ")
    CreateLabelFile("output/" + str(imageNumber),label)
    imageNumber += 1