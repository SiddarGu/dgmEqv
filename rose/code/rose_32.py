

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Math', 'Science', 'Social Sciences', 'Humanities', 'Languages', 'Arts', 'Physical Education', 'Computer Science']
data = [350, 450, 600, 400, 250, 150, 100, 50]
line_labels = ['Subject', 'Number of Students']

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
sector_angle = (2 * np.pi) / len(data_labels)

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, 
# and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
for i in range(len(data_labels)):
    ax.bar(sector_angle * i + np.pi/2, data[i], width=sector_angle, color=plt.cm.jet(i/len(data_labels)), edgecolor='k', label=data_labels[i])

# Assign a different color to each sector and add a legend next to the chart that clearly labels the category each sector represents, ensuring that the legend does not obscure any part of the chart.
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels) + 1)[:-1])

# Make sure each category label is correctly positioned at the center of its corresponding sector. 
ax.set_xticklabels(data_labels, fontsize=11, rotation=-90, ha='center')

# Add a title to the figure.
ax.set_title("Enrolment in Academic Programs at a University in 2021", fontsize=14)

# Save the image in the given path.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_116.png')

# Clear the current image state at the end of the code.
plt.clf()