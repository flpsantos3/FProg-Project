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
    
    droneH = readFiles.readHeader(fileNameDrones)
    parcelH = readFiles.readHeader(fileNameParcels)

    #drones data
    dName = 0
    dArea = 1
    dMaxW = 2
    dMaxDkm = 3
    dTotalD = 4
    dAutoKm = 5
    dDate = 6
    dHour = -1

    #parcels data
    pName = 0
    pArea = 1
    pDate = 2
    pHour = 3
    pMaxDm = 4
    pWeight = 5
    pTimeMin = -1

    #conditions the drones have to respect:
    #1) the area of operaation must be the same as the parcel
    #2) max weight the drone can carry must be > than the weight of the parcel
    #3) maximum distance to base must be > than the distance of the parcel/1000
    #4) autonomy must be enough to deliver the package and come back: sautonomy > 2*distance for the parcel
    #5) date of availability must be equal to date of delivery
    #6) hour of delivery is the earliest between the hour for the drone and the parcel
    #total distance and autonomy are float
    
    drones = readFiles.readDronesFile(fileNameDrones)
    parcels = readFiles.readParcelsFile(fileNameParcels)

    #removing header info
    parcels.pop(0)
    drones.pop(0)

    #cancelled is a list that will contain parcels that were not allocated to a drone
    cancelled = parcels

    #ordering drone lists by choice criteria - time, most autonomy, less distance, name
    from operator import itemgetter
    #NAO ESQUECER dAutoKm tem de ser reverse, mais alta primeiro
    drones = sorted(drones, key = itemgetter(dHour, -dAutoKm, dTotalD, dName))
    print(drones)
    pairings = []
    i = 0
    for parcels[i] in range(len(parcels)-1):
        j = 0
        for drones[j] in range(len(drones)-1):
            stop = False
            while stop == False:
                if drones[j][dArea] == parcels[i][pArea] and drones[j][dMaxW] >= parcels[i][pWeight] and \
                   float(drones[j][dMaxDKm]) >= float(parcels[pMaxDm][4])/1000 and float(drones[j][dAutoKm]) >= \
                   float(parcels[i][pMaxDm])*(2/1000) and drones[j][dDate] == parcels[i][pDate]:
                
                                organize.updateDrone(parcels[i], drones[j])
                                pairings.append(organize.pairPD(parcels[i], drones[j]))
                                cancelled.pop(i)
                                
                else:
                    stop = True
                    j = j + 1
        i = i + 1

    ouputL = organize.cancelledP(cancelled)
    pairings = sorted(pairings, key = itemgetter(1,2))
    ouputL.append(pairings)
    
    writeFiles.writeBodyD(drones, fileNameDrones)
    writeFiles.writeBodyP(outputL, fileNameParcels)
    
    

#inputFileName1, inputFileName2 = sys.argv[1:]

#allocate(inputFileName1, inputFileName2)


