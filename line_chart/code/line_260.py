
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'Time':['00:00','01:00','02:00','03:00','04:00','05:00','06:00'], 
                     'Pollutant A':[15,14,12,10,13,15,18],
                     'Pollutant B':[20,18,15,12,11,14,19], 
                     'Pollutant C':[10,13,9,7,8,10,12]})

plt.figure(figsize=(8,6))
ax = plt.subplot()

ax.plot(data['Time'],data['Pollutant A'], label='Pollutant A', color='red')
ax.plot(data['Time'],data['Pollutant B'], label='Pollutant B', color='green')
ax.plot(data['Time'],data['Pollutant C'], label='Pollutant C', color='blue')

plt.xticks(data['Time'])
ax.set_title('Pollution levels in Los Angeles on April 15th, 2021')
ax.set_xlabel('Time')
ax.set_ylabel('Pollution Level')
ax.legend(loc='upper left', fontsize='large')
plt.grid(linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig('line chart/png/252.png')

plt.clf()