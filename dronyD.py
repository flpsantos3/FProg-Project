# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import sys
import times
import readFiles
import writeFiles
import organize

def allocate(fileNameDrones, fileNameParcels):
    """
    Assign given drones to given parcels.
    
    Requires: fileNameDrones, fileNameParcels are str, with the names
    of the files representing the list of drones and parcels, respectively,
    following the format indicated in the project sheet.
    Ensures: Two output files, respectively, with the listing of scheduled
    transportation of parcels and the updated listing of drones, following the format
    and naming convention indicated in the project sheet.
    """

    #drones data
    dName = 0
    dArea = 1
    dMaxW = 2
    dMaxDmt = 3
    dTotalD = 4
    dAutoKm = 5
    dDate = 6
    dHour = -1

    #parcels data
    pName = 0
    pArea = 1
    pDate = 2
    pHour = 3
    pMaxDmt = 4
    pWeight = 5
    pTimeMins = -1

    #conditions the drones have to respect:
    #1) the area of operaation must be the same as the parcel
    #2) max weight the drone can carry must be > than the weight of the parcel
    #3) maximum distance to base must be > than the distance of the parcel/1000
    #4) autonomy must be enough to deliver the package and come back: autonomy > 2*distance for the parcel
    #5) hour of delivery is the later between the hour for the drone and the parcel
    
    drones = readFiles.readDronesFile(fileNameDrones)
    parcels = readFiles.readParcelsFile(fileNameParcels)

    #saving filetime to use in if clause
    fileTime = drones[0][0]

    #removing header info
    parcels.pop(0)
    drones.pop(0)

    #cancelled is a list that will contain only parcels that were not allocated
    #after a parcel is allocated, it's removed from cancelled
    cancelled = parcels[:]
    #pairings is an empty list where paired parcels and drones will be stored
    pairings = []

    #converting autonomy (index 5) to float so it can be ordered in reverse
    for a in range(len(drones)):
        for b in range(len(drones[a])):
            drones[a][dAutoKm] = float(drones[a][dAutoKm])

    #ordering drone lists by choice criteria - time, most autonomy, less distance, name
    from operator import itemgetter
    drones = sorted(drones,key = lambda d:(d[dHour], -d[dAutoKm], d[dTotalD], d[dName]))
    
    for i in range(len(parcels)):
        pairing = True
        for j in range(len(drones)):
            if pairing: 
                if drones[j][dArea] == parcels[i][pArea] and int(drones[j][dMaxW]) \
                   >= int(parcels[i][pWeight]) and int(drones[j][dMaxDmt]) >= \
                   int(parcels[i][pMaxDmt]) and float(drones[j][dAutoKm]) >= \
                   float(parcels[i][pMaxDmt])*(2/1000):
                            
                    pairings.append(organize.pairPD(parcels[i], drones[j]))
                    drones[j] = organize.updateDrone(parcels[i], drones[j])
                    drones = sorted(drones,key = lambda d:(d[dHour], -d[dAutoKm], \
                                                           d[dTotalD], d[dName]))
                    cancelled.remove(parcels[i])
                    pairing = False
                    
    #sorting drones by file ordering criteria: time > most autonomy > drone name
    drones = sorted(drones,key = lambda d:(d[dDate], d[dHour], -d[dAutoKm], d[dName]))

    #converting autonomy back to str, to be written in the file
    for x in range(len(drones)):
        for y in range(len(drones[x])):
            drones[x][dAutoKm] = str(drones[x][dAutoKm])
            
    #cancelled parcels first
    timeline = organize.cancelledP(cancelled)
    
    #ordering pairings by date, time then client name
    pairings = sorted(pairings, key = itemgetter(0,1,2))
    
    #adding each item of pairings to timeline
    for i in range(0, len(pairings)):
        timeline.append(pairings[i])
        
    writeFiles.writeBodyD(drones, fileNameDrones)
    writeFiles.writeBodyP(timeline, fileNameParcels)


#inputFileName1, inputFileName2 = sys.argv[1:]

#allocate(inputFileName1, inputFileName2)


