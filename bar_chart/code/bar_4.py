

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111)

# Data
Region = np.array(['North America','South America','Europe','Asia'])
Renewable_Energy = np.array([400,450,420,470])
Fossil_Energy = np.array([500,450,480,520])

# Plot bar
bar_width = 0.35
index = np.arange(len(Region))
ax.bar(index, Renewable_Energy, bar_width, color='b', label='Renewable Energy')
ax.bar(index+bar_width, Fossil_Energy, bar_width, color='g', label='Fossil Energy')

# Setting labels
ax.set_xticks(index + bar_width/2)
ax.set_xticklabels(Region, rotation = 0, wrap=True)
ax.set_title('Renewable and fossil energy consumption in four regions in 2021')
ax.set_ylabel('Energy(TWh)')
ax.legend(loc='upper left')

# Setting background
ax.grid(linestyle='--', color='gray')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save image
plt.savefig('bar chart/png/553.png')

# Clear current image state
plt.clf()