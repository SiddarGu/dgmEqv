

import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ['Clothing Retail', 'Electronics Retail', 'Grocery Retail', 'Food and Beverage E-commerce', 'Luxury Goods E-commerce', 
               'Home and Garden E-commerce', 'Online Marketplace', 'Other']
data = [100, 150, 200, 50, 60, 75, 80, 50]
line_labels = ['Category', 'Number']

# Plot the data with rose chart
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Assign a different color to each sector and add a legend
for i in range(num_categories):
  ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.Set1(i))
  ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
  ax.set_xticklabels(data_labels, fontsize=10, rotation=90)

# Make sure the legend is clearly visible and does not overlap with the chart
ax.legend(data_labels, fontsize=10, bbox_to_anchor=(1.2, 0.9))
ax.set_title('Distribution of Retail and E-commerce Businesses in 2021', fontsize=15)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_6.png')
plt.clf()