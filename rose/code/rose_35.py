

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Music', 'Theatre', 'Visual Arts', 'Film', 'Dance', 'Literature', 'Architecture', 'Photography', 'Sculpture']
data = [50, 45, 40, 35, 30, 25, 20, 15, 10]
line_labels = ['Category', 'Number']

# Create figure
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Set x-axis labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)

# Add title and legend
plt.title('Popularity of Arts and Culture Among People in 2021', fontsize=20)
ax.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=20)

# Resize and save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_123.png')

# Clear current image
plt.clf()