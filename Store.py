store = {}

storeReadFile = open("Store.txt","r")
for line in storeReadFile.readlines():
    keyValue = line.strip().split("=")
    store[keyValue[0]] = keyValue[1]

def Get(key):
    return store[key]

def Set(key,value):
    store[key] = value
    storeWriteFile = open("Store.txt","w")
    lines = ""
    for storeItem in list(store.items()):
        lines += (storeItem[0] + "=" + storeItem[1] + "\n")
    storeWriteFile.write(lines)
    

    
