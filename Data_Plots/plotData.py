#Used to plot the data in the first part of lab 1
import matplotlib.pyplot as plt
ans = 'y'
data = []
cellNumber = list(range(1,6))
while ans != 'n':
    data.append(float(input('Volts: ')))
    ans = input('would you like to enter more data: ')
plt.plot(time, data)
plt.xlabel('Number of Cells')
plt.ylabel('Voltage (Volt)')
plt.show()