import matplotlib.pyplot as plt

# Restructured data
data = [
    ['Social Media', [0.3, 1.5, 2.5, 3.5, 4], []],
    ['Streaming', [0.5, 1.7, 2.7, 3.7, 4.5], [5.2]],
    ['Online Shopping', [0.4, 1.2, 2, 2.8, 3.6], [4.8, 5.5, 6.0]],
    ['Research', [0.7, 1.8, 2.4, 3, 4], []],
    ['Gaming', [0.6, 2, 2.9, 3.8, 4.7], [5.5, 5.6, 7]]
]

# Extract boxplot data and outliers
labels, boxplot_data, outliers = zip(*data)

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Box plot
ax.boxplot(boxplot_data, whis=1.5, notch=True)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Tweak plot appearance
ax.grid(True)
ax.set_xticklabels(labels, rotation=30, ha='right')
ax.set_ylabel('Usage (Hours)')
plt.title('Daily Internet Usage Distribution for Different Activities (2022)')

plt.tight_layout()
# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/235_202312310058.png')

# Clear the current figure
plt.clf()
