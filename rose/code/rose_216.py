
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ['Fast Food', 'Beverages', 'Grocery', 'Snacks', 'Coffee', 'Dairy', 'Frozen Foods', 'Organic Foods', 'Baked Goods', 'Specialty Foods']
line_labels = ['Type', 'Number of Companies']
data = np.array([[200, 100, 90, 80, 70, 60, 50, 40, 30, 20]])

# Plot the data with the type of rose chart. Create figure before plotting, i.e., add_subplot() follows plt.figure(). Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar') 

# All sectors should cover the entire circumference evenly, and each sector should have the same angle.
sector_angle = (2 * np.pi) / len(data_labels)

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[0, i], width=sector_angle, color=plt.cm.tab20(i), label=data_labels[i])

# Assign a different color to each sector, and add a legend next to the chart that clearly labels the category each sector represents, ensuring that the legend does not obscure any part of the chart. Reposition the legend so that it does not cover any part of the chart.
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 0.9))

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))

# Make sure that each category label is correctly positioned at the center of its corresponding sector.
# This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method.
ax.set_xticklabels(data_labels, fontdict={'fontsize':16}, rotation=30, ha='center')

# Drawing techniques such as background grids can be used.
ax.grid(linestyle='--')

# The title of the figure should be  Number of Companies in the Food and Beverage Industry in 2021.
ax.set_title("Number of Companies in the Food and Beverage Industry in 2021", fontdict={'fontsize':20})

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_26.png')

# Clear the current image state at the end of the code
plt.clf()