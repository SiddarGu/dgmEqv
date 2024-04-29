import matplotlib.pyplot as plt

# data
data = [
    ['USA', [10, 20, 30, 40, 50], []],
    ['Canada', [15, 30, 45, 60, 75], [98]],
    ['Australia', [5, 10, 20, 30, 40], [1, 60]],
    ['Germany', [12, 24, 35, 46, 60], []],
    ['Japan', [20, 40, 60, 80, 100], [120, 150]]
]

# Separating data
countries = [row[0] for row in data]
values = [row[1] for row in data]
outliers = [row[2] for row in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# boxplot with 1.5 whiskers
bplot = ax.boxplot(values, whis=1.5, labels=countries, patch_artist=True)

# plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

# grid, axis labels, title
ax.yaxis.grid(True)
ax.set_title('Annual Rainfall Distribution in Different Countries (Environment and Sustainability)')
ax.set_xlabel('Country')
ax.set_ylabel('Annual Rainfall (Inches)')
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/184_202312310058.png', dpi=300)

# Clear figure
plt.clf()
