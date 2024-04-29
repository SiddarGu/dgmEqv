
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Single Family Homes','Apartments','Condos','Townhomes','Mobile Homes','Vacation Homes','Multi-Family Homes']
data = [20, 18, 15, 12, 10, 8, 5]
line_labels = ['Property Type']

# Create figure before plotting
fig = plt.figure(figsize=(12, 8))

# Plot the data with the type of rose chart
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Set up the axes in polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_ylim(0, 25)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i + np.pi / 2, data[i], width=sector_angle, color=f'C{i}', align='center', edgecolor='red', linewidth=1, label=data_labels[i])

# Set the number of ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# Set tick labels
ax.set_xticklabels(data_labels)

# Reposition the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., labelspacing=2, fontsize=12)

# Set the title of the figure
ax.set_title('Property Breakdown of US Housing Market in 2021', fontsize=14)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_114.png')
plt.clf()