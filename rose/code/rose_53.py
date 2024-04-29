
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Single-Family Homes', 'Condominiums', 'Townhouses', 'Multi-Family Homes', 'Co-ops']
data = np.array([130, 90, 60, 40, 25])
line_labels = np.array(['Type', 'Number'])

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, label=data_labels[i], color=f'C{i}')

# Set the legend of the chart and position it in a way that does not overlap with the chart
ax.legend(bbox_to_anchor=(1.2, 1.1))

# Set the number of ticks to match the number of categories
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))

# Set each category label to the center position of its corresponding sector
ax.set_xticklabels(data_labels, wrap=True)

# Set the title of the figure
ax.set_title('Number of Real Estate Properties in the Housing Market')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_145.png')

# Clear the current image state
plt.clf()