import Grid
import Langauge
import Store
import File

outputDirectory = Store.Get("outputDirectory")
nextFilename = Store.Get("nextFilename")

components = []
requestExit = False

filePath = "./" + outputDirectory + "/" + nextFilename + ".png"
print("# Creating Sample",nextFilename)

while not requestExit:

    command = input("> ").lower()

    if command == "" or command.isspace():
        continue

    elif command == "e" or command == "exit":
        requestExit = True

    elif "sample" in command:
        tokens = command.split(" ")
        if len(tokens) == 1:
            print("# Creating Sample",nextFilename)
        elif len(tokens) == 2:
            nextFilename = tokens[1]
            Store.Set("nextFilename",nextFilename)
            filePath = "./" + outputDirectory + "/" + nextFilename + ".png"
            print("# Creating Sample",nextFilename)
        else:
            print("H")


    elif "cd" == command:
        print("#",outputDirectory)
    elif "dir" in command or "create" in command:
        tokens = command.split(" ")

        if len(tokens) == 2:
            outputDirectory = tokens[1]
            File.CreateDirectory(outputDirectory)
            Store.Set("outputDirectory",outputDirectory)
            filePath = "./" + outputDirectory + "/" + nextFilename + ".png"
        else:
            print("# The directory change command requires a directory.")


    elif command == "s" or command == "save":
        print("# Saving")
        print("--------")
        errorMessage = Grid.Save(components,filePath)
        if errorMessage != "":
            print("# Error Saving:",errorMessage)
        else:
            components = []
            nextFilename = str(int(nextFilename) + 1)
            filePath = "./" + outputDirectory + "/" + nextFilename + ".png"
            Store.Set("nextFilename",nextFilename)
            print("# Creating Sample",nextFilename)
            Grid.Display(components)

    elif command == "fp" or command == "filepath":
        print("# Filepath:",filePath)

    elif "rm" in command or "remove" in command:
        tokens = command.split(" ")
        if len(tokens) > 1:
            errorMessage = File.RemoveDirectory(tokens[1])
            if errorMessage != "":
                print("# ",errorMessage)
        else:
            print("# The Remove command requires a directory name.")
        
    ## Handling for image processing commands
    else:
        newComponents, errorMessage = Langauge.Parse(command)
        components += newComponents
        if errorMessage != "":
            print("#",errorMessage)
        else:
            Grid.Display(components)