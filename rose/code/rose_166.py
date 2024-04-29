
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Electronics', 'Automotive', 'Textiles', 'Machinery', 'Food Processing', 'Furniture', 'Plastics', 'Printing']
data = [500, 400, 300, 200, 150, 100, 50, 10]
line_labels = ['Manufacturing Type', 'Number of Units']

# Plot the data with the type of rose chart. 
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories.
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Set the axes labels and legend.
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, rotation=-90)
ax.legend(bbox_to_anchor=(1.1, 1.1))

# Set title.
plt.title('Production Volume of Different Manufacturing Types in 2021')

# Resize and save image.
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_66.png')

# Clear current image state.
plt.clf()