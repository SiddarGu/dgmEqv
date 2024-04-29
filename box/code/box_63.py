import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


data = [['Theatre', 1, 2, 3, 4, 5, []],
        ['Classical Music', 2, 3, 4, 5, 6, [7, 8]],
        ['Painting Exhibition', 0.5, 1, 1.5, 2, 2.5, [3, 4]],
        ['Literary Festival', 2, 3, 4, 5, 6, [1, 7]], 
        ['Sculpture Exhibition', 1, 2, 3, 4, 5, [6, 7]]]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

categories = [item[0] for item in data]
values = [item[1:6] for item in data]
outliers = [item[6] for item in data]

ax.boxplot(values, whis=1.5)
ax.set_xticklabels(categories, rotation=45, ha='right')

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')
        
ax.set_ylabel('Duration (Hours)')
ax.grid(True)

fig.subplots_adjust(bottom=0.15)
fig.suptitle('Event Duration Distribution in Different Art Genres (2023)')
fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/209_202312310058.png')
plt.clf()
