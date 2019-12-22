import readFiles
import writeFiles
import organize
from operator import itemgetter
import times
import dronyD

#drones data
dName = 0
dArea = 1
dMaxW = 2
dMaxDm = 3 
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

#dronyD.allocate("drones11h00_2019y11m5.txt","parcels11h00_2019y11m5.txt")
    #erro na autonomia final dos drones

#dronyD.allocate("drones16h00_2019y11m5.txt","parcels16h00_2019y11m5.txt")
    #pat riley aparece cancelled mas nao devia

#dronyD.allocate("drones19h30_2019y11m5.txt","parcels19h30_2019y11m5.txt")
    #ver time_deliv + mins == 20

#dronyD.allocate("drones15h30_2019y11m4h.txt","parcels15h30_2019y11m4h.txt")

#Exceptions:

#organize.compNameHeader("parcels15h30_2019y11m4.txt")
#print(organize.compNameHeader("drones15h30_2019y11m4h.txt"))
#print(readFiles.readHeader("parcels15h30_2019y11m4h.txt"))
#print(readFiles.readHeader("drones15h30_2019y11m4h.txt"))
#dronyD.allocate("drones15h30_2019y11m4.txt","parcels15h30_2019y11m4.txt")

#print(organize.compNameHeader("drones15h30_2019y11m4n.txt"))

