
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Economics', 'History', 'Sociology', 'Anthropology', 'Geography', 'Political Science', 'Psychology', 'Philosophy']
data = [45, 75, 30, 25, 50, 40, 20, 15]
line_labels = ['Field','Number']

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Number of categories
num_categories = len(data_labels)

# Calculate sector angle
sector_angle = (2 * np.pi) / num_categories

# Create sectors
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# Label the sectors
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(bbox_to_anchor=(1.2,1.1))

# Add title
ax.set_title('Popularity of Social Science and Humanities Fields in 2021')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_74.png')

# Clear current image state
plt.clf()