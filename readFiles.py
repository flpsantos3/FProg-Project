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
    lists corresponding to the drones and their characteristics
    """
    outputList = []

    header = readHeader(fileName)
    
    outputList.append(header)
    
    fileIn = open(fileName, 'r')

    #converts the lines after the scope of the file into a list
    #where each line is a different str
    drones = list(fileIn)[7:]
    
    #goes through each line of drones and splits each characteristic into
    #a different str
    i = 0
    for i in range(len(drones)):
        drones[i] = drones[i][:-1]
        drones[i] = drones[i].split(", ")
        i = i + 1

    #each drone is represented by a list with the format [name, operating zone,
    #max weight, max range from base (m), total distance (km), autonomy (km),
    #date of availability yyyy-mm-dd, time of availability (hh:mm)]

    outputList.extend(drones)

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
    #and not the first line of the scope
    scope = fileIn.readline().strip().replace("\n", "")


    fileIn.close()

    #converted the return into a list so it is possible for write.Header function
    #to assign a new value to the scope (converts "Parcels:" into "Timeline:")
    return [time, day, company, scope]

def readParcelsFile(fileName):
    """
    Converts a given file listing delivery orders into a collection.
    
    Requires: fileName is str, the name of a .txt file listing parcels,
    following the format specified in the project sheet.
    Ensures: list whose first element is the header of fileName, followed by
    lists corresponding to the clients and the parcels they ordered
    """
    outputList = []

    header = readHeader(fileName)
    
    outputList.append(header)
    
    fileIn = open(fileName, 'r')

    parcels = list(fileIn)[8:]

    i = 0
    for i in range(len(parcels)):
        parcels[i] = parcels[i][:-1]
        parcels[i] = parcels[i].split(", ")
        i = i + 1

    #each drone is represented by a list with the format [name, operating zone,
    #max weight, max range from base (m), total distance (km), autonomy (km),
    #date of availability yyyy-mm-dd, time of availability (hh:mm)]

    outputList.extend(drones)

    fileIn.close()

    return outputList
    
