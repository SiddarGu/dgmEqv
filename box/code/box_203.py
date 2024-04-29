import matplotlib.pyplot as plt
import numpy as np

data = [
    ["New York", 300, 400, 500, 600, 700, [800,900]],
    ["San Francisco", 400, 500, 600, 700, 800, [900,1000]],
    ["Seattle", 200, 300, 400, 500, 600, []],
    ["Boston", 250, 350, 450, 550, 650, [750,850]],
    ["Atlanta", 150, 250, 350, 450, 550, [450,650]]
]

five_num_summary = [[city[1], city[2], city[3], city[4], city[5]] for city in data]
outliers = [city[6] for city in data]

fig, ax = plt.subplots(figsize=(10, 10))
ax.boxplot(five_num_summary, whis=1.5)
x_labels = [city[0] for city in data]
ax.set_xticklabels(x_labels, rotation=30)

for i, outlier in enumerate(outliers):
    if outlier:
        y = np.array(outlier)
        x = np.array([i + 1] * len(outlier))
        ax.plot(x, y, 'r.')

ax.set_title("House Price Distribution in Various U.S. Cities (2022)")
ax.set_ylabel("House Price (in $1000)")
ax.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/157_202312310058.png")
plt.clf()
