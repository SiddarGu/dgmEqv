import matplotlib.pyplot as plt

# Define the data
websites = ['Website A', 'Website B', 'Website C', 'Website D', 'Website E']
data = [[2, 10, 13, 18, 20], [3, 10, 13, 16, 20], [1, 8, 12, 16, 20], [5, 10, 13, 18, 24], [2, 9, 12, 15, 18]]
outliers = [[30], [1], [], [28, 30], [27, 30]]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Create box plot
bp = ax.boxplot(data, vert=True, patch_artist=True, widths=0.5, whis=1.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Adjust chart style
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Add labels and title
ax.set_xticklabels(websites, rotation=90)
ax.set_title('User Visit Duration Distribution Across Different Websites (2024)')
ax.set_ylabel('Visit Duration (Minutes)')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/53_202312270030.png')

# Clear the current figure
plt.clf()
