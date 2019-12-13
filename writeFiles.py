# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def writeHeaderD(fileName):
    """Uses the header info from a file of drones to write a new file
    Requires: fileName is str, the name of a .txt file listing available drones
    Returns: a .txt file with the updated header, where the scope is "Drones:"
    """

    import times
    import readFiles
    
    info = readFiles.readHeader(fileName)

    t = info[0]
    title = "drones"
    time_next = times.new_time(t)

    #if the file is the first of the day (8:00) the date changes
    d = info[1]
    if time_next == "8h00": 
        date_next = times.new_date(d)
    else:
        date_next = d
    
    ddmmyy = date_next.split("-")   
    day = ddmmyy[0]
    month = ddmmyy[1] 
    year = ddmmyy[2] 

    new_name = "drones" + time_next + "_" + year + "y" + month + "m" + day + ".txt"

    outputfile = open(new_name, 'w')

    company = info[2]

    #writes the header with the update info
    header = "Time:\n" + time_next + "\n" + "Day:\n" + date_next + "\n" + "Company:\n" + company + "\n" + "Drones:\n"

    outputfile.write(header)

    outputfile.close()

    return fileOut

def writeHeaderP(fileName):
    """Uses the header info from fileName to write a new file
    Requires: fileName is str, the name of a .txt file with time, day, company info
    Returns: a .txt file with the updated info
    """

    import times
    import readFiles
    
    info = readFiles.readHeader(fileName)
    
    #info is a list with the format[time, date, company, scope]
    time = info[0]
    title = "timetable"
    date = info[1]
    company = info[2]

    #splits date to be able to write the name of the new file in the correct format
    ddmmyy = date.split("-")   
    day = ddmmyy[0]
    month = ddmmyy[1] 
    year = ddmmyy[2]

    #formats fileName to fit with the intended format
    new_name = title + time + "_" + year + "y" + month + "m" + day + ".txt"

    fileOut = open(new_name, 'w')

    header = "Time:\n" + time + "\n" + "Day:\n" + date + "\n" + "Company:\n" + company + "\n" + "Timetable:\n"

    fileOut.write(header)

    return fileOut

def writeBodyD(info, fileName):
    """Receives a list of updated drone info and writes it on fileName, a .txt file
    Receives: info is a list of updated drone info after pairing with a parcel
    fileName is a .txt file containing drone info
    Return: a .txt file with the updated header info and the info from info list
    """
    
    fileOut = writeHeaderD(fileName)
    
    #removes header info (info[0]), keeping only the drones or pairings info
    info.pop(0) 

    #changes line when the list of info for a particular drone/parcel ends
    #adds comma space otherwise
    j = 0
    for j in range(len(info)):
        i = 0
        for i in range(len(info[j])):
            if i == len(info[j]) - 1:
                info[j][i] = info[j][i] + "\n"
                fileOut.write(info[j][i])
            else:
                info[j][i] = info[j][i] + ", "
                fileOut.write(info[j][i])
                i = i + 1
                
    fileOut.close()

def writeBodyP(info, fileName):
    """Receives a list of drones pairings and writes it on fileName, a .txt file
    Receives: info is a list of lists with date, time, client name and drone name of a pairing
    fileName is the parcel .txt file from where the information was read
    Return: a .txt file with the header info from fileName and the info from info list
    """
    
    fileOut = writeHeaderP(fileName)
    
    #removes header info (info[0]), keeping only the drones or pairings info
    info.pop(0) 

    #changes line when the list of info for a particular drone/parcel ends
    #adds comma space otherwise
    j = 0
    for j in range(len(info)):
        i = 0
        for i in range(len(info[j])):
            if i == len(info[j]) - 1:
                info[j][i] = info[j][i] + "\n"
                fileOut.write(info[j][i])
            else:
                info[j][i] = info[j][i] + ", "
                fileOut.write(info[j][i])
                i = i + 1
                
    fileOut.close()    
