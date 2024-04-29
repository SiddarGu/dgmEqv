

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Clothing', 'Electronics', 'Home Appliances', 'Furniture', 'Grocery', 'Pet Supplies', 'Sporting Goods']
data = [90, 67, 50, 35, 25, 10, 5]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# Set category labels.
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)

# Position the legend where it does not overlap with the chart.
ax.legend(bbox_to_anchor=(1.15, 1.0))

# Set title.
ax.set_title('Number of Retailers for Different Product Categories in 2021')

# Automatically resize the image.
plt.tight_layout()

# Save the image.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_29.png')

# Clear the current image state.
plt.clf()