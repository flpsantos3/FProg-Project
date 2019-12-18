# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def new_time(time):
    """Receives the time from the previous drone list and returns
    the time for the updated list
    Requires: time is str, with the format HHhMM
    Ensures: a string with the time for the updated drone list
    """

    #time is a list in constants.py and contains all possible times,
    #from 8h00 to 20h00, in 30 minute intervals
    import constants
    
    hour = constants.time

    #advancing the time 30 mins or to 8:00, in case the original time is 20:00
    i = hour.index(time) 
    if time != "20h00":
        newTime = constants.time[i + 1]    
    else:
        newTime = constants.time[0]
        
    return newTime


def new_date(date):
    """Receives the date from the previous drone list and returns the date for the updated list
    Requires: date is str with day-month-year format
    Ensures: returns a str with day, month and year for the updated list
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


def deliv_time(parcel, drone):
    """Takes a drone and a parcel and returns the time of availability after the
    parcel is delivered
    Requires: parcel and drone are lists representing a parcel and a drone, respectively
    Ensures: the final time (str) indicating the time of availability of
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
    if mins >= 60:
        hour = hour + 1
        mins = mins + timeDeliv - 60

    finalTime = str(hour) + ":" + str(mins)

    return finalTime


def nextDay(firstDate):
    """Receives a date with the format yyyy-mm-dd and returns the following date
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
