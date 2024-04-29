
import matplotlib.pyplot as plt
import numpy as np

# transform the data into three variables
data_labels = ['Wheat','Rice','Corn','Soybeans','Sunflowers','Barley','Sorghum','Oats','Potatoes','Tomatoes']
data = [5,6,7,8,9,10,11,12,13,14]
line_labels = ['Crop','Yield']

# plot the data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, polar=True)

# create sectors
for i in range(0,num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.jet(i/num_categories))

# Create legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 1),loc='upper right', fontsize='x-large')

# Set the number of ticks equal to the number of categories
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set the labels for each tick
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=90)

# Set the title
ax.set_title("Yield of Major Crops in 2021", fontsize=15)

# Adjust the space between the legend and chart
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_20.png")

# Clear the current image state
plt.clf()