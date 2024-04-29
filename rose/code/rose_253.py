
import matplotlib.pyplot as plt
import numpy as np

# Transform given data into three variables
data_labels = ["Fruits", "Vegetables", "Dairy", "Grains", "Meat", "Seafood", "Nuts", "Eggs"]
data = [7000, 6000, 5000, 4000, 3000, 2000, 1000, 500]
line_labels = ["Type of Food", "Production Volume"]

# Plot the data
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="polar")

# Draw rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=f"C{i}")

# Position the legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 0.8))

# Set ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=45, ha="right")

# Set title
ax.set_title("Global Food Production in 2021")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_2.png')

# Clear the current image state
plt.clf()