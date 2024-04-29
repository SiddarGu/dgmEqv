
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data
data_labels = ["Automotive", "Mining", "Logistics", "Construction", "Manufacturing", "Textiles", "Electronics", "Packaging", "Metals", "Chemicals"]
line_labels = ["Category", "Number of Workers"]
data = np.array([[180, 170, 150, 130, 100, 90, 80, 70, 60, 50]])

# Plot the data with the type of rose chart
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection="polar")
num_categories = np.shape(data)[1]
sector_angle = (2 * np.pi) / num_categories

# Create sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i], color="C"+str(i))

# Set the legend of categories
ax.legend(data_labels, bbox_to_anchor=(1.15, 0.7))

# Set the ticks of categories
ax.set_xticks(np.linspace(sector_angle/2, 2*np.pi, num=num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=11, rotation='vertical')

# Set the title
ax.set_title("Number of Employees in Different Manufacturing and Production Sectors in 2020", fontsize=18)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_23.png', dpi=300)

# Clear the current image state at the end of the code
plt.clf()