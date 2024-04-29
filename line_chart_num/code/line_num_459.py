
import matplotlib.pyplot as plt
import numpy as np 

Time = np.array(['00:00', '01:00', '02:00', '03:00', '04:00', '05:00'])
Number_of_Planes = np.array([10, 11, 13, 15, 18, 19])
Number_of_Trains = np.array([15, 13, 10, 12, 14, 15])
Number_of_Cars = np.array([20, 18, 15, 17, 20, 22])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.plot(Time, Number_of_Planes, label='Number of Planes')
ax.plot(Time, Number_of_Trains, label='Number of Trains')
ax.plot(Time, Number_of_Cars, label='Number of Cars')
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 0.9))
ax.set_title('Transportation usage in North America on March 19, 2023')
ax.set_xlabel('Time')
ax.set_ylabel('Number of Transportation')
ax.grid(linestyle='--')
ax.xaxis.set_ticks(Time)
plt.tight_layout()

for i, j in zip(Time, Number_of_Planes):
    ax.annotate(str(j), xy=(i, j))

for i, j in zip(Time, Number_of_Trains):
    ax.annotate(str(j), xy=(i, j))

for i, j in zip(Time, Number_of_Cars):
    ax.annotate(str(j), xy=(i, j))

plt.savefig('line chart/png/302.png')
plt.clf()