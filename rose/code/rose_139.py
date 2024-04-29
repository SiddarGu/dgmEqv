
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Sports','Music','Film','Television','Gaming','Theatre','Art']
data = [250, 350, 400, 220, 120, 150, 80]
line_labels = ['Category', 'Number of People']

# Plot the data with the type of rose chart.
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Assign different color to each sector and add legend
colors = ['#0099FF', '#FF9900', '#99FF00', '#FF0099', '#00FFFF', '#FF0000', '#FFFF00']
# Calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Set up the axes in polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10,  wrap=True, ha='center')

# Modify the figure
plt.title('Popularity of Entertainment and Sports Among People in 2021', fontsize=14)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_149.png')

# Clear the current image state
plt.clf()