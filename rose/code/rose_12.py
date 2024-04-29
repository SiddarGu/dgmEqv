
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Renewable Energy', 'Hydroelectric', 'Nuclear Energy', 'Oil and Gas', 'Coal', 'Solar', 'Wind']
data = [45, 50, 20, 60, 30, 90, 40]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# Create figure before plotting
category_num = len(data)
sector_angle = (2 * np.pi) / category_num

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value
for sector_index in range(category_num):
    start_angle = sector_angle * sector_index
    end_angle = start_angle + sector_angle
    ax.bar(start_angle, data[sector_index], width=sector_angle, label=data_labels[sector_index])

# Add a legend next to the chart
ax.legend(bbox_to_anchor=(1.25, 1.03), labels=data_labels)

# Set ax.set_xticks
ax.set_xticks(np.linspace(0, 2 * np.pi, category_num + 1)[:-1])
ax.set_xticklabels(data_labels, fontsize=14, wrap=True, rotation=90)

# Set title
ax.set_title("Number of Energy and Utility Providers in 2021", fontsize=20)

# Ensure the labels are correctly positioned at the center of its corresponding sector
ax.set_theta_direction(-1)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_2.png')

# Clear the current image state
plt.clf()