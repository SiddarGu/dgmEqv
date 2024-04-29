
import matplotlib.pyplot as plt
import numpy as np

# Create new figure and plot data
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

# Create data
year = ['2010','2011','2012','2013']
fruit_prod = [50000,55000,70000,60000]
veg_prod = [60000,70000,65000,55000]
grain_prod = [70000,65000,60000,70000]

# Plot data
ax.plot(year, fruit_prod, color="red", label="Fruit Production (tons)")
ax.plot(year, veg_prod, color="green", label="Vegetable Production (tons)")
ax.plot(year, grain_prod, color="blue", label="Grain Production (tons)")

# Set x axis label
plt.xlabel('Year')

# Set title
plt.title('Crop Production in the U.S. from 2010 to 2013')

# Show legend
ax.legend(loc="upper left", bbox_to_anchor=(1,1))

# Set grid
plt.grid(True)

# Set ticks
xticks = np.arange(0, 4, 1) 
plt.xticks(xticks, year, rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/195.png')

# Clear the current image state
plt.clf()