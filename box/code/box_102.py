import matplotlib.pyplot as plt
import numpy as np

data = {
    "Painting": [30, 90, 150, 210, 300, []],
    "Sculpture": [45, 75, 130, 190, 280, [1, 400]],
    "Photography": [60, 120, 180, 240, 320, [10, 15]],
    "Digital art": [15, 60, 100, 140, 200, [300]],
    "Street art": [20, 50, 90, 130, 170, [320]]
}

labels = list(data.keys())
stats = [v[:-1] for v in data.values()]
outliers = [v[-1] for v in data.values()]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Create box plot
bp = ax.boxplot(stats, vert=False, patch_artist=True, notch=True, whis=1.5)

colors = ['#D0DBEE', '#C2C4E2', '#EED4E5', '#D3E2D1', '#F7D6D2']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.yaxis.grid(True)
plt.title("Audience Attendance Distribution in Art Genres (2022)")
plt.xlabel("Audience Attendance (Thousand)")
plt.yticks(np.arange(1, len(labels) + 1), labels)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ko')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/97_202312270030.png', dpi=300)
plt.clf()
