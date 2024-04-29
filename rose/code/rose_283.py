
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ["Retail", "Manufacturing", "Banking", "Investment", 
               "Real Estate", "Insurance", "Technology", "Logistics", "Consultancy"]
data = [50, 100, 80, 120, 90, 150, 200, 60, 30]
line_labels = ["Business Category", "Profit"]

# Create plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], 
           color=f"C{i}")

# Set labels
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=14, rotation=30)
ax.set_title("Profits of Different Business Categories in 2021", fontsize=20)

# Set legend
plt.legend(bbox_to_anchor=(1.25, 1), loc="upper right")
plt.tight_layout()

# Save plot
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_82.png")

# Clear plot
plt.clf()