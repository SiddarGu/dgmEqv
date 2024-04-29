import matplotlib.pyplot as plt

# Data
crop_types = ['Corn', 'Apple', 'Soybeans', 'Wheat', 'Rice']
yield_data = [[2, 5, 7, 10, 14], [1, 3.5, 6, 8.5, 12], [1.5, 4, 6.5, 9, 12.5], [3, 6, 9, 12, 15], [1.2, 3.8, 6.2, 8.6, 11]]
outliers = [[], [20], [0.7, 15.5], [], [17.5]]

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Boxplot
ax.boxplot(yield_data, labels=crop_types, whis=1.5, patch_artist=True, notch=True, 
           flierprops=dict(marker='o', markerfacecolor='red', markersize=12, linestyle='none', alpha=0.5))

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x')

# Set titles and labels
ax.set_title('Yield Distribution for Different Crops (2022)')
ax.set_ylabel('Yield (Tons)')
ax.yaxis.grid(True)
ax.xaxis.grid(True)
ax.margins(0.05)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/246_202312310058.png')

# Clear figure
plt.clf()
