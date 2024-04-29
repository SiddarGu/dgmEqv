
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Literature','History','Philosophy','Psychology','Anthropology','Sociology','Political Science','Economics','Geography'] 
data = [100,200,150,250,100,200,150,300,100]
line_labels = ['Subject','Number of Students']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart

# Different sectors represent different categories with the same angle,
# whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Assign a different color to each sector
# Use a loop to assign a label to each sector when you create them with `ax.bar`
# Then, when you call `ax.legend()`, it will display labels for all categories
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'magenta', 'cyan', 'purple', 'pink']
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

# Ensure that the number of ticks set with `ax.set_xticks()`
# matches exactly the number of categories or labels you have in `data_labels`
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels)

# Make sure the legend is positioned in such a way that it doesn't overlap with the chart
ax.legend(bbox_to_anchor=(1.2, 1.05))

# Make sure that each category label is correctly positioned at the center of its corresponding sector
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be Number of Students Majoring in Social Sciences and Humanities in 2021.
plt.title('Number of Students Majoring in Social Sciences and Humanities in 2021')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_46.png
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_46.png')

# Clear the current image state at the end of the code
plt.clf()