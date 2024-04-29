
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Fashion','Home Appliances','Technology','Beauty','Toys','Sports','Grocery','Pet Supplies']
data = [150,120,100,80,60,50,40,20]
line_labels = ['Product Category','Number']

# Set up figure
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=f'C{i}')

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=90)
ax.legend(bbox_to_anchor=(1.2, 0.6))
ax.set_title('Number of Products Sold in E-Commerce Stores in 2021')

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_40.png')

# Clear the current image state
plt.clf()