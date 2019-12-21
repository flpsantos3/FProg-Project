# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes

import times
import readFiles
    
def writeHeaderD(fileName):
    """Uses the header info from a file of drones to write a new file, updating
    time and date (if needed)
    Requires: fileName is str, the name of a .txt file listing available drones
    Returns: a .txt file with the updated header, containing time, date, company
    name and where the scope is "Drones:"
    """

    info = readFiles.readHeader(fileName)

    t = info[0]
    title = "drones"
    timeNext = times.newTime(t)

    #if the file is the first of the day (8h00) the date changes
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

    #assembling the new file name
    newName = "drones" + timeNext + "_" + year + "y" + month + "m" + day + ".txt"

    fileOut = open(newName, 'w')

    company = info[2]

    #writing the header with the update info
    header = "Time:\n" + timeNext + "\n" + "Day:\n" + dateNext + "\n" + "Company:\n" + company + "\n" + "Drones:\n"

    fileOut.write(header)
    #file is not closed so this function can be called later
    return fileOut

def writeHeaderP(fileName):
    """Uses the header info from fileName to write the header for a new file,
    updating time and date (if needed)
    Requires: fileName is str, the name of a .txt file containing parcel info,
    with time, day and company info
    Returns: a .txt file with the updated header info, containing time, date,
    company name and where the scope is "Timeline:"
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
    header = "Time:\n" + time + "\n" + "Day:\n" + date + "\n" + "Company:\n" + \
             company + "\n" + "Timeline:\n"

    fileOut.write(header)
    #file is not closed so this function can be called later
    return fileOut

def writeBodyD(info, fileName):
    """Receives a list of updated drone info and writes it a new .txt
    file, where the header contents are fetched from fileName and updated
    Receives: info is a list of lists, each representing a drone, with the
    updated info after pairing with a parcel; fileName is the original drones
    .txt file
    Return: a .txt file with the updated header info and the updated info for
    all drones
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
    """Receives a list of drone pairings and writes it on a new .txt file,
    where the header contents are fetched from fileName and updated
    Receives: info is a list of lists with date, time, client name and drone name,
    representing a pairing, or cancelled deliveries; fileName is the original
    parcels .txt file
    Return: a .txt file with the header info from fileName and the info
    for all the pairings, even the cancelled
    """
    
    fileOut = writeHeaderP(fileName)

    #writing each element of a list to the output file;
    #changing lines after the last element of that list
    for j in range(0, len(info)):
        for i in range(0, len(info[j])):
            if i == len(info[j]) - 1:
                info[j][i] = info[j][i] + "\n"
                fileOut.write(info[j][i])
            else:
                info[j][i] = info[j][i] + ", "
                fileOut.write(info[j][i])
                
    fileOut.close()    
