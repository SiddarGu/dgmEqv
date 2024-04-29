
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[3000, 4], [2000, 8], [6000, 12], [4000, 6]])

plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(data[:, 0], data[:, 1], width=1000, bottom=0)
ax.set_title('Distance and time of transportation by different modes in 2021')
ax.set_ylabel('Time (hours)')
ax.set_xlabel('Distance (miles)')
ax.set_xticks(data[:, 0])
ax.set_xticklabels(('Plane', 'Train', 'Ship', 'Truck'))
ax.tick_params(axis='x', rotation=90, labelsize=9, labelcolor='black')
ax.legend(('Mode',), loc='upper right', fontsize=10)
plt.tight_layout()
plt.savefig('bar chart/png/151.png')
plt.clf()