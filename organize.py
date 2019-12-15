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

    #drones [nome, zona, peso max kg, dist max km, dist total km, autonomia km
    #data disponibilidade, hora disp]

    #parcels [nome, zona, data entrega, hora entrega, dist à base metros,
    #peso, tempo em min até voltar à base]

    #updating drone's total distance after delivery
    dist = float(parcel[4])/1000
    totD = float(drone[4])
    drone[4] = str(round(totD + dist*2, 1))
    
    #updating autonomy after delivery
    auto = float(drone[5])
    drone[5] = str(round(auto - dist*2, 1))

    #updating time of availability after delivery
    pTime = parcel[3]
    dTime = drone[-1]
    if dTime < pTime:
        time = pTime
    else:
        time = dTime

    time = time.split(":")
    hour = time[0]
    mins = time[1]
    timeDeliv = parcel[-1]

    mins = str(int(mins) + int(timeDeliv))
    if int(mins) >= 60:
        if int(hour) < 10:
            hour = "0" + hour
            mins = str(int(mins) + int(timeDeliv) - 60)
        #deliveries that cant be finished till 20:00 get scheduled for 8:00
        elif int(hour) > 20:
            mins = timeDeliv
            hour = "08"
        else:
            mins = str(int(mins) + int(timeDeliv) - 60)
            hour = str(int(hour) + 1)

    upTime = hour + ":" + mins

    drone[-1] = upTime

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

    pairing = [date, time, cname, dname]

    return pairing

    
def cancelledP(parcels):
    """Receives a list of parcels that were not allocated to any drone
    and writes them on a list where the last element is "cancelled"
    Requires: parcels is a list of parcels not allocated to any drone
    Ensures: returns a list of lists with all the non-allocated parcels with
    the format [client name, date, time, "cancelled"]
    """

    from operator import itemgetter
    
    cancelled = []
    for i in range(0, len(parcels)):
        cname = parcels[i][0]
        date = parcels[i][2]
        time = parcels[i][3]
        cancelled.append([date, time, cname, "cancelled"])

    cancelled = sorted(cancelled, key = itemgetter(2))

    return cancelled
