# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def writeHeader(fileName):
    """Uses the header info from fileName to write a new file
    Requires: fileName is str, the name of a .txt file with time, day, company info
    Returns: a .txt file with the updated info
    """


    import times
    import readFiles
    
    info = readFiles.readHeader(fileName)
    
    #info is a list with the format[time, date, company, scope]
    t = info[0]
    time_next = times.new_time(t)

    #if the file is the first of the day (8:00) the date changes
    #else the date is the same as the entry file

    #need to evaluate if it's working as intended for a file with 8:00 as the time

    d = info[1]
    if t == "8h00": #should be time_next == "8:00"??
        date_next = times.new_date(d)
    else:
        date_next = d 
    
    ddmmyy = date_next.split("-")   #splits date into a list with 3 elements
                                        #day, month, year
    day = ddmmyy[0]
    month = ddmmyy[1] 
    year = ddmmyy[2]

    title = "drones"

    if info[3] == "Parcels:":   #changes title to timeline if fileName's scope is parcels
        title = "timetable"
        info[3] = "Timeline:"

    #formats fileName to fit with the intended format
    new_name = title + time_next + "_" + year + "y" + month + "m" + day + ".txt"

    fileOut = open(new_name, 'w')

    company = info[2]

    #writes the header with the update info
    header = "Time:\n" + time_next + "\n" + "Day:\n" + date_next + "\n" + "Company:\n" + company + "\n" + info[3] + "\n"

    fileOut.write(header)

    return fileOut

def writeBody(info, fileName):
    """Receives a list of updated drone info or parcels and drones pairings and writes it on fileName, a .txt file
    Receives: info is a list of either: 1) updated drone info after pairing with a parcel; 2) date, time, client name and drone name of a pairing
    fileName is the original .txt file from where the information was read
    Return: a .txt file with the header info from writeHeader and the info from info list
    """

    fileOut = writeHeader(fileName)
    info.pop(0) #removes header info (info[0]), keeping only the drones or pairings info
    
    j = 0
    for j in range(len(info)):
        i = 0
        for i in range(len(info[j])):
            if i == len(info[j]) - 1:   #if i is the last element of the list, the line changes
                info[j][i] = info[j][i] + "\n"
                fileOut.write(info[j][i])
            else:
                info[j][i] = info[j][i] + ", "  #if the element is not the last, ", " is added to continue writing on the same line
                fileOut.write(info[j][i])
                i = i + 1
                
    fileOut.close()

    
