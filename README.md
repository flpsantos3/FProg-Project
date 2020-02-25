# Assessment for the class Fundamentos de Programação (Programming Fundamentals)

## Context

A certain company wants to use drones to deliver packages or parcels across various areas of Lisbon. 
To do that, they need a program that receives two .txt entry files, **drones** and **parcels**, and returns two .txt files, the **drone-parcel pairings** and the **updated drones list**.

## The Program

There are a total of 5 modules, with the main module being **dronyD.py**, which contains `allocate`, the main function of the program. **dronyD.py** can be executed in command line by running the command `python dronyD.py inputFile1 inputFile2`.

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

Contains 3 functions that deal with converting the content in the input files to various lists:

+ `readDronesFile` and `readParcelsFile` create a list with the contents of the drones and parcels files, respectively.
+ `readHeader` creates a list with the contents of the header of the file.

### `writeFiles.py`

Contains 4 functions that create and write the content for both output files:

+ `writeHeaderD` and `writeBodyD`: create and write the header and content for the updated drones file, respectively. 
+ `writeHeaderP` and `writeBodyP`: create and write the header and content for the pairings output file, respectively. 

### `organize.py`

Contains 5 functions where 3 deal with drones and pairing info and the last 2 are functions created to evaluate exceptions:

+ `updateDrone`: updates drone characteristics after it's paired to a parcel.
+ `pairPD`: creates a list with each pairing.
+ `cancelledP`: creates a list of unattended orders.
+ `compareHeaders` and `compNameHeader`: used to raise exceptions if the headers contents of the entry files do not match.

### `dronyD.py`

Contains the code to be executed and the main function of the program - `allocate`: 

+ `allocate`: receives the drones and parcels .txt files and creates the pairings and updated drones .txt files.
