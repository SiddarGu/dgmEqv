import matplotlib.pyplot as plt

# Data 
categories = ['Electronic Gadgets', 'Furniture', 'Vehicles', 'Textiles', 'Food Products']
data = [[3, 8, 15, 20, 25],
        [6, 18, 25, 33, 40],
        [10, 22, 30, 38, 45],
        [2, 6, 11, 16, 21],
        [1, 4, 7, 10, 13]]
outliers = [[],
            [1, 5, 50],
            [8, 55],
            [30, 35],
            [20, 25]]

# Create the figure and subplot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Plot the box plot
ax.boxplot(data, whis=1.5)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x')

# Set the title and labels
ax.set_title('Production Time Distribution in Different Manufacturing Sectors (2025)')
ax.set_ylabel('Production Time (Days)')
plt.xticks(range(1, len(categories) + 1), categories, rotation=90)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/175_202312310058.png')

# Clear the current figure
plt.clf()
