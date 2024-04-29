import matplotlib.pyplot as plt

labels = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'YouTube']
data = [[1, 2, 3, 4, 5], [0.5, 1.5, 2.5, 3.5, 4.5], [1.5, 2.5, 3.5, 4.5, 5.5], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
outliers = [[], [6], [0.5, 7], [0.3, 6.6], []]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Daily Usage Distribution in Different Social Media Platforms (2022)')
ax.boxplot(data, widths = 0.4, vert=False, notch=True, patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'), whiskerprops=dict(color='blue'), flierprops=dict(marker='o', markerfacecolor='red'))

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

ax.set_yticklabels(labels, fontsize = 8)
ax.set_xlabel('Usage (Hours/Day)')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/147_202312270030.png')
plt.clf()
