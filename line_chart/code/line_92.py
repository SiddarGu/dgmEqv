
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot line chart
x = np.arange(5)
y1 = np.array([14.4, 14.8, 15.2, 15.7, 16.1])
y2 = np.array([1000, 1200, 1300, 1400, 1500])
y3 = np.array([400, 450, 500, 550, 600])
ax.plot(x, y1, color='r', marker='o', linestyle='--', label='GDP(in trillions)')
ax.plot(x, y2, color='g', marker='o', linestyle='--', label='Income Tax(in billions)')
ax.plot(x, y3, color='b', marker='o', linestyle='--', label='Corporate Tax(in billions)')

# Add grids
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set range of x-axis
plt.xticks([0, 1, 2, 3, 4], ['2010', '2011', '2012', '2013', '2014'])

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Add titles
plt.title('Economic development of the United States in 2010-2014')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/232.png')

# Clear current image state
plt.clf()