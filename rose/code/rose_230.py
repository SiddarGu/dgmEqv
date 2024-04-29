
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ["Cloud Computing", "Artificial Intelligence", "Cyber Security", "Machine Learning", "Networking", "Big Data", "Programming", "Web Development"]
data = [43, 97, 17, 36, 96, 60, 68, 32]
line_labels = ["Number"]

# Plot the data with the type of rose chart. Create figure before plotting, i.e., add_subplot() follows plt.figure(). Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
sector_angle = (2 * np.pi) / len(data_labels)

# Use a loop to assign a label to each sector when you create them with `ax.bar`. Then, when you call `ax.legend()`, it will display labels for all categories.
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.arange(len(data_labels)) * sector_angle)

# Reposition the legend so that it does not cover any part of the chart. You can achieve this by adjusting the `bbox_to_anchor` parameter in the `ax.legend()` method.
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8))

# Make sure that each category label is correctly positioned at the center of its corresponding sector. This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method.
ax.set_xticklabels(data_labels, ha='center', va='top', rotation='vertical')

# Drawing techniques such as background grids can be used.
ax.grid(True)

# Set the title of the figure
plt.title("Usage of Technology and Internet Services in 2021")

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the image as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_64.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_64.png")

# Clear the current image state at the end of the code.
plt.clf()