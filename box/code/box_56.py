# necessary libraries
import matplotlib.pyplot as plt

# data 
data = [
    ["Hydroelectric", 200, 500, 900, 1300, 2000],
    ["Thermal", 250, 550, 950, 1350, 2050],
    ["Nuclear", 300, 600, 1000, 1400, 2100],
    ["Wind", 100, 400, 800, 1200, 1750],
    ["Solar", 150, 450, 850, 1250, 1850]
]

outliers = [[], [2200,2300], [], [2000], [1900]]

# restructure data
data = [x[1:] for x in data]

# create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# create box plot
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=0, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# customize grid, labels, title
ax.yaxis.grid(True)
ax.set_yticklabels(["Hydroelectric", "Thermal", "Nuclear", "Wind", "Solar"])
ax.set_xlabel("Production (GWh)")
ax.set_title("Electricity Production Distribution in Different Power Plants (2021)")

# save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/140_202312270030.png")

# clear figure for re-use
plt.clf()
