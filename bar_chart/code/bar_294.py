
import numpy as np
import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure(figsize=(14,7))

# Create an Axes object
ax = fig.add_subplot()

# Plot data
x = np.arange(4)
galleries = [150,200,180,250]
museums = [230,320,280,310]
ax.bar(x - 0.2, galleries, width = 0.4, color = 'b', label = 'Galleries')
ax.bar(x + 0.2, museums, width = 0.4, color = 'orange', label = 'Museums')

# Set up the x-axis
ax.set_xticks(x)
ax.set_xticklabels(['USA','UK','Germany','France'], rotation = 0, fontsize = 12, wrap = True)

# Set up the title
ax.set_title('Number of Art Galleries and Museums in Four Countries in 2021', fontsize = 16)

# Set up the legend 
ax.legend(loc = 'upper left')

# Add grids
ax.grid(axis = 'y', linestyle = '-.', alpha = 0.5)

# Automatically adjust the figure size
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/501.png')

# Clear the current image state
plt.cla()