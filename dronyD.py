# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import sys
import times
import readFiles
import writeFiles


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

    

    i = 1
    for parcels[i] in range(len(parcels)-1):
        stop = FALSE
        while stop == FALSE:
            if parcels[i][1] == drones[i][1]:       #zona operaçao tem de ser igual
                if parcels[i][5] <= drones[i][2]:   #peso encomenda > peso max
                    if 2*int(parcels[i][4]) <= int(drones[i][3]):   #distancia max
                        

                    else:
                        stop = TRUE
                        i = i + 1
                else:
                    stop = TRUE
                    i = i + 1

            else:
                stop = TRUE
                i = i + 1



inputFileName1, inputFileName2 = sys.argv[1:]

allocate(inputFileName1, inputFileName2)


