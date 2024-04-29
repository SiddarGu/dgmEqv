
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

Type = np.array(['Bus', 'Car', 'Bicycle', 'Motorcycle'])
Distance = np.array([20, 20, 20, 20])
Time = np.array([20, 15, 30, 25])

ax.plot(Type, Distance, color='g', label='Distance(miles)')
ax.plot(Type, Time, color='r', label='Time(minutes)')
ax.set_xticks(Type)
ax.set_title("Comparing the Time and Distance of Different Modes of Transportation for a 20-Mile Journey")
ax.grid()
ax.legend()

for i,j in zip(Type,Time):
    ax.annotate(str(j),xy=(i,j+1))

plt.tight_layout()
plt.savefig("line chart/png/379.png")
plt.show()
plt.clf()