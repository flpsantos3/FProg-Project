# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def new_time(time):
    """Receives the time from the previous drone list and returns the date for the updated list
    Requires: time is string
    Ensures: returns a string with the time for the updated drone list
    """

    #time is a list in constants.py and contains all possible times,
    #from 8h00 to 22h00, in 30 minute intervals
    import constants
    
    hour = constants.time

    i = hour.index(time)

    if time != "22h00":
        time_new = constants.time[i + 1]             
    else:
        time_new = constants.time[0]

    return time_new



def new_date(date):
    """Receives the date from the previous drone list and returns the date for the updated list
    Requires: date is str with day-month-year format
    Ensures: returns a str with day, month and year for the updated list
    """

    data = date.split("-")
    day = data[0]
    month = data[1]
    year = data[2]

    #per the project description, all months have 30 days
    #guarantees that the months change for 30+ days, and year changes for 12+ months

    if day == "30":
        if month == "12":
            year = str(int(year) + 1)
            month = "1"
            day = "1"
        else:
            month = str(int(month) + 1)
            day = "1"
    else:
        day = str(int(day) + 1)
    
    date_new = day + "-" + month + "-" + year

    return(date_new)
