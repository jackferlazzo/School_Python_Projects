#Used to plot the data in the Lab 2 part B
import matplotlib.pyplot as plt
ans = 'y'
data = []
cellNumber = list(range(1,6))
while ans != 'n':
    data.append(float(input('Volts: ')))
    ans = input('would you like to enter more data: ')
plt.plot(cellNumber, data)
plt.xlabel('Number of Cells')
plt.ylabel('Voltage (Volt)')
plt.axis
plt.xticks(cellNumber)
plt.show()