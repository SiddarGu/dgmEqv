

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Department Stores', 'Grocery Stores', 'E-Commerce', 'Clothing Stores', 'Electronics Stores', 'Specialty Stores', 'Home Improvement Stores', 'Beauty & Health Stores', 'Pet Stores', 'Restaurant Supply Stores']
data = [200, 150, 300, 250, 120, 100, 90, 80, 60, 40]
line_labels = ['Category', 'Number']

# Plot the data with type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('Number of Retail and E-Commerce Stores in 2021', fontsize=20)
sector_angle = (2 * np.pi) / len(data_labels)

# Draw sectors corresponding to different categories
for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=plt.cm.Set3(i))

# Set the category labels
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True, rotation=15)

# Set the legend
ax.legend(bbox_to_anchor=(1.3, 1))

# Show and save the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_129.png')
plt.clf()