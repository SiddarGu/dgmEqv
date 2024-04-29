
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Taxation', 'Social Welfare', 'National Security', 'Transportation', 'Civil Services', 'Environmental Protection', 'Education', 'Trade']
data = [120, 100, 80, 60, 50, 40, 20, 10]
line_labels = ['Category', 'Number of Regulations']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create each sector and assign a different color
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.jet(i / num_categories))

# Set the ticks to the center of each sector
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Position the legend at the top of the chart
ax.legend(data_labels, bbox_to_anchor=(0.5, 0.95))

# Set the title of the figure
plt.title('Number of Government Regulations by Domain in 2021')

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_143.png')

# Clear the current image state
plt.clf()