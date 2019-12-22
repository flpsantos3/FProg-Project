# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def readDronesFile(fileName):
    """
    Converts a given file listing drones into a collection.
    
    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified in the project sheet.
    Ensures: list whose first element is the header of fileName, followed by
    lists corresponding to each of the drones and their characteristics
    """
    
    outputList = []

    header = readHeader(fileName)
    
    outputList.append(header)
    
    fileIn = open(fileName, 'r')

    #converts each line containing drone info into a list
    drones = list(fileIn)[7:]
    
    #spliting each line into a list where each element is a different characteristic
    for i in range(len(drones)):
        drones[i] = drones[i][:-1] #removes "\n" from the end of the string
        drones[i] = drones[i].split(", ")

    #removing excess blank spaces from every element except drone name
    for i in range(len(drones)):
        for j in range(1, len(drones[i])):
            drones[i][j] = drones[i][j].replace(" ","")

    outputList.extend(drones)

    fileIn.close()

    return outputList


def readParcelsFile(fileName):
    """
    Converts a given file listing parcel info into a collection.
    
    Requires: fileName is str, the name of a .txt file listing parcels,
    following the format specified in the project sheet.
    Ensures: list whose first element is the header of fileName, followed by
    lists corresponding to each of the clients and the parcels they ordered
    """
    outputList = []

    header = readHeader(fileName)
    
    outputList.append(header)
    
    fileIn = open(fileName, 'r')

    #converts each line containing parcel info into a list
    parcels = list(fileIn)[7:]

    #spliting each line into a list where each element is a different characteristic
    for i in range(len(parcels)):
        parcels[i] = parcels[i][:-1] #removes "\n" from the end of the string
        parcels[i] = parcels[i].split(", ")

    #removing excess blank spaces from every element except client name
    for i in range(len(parcels)):
        for j in range(1, len(parcels[i])):
            parcels[i][j] = parcels[i][j].replace(" ","")

    outputList.extend(parcels)

    fileIn.close()

    return outputList


def readHeader(fileName):
    """
    Reads a .txt file and returns the day, time, company and scope of the file
    
    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified on the project
    Ensures: returns a list with the day, time, company and scope of fileName
    """

    fileIn = open(fileName, 'r')
    
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    #fileIn.readline() - removed this line so the scope is "Parcels:" or "Drones:"
    scope = fileIn.readline().strip().replace("\n", "")

    fileIn.close()

    return [time, day, company, scope]


    
