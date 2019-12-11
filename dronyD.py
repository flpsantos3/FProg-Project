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
        #to be completed

    drones = readFiles.readHeader(fileNameDrones)
    parcels = readFiles.readHeader(filenameParcels)

    #drones [nome, zona, peso max kg, dist max km, dist total, autonomia
    #data disponibilidade, hora disp]

    #parcels [nome, zona, data entrega, hora entrega, dist à base,
    #peso, tempo em min até voltar à base]
<<<<<<< Updated upstream
=======

    #conditions the drones have to respect:
    #1) the area of operaation must be the same as the parcel
    #2) max weight the drone can carry must be > than the weight of the parcel
    #3) maximum distance to base must be > than the distance of the parcel
    #4) autonomy must be enough to deliver the package and come back: sautonomy > 2*distance for the parcel
    #5) date of availability must be equal to date of delivery
    #6) hour of delivery is the earliest between the hour for the drone and the parcel
    #total distance and autonomy are float
    
    drones = readFiles.readDronesFile(fileNameDrones)
    parcels = readFiles.readParcelsFile(fileNameParcels)
>>>>>>> Stashed changes
    
    pairings = []
    parcels = parcels.pop(0)
    cancelled = parcels

    from operator import itemgetter
    drones.pop(0)
    drones = sorted(drones, key = itemgetter(-1,5,4,0))
    
<<<<<<< Updated upstream
    outputL = []
    i = 1
    for parcels[i] in range(len(parcels)-1):
        pairing = []
        for drones[j] in range(len(drones)-1):
            stop = FALSE
            while stop == FALSE:
                if parcels[i][1] == drones[j][1]:       #zona operaçao tem de ser igual
                    if parcels[i][5] <= drones[j][2]:   #peso encomenda > peso max
                        if 2*int(parcels[i][4]) <= int(drones[j][3]):   #distancia max
                            if int(parcels[i][4])+int(drones[j][4]) < int(drones[j][5]):
                                if parcels[i][2] == drones[j][6]:
                                    if parcels[i][3] > drones[j][-1]:

                                        pairing.append(parcels[i][2])
                                        pairing.append(parcels[i][3])
                                        pairing.append(parcels[i][1])
                                        pairing.append(drones[j][1])
                                        #funcao que coloca nome do drone e do cliente
                                        #juntos e funcao que atualiza valores de
                                        #distancia total, autonomia, hora disponibilidade
                    
                                    else:
                                        stop = TRUE
                                        i = i + 1
                                else:
                                    stop = TRUE
                                    i = i + 1
                            else:
                                stop = TRUE
                                i = i + 1

                        else:
                            stop = TRUE
                            i = i + 1
                   else:
                        stop = TRUE
                        i = i + 1

                else:
                    stop = TRUE
                    i = i + 1
                    
        ouputL.append(pairing)

#ver se preciso de uma funcao que nao possa atribuir o drone se hora atual +
#tempo de entrega > 20h00
=======
    i = 1
    for parcels[i] in range(len(parcels)-1):
        j = 0
        for drones[j] in range(len(drones)-1):
            stop = False
            while stop == False:
                if drones[j][0] == parcels[i][0] and drones[j][2] >= parcels[i][5] and drones[j][3] >= parcels[i][4] and \
                float(drones[j][5]) >= float(parcels[i][4])*2 and drones[j][6] == parcels[i][2]:
                
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
    
    #!: tarefas que nao forem completadas até às 20 passam para as 8 do dia seguinte
>>>>>>> Stashed changes

inputFileName1, inputFileName2 = sys.argv[1:]

allocate(inputFileName1, inputFileName2)


