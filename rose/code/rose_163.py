
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Automotive', 'Electronics', 'Textiles', 'Pharmaceuticals', 'Aerospace', 'Food Processing', 'Industrial Machinery']
data = [130, 90, 50, 70, 80, 55, 100]
line_labels = ['Category', 'Number of Manufacturing Units']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Plot data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color = plt.cm.Set1(i / num_categories))

# Set axis labels
ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Set title
plt.title('Manufacturing Units by Industry in 2021', fontsize=20)

# Resize image
fig.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_58.png')

# Clear
plt.clf()