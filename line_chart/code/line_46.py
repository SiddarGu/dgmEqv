
import matplotlib.pyplot as plt
import numpy as np

data = [['January',7.5,15,1012],
        ['February',8,18,1015],
        ['March',9.2,20,1017],
        ['April',7.8,22,1020],
        ['May',6.3,25,1022],
        ['June',5.5,28,1025],
        ['July',4.2,31,1027],
        ['August',3.9,33,1030]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.set_title('Variation of wind speed, temperature and pressure in the summer of 2021')
ax.set_ylabel('Value (m/s, degrees Celsius, hPa)')
ax.set_xlabel('Month')
ax.grid(axis='y', alpha=0.75)

Month, Wind_Speed, Temperature, Pressure =[],[],[],[]
for row in data:
    Month.append(row[0])
    Wind_Speed.append(row[1])
    Temperature.append(row[2])
    Pressure.append(row[3])

ax.plot(Month, Wind_Speed, label='Wind Speed',color='red', linewidth=2, marker='o', markerfacecolor='blue', markersize=3)
ax.plot(Month, Temperature, label='Temperature',color='green', linewidth=2, marker='o', markerfacecolor='blue', markersize=3)
ax.plot(Month, Pressure, label='Pressure',color='black', linewidth=2, marker='o', markerfacecolor='blue', markersize=3)

ax.set_xticklabels(Month, rotation=45, ha="right", rotation_mode="anchor")
ax.legend(loc='upper right')
#ax.set_yticks(np.arange(0,36,5))
plt.tight_layout()
plt.savefig('line_46.png')
plt.clf()