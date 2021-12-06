# Programming Problem 1
# File: HW4_Prob1_jferlazz.py
# Date: 2 October 2020
# By: Jack Ferlazzo
# jferlazz
# Section: 5
# Team: 72
#
# ELECTRONIC SIGNATURE
# Jack Ferlazzo
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# This program approximates the value of a definite integral using a
# user inputed upper and lower bounds and a convergence criterion value.
# It also checks that the upper bound is greater than the lower bound, and
# that the convergence crierion value is positive or an error is thrown

#---------------------------------------------------
#  Inputs
#---------------------------------------------------
import math as m
lowerBound = float(input("Enter the lower bound: "))
upperBound = float(input("Enter the upper bound: "))
conCrit = float(input("Enter the convergence criterion value: "))

#---------------------------------------------------
#  Computations
#---------------------------------------------------
def calculatePoint(x):
    return (pow((m.e),(m.cos(x))))

    #calculates an point for f(x) at value x
def calculateSn (nValue, lowerBound, upperBound):
    deltaX = (upperBound-lowerBound)/nValue
    fA = calculatePoint(lowerBound)
    
    #calculates f(a)
    fB = calculatePoint(upperBound)
    
    #calculates f(b)
    summationNum = 0.0
    for k in range(1, nValue):
        summationNum = summationNum + calculatePoint(lowerBound + (k * deltaX))
        
        #evaluates the summation
    sN = (deltaX / 2.0) * (fA + 2 * summationNum + fB)
    
    #calculates Sn
    return(sN)

if(upperBound <= lowerBound):
    print("Error: upper bound must be greater than lower bound")
elif(conCrit <= 0):
    print("Error: convergence criterion must be greater than 0")
else:
    nValue = 2
    
    #intial N value to test
    
    approxValue = 0.0
    
    #this is Sn it is just being initialized as 0.0 and calculated later
    test = True
    while(test):
        approxValue = calculateSn(nValue, lowerBound, upperBound)
        if(abs(approxValue - calculateSn(nValue-1, lowerBound, upperBound)) < conCrit):
            test = False
            
        #test to see if |Sn - Sn-1| < e, if so the loop ends
        #if not N is incrimented and tested again
        else:
            nValue = nValue + 1
#---------------------------------------------------
#  Outputs
#---------------------------------------------------
    print("The value of the intergral is ", approxValue)
    
    #still under the else statement so if any errors are thrown the program
    #will still end

