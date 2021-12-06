# Activity: Program HW Problem 1
# File:     HW3_Prob1_jferlazz.py
# Date:     18 September 2020
# By:       Jack Ferlazzo
#           jferlazz
# Section:  5
# Team:     72
# ELECTRONIC SIGNATURE
# Jack Ferlazzo
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work.  I have
# a general understanding of all aspects of its development
# and execution.
#
# This program take input from the user on the cooridates, forces on 3 cables,
# height of the tower and the maximum value for the overturning moment. 
# This program breaks down the cables forces into components. It then find the
# resultant vector of all three cables, and then using the <0,0,1> unit
# vector for the cell, the program finds the perpendicular vect or its 
# magnitude, then the program outputs the overtuning moment magnitude and 
# wether or not the restaints are safe for overturning
#----------------------------------------------------------------------------------------------------------------------------
#                                                         input
# Cordlist is the list of cable coordinates
# Force1 is the force magnitude of cable 1, Force2 is the force magnitude 
# of cable 2, Force3 is the force magnitude of cable 3
# all forces are in newtons
# height is the height of the cell tower in meters
# Mmax is the maximum overturning moment magnitude  that is acceptable, in N-m
#----------------------------------------------------------------------------------------------------------------------------
import math
cycle = 0
cordList = []
cableName = ["A", "B", "C"]

while (cycle <= 2):
    cordList = cordList + (input("please enter the coordinates "
        +"of the cable anchored at " + cableName[cycle] 
        +" (in meters) in the form x,y: ")).split(",")      #Meters

    #takes the input of the coordinates of each cable from the user in x,y form
    #and splits at the comma creating a list of all x and y coordinate split up
    #but in corresponding grousp of 2
    cycle = cycle + 1
    
    #incriments cycle
cycle = 0

#resets cycle to 0 for the next list

while (cycle < 6):
    cordList[cycle] = float(cordList[cycle])        #Meters                    
    cycle = cycle + 1 

    #incriments the count                                               
                                                                 
    #when inputed in the by the user the coodinates are strings in
    #order for them to used mathmatically they need to be casted as floats

cycle = 0                                                         
forceList = []                  #Newtons
cableName = ["DA", "DB", "DC"]                                             
while (cycle <= 2):
    forceList.append(float(input("please enter the tensile force of cable " 
                    + cableName[cycle] + " (in Newtons): ")))   #Newtons
    cycle = cycle + 1
    
    #incriments the count

    #takes user input on the cable force then casts 
    #them as float while appending them onto a list

height = float(input("Enter height (in meters): "))     #Meters

maxOver = float(input("Enter the maximum value for "
                      +"the overturning moment (in N-m): "))    #N-m

#----------------------------------------------------------------------------------------------------------------------------------
#                                                                Calculations
#----------------------------------------------------------------------------------------------------------------------------------

def forceComponents(forceMag, xComp, yComp, height):
    posMag = math.sqrt((pow(xComp, 2)) + pow(yComp, 2) + pow(height, 2))    #N
    
    #Calculated the magnitude of the position vector sent in
    unitVec = [(xComp / posMag),(yComp / posMag),(height / posMag)]
    
    #This magnitude is used to find the unit vector
    forceVec = []               #Newtons
    for comp in unitVec:
        forceVec.append(comp * forceMag)        #Newtons
    
    #The unit vector's components are then multipled by the force magnitude
    #to find the force vector
    return forceVec     #This is a list (vectors) with its elements in Newtons

forceVecDA = forceComponents(forceList[0], cordList[0], cordList[1],height)
forceVecDB = forceComponents(forceList[1], cordList[2], cordList[3],height)
forceVecDC = forceComponents(forceList[2], cordList[4], cordList[5],height)               

#breaking up each force into vector components using the unit vector found from position

resForceVec = []
count = 0
for forceDA in forceVecDA:
    resForceVec.append(forceDA + forceVecDB[count] + forceVecDC[count])                 
    
    #adding up get vector components above to get the resulant vector
    count = count + 1
    
    #incriments the count


heightUnitVec = [0.0,0.0,1.0]
resUnitDotProduct = 0.0
count = 0
for resForce in resForceVec:
    resUnitDotProduct += resForce * heightUnitVec[count]                                
    
    #finds the dot product between resultant vector and the unit vector
    count = count + 1
    
    #incriments the count

perpForce = []
count = 0
for unitVec in heightUnitVec:
    perpForce.append(resForceVec[count] - (unitVec*resUnitDotProduct))                   
    
    #finds the perpendicular force vector by multiplying the dot product of
    #resultant vector and the unit vector by the unit vector, then
    #then subtracting that from the resultant vector to find the perpendicular
    #vecto
    count = count + 1     

    #incriments the count                                                  
                                                                               

perpVecMag = math.sqrt(pow(perpForce[0], 2) + pow(perpForce[1], 2) 
                      + pow(perpForce[2], 2))   #Newtons

#Finds the magnitude of the perpendicular vector
mOver = height * perpVecMag         #N-m

#Finds the overturning magnitude with the magnitude of the perpendicular
#force vector and the height

#--------------------------------------------------------------------------------------------------------
#                                                Output
#--------------------------------------------------------------------------------------------------------

print("The overturning moment magnitude is "+str(round(mOver, 1)) + " N-m")

#Outputs the calculated overturning magnitude rounded the nearest tenths place

#If the calculated overturning magnitude is less then the max overturning
#magnitude
if (mOver < maxOver):
    print("This restraining system is safe.")
    
    #If true it outputs that the restaining system is safe
else:
    print("This restraining system isn't safe")
    
    #If false it outputs that the restraining system isn't safe
