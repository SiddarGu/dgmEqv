import matplotlib.pyplot as plt

# restructure data
product_types = ["Automobile", "Electronics", "Food & Beverage", "Textiles", "Pharmaceuticals"]

production_time_data = [
    [10, 20, 30, 45, 60],
    [7, 15, 22, 32, 40],
    [5, 10, 15, 22, 30],
    [6, 14, 21, 29, 35],
    [12, 25, 36, 45, 60]
]

outlier_data = [ [], [2,50], [4,35], [1,40], [70] ]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# box plot
bp = ax.boxplot(production_time_data, vert=False, patch_artist=True, notch=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outlier_data):
    if outlier:  # if there are outliers
        ax.plot(outlier, [i + 1] * len(outlier), 'x', color='red', markersize=8)

ax.set_yticklabels(product_types, rotation=45)
ax.set_xlabel('Production Time (Days)')
ax.set_title('Product Production Time Distribution in Different Manufacturing Sectors (2021)')
ax.grid(True)

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/99_202312270030.png', bbox_inches='tight')
plt.clf()
