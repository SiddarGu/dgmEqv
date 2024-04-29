import matplotlib.pyplot as plt

# restructure the data
materials = ['Steel', 'Aluminum', 'Titanium', 'Plastic', 'Carbon Fiber']
values = [[200, 300, 400, 500, 600], [100, 200, 300, 400, 500], [300, 400, 500, 600, 700], [50, 100, 150, 200, 250], [400, 500, 600, 700, 800]]
outliers = [[], [750, 800], [950], [30, 320], [1000]]

# set up the plot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# draw boxplots
ax.boxplot(values, whis=1.5)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ko')

# aesthetics
ax.set_title('Compression Strength Distribution in Different Engineering Materials (2022)')
ax.set_ylabel('Compression Strength (MPa)')
ax.set_xticks(range(1, len(materials) + 1))
ax.set_xticklabels(materials, rotation=45)
ax.grid(True)

# save and clear the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/158_202312310058.png')
plt.clf()
