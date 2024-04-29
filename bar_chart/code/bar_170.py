
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)

# Define data
cities = ['New York', 'Los Angeles', 'Chicago', 'Dallas']
houses_sold = [400, 500, 600, 700]
avg_sale_price = [400, 500, 350, 450]

# Plot data
ax.bar(cities, houses_sold, width=0.2, label='Houses Sold')
ax.bar(cities, avg_sale_price, width=-0.2, label='Average Sale Price(thousand)', bottom=houses_sold)

# Set axes ticks
ax.set_xticks(cities)

# Add title and legend
ax.set_title('Number of Houses sold and Average Sale Price in four cities in 2021')
ax.legend(loc='upper right')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('bar_170.png')

# Clear image
plt.clf()