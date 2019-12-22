# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import constants

def newTime(time):
    """Receives a time (with the format HHhMM) present in constants.time
    and returns the next element of that list
    
    Requires: time is str, with the format HHhMM and present in the list
    constants.time
    Ensures: a time string (with format HHhMM), the following element of
    constants.time
    """


    #time is a list of all possible times, from 8h00 to 20h00,
    #in 30 minute intervals
    hour = constants.time

    #advancing the time 30 mins or to 8h00, in case the original time is 20h00
    i = hour.index(time) 
    if time != "20h00":
        newTime = constants.time[i + 1]    
    else:
        newTime = constants.time[0]
        
    return newTime


def newDate(date):
    """Receives a date with the format dd-mm-yyyy and returns the date
    for the following day
    
    Requires: date is str, with the format dd-mm-yyyy
    Ensures: a str with day, month and year for the next date,
    following the format dd-mm-yyyy
    """

    date = date.split("-")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    #advancing to the next day, changing month and/or year if needed
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

    newDate = day + "-" + month + "-" + year 

    return newDate


def laterTime(time1, time2):
    """Receives two strings representing time (hh:mm) and returns the later
    between them
    
    Requires: time1, time2 are str, with the format hh:mm
    Ensures: the later between time1 and time 2
    """

    if time1 > time2:
        return time1
    else:
        return time2


def delivTime(parcel, drone):
    """Takes a drone and a parcel and returns the time of availability of the
    drone after that parcel is delivered
    
    Requires: parcel and drone are lists representing a parcel and a drone,
    respectively
    Ensures: the final time (str) indicating the time of availability of the
    drone after parcel is delivered
    """
    #chosing the later time
    timeP = parcel[3]
    timeD = drone[-1]
    time = laterTime(timeP, timeD)

    #splitting time into numbers
    time = time.split(":")
    hour = int(time[0])
    mins = int(time[1])
    timeDeliv = int(parcel[-1])

    #calculating time of availability after delivery
    mins = mins + timeDeliv
    if mins > 60:
        hour = hour + 1
        mins = mins + timeDeliv - 60
    elif mins == 60:
        mins = "00"
        hour = hour + 1

    finalTime = str(hour) + ":" + str(mins)

    return finalTime


def nextDay(firstDate):
    """Receives a date with the format yyyy-mm-dd and returns the date for
    the following day
    
    Requires: firstdate is str, with the format yyyy-mm-dd
    Ensures: a str with the format yyyy-mm-dd, corresponding to the date after
    firstDate
    """

    #this functon is similar to new_date but returns a different date format
    date = firstDate.split("-")
    day = int(date[2])
    month = int(date[1])
    year = int(date[0])
    
    #advancing to the next day, changing month and/or year if needed
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
            
    newDate = str(year) + "-" + str(month) + "-" + str(day)

    return newDate
