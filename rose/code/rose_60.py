
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Permanent', 'Part-time', 'Contract', 'Casual', 'Freelance', 'Internship']
data = [100, 90, 80, 70, 60, 50]
line_labels = ['Employment Status', 'Number of Employees']

# Create figure and plot a rose chart
fig = plt.figure(figsize=(10, 10)) 
ax = fig.add_subplot(111, polar=True)

# Calculate the number of categories
num_categories = len(data_labels)

# Calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i in range(num_categories):
    ax.bar(sector_angle * i, 
           data[i], 
           width=sector_angle, 
           edgecolor='k', 
           color=plt.cm.cool(i/num_categories), 
           label=data_labels[i])

# Set ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Title
plt.title("Number of Employees by Employment Status in 2021")

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_21.png', dpi=300)

# Clear current figure
plt.clf()