import readFiles
import writeFiles
import organize
from operator import itemgetter
import constants
import dronyD

fileName = "drones15h30_2019y11m4.txt"

print(organize.titleHeader(fileName))

#dronyD.allocate("drones11h00_2019y11m5.txt","parcels11h00_2019y11m5.txt")
    #erro na autonomia final dos drones

#dronyD.allocate("drones15h30_2019y11m4.txt","parcels15h30_2019y11m4.txt")
    #erro no tempo (15:10)- para testar exceções

#dronyD.allocate("drones16h00_2019y11m5.txt","parcels16h00_2019y11m5.txt")
    #pat riley aparece cancelled mas nao devia

#dronyD.allocate("drones19h30_2019y11m5.txt","parcels19h30_2019y11m5.txt")
    #erro na ordem dos drones; nome do drone devia vir primeiro

#drones data
dName = 0
dArea = 1
dMaxW = 2
dMaxDm = 3 
dTotalD = 4
dAutoKm = 5 #AUTONOMIA NAO BATE CERTO COM FICHEIROS DO STOR
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
#6) hour of delivery is the earliest between the hour for the drone and the parce
#total distance and autonomy are float


