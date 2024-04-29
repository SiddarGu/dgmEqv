
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables: data_labels, data, line_labels.
data_labels = ['Solar','Wind','Hydro','Natural Gas','Petroleum','Nuclear']
data = [120,95,85,70,50,20]
line_labels = ['Type of Energy','Number of Consumers']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Create the sectors
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# Set the angles and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)

# Add a legend
ax.legend(bbox_to_anchor=(1, 0.9))
ax.set_title("Energy Consumption by Type in 2023")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_12.png")

# Clear the current image state
plt.clf()