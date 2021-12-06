# Python Homework 6 Problem 2 Script
# File: HW6_Prob2_script_jferlazz.py
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
# This program accept user input for the floating point values of amplitude, 
# period, the upper time limit of the sawtooth function, and the integer value
# of capK that indicates the number of terms in the Fourier series you will 
# use to approximate the sawtooth function, this code then finds the 
# approximate and actual values of the sawtooth function and graphs them both

#---------------------------------------------------
#  Inputs
#---------------------------------------------------

from HW6_Prob2_sawtooth_jferlazz import sawtoothFunction 

#importing the sawtooth function from the sawtooth file
import matplotlib.pyplot as plot
import numpy as np
import math

#importing libraries
ampl = float(input("Enter the amplitude of the sawtooth function: "))
period = float(input("Enter the period of the sawtooth function"
                     + "(in seconds): "))
tMax = float(input("Enter the upper time limit for plotting the sawtooth "
          + "function (in seconds): "))
kCap = int(input("Enter the number of terms to use in the Fourier series: "))

#user imports

#---------------------------------------------------
#  Computations
#---------------------------------------------------

tStep = period / 60

#30 steps per period
approximateValues = sawtoothFunction(ampl, period, tMax, tStep)

#calling the function from the other file
timeList = np.arange(0, tMax + tStep, tStep)   #creates a list of floats
actualValues = []
time = 0
while time <= (tMax + tStep):  #so the program won't evalute time over tMax
    sumValue = 0
    for kValue in range(1, kCap+1):
        bKVal = (((-2 * ampl) / (math.pi * kValue)) * pow(-1, kValue)) 
        
        #bk element of the summation
        secondValue = math.sin(time * ((2 * kValue * math.pi) / period))
        
        #sine element of the summation
        sumValue = sumValue + (bKVal * secondValue)
        
        #incrimenting the sum by the 2 elements
    time = time + tStep     #incrimenting time by tStep
    actualValues.append(sumValue)   
    
    #add the sum value for each time on the list actualValues
fig, data = plot.subplots()
data.plot(timeList, approximateValues, "red", label="Approximate")
data.plot(timeList, actualValues, "blue", label="Actual")
leg = data.legend() 
plot.title("Sawtooth Function: Actual vs Approximate")
plot.xlabel("Time, t (seconds)")
plot.ylabel("S(t)")