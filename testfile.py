import readFiles
import writeFiles
import organize
import dronyD
from operator import itemgetter

#print(readFiles.readHeader("parcels11h00_2019y11m5.txt"))

#drones = readFiles.readDronesFile("drones11h00_2019y11m5.txt")
#drones.pop(0)
#drones = sorted(drones, key=itemgetter(-1,5,4,0))
#print(drones)

parcels = readFiles.readDronesFile("parcels11h00_2019y11m5.txt")
#parcels.pop(0)
#print(organize.cancelledP(parcels))
#a = sorted(drones, key=itemgetter(-1))

#print(a)

#writeFiles.writeHeader("drones11h00_2019y11m5.txt")

a = "Jupiter, alvalade, 20, 2000, 500.0, 20.0, 2019-11-05, 10:15"

drone = a.split(", ")

b = "Daenerys Targaryen, lumiar, 2019-11-05, 11:00, 900, 15, 20"

parcel = b.split(", ")

#print(len(drone))


#print(organize.updateDrone(parcel,drone))

#print(organize.pairD(parcel,drone))

dronyD.allocate("drones11h00_2019y11m5.txt", "parcels11h00_2019y11m5.txt")
