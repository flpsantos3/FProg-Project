import readFiles
import writeFiles
import organize
import dronyD
from operator import itemgetter


#print(readFiles.readHeader("drones11h00_2019y11m5.txt"))

drones = readFiles.readDronesFile("drones11h00_2019y11m5.txt")

drones.pop(0)

drones = sorted(drones, key = itemgetter(-1,5,4,0))


#print(drones)

#writeFiles.writeHeader("drones11h00_2019y11m5.txt")

a = "Jupiter, alvalade, 20, 2000, 500.0, 20.0, 2019-11-05, 10:15"

"Jupiter, alvalade, 20, 2000, 503.4, 16.6, 2019-11-05, 11:30"

drone = a.split(", ")

b = "Arya Stark, alvalade, 2019-11-05, 11:05, 1700, 15, 25"

parcel = b.split(", ")

print(organize.updateDrone(parcel,drone))

#print(organize.pairPD(parcel,drone))

