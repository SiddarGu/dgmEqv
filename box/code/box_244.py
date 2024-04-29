import matplotlib.pyplot as plt
import numpy as np
# Define data
categories = ['Apartment', 'Detached House', 'Semi-Detached House', 'Townhouse', 'Condo']
box_plot_data = [[180000, 220000, 310000, 400000, 570000],
                 [250000, 320000, 420000, 500000, 650000],
                 [190000, 270000, 360000, 420000, 530000],
                 [200000, 280000, 350000, 450000, 540000],
                 [150000, 200000, 300000, 380000, 450000]]
outliers_data = [[25000, 700000], [], [10000, 600000], [180000], [80000, 500000]]

# Create figure 
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Box plot
bp = ax.boxplot(box_plot_data, whis=1.5)

# Customization
plt.setp(bp['medians'], color='red') 
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='blue')
ax.set_xticklabels(categories)

# Plot outliers
for i, outliers in enumerate(outliers_data):
    if outliers:  # if there are outliers for this category
        x = [i + 1] * len(outliers)  # x-coordinates
        ax.plot(x, outliers, 'ro')

# Title, labels & grid
ax.set_title('Property Price Distribution in Housing Market (2022)')
ax.set_ylabel('Price ($)')
plt.grid(axis='y')
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# Set the layout of the figure 
fig.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/185_202312310058.png')

# Clear figure
plt.clf()
