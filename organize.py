# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def updateDrone(parcel, drone):
    """Updates total distance, autonomy and time of availability for a drone with
    the data from a parcel allocated to that drone
    Receives: parcel is a list of parcel characteristics, drone is a list of
    characteristics for a drone alocated to that parcel    Returns: a list with the updated distance, autonomy and time for the drone
    """

    #list1 corresponds to a drone to which was allocated a parcel
    #total distance, autonomy and time of availability are calculated with
    #the values from the parcel delivery

    dist = float(drone[3])*2
    totd = float(drone[4])

    drone[4] = str(float(totd - dist))

    auto = float(drone[5])

    drone[5] = str(auto - float(parcel[4]))

    parc = parcel[3].split(":")
    dron = drone[-1].split(":")

    if int(dron[1]) + int(parc[1]) >= 60:
        dron[1] = str(int(dron[1]) + int(parc[1]) - 60)
        dron[0] = str(int(dron[0]) + 1)
        if int(dron[1]) < 10:
            dron[1] = "0" + str(dron[1])
        if int(dron[0]) > 20:
            dron[1] = "00"
            dron[0] = "8"
    else:
        dron[1] = str(int(dron[1])+int(parc[1]))

    hour = dron[0] + ":" + dron[1]

    drone[-1] = hour

    return drone


def pairPD(parcel, drone):
    """Creates a list with the date and time of delivery, the name of the
    client and the drone allocated to their order
    Requires: parcel is a list of str representing a parcel, drone is a
    list of str representing a drone, with the format from the project statement
    Ensures: a list with date, time, client name and drone name
    """

    date = parcel[2]
    
    time = parcel[3]
    if parcel[3] < drone[-1]:
        time = drone[-1]
        
    cname = parcel[0]
    dname = drone[0]

    outputL = [date, time, cname, dname]

    return outputL
    
def cancelledP(parcels):
    """Receives a list of parcels that were not allocated to any drone
    and writes them on a list where the last element is "cancelled"
    Requires: parcels is a list of parcels not allocated to any drone
    Ensures: returns a list of lists with all the non-allocated parcels with
    the format [client name, date, time, "cancelled"]
    """

    from operator import itemgetter
    
    cancelled = []
    for i in range(len(parcels)-1):
        cname = parcels[i][0]
        date = parcels[i][2]
        time = parcels[i][3]
        cancelled.append([date, time, cname, "cancelled"])

    cancelled = sorted(cancelled, key = itemgetter(2))

    return cancelled
