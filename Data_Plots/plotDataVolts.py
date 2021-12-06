#Used to plot the data in the first part of lab 1
import matplotlib.pyplot as plt
ans = 'y'
data = []
time = list(range(0,330,30))
print(time)
while ans != 'n':
    data.append(float(input('Temp in Kelvin: ')))
    ans = input('would you like to enter more data: ')
plt.plot(time, data)
plt.xlabel('Time (m)')
plt.ylabel('Temperature (K)')
plt.show()