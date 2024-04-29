
import matplotlib.pyplot as plt
import numpy as np

# Read data
data = [['USA', 4000, 3000],
        ['UK', 3500, 2500],
        ['Germany', 3000, 3500],
        ['Australia', 2500, 4000]]

# Define variables
country = [row[0] for row in data]
fast_food = [row[1] for row in data]
healthy_food = [row[2] for row in data]

# Create an image
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot data
ax.plot(country, fast_food, color='tomato', label='Fast Food')
ax.plot(country, healthy_food, color='dodgerblue', label='Healthy Food')

# Set the title and legend
ax.set_title('Fast food consumption versus healthy food consumption in selected countries')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=2)

# Set the ticks and tick labels
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country, rotation=45, ha='right')

# Adjust the layout
fig.tight_layout()

# Save the figure
plt.savefig('line chart/png/13.png')

# Clear the current image state
plt.clf()