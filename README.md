# Assessment for the class Fundamentos de Programação (Programming Fundamentals)

## Context

A certain company wants to use drones to deliver packages or parcels accross various areas of Lisbon. 
To do that, we need to write a program that receives two `.txt` entry files, **drones** and **parcels**, and returns two `.txt` files, the **drone-parcel pairings** and the **updated drones list**.

## The Program

### `constants.py`

Contains only a list of all the possible times the files can take (from 8:00 to 20:00 in 30 minute intervals) that will be iterated by other functions.

### `times.py`

Contains 5 functions, all related to the time and/or date of the input and output files:

+ `newTime`
+ `newDate`
+ `nextDay`
+ `delivTime` 
+ `laterTime`

### `readFiles.py`

Contains 3 functions:

+ `readDronesFile` and `readParcelsFile` create a list with the contents of the drones and parcels files, respectively.
+ `readHeader` creates a list with the contents of the header of the file.

### `writeFiles.py`

Contains the functions `writeHeaderD` and `writeBodyD` which create and write the header and content for the updated drones file, respectively. `writeHeaderP` and `writeBodyP` do the same for the pairings output file.

### `organize.py`

Contains 5 functions:

+ `updateDrone`: updates drone characteristics after it's paired to a parcel.
+ `pairPD`: creates a list with each pairing.
+ `cancelledP`: creates a list of unattended orders.
+ `compareHeaders` and `compNameHeader`: used to raise exceptions if the headers contents of the entry files do not match.

### `dronyD.py`

Contains the code to be executed and the main function of the program - `allocate`: 

+ `allocate`: receives the drones and parcels `txt` files and creates the pairings and updated drones `.txt` files.
