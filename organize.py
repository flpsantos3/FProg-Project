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

    list1[4] = totd - dist

    auto = list1[5]

    list1[5] = auto - list1[4]

    time = list1[4].split(":")

    hour = time[1]
    mint = time[2]

    

    

    
