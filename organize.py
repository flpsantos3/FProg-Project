# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import times

def updateDrone(parcel, drone):
    """Updates total distance, autonomy and time of availability for a drone with
    the data from a parcel allocated to that drone
    Receives: parcel is a list of parcel characteristics, drone is a list of
    characteristics for a drone alocated to that parcel    Returns: a list with the updated distance, autonomy and time for the drone
    """
    
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

    #storing date of availability in case the parcel is delivered on the next day
    date = drone[6].split("-")
    day = int(date[2])
    month = int(date[1])
    year = int(date[0])

    #updating time of availability after delivery
    pTime = parcel[3]
    dTime = drone[-1]
    if dTime < pTime:
        time = pTime
    else:
        time = dTime

    time = time.split(":")
    hour = int(time[0])
    mins = int(time[1])
    timeDeliv = int(parcel[-1])

    mins = mins + timeDeliv
    if mins > 60:
        hour = hour + 1
        mins = mins + timeDeliv - 60
        #deliveries that cant be finished till 20:00 get scheduled for 8:00
        if hour >= 20 and mins > 0:
            mins = timeDeliv
            hour = "8"
            day = day + 1
            if day > 30:
                day = "01"
                month = month + 1
                if month > 12:
                    month = "01"
                    year = year + 1
                elif month < 10:
                    month = "0" + str(month)
            elif day < 10:
                day = "0" + str(day)
            drone[6] = str(year) + "-" + str(month) + "-" + str(day)
    elif mins == 60:
        mins = "0"
        hour = hour + 1

    if int(hour) < 10:
        hour = "0" + str(hour)
    if int(mins) < 10:
        mins = "0" + str(mins)
        
    upTime = str(hour) + ":" + str(mins)
    
    drone[-1] = upTime
    
    return drone


def pairPD(parcel, drone):
    """Creates a list with the date and time of delivery, the name of the
    client and the drone allocated to their order
    Requires: parcel is a list of str representing a parcel, drone is a
    list of str representing a drone, with the format from the project statement
    Ensures: a list with date, time, client name and drone name
    """

    from times import deliv_time
    timeD = drone[-1]
    timeP = parcel[3]
    timeDeliv = times.deliv_time(parcel, drone)
    date = parcel[2]
    
    if timeP > timeD:
        time = timeP
    else:
        time = timeD

    if timeDeliv > "20:00":
        time = "08:00"
        date = parcel[2]
        date = date.split("-")
        day = int(date[2])
        month = int(date[1])
        year = int(date[0])
        day = day + 1
        if day > 30:
                day = "01"
                month = month + 1
                if month > 12:
                    month = "01"
                    year = year + 1
                elif month < 10:
                    month = "0" + str(month)
        elif day < 10:
            day = "0" + str(day)
        date = str(year) + "-" + str(month) + "-" + str(day)            
        
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
