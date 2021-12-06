# Activity: Program HW Problem 2
# File:     HW3_Prob2_jferlazz.py
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
# This program take input from the user on a guitar's string
# fundemential frequnency, Lower frequency, and upper frequency bound
# and the number of hamonics the user want to evaluate, and determines which
# harmonics will be filter fully, partially or not at all
#----------------------------------------------------------------------------------------
#                                       Input
# The fundamental frequency f1 of a certain guitar string (in Hertz)
# The values of fLow and fHigh (in Hertz) that define the band-pass filer
# An integer N that indicates how many harmonics the sound engineer wishes 
# to investigate
#----------------------------------------------------------------------------------------
funFreq = float(input("Enter the fundamental frequency of a "
                      +"certain guitar string (in Hertz): "))   #Hertz
freqLow = float(input("Enter the lowest frequency of the" 
                      +"band pass filter (in Hertz): "))        #Hertz
freqHigh = float(input("Enter the highest frequency of the "
                       +"band pass filter (in Hertz): "))       #Hertz
harmonics = int(input("How many harmonics do want to investigate: "))
count = 1
while (count <= harmonics):
    testFreq = funFreq*count    #Hertz
    
    #the frequency being tested is equal to fundimental frequency times the
    #hamonic level being tested
    
    #if test frequency is greater than the higher bound or less than the
    #lower bound filter it our
    if (freqHigh < testFreq) or (freqLow > testFreq):
        print("Harmonic " + str(count) + " is completely filtered")
        
    #If true output that the harmonic is completely filtered
    #If false test if test frequency is greater than the upperbound *.9
    #or is it is less than the lower bound *1.1
    elif (freqHigh * .9 < testFreq) or (freqLow * 1.1 > testFreq):
        print("Harmonic " + str(count) + " is partial filtered")
    
    #If true output that the harmonic is partial filtered
    #If false output that the jarmonic is not filtered
    else:
        print("Harmonic " + str(count) + " is not filtered")
    count = count + 1
    
    #increment the counter to test a new harmonic level
    