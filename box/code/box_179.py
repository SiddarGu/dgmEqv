import matplotlib.pyplot as plt

# Data
crop_types = ['Rice', 'Wheat', 'Corn', 'Soybean', 'Cotton']
data = [[2, 3.5, 5, 6.5, 8], [1.5, 3, 4.5, 6, 7.5], [3, 5, 7, 9, 11], [1.2, 2.5, 3.8, 5.1, 6.4], [0.8, 1.6, 2.4, 3.2, 4]]
outliers = [[0.5,10], [12], [2.5,15], [8], []]

# Create figure 
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot box plot
bp = ax.boxplot(data, whis=1.5)

# Iterate through outliers and plot them
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Configurations
ax.yaxis.grid(True)
ax.set_xticks([y + 1 for y in range(len(data))])
ax.set_xlabel('Crop Type')
ax.set_ylabel('Yield (Tons/Hectare)')
plt.xticks([y + 1 for y in range(len(data))], crop_types, ha='right', rotation=45)
plt.title('Crop Yield Distribution in Agricultural Food Production (2021)')

# Save the fig
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/143_202312270030.png')

# Clear the figure 
plt.clf()
