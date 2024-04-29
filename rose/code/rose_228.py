
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Dairy','Fruits','Vegetables','Grains','Livestock','Aquaculture','Herbs']
data = [300, 180, 120, 90, 60, 30, 15]
line_labels = ['Crop Type','Number of Farms']

# Create figure and set axes to use polar coordinates
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# Plot data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i,category in enumerate(data_labels):
    ax.bar(i*sector_angle, data[i], width=sector_angle, label=category, color=plt.cm.Set1(i/num_categories))

# Set the legend
ax.legend(bbox_to_anchor=(0, 0, 0.75, 0.75), loc='upper center', labelspacing=0.4, ncol=2)

# Set the xticks
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=10)

# Set the title
fig.suptitle("Number of Farms Producing Food in 2021")

# Resize the image
fig.tight_layout()

# Save the image
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_50.png')
plt.clf()