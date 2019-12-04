# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

def updateDrone(list1, list2):
    """Updates total distance, autonomy and time of availability for a drone with
    the data from a parcel allocated to that drone
    Receives: list1 is a list of drone characteristics, list 2 is a list
    representing a parcel allocated to that drone
    Returns: a list with the updated distance, autonomy and time for the drone
    """

    #list1 corresponds to a drone to which was allocated a parcel
    #total distance, autonomy and time of availability are calculated with
    #the values from the parcel delivery

    totd = list1[4]
    dist = int(list2[3])*2

    list1[4] = str(totd - dist)

    auto = int(list1[5])

    list1[5] = str(auto - int(list1[4]))

    drone = list1[-1].split(":")
    parcel = list2[3].split(":")

    if int(drone[1]) + int(parcel[1]) >= 60:
        drone[1] = str(int(drone[1]) + int(parcel[1]) - 60)
        drone[0] = str(int(drone[0]) + 1)
        if int(drone[1]) < 10:
            drone[1] = "0" + str(drone[1])
        if int(drone[0]) > 20:
            drone[1] = "00"
            drone[0] = "8"
    else:
        drone[1] = str(int(drone[1])+int(parcel[1]))

    hour = drone[0] + ":" + drone[1]

    list1[4] = hour

    return list1


def pairD(parcel, drone):
    """Creates a list with the date and time of delivery, the name of the
    client and the drone allocated to their order
    Requires: parcel is a list of str representing a parcel, drone is a
    list of str representing a drone, with the format from the project statement
    Ensures: a list with date, time, client name and drone name
    """

    outputL = []
    cname = parcel[0]
    

    
    

    
    
    


