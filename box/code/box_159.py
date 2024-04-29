import matplotlib.pyplot as plt

# Restructure the data
data = [['Facebook', 845, 1000, 1200, 1500, 1820], ['Instagram', 300, 700, 800, 1000, 1200], ['Twitter', 200, 275, 350, 450, 550], ['LinkedIn', 80, 150, 200, 275, 325], ['Snapchat', 100, 150, 200, 250, 300]]
outliers = [[500, 2200], [], [150, 650], [70, 360], [75, 350]]

# Create figure and axes
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

# Boxplot
bp = ax.boxplot([d[1:] for d in data], whis=1.5, patch_artist=True)

# Colors for each boxplot
colors = ['lightblue', 'lightgreen', 'pink', 'yellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Setting axises, legend and title
ax.set_xticklabels([d[0] for d in data], rotation=45, ha='right')
ax.set_ylabel('Active Users (Millions)')
plt.title('Distribution of Active Users on Popular Social Media Platforms (2022)')

# Grid and layout
plt.grid(axis='y')

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/211_202312310058.png')
plt.grid(axis='y')
plt.cla()
