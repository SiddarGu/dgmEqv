
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot the data with the type of bar chart
region =['North America', 'South America','Europe', 'Asia']
users_million = [200, 150,350, 550]
data_consumption = [1300, 1000, 1800,2500]
x = np.arange(len(region))

ax.bar(x - 0.2, users_million, width=0.4, color='b', label='Users (million)')
ax.bar(x + 0.2, data_consumption, width=0.4, color='g', label='Data Consumption (GB)')

# Positioning of the legend should not interfere with the chart and title
ax.legend(loc='best')

# Automatically resize the image by tight_layout()
fig.tight_layout()

# Use xticks to prevent interpolation
plt.xticks(x, region)

# The title of the figure
plt.title('Technology and internet usage in four regions in 2021')

# Save the image 
plt.savefig('bar chart/png/541.png')

# Clear the current image state
plt.clf()