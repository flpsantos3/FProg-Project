import readFiles
import writeFiles
import organize

from operator import itemgetter

#print(readFiles.readHeader("drones11h00_2019y11m5.txt"))

#drones = readFiles.readDronesFile("drones11h00_2019y11m5.txt")

#drones.pop(0)

#a = sorted(drones, key=itemgetter(-1))

#print(a)

#writeFiles.writeHeader("drones11h00_2019y11m5.txt")

a = "Jupiter, alvalade, 20, 2000, 500.0, 20.0, 2019-11-05, 10:15"

drone = a.split(", ")

b = "Daenerys Targaryen, lumiar, 2019-11-05, 11:00, 900, 15, 20"

parcel = b.split(", ")

#print(organize.updateDrone(parcel,drone))

print(organize.pairD(parcel,drone))

