
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

region = ['North', 'South', 'East', 'West']
house_price = [500000, 600000, 450000, 700000]
rent = [2000, 2400, 1800, 2200]

# Plot house_price
x = np.arange(len(region))
ax.bar(x, house_price, label='house price', color='b', width=0.4)

# Plot rent
ax.bar(x + 0.4, rent, label='rent', color='g', width=0.4)

# Add xticks
ax.set_xticks(x + 0.2)
ax.set_xticklabels(region)

# Add legend and title
ax.legend(bbox_to_anchor=(1, 1))
ax.set_title('Average house prices and rents in four regions in 2021')

# Save figure
plt.tight_layout()
plt.savefig('bar chart/png/166.png')

# Clear the current image state
plt.clf()