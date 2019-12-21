# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import times
import readFiles
    
def writeHeaderD(fileName):
    """Uses the header info from a file of drones to write a new file
    Requires: fileName is str, the name of a .txt file listing available drones
    Returns: a .txt file with the updated header, where the scope is "Drones:"
    """

    info = readFiles.readHeader(fileName)

    t = info[0]
    title = "drones"
    timeNext = times.newTime(t)

    #if the file is the first of the day (8:00) the date changes
    d = info[1]
    if timeNext == "8h00": 
        dateNext = times.new_date(d)
    else:
        dateNext = d

    #splitting date string into 3 strings that can be written in the file name
    ddmmyy = dateNext.split("-")   
    day = ddmmyy[0]
    month = ddmmyy[1] 
    year = ddmmyy[2] 

    #"building" the new file name
    
    newName = "drones" + timeNext + "_" + year + "y" + month + "m" + day + ".txt"

    fileOut = open(newName, 'w')

    company = info[2]

    #writing the header with the update info
    header = "Time:\n" + timeNext + "\n" + "Day:\n" + dateNext + "\n" + "Company:\n" + company + "\n" + "Drones:\n"

    fileOut.write(header)
    #file is not closed so this function can be called after
    return fileOut

def writeHeaderP(fileName):
    """Uses the header info from fileName to write a new file
    Requires: fileName is str, the name of a .txt file with time, day, company info
    Returns: a .txt file with the updated info
    """

    
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
    newName = title + time + "_" + year + "y" + month + "m" + day + ".txt"

    fileOut = open(newName, 'w')

    #writing the header with the update info
    header = "Time:\n" + time + "\n" + "Day:\n" + date + "\n" + "Company:\n" + company + "\n" + "Timetable:\n"

    fileOut.write(header)
    #file is not closed so this function can be called after
    return fileOut

def writeBodyD(info, fileName):
    """Receives a list of updated drone info and writes it on fileName, a .txt file
    Receives: info is a list of updated drone info after pairing with a parcel
    fileName is a .txt file containing drone info
    Return: a .txt file with the updated header info and the info from info list
    """
    
    fileOut = writeHeaderD(fileName)

    #writing each element of a list to the output file;
    #changing lines after the last element of the list
    for j in range(0, len(info)):
        for i in range(0, len(info[j])):
            if i == len(info[j]) - 1:
                info[j][i] = info[j][i] + "\n"
                fileOut.write(info[j][i])
            else:
                info[j][i] = info[j][i] + ", "
                fileOut.write(info[j][i])
                
    fileOut.close()

def writeBodyP(info, fileName):
    """Receives a list of drones pairings and writes it on fileName, a .txt file
    Receives: info is a list of lists with date, time, client name and drone name of a pairing
    fileName is the parcel .txt file from where the information was read
    Return: a .txt file with the header info from fileName and the info from info list
    """
    
    fileOut = writeHeaderP(fileName)

    #writing each element of a list to the output file;
    #changing lines after the last element of the list
    for j in range(0, len(info)):
        for i in range(0, len(info[j])):
            if i == len(info[j]) - 1:
                info[j][i] = info[j][i] + "\n"
                fileOut.write(info[j][i])
            else:
                info[j][i] = info[j][i] + ", "
                fileOut.write(info[j][i])
                
    fileOut.close()    
