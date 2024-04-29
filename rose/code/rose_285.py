

import matplotlib.pyplot as plt
import numpy as np

# Transforming given data into three variables
data_labels = ['Fundraising', 'Volunteering', 'Community Outreach', 'Education', 'Poverty Alleviation', 'Disaster Relief', 'Humanitarian Aid', 'Environmental Protection', 'Animal Welfare']
line_labels = ['Category', 'Number']
data = [[100, 90, 80, 60, 50, 40, 30, 20, 10]]

# Plotting the data in a rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Creating multiple sectors with different colors
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999"]
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i], color=colors[i])

# Adding legend to the chart
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.05))

# Setting ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, rotation=90)

# Setting the title
ax.set_title('Number of Nonprofit Organizations Engaged in Various Activities in 2021', fontsize=20)

# Resizing the image
plt.tight_layout()

# Saving the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_86.png')

# Clearing the current image state
plt.clf()