
import matplotlib.pyplot as plt
import numpy as np

speed = [0, 10, 20, 30, 40, 50]
time = [0, 2, 4, 6, 8, 10]
distance = [0, 20, 40, 60, 80, 100]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(1,1,1)
ax.plot(time, speed, label='Speed (m/s)', color='red', marker='o', markerfacecolor='blue', markersize=7)
ax.plot(time, distance, label='Distance (m)', color='blue', marker='o', markerfacecolor='red', markersize=7)
plt.title("Speed and Distance Relationship of a Moving Object on May 15, 2021")
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.xlabel('Time (s)')
plt.xticks(time)
plt.ylabel('Distance and Speed (m/s)')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/542.png')
plt.clf()