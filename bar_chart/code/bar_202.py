
import matplotlib.pyplot as plt
import numpy as np

# Set figure size and dpi
plt.figure(figsize=(14, 8), dpi=100)

# Set chart title and label axes
plt.title('Fruit and Vegetable Production in four regions in 2021')
plt.xlabel('Region')
plt.ylabel('Production (tonnes)')

# Set data
regions = ['North America', 'South America', 'Europe', 'Asia']
fruits = [250000, 200000, 400000, 270000]
vegetables = [300000, 200000, 350000, 400000]

# Plot bars
x_pos = np.arange(len(regions))
width = 0.35

ax = plt.bar(x_pos - width/2, fruits, width, label='Fruit Production')
ax = plt.bar(x_pos + width/2, vegetables, width, label='Vegetable Production')

# Set x-axis tickes
plt.xticks(x_pos, regions, rotation=90, wrap=True)

# Add legend
plt.legend()

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/116.png')

# Clear the current image state
plt.cla()