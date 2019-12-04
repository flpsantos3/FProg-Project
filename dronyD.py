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
    
    
    outputL = []
    i = 1
    for parcels[i] in range(len(parcels)-1):

        for drones[j] in range(len(drones)-1):
            stop = FALSE
            
            while stop == FALSE:
                
                if parcels[i][1] == drones[j][1] AND if parcels[i][5] <= drones[j][2]: AND if 2*int(parcels[i][4]) <= int(drones[j][3]):
                            if int(parcels[i][4])+int(drones[j][4]) < int(drones[j][5]):
                                if parcels[i][2] == drones[j][6]:   #data
                                    if parcels[i][3] > drones[j][-1]:   #hora

                                        outputL.extend(organize.pairD(parcels[i],drones[j])
                                        drones[j] = organize.updateDrone(parcels[i],drones[j])
                    
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


#ver se preciso de uma funcao que devolva "cancelled" se não existir nenhum drone

inputFileName1, inputFileName2 = sys.argv[1:]

allocate(inputFileName1, inputFileName2)


