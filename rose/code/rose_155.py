
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Livestock', 'Aquaculture', 'Forestry', 'Herbs']
data = np.array([80, 90, 70, 50, 40, 30, 20, 10])
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart.
fig, ax = plt.subplots(figsize=(8, 8))
sector_angles = (2 * np.pi) / len(data_labels)

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
ax = plt.subplot(111, projection='polar')

# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value, 
# and the angles of these sectors must add up to 360 degrees
# use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle 
# and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
for i in range(len(data_labels)):
    ax.bar(i * sector_angles, data[i], width=sector_angles, label=data_labels[i], color=plt.cm.Set1(i))

# Assign a different color to each sector, and add a legend next to the chart that clearly labels the category each sector represents,
# ensuring that the legend does not obscure any part of the chart.
ax.legend(bbox_to_anchor=(1.2, 0.9))

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
# Set the labels of categories at the center of corresponding sector
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angles))
ax.set_xticklabels(data_labels, fontsize=7)

# The title of the figure should be Global Production of Agricultural Goods in 2020.
plt.title('Global Production of Agricultural Goods in 2020')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_44.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_44.png")

# Clear the current image state at the end of the code.
plt.clf()