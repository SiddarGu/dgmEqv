
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Electrical Engineering','Mechanical Engineering','Civil Engineering','Computer Science','Chemical Engineering','Aerospace Engineering','Biomedical Engineering','Nanotechnology']
data = np.array([87,97,75,65,41,22,14,8])
line_labels = ['Category', 'Number']

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color='C'+str(i))

# Set ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, wrap=True, rotation=90)

# Set legend
ax.legend(bbox_to_anchor=(1.15, 1.05))

# Set title
plt.title('Number of Graduates in Science and Engineering Fields in 2021')

# Adjust display
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_45.png')

# Clear current figure
plt.clf()