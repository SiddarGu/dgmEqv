import matplotlib.pyplot as plt

# Restructuring the data
data = [["School A", 60, 70, 82, 90, 98, []], ["School B", 54, 68, 79, 88, 95, [47,103]], ["School C", 62, 72, 80, 89, 99, []], ["School D", 58, 68, 77, 85, 93, [-5,107]], ["School E", 65, 74, 84, 93, 100, [59,102]]]
stats, outliers = [], []

for school_data in data:
    stats.append(school_data[1:6])
    outliers.append(school_data[6])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Create a boxplot
bplot = ax.boxplot(stats, vert=True, patch_artist=True, widths=0.5, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# iterate over outliers and plot on graph
for i, outlier in enumerate(outliers):
    if outlier: # Check if outlier list is not empty
        ax.plot([i + 1] * len(outlier), outlier, "ko")

grid = plt.GridSpec(5, 2, wspace=0.4, hspace=0.3)

ax.set_yticks(range(0,120,20))
ax.set_xticklabels([x[0] for x in data], rotation=15, fontsize=10) # print school names at the X-axis
ax.set_ylabel('Score (Points)', fontsize=12)
ax.set_title('Student Score Distribution by School (2021-2022)', fontsize=14)

plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/162_202312310058.png')
plt.clf()  # to clear the image state
