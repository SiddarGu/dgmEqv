
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Machinery', 'Automation', 'Quality Control', 'Supply Chain', 'Logistics', 'Maintenance', 'Production', 'Research and Development']
data = np.array([53, 40, 25, 37, 48, 22, 60, 15])
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(projection='polar', polar=True)
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=plt.cm.hsv(i/num_categories), label=data_labels[i], alpha=1)
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, fontweight='bold')

# Set the title of the figure
ax.set_title('Number of Companies Involved in Manufacturing and Production in 2021', fontsize=20, fontweight='bold')

# Create a legend
ax.legend(data_labels, bbox_to_anchor=(1.3, 0.5), fontsize=10, frameon=True)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_32.png')

# Clear the current image state
plt.clf()