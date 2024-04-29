
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Grains', 'Vegetables', 'Fruits', 'Dairy', 'Nuts', 'Livestock', 'Aquaculture']
data = np.array([100, 200, 150, 50, 120, 80, 40])
line_labels = ['Crop Type', 'Quantity']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar', polar=True)
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories
# color
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9']

# draw different sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

# Set the category labels for each sector 
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)

# Add legend
ax.legend(bbox_to_anchor=(1.1,1.1))

# Set title
ax.set_title('Quantity of Agricultural Products in 2020', fontsize=14)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_59.png')

# Clear the current figure
plt.clf()