
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Automobiles", "Electronics", "Machinery", "Chemicals", "Plastics", "Industrial Components", "Textiles", "Metals"]
data = [1000, 1500, 800, 1200, 700, 200, 500, 600]
line_labels = ["Product Type", "Number of Units"]

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Position the legend outside the main chart area
ax.legend(bbox_to_anchor=(1.15, 1), loc="upper right")

# Set the x-ticks to the center of each sector
ax.set_xticks(sector_angle / 2 + sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=15, rotation=45, wrap=True)

# Add a title to the figure
ax.set_title("Number of Units Manufactured in 2021", fontsize=15)

# Resize the image to fit content
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_53.png")

# Clear the current image state
plt.clf()