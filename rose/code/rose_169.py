
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Dairy Products", "Fruits", "Vegetables", "Grains", "Poultry", "Beef", "Pork", "Fish", "Processed Foods"]
data = [200, 150, 250, 200, 100, 150, 120, 50, 75]
line_labels = ["Category", "Number"]

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True) 

# Calculate the sector angle 
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
for i, data_label in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, edgecolor='black', label=data_label, color=np.random.rand(3,))

# Set the labels for each sector
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.25, 1.02))

# Set the title 
ax.set_title("Distribution of Agricultural and Food Production in 2021")

# Automatically resize the image
plt.tight_layout()

# Save the plot
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_73.png')

# Clear the current image
plt.clf()