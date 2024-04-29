import matplotlib.pyplot as plt

# Restructured data
data = [
    ["Red Cross", [100, 500, 1000, 1500, 2000], []],
    ["UNICEF", [200, 800, 1500, 2200, 2900], [3200, 3400]],
    ["WHO", [150, 700, 1200, 1800, 2400], [2500, 2600]],
    ["Greenpeace", [50, 250, 500, 750, 1000], [55, 60]],
    ["Oxfam", [300, 1000, 2000, 3000, 4000], [5000]]
]

# Extracting category names, values and outliers
categories = [item[0] for item in data]
values = [item[1] for item in data]
outliers = [item[2] for item in data]

# Creating a figure and adding subplot
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

# Box plot
bp = ax.boxplot(values, vert=False, patch_artist=True, notch=True, whis=1.5)

# Coloring boxes
colors = ['lightblue', 'pink', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plotting outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "x")

# Setting labels and title
ax.set_yticklabels(categories)
ax.set_xlabel('Donation Amount ($)')
ax.set_title('Donation Amount Distribution among Charities and Nonprofit Organizations in 2022')

# Saving figure and clearing the figure
plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/121_202312270030.png", dpi=100)
plt.close(fig)
