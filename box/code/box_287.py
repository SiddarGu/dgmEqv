import matplotlib.pyplot as plt

# Restructured data
categories = ['Painting', 'Sculpture', 'Photography', 'Digital Art', 'Performing Art']
numerical_data = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [5, 15, 25, 35, 45], [8, 18, 28, 38, 48], [12, 22, 32, 42, 52]]
outliers = [[], [5, 65], [3, 53], [1, 58], [70]]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Box plot
ax.boxplot(numerical_data, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Add background grid and labels
ax.grid()
plt.xticks(range(1, len(categories) + 1), categories, rotation=45)
plt.xlabel('Art Genre')
plt.ylabel('Creation Time (Hours)')
plt.title('Creation Time Distribution in Different Genres of Art (2021)')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/221_202312310058.png')

# Clear the current figure
plt.clf()
