
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Beer', 'Wine', 'Spirits', 'Soft Drinks', 'Juice', 'Water', 'Tea']
data = [200, 150, 100, 80, 60, 40, 20]
line_labels = ['Beverage Type', 'Sales Volume']

#Create figure
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, polar=True)

# Plot the data with the type of rose chart.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for idx, (d, l) in enumerate(zip(data, data_labels)):
    ax.bar(sector_angle*idx, d, sector_angle, color=plt.cm.Set3(idx), label=l)

ax.set_title('Beverage Sales Volume in the Food and Beverage Industry in 2021')

# Set ticks and labels
ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=11, wrap=True, rotation=25)

# Position legend to the side of the chart
ax.legend(bbox_to_anchor=(1.1, 1.15)) 

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_7.png')

# Clear the current image state
plt.clf()