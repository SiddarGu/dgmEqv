import matplotlib.pyplot as plt

# Data preparation
social_media = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Snapchat']
data = [[1000, 1500, 2000, 2500, 3000], [300, 500, 700, 900, 1100], [600, 800, 1000, 1200, 1400], [200, 400, 600, 800, 1000], [100, 200, 300, 400, 500]]
outliers = [[], [1500], [1800], [1300, 1400], [700]]

# Create figure and subplot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Generate box plots
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

colors = ['blue', 'green', 'red', 'yellow', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ko')

# Set chart title and labels
ax.set_title('User Count Distribution on Major Social Media Platforms (2022)')
ax.set_xlabel('User Count (Million)')
ax.set_yticklabels(social_media)
ax.set_ylabel('Social Media Platform')

# Save the figure
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/66_202312270030.png', dpi=300)
plt.clf()
