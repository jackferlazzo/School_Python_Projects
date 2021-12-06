# Python Homework 6 Problem 2 Sawtooth
# File: HW6_Prob2_sawtooth_jferlazz.py
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
# This program accepts the following floating point values as inputs: ampl,
# the amplitude of the sawtooth function, period, the period of the sawtooth
# function, tMax the upper limit of time for the plot, and tStep the time step.
# This program then returns the approximate values of the sawtooth function for each t from
# t = 0 to t =tMax in the steps size tStep

#---------------------------------------------------
#  Inputs
#---------------------------------------------------

import numpy as np
import math

#---------------------------------------------------
#  Computations
#---------------------------------------------------
def sawtoothFunction(ampl, period, tMax, tStep):
    timeList = list(np.arange(0, tMax+tStep, tStep))
    floorValues = []
    sawtoothValues = []
    for time in timeList:
        floorN = math.floor(time / period)   #floor(t/T)
        floorValues.append(time - (floorN * period))
        
        #making sure each time is between 0 and the period
    for value in floorValues:
        if(value >= 0 and value < (period/2)): 
            
        #if the time is between 0 and half the period
            sawtoothValues.append(((2 * value * ampl) / period)) 
            
            #approximation at that time
        else:
            sawtoothValues.append(((2 * value * ampl) / period) - (2 * ampl))
            
            #approximation at that time
    
#---------------------------------------------------
#  Output
#---------------------------------------------------
    return (sawtoothValues)
        
        