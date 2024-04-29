
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education', 'Environment', 'Human Rights', 'Health', 'Poverty', 'Animal Rights', 'Art and Culture', 'Economic Development']
data = [45, 40, 30, 25, 20, 15, 10, 5]
line_labels = ['Category', 'Number']

# Set up figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# Set up colors
colors = plt.cm.rainbow(np.linspace(0, 1, len(data_labels)))

# Plot data
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], bottom=0.0, width=sector_angle, color=colors[i], label=data_labels[i])

# Set axes
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=12)

# Set title
ax.set_title('Number of Nonprofit Organizations in Different Fields', fontsize=14)

# Set legend
ax.legend(bbox_to_anchor=(1.05, 1.05))

# Save and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_54.png')
plt.clf()