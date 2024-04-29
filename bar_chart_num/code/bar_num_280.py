
import matplotlib.pyplot as plt
import numpy as np

mode = ['Air', 'Sea', 'Rail', 'Road']
capacity = [200, 400, 300, 500]
delivery_time = [3, 7, 4, 2]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(mode, capacity, width=0.5, label='Capacity', color='lightblue')
ax.bar(mode, delivery_time, width=0.5, bottom=capacity, label='Delivery Time', color='pink')

ax.set_title('Capacity and delivery time of four modes of transportation in 2021')

ax.set_xticks(mode)
ax.set_xticklabels(mode, rotation=30, ha='right')
ax.legend(loc='upper left')

for i in range(len(mode)):
     ax.annotate(capacity[i], xy=(i-0.05, capacity[i]/2))
     ax.annotate(delivery_time[i], xy=(i-0.05, capacity[i]+delivery_time[i]/2))

plt.tight_layout()
plt.savefig('Bar Chart/png/26.png')
plt.clf()