
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
# data_labels represents the labels of each column except the first column. 
# line_labels represents the labels of each row except the first row. 
# Data represent the numerical array in the data.
data_labels = ['0-18', '19-35', '36-50', '51-65', '65+']
line_labels = ['Number of Patients']
data = np.array([400, 900, 650, 750, 500])

#Create figure before plotting, i.e., add_subplot() follows plt.figure()
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
# This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
ax.set_theta_direction(-1)  # clockwise
ax.set_theta_zero_location('N')

# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value, 
# and the angles of these sectors must add up to 360 degrees, 
# i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate 
# the sector angle and draw sectors corresponding to different categories by making 
# the width parameter in "ax.bar" sector_angle.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# assign a different color to each sector
colors = ['red', 'orange', 'green', 'blue', 'purple']

# draw the sectors
for i in range(num_categories):
    angle = i * sector_angle
    ax.bar(angle, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

# Set the theta ticks and labels
ax.set_xticks(np.linspace(0, 2.0 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True)

# Set the title
ax.set_title('Number of Patients by Age Group in Healthcare and Health', y=1.1)

# Position the legend outside the main chart area
ax.legend(data_labels, bbox_to_anchor=(1.35, 0.7))

# Prevent content from being displayed
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_93.png')

# Clear the current image state
plt.clf()