# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

time = ["8h00","8h30","9h00","9h30","10h00","10h30","11h00","11h30","12h00",
"12h30","13h00","13h30","14h00","14h30","15h00","15h30","16h00","16h30",
"17h00","17h30","18h00","18h30","19h00","19h30","20h00"]

#droneDistanciaMax=drones[][3]
#parcelDistanciaBase=parcels[0][3]


def droneDistanciaMax (linha):
    return drones[linha][3]
    
#print(droneDistanciaMax(0))


#test to remove
parcels=[['Daenerys Targaryen', 'lumiar', '2019-11-05', '11:00', '900', '15', '20'],['John Snow', 'lumiar', '2019-11-05', '11:05', '1200', '10', '30']]
drones=[['Jupiter', 'alvalade', '20', '2000', '500', '20', '2019-11-05', '10:15'],['Terra', 'ameixoeira', '15', '1500', '400', '20', '2019-11-05', '10:20']]




#drones data


def dName (line):
    return drones[line][0]

def dAreaName (line):
    return drones[line][1]

def dMaxCapacityKg (line):
    return drones[line][2]

def dMaxDistM (line):
    return drones[line][3]

def dAcumDistKm (line):
    return drones[line][4]

def dAutonomyKm (line):
    return drones[line][5]

def dAvailableDate (line):
    return drones[line][6]

def dAvailableHour (line):
    return drones[line][7]


#parcels data

def pName (line):
    return parcels[line][0]

def pAreaName (line):
    return parcels[line][1]

def pRequestDate (line):
    return parcels[line][2]

def pRequestHour (line):
    return parcels[line][3]

def pDistM (line):
    return parcels[line][4]

def pWeightKg (line):
    return parcels[line][5]

def pDurationMin (line):
    return parcels[line][6]




