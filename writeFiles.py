# 2019-2020 Fundamentos de Programação
# Grupo 20
# 55142 Filipe Santos
# 28115 Lara Nunes


def writeHeader(fileName):
    """Uses the header info from fileName to write a new file
    Requires: fileName is str, the name of a .txt file with time, day, company name and scope of the file
    Returns: a .txt file with the updated info
    """

    import times
    import readFiles
    
    info = readFiles.readHeader(fileName)

    t = info[0]
    time_next = times.new_time(t)

    d = info[1]
    if t == "8h00":
        date_next = times.new_date(d)
    else:
        date_next = d 
    
    ddmmyy = date_next.split("-")   #splits date into a list with 3 elements
                                        #day, month, year
    day = ddmmyy[0]
    month = ddmmyy[1] 
    year = ddmmyy[2]

    scope = info[3].lower().replace(":","") #removes ":" from scope

    new_name = scope + time_next + "_" + year + "y" + month + "m" + day + ".txt"

    outputfile = open(new_name, 'w')

    company = info[2]

    header = "Time:\n" + time_next + "\n" + "Day:\n" + date_next + "\n" + "Company:\n" + company + "\n" + info[3] + "\n"

    outputfile.write(header)

    outputfile.close()

def writeTimeline(pairings):
    """Creates a new .txt with the paired drones and parcels
    Requires: pairings is a list where each element is a drone and parcel pairing
    Ensures: a .txt file with the paired drones and parcels, where each line corresponds
    to a pairing
    """



    
