
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Computer Science', 'Engineering', 'Physics', 'Chemistry', 'Bioengineering', 'Mathematics', 'Mechanical Engineering', 'Aerospace Engineering']
data = [83, 97, 17, 36, 96, 60, 68, 20]
line_labels = []

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot and label data
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=f'C{i}', label=data_labels[i])

# Set x-axis ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set x-axis tick labels
ax.set_xticklabels(data_labels, fontsize=8, wrap=True)

# Set legend outside of plot area
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Set title
ax.set_title('Number of Students Studying in Science and Engineering Fields in 2021')

# Set tight_layout to prevent content from being displayed
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_24.png')

# Clear current image state
plt.clf()