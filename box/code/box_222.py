import matplotlib.pyplot as plt
import numpy as np

fields = ["Chemical Engineering", "Mechanical Engineering", 
          "Electrical Engineering", "Civil Engineering", 
          "Computer Engineering"]
data = [[40, 90, 120, 180, 250], [50, 100, 150, 200, 250],
        [80, 130, 180, 230, 280], [75, 125, 175, 225, 275], 
        [60, 110, 160, 210, 260]]
outliers = [[], [0, 300], [350], [325], [295]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(data, whis=1.5, patch_artist=True, notch=True, vert=True)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

plt.grid()
ax.set_title("Research Period Distribution in Engineering Fields (2022)")
ax.set_ylabel("Research Period (Days)")
plt.xticks(np.arange(1, len(fields) + 1), fields, rotation=30, ha="right")
plt.title="Research Period Distribution in Engineering Fields (2022)"

plt.tight_layout()

plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/187_202312310058.png")

plt.clf()
