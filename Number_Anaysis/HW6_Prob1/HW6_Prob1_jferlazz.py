# Python Homework 6 Problem 1
# File: HW6_Prob1_jferlazz.py
# Date: 19 October 2020
# By: Jack Ferlazzo
# jferlazz
# Section: 5
# Team: 72
#
# ELECTRONIC SIGNATURE
# Jack Ferlazzo
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# This program takes the data of PlantId, Status, StartingHeight, EndingHeight,
# and Concentration for a number of plants from a file 
# plant_treatment_data.txt, then user enters a code on how to resort the data,
# outputting the resorted data to a new file using the name the user entered

#---------------------------------------------------
#  Inputs
#---------------------------------------------------
fileName = input("Enter a file name for the reorganized data: ")
dataCode = input("Enter a code for the reorganization: ")
fidI = open("./plant_treatment_data.txt", "r")

#opens the file plant_treatment_data.txt in read mode

#---------------------------------------------------
#  Computations
#---------------------------------------------------
def sortData (dataCode, dataBeingSorted, dataPoints):
    sortedList = [] #empty list to be appended to later
    if (dataCode[1] == "A"): #ascending mode
        while(len(dataPoints) > 0): #while the list still has data in it
            minimum = dataPoints[0] #sets the first element as minimum
            for data in dataPoints: #goes through each plant's data
                if (data[dataBeingSorted] < minimum[dataBeingSorted]):
                    minimum = data
                    
                #if the data point being looked at i.e. plant id
                #is less than the current minimum it becomes the new minimum
            sortedList.append(dataPoints.pop(dataPoints.index(minimum)))
            
            #pops off the plant with the minimum value being looked at
            #from list dataPoints and appends it to the end of sortedList
            
    else: #decending mode
        while(len(dataPoints) > 0): #while the list still has data in it
            maximum = dataPoints[0] #sets the first element as maximum
            for data in dataPoints:
                if (data[dataBeingSorted] > maximum[dataBeingSorted]):
                    maximum = data
                    
                #if the data point being looked at i.e. plant id
                #is more than the current maximum it becomes the new maximum
            sortedList.append(dataPoints.pop(dataPoints.index(maximum)))
            
            #pops off the plant with the minimum value being looked at
            #from list dataPoints and appends it to the end of sortedList
    return(sortedList)
            
fileList = fidI.readlines() #reads fidI into a list
fidI.close()
header = fileList.pop(0)
headerList = header.split()
headerList.pop(2)
headerList[2] = "Growth"

#pulls off the header from the fileList and removes both StartingHeight and 
#EndingHeight replacing it will the header Growth
dataPoints = []
for element in fileList:
    dataPoints.append(element.split())
for data in dataPoints:
    start = float(data.pop(2))
    end =float(data.pop(2))
    data.insert(2,str(round(end-start, 2)))
    
    #inserts how much each plant has grown replacing both starting and ending
    #heights
sortedList = []
if (dataCode[0] == "P"): #sort by plant id
    sortedList = sortData(dataCode, 0, dataPoints) #plantId is in the 0 index
elif (dataCode[0] == "S"): #sort by Status
    sortedList = sortData(dataCode, 1, dataPoints) #Status is in the 1st index
elif (dataCode[0] == "G"): #sort by growth
    sortedList = sortData(dataCode, 2, dataPoints) #Growth is in the 2nd index
else: #sort by concentration
    sortedList = sortData(dataCode, 3, dataPoints) 
    #Concentration is in the 3rd index   
#---------------------------------------------------
#  Output
#---------------------------------------------------
newFile = open(fileName, "w") 

#opens a file with the name the user entered in write mode
newFile.write("%s  %s  %s  %s\n" % 
              (headerList[0], headerList[1], headerList[2], headerList[3]))

#formats the header onto the file
for storedData in sortedList:
    string = ("%s      %s       %s    %s\n" % 
    (storedData[0], storedData[1], storedData[2], storedData[3]))
    newFile.write(string)
    
    #formats each plant's data in a sorted order onto the file
newFile.close()