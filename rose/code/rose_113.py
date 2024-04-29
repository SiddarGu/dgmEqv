
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = [ 'Social Networking', 'E-commerce', 'Video Streaming', 'Web Design', 'Cyber Security', 'Search Engines', 'Cloud Computing', 'Mobile Apps', 'Web Analytics']
data = [400, 350, 300, 250, 200, 150, 100, 80, 60]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart. Create figure before plotting, i.e., add_subplot() follows plt.figure(). Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
fig, ax = plt.subplots(figsize=(12,9), subplot_kw=dict(polar=True))

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Assign a different color to each sector, and add a legend next to the chart that clearly labels the category each sector represents, ensuring that the legend does not obscure any part of the chart.
for i, label in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=label, color=plt.cm.Set1(i))

# Make sure the legend is positioned in such a way that it doesn't overlap with the chart.
ax.legend(bbox_to_anchor=(1.1, 1.05))

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# Ensure that each category label is correctly positioned at the center of its corresponding sector. This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method. Ensure that each angle parameter corresponds to the center position of each sector, and then use `ax.set_xticklabels` to set these category labels.
ax.set_xticklabels(data_labels, rotation=90)

# The title of the figure should be  Number of Websites Engaged in Each Field in 2021.
ax.set_title("Number of Websites Engaged in Each Field in 2021")

# Automatically resize the image by tight_layout(). 
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_104.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_104.png')

# Clear the current image state at the end of the code.
plt.clf()