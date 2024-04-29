

import matplotlib.pyplot as plt
import numpy as np

# Create figure 
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Data
data = [[1000, 800, 1200, 1500],
        [1200, 900, 1100, 1600],
        [800, 1100, 1300, 1200],
        [1500, 1200, 1400, 800]]

# Months
months = ['April', 'May', 'June', 'July']

# Hotels
hotels = ['Hotel A', 'Hotel B', 'Hotel C', 'Hotel D']

# Set color
colors = ['b', 'r', 'g', 'y']

# Plot chart
for i in range(len(hotels)):
    ax.plot(data[i], color=colors[i], label=hotels[i], marker='o')

# Label each point
for i in range(len(hotels)):
    for j in range(len(months)):
        ax.annotate(str(data[i][j]), xy=(i, data[i][j]), xytext=(i-0.1, data[i][j]+50))

# Set xticks
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=20, wrap=True)

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Adjust layout
plt.tight_layout()

# Set title
plt.title('Accommodation Occupancy Rate in Four Hotels during Spring and Summer')

# Save figure
plt.savefig('line chart/png/154.png')

# Clear figure
plt.clf()