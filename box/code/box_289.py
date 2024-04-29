import numpy as np
import matplotlib.pyplot as plt

# Define data
data = [
    ["Fast Food", [40, 70, 100, 130, 180], []],
    ["Alcoholic Beverages", [50, 100, 150, 200, 250], [1, 300]],
    ["Ready-made Meals", [30, 60, 90, 120, 160], [20, 10]],
    ["Hot Drinks", [20, 50, 75, 100, 150], [200]],
    ["Ice Cream", [10, 30, 55, 80, 120], [5, 150]]
]

# Extract values from data
categories = [i[0] for i in data]
values = [i[1] for i in data]
outliers = [i[2] for i in data]

# Create box plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

bplot = ax.boxplot(values, vert=False, patch_artist=True, notch=True, whis=1.5, labels=categories)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'lavender']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'X')

# Add title and axis labels
plt.title('Sales Distribution for Different Product Types in Food and Beverage Industry (2021)')
plt.xlabel('Sales (Thousands)')
plt.grid(True, linestyle='--', which='major', color='grey', alpha=.7)

# Rotate x-labels if they are too long
plt.xticks(rotation=45)

# Save the figure to a file
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/108_202312270030.png')

# Clear plot
plt.clf()
