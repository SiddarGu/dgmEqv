
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Data represent the numerical array in the data.
data_labels = ['Recruitment', 'Training', 'Retention', 'Performance Management', 'Benefits and Compensation', 'Employee Relations', 'Discipline']
line_labels = ['Category', 'Number of Employees']
data = [120, 90, 80, 60, 50, 30, 20]

# Plot the data with the type of rose chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees, 
# i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories 
# by making the width parameter in "ax.bar" sector_angle.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Assign a different color to each sector, and add a legend next to the chart 
# that clearly labels the category each sector represents, ensuring that the legend does not obscure any part of the chart.
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# You should use a loop to assign a label to each sector when you create them with `ax.bar`. 
# Then, when you call `ax.legend()`, it will display labels for all categories. 
# Make sure the legend is positioned in such a way that it doesn't overlap with the chart
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`. 
# Make sure that each category label is correctly positioned at the center of its corresponding sector. 
# This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method.
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, rotation=45, wrap=True)

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be  Employee Counts by Department in 2021.
plt.title("Employee Counts by Department in 2021")

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_99.png
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_99.png', bbox_inches='tight')

# Clear the current image state at the end of the code
plt.clf()