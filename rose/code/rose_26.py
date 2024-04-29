
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Cloud Computing', 'Artificial Intelligence', 'Cyber Security', 'Big Data', 'Robotics', 'Internet of Things', 'Virtual Reality', 'Blockchain']
data = [80, 100, 50, 60, 70, 40, 30, 20]
line_labels = ['Category', 'Number']

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, 
           label=data_labels[i], color=plt.cm.Dark2(i/num_categories))

# Set ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, horizontalalignment='center')

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=4)

# Set title
ax.set_title('Popularity of Technological Developments in the Digital Age')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_108.png')

# Clear current image state
plt.clf()