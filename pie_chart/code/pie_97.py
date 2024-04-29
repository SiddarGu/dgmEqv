
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Data
labels = 'Air', 'Rail', 'Road', 'Water'
sizes = [25, 15, 50, 10]

# Plot
ax.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%', textprops={'fontsize': 16})
ax.axis('equal')
ax.set_title('Global Transportation Modes Distribution in 2023')
ax.legend(labels, loc="upper left", bbox_to_anchor=(-0.1, 1.))
plt.tight_layout()
plt.savefig('pie chart/png/3.png')
plt.clf()