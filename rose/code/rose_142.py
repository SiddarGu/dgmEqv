
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Fast Food', 'Delicacies', 'Desserts', 'Street Food', 'Beverages', 'Ethnic Cuisine']
data = [120, 80, 30, 40, 20, 10]
line_labels = ['Type of Food', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, 
           color=plt.cm.Set1(i / num_categories), label=data_labels[i])

# Position the legend, make sure the legend is visible and not overlap with the chart
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.05))

# Set the ticks and labels for the categories
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=15)

# Set the title of the figure
plt.title('Food and Beverage Consumption in 2020', fontsize=20)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_2.png')

# Clear the current image state
plt.clf()