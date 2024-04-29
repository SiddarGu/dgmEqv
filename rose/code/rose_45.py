
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Wheat", "Rice", "Maize", "Barley", "Sorghum", "Millet", "Oats", "Rye"]
data = [80000, 100000, 70000, 50000, 40000, 30000, 20000, 10000]
line_labels = np.arange(len(data))

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Assign a different color to each sector
ax.set_facecolor('#F1F1F1')
ax.legend(data_labels, bbox_to_anchor=(1.15, 1.0))

# Make sure the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(sector_angle * line_labels)
ax.set_xticklabels(data_labels, fontsize=8, ha='center')

# Set figure title
ax.set_title('Tonnes of Crops Produced in 2021', fontsize=20)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image to the specified path
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_135.png')

# Clear the current image state at the end of the code
plt.clf()