
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Waste Management', 'Renewable Resources', 'Global Warming', 'Pollution Control', 'Biodiversity', 'Sustainable Development', 'Climate Change', 'Energy Conservation']
data = [80, 60, 50, 41, 30, 25, 20, 15]
line_labels = ['Topic', 'Number']

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Set chart title
ax.set_title('Number of Countries Adopting Sustainable Practices in 2021', fontsize=15)

# Plot the data
for i, category in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=category, color=plt.cm.Set1(i/num_categories))

# Set ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, ha="center")

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.25, 0.75), fontsize=10)

# Adjust the figure size to prevent content from being displayed
plt.gcf().set_size_inches(8, 8)
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_135.png')

# Clear the current image state
plt.clf()