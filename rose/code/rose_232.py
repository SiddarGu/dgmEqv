
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ["Economic Policy", "Social Policy", "Education Policy", 
               "Infrastructure Policy", "Environmental Policy", 
               "Public Health Policy", "Technology Policy", "Foreign Policy"]
data = [80, 70, 60, 50, 40, 30, 20, 10]
line_labels = ["Number of Policies"]

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Compute the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(len(data)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Set the ticks to be the category labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True)

# Add the legend
ax.legend(bbox_to_anchor=(1, 0.5))

# Set plot title
plt.title("Number of Government Policies in 2021 by Category")

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_67.png")

# Clear the current image state
plt.clf()