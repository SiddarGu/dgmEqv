
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Social Policy', 'Economic Policy', 'International Relations', 'Education Policy', 'Environmental Policy', 'Defense Policy', 'Health Policy', 'Law Policy']
data = [75, 120, 90, 105, 75, 95, 110, 130]
line_labels = ['Category']

# Create figure before plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle 
sector_angle = (2 * np.pi) / len(data)

# Plot data with the type of rose chart
for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Set ticks
ax.set_xticks(np.linspace(0, 2*np.pi, len(data), endpoint=False))

# Set ticks labels
ax.set_xticklabels(data_labels, fontsize=14)

# Set legend
ax.legend(bbox_to_anchor=(1.1, 1.1), fontsize=14)

# Set title
ax.set_title("Overview of Government and Public Policy in 2021", fontsize=20)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_80.png')

# Clear state
plt.cla()