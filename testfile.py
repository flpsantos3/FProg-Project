import readFiles
import writeFiles
import organize
from operator import itemgetter
import constants
import dronyD


#print(readFiles.readHeader("drones11h00_2019y11m5.txt"))

#drones = readFiles.readDronesFile("drones11h00_2019y11m5.txt")
#parcels = readFiles.readParcelsFile("parcels11h00_2019y11m5.txt")
#print(parcels)
#writeFiles.writeHeader("drones11h00_2019y11m5.txt")

#parcel = ['Bran Stark', 'alvalade', ' 2019-11-05', '11:10', '1200', '20', '30']

#parcel[2] = parcel[2].replace(" ","")

#print(parcel)


#print(organize.updateDrone(parcel,drone))
#print(organize.cancelledP(cancelled))
#print(organize.pairD(parcel,drone))
#writeFiles.writeBodyP(parcels, "parcels11h00_2019y11m5.txt")
#writeFiles.writeBodyD(drones, "drones11h00_2019y11m5.txt")

dronyD.allocate("drones11h00_2019y11m5.txt","parcels11h00_2019y11m5.txt")
