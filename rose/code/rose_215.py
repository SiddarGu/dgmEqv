
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Social Networking Platforms", "Online Shopping", "Video Sharing", "News and Entertainment", "Discussion Forums", "Blogging", "Web Search Engines", "Image Sharing", "Online Advertising"]
data = [90, 80, 70, 60, 50, 40, 30, 20, 10]
line_labels = ["Topic", "Number"]

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.

# Different sectors represent different categories with the same angle,
# whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees,
# i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i])

# Assign a different color to each sector.
ax.set_thetamin(0)
ax.set_thetamax(360)
ax.set_rlabel_position(90)

# Set the number of ticks with `ax.set_xticks()` to match the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Adjust the angle parameters in the `ax.set_xticks` method to position each category label correctly at the center of its corresponding sector.
ax.set_xticklabels(data_labels, fontsize=10, rotation=30, ha='right', va='top')

# Reposition the legend so that it does not cover any part of the chart.
# Adjust the `bbox_to_anchor` parameter in the `ax.legend()` method,
# try different values for `bbox_to_anchor` to find a position for the legend that is outside of the main chart area.
ax.legend(data_labels, bbox_to_anchor=(1.15, 1.0))

# Set the title of the figure.
plt.title("Popularity of Different Types of Web Content in 2023")

# Tight the layout and save the image.
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_24.png")

# Clear the current image state.
plt.clf()