
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Grocery", "Apparel", "Electronics", "Toys and Games", "Home Decor", "Furniture", "Jewelry", "Beauty Products", "Pet Supplies"]
data = [90, 70, 80, 60, 40, 30, 20, 10, 5]
line_labels = ["Category", "Number"]

# Create a figure
fig = plt.figure(figsize=(8, 8))

# Set up the axes in polar coordinates
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set2(i / num_categories))

# Set the labels and ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, rotation='vertical')

# Add the legend
ax.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")

# Add the title
ax.set_title("Distribution of E-commerce Sales by Category in 2021", fontsize=14)

# Resize the image
plt.tight_layout()

# Save the image
fig.savefig(
    "/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_43.png"
)

# Clear the current image state
plt.clf()