# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import times
import readFiles

def updateDrone(parcel, drone):
    """Updates total distance, autonomy and time of availability for a drone with
    the info from the parcel allocated to that drone
    
    Requires: parcel is a list of str representing a parcel, drone is a list of
    strings representing a drone allocated to that parcel
    Ensures: a list representing a drone, with the updated distance, autonomy,
    time (and date, if needed) of availability
    """

    #updating drone's total distance after delivery
    dist = float(parcel[4])/1000
    totD = float(drone[4])
    drone[4] = str(round(totD + dist*2, 1))
    
    #updating autonomy after delivery
    auto = float(drone[5])
    drone[5] = round(auto - dist*2, 1)

    #storing date of availability in case the parcel is delivered
    #on the next day
    date = drone[6]

    #updating time of availability after delivery
    pTime = parcel[3]
    dTime = drone[-1]
    timeDeliv = int(parcel[-1])
    
    time = times.laterTime(pTime, dTime)
    time = time.split(":")
    hour = int(time[0])
    mins = int(time[1])
    
    mins = mins + timeDeliv
    #changing hour if needed
    if mins > 60:
        mins = mins + timeDeliv - 60
        hour = hour + 1
        #deliveries that can't be finished till 20:00 get scheduled for 8:00
        #of the next day
        if hour >= 20 and mins > 0:
            mins = timeDeliv
            hour = "8"
            drone[6] = times.nextDay(date)
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
    Ensures: a list with date and time of delivery, client name and drone name
    """

    timeD = drone[-1]
    timeP = parcel[3]
    date = parcel[2]
    cname = parcel[0]
    dname = drone[0]
    
    #the time of delivery is the later of the two times
    time = times.laterTime(timeP, timeD)
        
    #calculating the time after the parcel is delivered
    timeDeliv = times.delivTime(parcel, drone)
    
    #parcels that can't be delivered until 20:00 are delivered the next day
    if timeDeliv > "20:00":
        time = "08:00"
        date = times.nextDay(parcel[2])

    pairing = [date, time, cname, dname]

    return pairing

    
def cancelledP(parcels):
    """Receives a list of lists representing parcels that were not allocated
    to any drone and writes date, time and client name on a list where the last
    element is "cancelled"
    
    Requires: parcels is a list of lists, each representing parcels not
    allocated to any drone
    Ensures: a list of lists (of str) with the info for all non-allocated
    parcels and the format [date, time, client name, "cancelled"]
    """

    from operator import itemgetter
    
    cancelled = []
    for i in range(len(parcels)):
        cname = parcels[i][0]
        date = parcels[i][2]
        time = parcels[i][3]
        cancelled.append([date, time, cname, "cancelled"])

    #sorting by client name
    cancelled = sorted(cancelled, key = itemgetter(2))

    return cancelled


class differentHeaders(Exception):
    """Raised if any of the header elements do not match"""
    
    
def compareHeaders(fileParcels, fileDrones):
    """Receives two .txt files containing parcels and drones and compares
    their headers, returning True if equal, False otherwise
    
    Requires: fileParcels, fileDrones are str, the name of two .txt files
    containing info for parcels and drones, respectively
    Ensures: True if the headers of the files are equal (minus scope),
    False if any of date, time or company are different
    """
    
    parcHead = readFiles.readHeader(fileParcels)
    dronHead = readFiles.readHeader(fileDrones)
    
    if parcHead[0] == dronHead[0] and parcHead[1] == dronHead[1] and \
       parcHead[2] == dronHead[2]:
        return True
    
    else:
        raise differentHeaders
        parcHead.close()
        dronHead.close()


class difNameHeader(Exception):
    """raised if the info from the file name does not match the contents
    of the file header"""

    
def compNameHeader(fileName):
    """Receives a string representing the name of a .txt file containing info
    for parcels or drones and compares its title to the contents of the header
    inside, returning True if they match and False otherwise
    
    Requires: fileName is str, the name of a .txt file containing parcels or
    drones info
    Ensures: True if the name of the file matches all the contents of its
    header (minus company), False otherwise
    """
        
    #removing .txt from the name
    name = fileName[:-4]

    #separating scope, time and date info
    name = name.split("_")
    scopeTime = name[0].split("s")
    nameScope = scopeTime[0]
    nameTime = scopeTime[1]

    #formating name date to match the header date info format
    date = name[1]
    date = date.split("y")
    year = date[0]
    monthday = date[1]
    monthday = monthday.split("m")
    month = monthday[0]
    day = monthday[1]
    nameDate = day + "-" + month + "-" + year

    header = readFiles.readHeader(fileName)
    headerTime = header[0]
    headerDate = header[1]
    #formatting header scope to the same format as name scope
    headerScope = header[-1].lower()
    
    #removes "s:" to be able to directly compare the 2 strings
    headerScope = headerScope[:-2]
    
    if headerScope == nameScope and headerTime == nameTime and \
       headerDate == nameDate:
        return True

    else:
        raise difNameHeader
        header.close()
    
