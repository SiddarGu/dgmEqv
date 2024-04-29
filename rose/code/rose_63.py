
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Beach Tourism", "Ski Tourism", "Cultural Tourism", "Eco Tourism", "Adventure Tourism", "Religious Tourism", "Cruise Tourism", "Medical Tourism"]
data = [500, 400, 300, 250, 200, 150, 100, 50]
line_labels = ["Number of Visitors"]

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], sector_angle, label=data_labels[i], color=f"C{i}")

# Add a legend to the chart that clearly labels the category each sector represents
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.1))

# Set the chart's title 
ax.set_title("Number of Tourists by Type of Tourism in 2021")

# Set the number of ticks to match the number of categories or labels
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))

# Set the category labels for each tick
ax.set_xticklabels(data_labels, rotation=45, ha="right", wrap=True)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_25.png")

# Clear the current image state
plt.clf()