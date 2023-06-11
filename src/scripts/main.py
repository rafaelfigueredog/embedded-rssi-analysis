import rssi
import time
import json

# Set wireless interface of your machine 
INTERFACE = 'wlp0s20f3'

# set ssids you are interested to collect rssi
SSIDS = ['NOKIA-402343AC9C25-5']

# set the size of collections 
SIZE_OF_DATA = 100

# instanciate the scanner
scanner = rssi.RSSI_Scan(INTERFACE)

# file name output
outputFile = '../data/new-collection.json'


# validate scanner data
def isValidSignalStrength(signalInfo): 
    if type(signalInfo) == bool: 
        return False
    return True

# get signal power
def getSignalStrength(): 
    while True: 
        signalInfo = scanner.getAPinfo(networks=SSIDS, sudo=True)
        if (isValidSignalStrength(signalInfo)): 
            return signalInfo[0]  

if __name__ == "__main__":

    # start the data  
    data = []
    
    while(len(data) < SIZE_OF_DATA):

        # get signal power
        signalStrength = getSignalStrength()

        # push signal power in the array
        data.append(signalStrength)
        
        # wait 5 seconds
        time.sleep(5)

        # progress logger. 
        print('Logger: %d/%d collected' %(len(data), SIZE_OF_DATA))   

    # save data on json file. 
    with open(outputFile, 'w') as outfile:
        json.dump(data, outfile)