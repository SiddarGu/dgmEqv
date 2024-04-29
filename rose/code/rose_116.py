
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data
data_labels = ['Wheat', 'Rice', 'Corn','Soybean','Potato','Onion','Tomato','Carrot','Cabbage']
data = [430,310,120,580,250,280,170,95,85]
line_labels = ['Crop Type', 'Harvest Amount']

# Create figure and plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Set xticks and xticklabels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels)

# Make legend
ax.legend(bbox_to_anchor=(1.2, 1.1))

# Set title
plt.title("Quantity of Produce Harvested in 2021")

# Tight layout
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_110.png')

# Clear current image
plt.clf()