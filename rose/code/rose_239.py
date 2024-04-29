
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Road', 'Rail', 'Air', 'Water', 'Pipeline', 'Space']
data = np.array([1000, 800, 400, 200, 100, 50])
line_labels = ['Mode of Transport', 'Number of Trips']

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Set up the axes in polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Set the number of ticks
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
ticks = np.arange(0, 2*np.pi, sector_angle)
ax.set_xticks(ticks)
ax.set_xticklabels(data_labels, fontsize=10, rotation=90)

# Plot the data
colors = ['#f5b7b1', '#d2b4de', '#a9cce3', '#a2d9ce', '#d7bde2', '#f7dc6f']
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, 
           align='center', color=colors[i], label=data_labels[i])

# Add legend
ax.legend(bbox_to_anchor=(1.1, 1.1))

# Set title
plt.title('Number of Trips Taken by Different Modes of Transport in 2021', fontsize=14)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_79.png')

# Clear the current image state
plt.clf()