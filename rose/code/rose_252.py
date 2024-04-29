
import matplotlib.pyplot as plt
import numpy as np
 
# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Data represent the numerical array in the data.
data_labels = ['Clothing','Electronics','Groceries','Home and Garden','Shoes and Accessories','Beauty and Cosmetics','Toys and Games','Sports and Outdoors']
data = [83,150,200,50,30,25,40,20]
line_labels = ['Number']
 
# Plot the data with the type of rose chart. 
# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='polar')
 
# Assign a different color to each sector
sector_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#C0C0C0', '#800000']
 
# All sectors should cover the entire circumference evenly, and each sector should have the same angle. 
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
 
# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value, 
# and the angles of these sectors must add up to 360 degrees, 
# i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle 
# and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
start_angle = 0
for i in range(num_categories):
    ax.bar(start_angle, data[i], width=sector_angle, color=sector_colors[i], edgecolor='black', label=data_labels[i])
    start_angle += sector_angle
 
# Use a loop to assign a label to each sector when you create them with `ax.bar`. 
# Then, when you call `ax.legend()`, it will display labels for all categories.
ax.legend(data_labels, bbox_to_anchor=(0.9, 0.1))
 
# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.linspace(0,2*np.pi, num_categories, endpoint=False))
 
# Make sure that each category label is correctly positioned at the center of its corresponding sector. 
# This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method. 
# Ensure that each angle parameter corresponds to the center position of each sector, 
# and then use `ax.set_xticklabels` to set these category labels.
ax.set_xticklabels(data_labels, rotation=90)
 
# Drawing techniques such as background grids can be used.
ax.grid(True)
 
# The title of the figure should be  Number of Products Sold in E-commerce Stores in 2021.
ax.set_title('Number of Products Sold in E-commerce Stores in 2021')
 
# Automatically resize the image by tight_layout().
plt.tight_layout()
 
# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_19.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_19.png')
 
# Clear the current image state at the end of the code.
plt.clf()