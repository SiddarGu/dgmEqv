import matplotlib.pyplot as plt
import numpy as np

# Data
data = [
    [1, 2, 3, 4, 5],  # Facebook
    [0.5, 1.5, 2.5, 3.5, 4.5],  # Twitter
    [1.5, 2, 3, 4, 6],  # Instagram
    [1, 1.5, 2, 2.5, 3],  # LinkedIn
    [0.5, 1, 1.5, 2, 4]  # TikTok
]
outliers = [[0.5, 6.5], [5.5], [0.4, 7.3], [3.5, 4], [4.5, 5.5, 6]]
labels = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'TikTok']

# Create figure and add subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Box plot
bp = ax.boxplot(data, whis=1.5, patch_artist=True, notch=True)

# Customizing boxplot colors
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
plt.setp(bp['medians'], color='red')

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'o', color='black')

# Set labels and title
ax.set_xticklabels(labels, rotation=15)
ax.set_ylabel('Time Spent (Hours)')
plt.title('User Time Spent Distribution on Different Social Media Platforms (2022)')
plt.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/218_202312310058.png')

# clear the current figure
plt.clf()
