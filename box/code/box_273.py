import matplotlib.pyplot as plt

# Data preparation
categories = ['Transportation', 'Electricity & Heat', 'Manufacturing & Construction', 'Residential & Commercial', 'Agriculture']
data = [[20, 45, 68, 95, 120], [25, 60, 80, 110, 150], [15, 35, 55, 75, 100], [10, 32, 50, 70, 90], [12, 38, 60, 85, 110]]
outliers = [[], [180,200], [130], [105,115], [5, 150]]

# Creating figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplots of each category
bplot = ax.boxplot(data, vert=False, patch_artist=True, whis=1.5)
colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'purple']

for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "o", color = 'darkgreen')

# Setting y axis labels
plt.yticks(range(1, len(categories) + 1), categories, ha = 'right')

# Setting grid and mirroring the axes
ax.xaxis.grid(True)
ax.yaxis.grid(True)
ax.xaxis.tick_top()
ax.yaxis.tick_right()

# Setting y axis title
ax.set_ylabel('Carbon Emission (M Tonnes)')

# Setting figure title
plt.title('Distribution of Carbon Emissions across Different Sectors (2019)')

# Saving figure in required path
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/100_202312270030.png')

plt.show()

# Clearing the current figure
plt.clf()
