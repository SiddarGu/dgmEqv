
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))
ax = plt.subplot(111)

time = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00']
mode = ['Car','Train','Bus','Bike','Motorcycle','Airplane','Boat']
number = [100,120,90,80,50,20,10]

ax.plot(time, number, label='Number of Passengers', color='red', marker='o', linewidth=2)
ax.set_title('Transportation passengers in a city at different times of the day on July 14, 2021')
ax.set_xlabel('Time')
ax.set_ylabel('Number of Passengers')
ax.legend()

for i, txt in enumerate(mode):
    ax.annotate(txt, (time[i], number[i]))

plt.xticks(time, rotation=90)
plt.tight_layout()
plt.savefig('line chart/png/55.png', bbox_inches='tight')
plt.clf()