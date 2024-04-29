

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Renewable Energy", "Carbon Emissions", "Pollution", "Natural Resources", 
               "Climate Change", "Waste Management", "Sustainable Agriculture", "Biodiversity"]
data = [90, 80, 60, 50, 40, 30, 20, 10]

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)

# Create multiple sectors in the graph, each representing a different category
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Assign a different color to each sector and add a legend
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
for i in range(num_categories):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

# Position the legend in such a way that it doesn't overlap with the chart
ax.legend(bbox_to_anchor=(1.25,1))

# Ensure the number of ticks set with `ax.set_xticks()` matches exactly the number of categories
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))

# Set category labels
ax.set_xticklabels(data_labels)

# Set the title
plt.title("Global Trends in Environment and Sustainability in 2021")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_42.png")

# Clear the current image state
plt.clf()