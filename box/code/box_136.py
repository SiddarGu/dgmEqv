import matplotlib.pyplot as plt

# Data
categories = ['McDonalds', 'Starbucks', 'KFC', 'Subway', 'Nestle']
statistics = [[3800, 4200, 5000, 5500, 6000],
              [2500, 3200, 3700, 4200, 5000],
              [1000, 2200, 3000, 3800, 4500],
              [750, 1600, 2100, 2700, 3200],
              [8000, 8500, 9000, 9500, 10000]]
outliers = [[],
            [2000, 7500],
            [820, 5200],
            [120, 4800],
            [7700, 11200]] 

# Create figure and box plot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(statistics, whis=1.5, patch_artist=True)

# Customizing boxplot colors
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'r.')

# Grid, title, and labels
ax.grid(True)
plt.title('Revenue Distribution in the Food and Beverage Company (2021)')
plt.xlabel('Category')
plt.ylabel('Revenue (Millions)')
ax.set_xticklabels(categories, rotation=45)

# Save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/247_202312310058.png')

# Clear the current image state
plt.clf()
