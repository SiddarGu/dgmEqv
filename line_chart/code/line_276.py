
import matplotlib.pyplot as plt
import numpy as np

Month=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
Temperature = [15,16,17,18,20,22,24,25]
Humidity = [50,45,40,35,30,25,20,15]
Wind_Speed = [3,4,2,1,3,4,2,1]

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)
ax1.plot(Month, Temperature, label='Temperature(degrees Celsius)', color='orange')
ax1.plot(Month, Humidity, label='Humidity(%)', color='green')
ax1.plot(Month, Wind_Speed, label='Wind Speed(m/s)', color='blue')
ax1.set_title('Weather changes in a tropical area in 2020', fontsize=14, fontweight=0, color='black')
plt.xticks(np.arange(len(Month)), Month, rotation=45, fontsize=10, fontweight=0)
plt.legend(loc='upper right', bbox_to_anchor=(1.0, 1.00))
plt.tight_layout()
plt.savefig(r'line chart/png/457.png')
plt.clf()