
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Solar', 'Wind', 'Nuclear', 'Hydroelectric', 'Geothermal', 'Biomass', 'Natural Gas']
data = [100, 90, 50, 75, 25, 20, 30]
line_labels = ['Source', 'Amount']

# Create figure
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, polar=True)

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# Set ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, rotation=15, wrap=True)

# Set legend
ax.legend(bbox_to_anchor=(1, 0.5))

# Set title
ax.set_title('Energy and Utility Sources and Their Associated Amounts', fontsize=20)

# Resize image
plt.tight_layout()

# Save figure
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_55.png')

# Clear image state
plt.clf()