

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Renewable Energy", "Waste Management", "Sustainable Agriculture", "Water Conservation", "Air Pollution", "Biodiversity", "Climate Change", "Sustainable Development", "Green Building"]
data = [100, 90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ["Area", "Number of Projects"]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='polar')

# Plot data
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create a color palette
colors = plt.cm.Set1(np.arange(num_categories)/num_categories)

# Draw sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

# Set up ax
ax.set_theta_direction(-1)
angles = [sector_angle * i for i in range(num_categories)]
ax.set_theta_zero_location("N")
ax.set_xticks(angles)
ax.set_xticklabels(data_labels, fontsize=12, ha="center")

# Set title
ax.set_title("Number of Environment and Sustainability Projects in 2021", fontsize=18, y=1.08)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_8.png")

# Clear the current image state
plt.clf()