
import matplotlib.pyplot as plt
import numpy as np

# Set figure size to prevent content from being displayed
plt.figure(figsize=(10,6))

# Create a figure
ax = plt.subplot()

# Set x, y and labels
region = np.arange(4)
restaurants = [200, 180, 220, 240]
cafes = [150, 170, 200, 190]
bars = [100, 90, 110, 140]
labels = ['North America', 'South America', 'Europe', 'Asia']

# Plot bar chart
bar_width = 0.2
ax.bar(region, restaurants, width=bar_width, label='Restaurants', color='b')
ax.bar(region+bar_width, cafes, width=bar_width, label='Cafes', color='g')
ax.bar(region+2*bar_width, bars, width=bar_width, label='Bars', color='r')

# Set xticks
plt.xticks(region+bar_width, labels, rotation=45, wrap=True)

# Add title and legend
ax.set_title('Number of food and beverage outlets in four regions in 2021')
ax.legend(loc="best")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig("bar chart/png/545.png")

# Clear the current image state
plt.clf()