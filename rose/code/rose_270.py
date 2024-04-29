
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Air Pollution", "Water Pollution", "Climate Change", "Waste Management", "Biodiversity", "Renewable Energy", "Sustainable Agriculture", "Sustainable Consumption", "Sustainable Development"]
data = [100, 90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ["Category", "Number"]

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). Modify the
# axes to use polar coordinates with `polar=True` or 'projection='polar'.
sector_angle = (2 * np.pi) / len(data_labels)

# Different sectors represent different categories with the same angle, whose radius is 
# proportional to the corresponding value, and the angles of these sectors must add up
# to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate
# the sector angle and draw sectors corresponding to different categories by making
# the width parameter in "ax.bar" sector_angle.
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number
# of categories or labels you have in `data_labels`.
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels)

# You should use a loop to assign a label to each sector when you create them with `ax.bar`.
# Then, when you call `ax.legend()`, it will display labels for all categories. Make sure
# the legend is positioned in such a way that it doesn't overlap with the chart.
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Make sure that each category label is correctly positioned at the center of its 
# corresponding sector. This can be achieved by adjusting the angle parameters in the 
# `ax.set_xticks` method. Ensure that each angle parameter corresponds to the center 
# position of each sector, and then use `ax.set_xticklabels` to set these category labels.
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be Frequency of Environmental and Sustainability Issues in 2021.
plt.title("Frequency of Environmental and Sustainability Issues in 2021")

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_6.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_6.png")

# Clear the current image state at the end of the code.
plt.clf()