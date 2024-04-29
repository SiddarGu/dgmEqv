
import matplotlib.pyplot as plt
import numpy as np

# Transform given data into three variables
data_labels = ['Single Family Homes', 'Condominiums', 'Townhomes', 'Multi-Family Homes', 'Vacant Land', 'Mobile Homes']
data = [800, 600, 400, 200, 150, 100]
line_labels = ['Property Type', 'Number of Transactions']

# Plot data with a rose chart
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='polar', polar=True)
ax.set_title('Real Estate Market Activity in 2023')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors corresponding to different categories
for i, data_value in enumerate(data):
    ax.bar(i * sector_angle, data_value, width=sector_angle, bottom=0.0, color=plt.cm.Set1(i/num_categories), label=data_labels[i])

# Set ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, horizontalalignment='center')

# Legend
ax.legend(bbox_to_anchor=(1.05, 1.2), loc='upper left', fontsize=10)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_55.png')

# Clear the current image state
plt.clf()