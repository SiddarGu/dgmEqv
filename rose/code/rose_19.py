
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Soccer', 'Basketball', 'Baseball', 'American Football', 'Hockey', 'Tennis', 'Golf']
data = np.array([1000, 800, 500, 300, 200, 100, 50])
line_labels = ['Category', 'Number of Fans']

# Plot the data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Draw sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Add legend
ax.legend(bbox_to_anchor=(1.2, 0.5), labels=data_labels)

# Set ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels, fontsize=14)

# Set title
plt.title('Number of Fans for Various Sports in the USA')

# Set layout
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_4.png')

# Clear the current image state
plt.clf()