
import matplotlib.pyplot as plt
import numpy as np

# Transform given data into three variables: data_labels, data, line_labels
data_labels = ["Raw Materials", "Machinery", "Parts", "Components", "Supplies", "Equipment", "Tools", "Finished Products"]
line_labels = ["Type", "Quantity"]
data = np.array([[70, 48, 32, 22, 15, 10, 8, 3]])

# Create figure and plot rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="polar", polar=True)
bars = ax.bar(np.arange(num_categories) * sector_angle, data[0], width=sector_angle,
            color=["#FF8C00","#32CD32","#0000CD","#A52A2A","#FF1493","#FFD700","#008000","#4B0082"])

# Set ticks to be data labels
ax.set_xticks(np.arange(num_categories) * sector_angle)
ax.set_xticklabels(data_labels, size=14, rotation=45, wrap=True)

# Set title
ax.set_title("Quantity of Manufacturing and Production Items in Inventory", size=14)

# Set legend
ax.legend(data_labels, bbox_to_anchor=(1.25, 1.05))

# Adjust the positioning of the legend
ax.legend(bbox_to_anchor=(1.25, 0.6))

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_62.png")

# Clear the current image state
plt.clf()