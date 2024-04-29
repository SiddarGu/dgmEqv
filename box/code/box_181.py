import matplotlib.pyplot as plt

data = [["Flu", 5, 10, 15, 20, 25, [30, 40]],
        ["Pneumonia", 15, 20, 25, 30, 35, []],
        ["Measles", 10, 15, 20, 25, 30, [35, 40]],
        ["Tuberculosis", 30, 35, 40, 45, 50, [55, 60]],
        ["Diphtheria", 20, 25, 30, 35, 40, [45, 50]]]

labels, box_data, outliers = zip(*[(d[0], d[1:6], d[6]) for d in data])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

boxprops = dict(linestyle='-', linewidth=1, color='k')
medianprops = dict(linestyle='-', linewidth=1.5, color='purple')

# plot box plot
box_plot = ax.boxplot(box_data, vert=True, patch_artist=True, 
                      labels=labels, whis=1.5, boxprops=boxprops, medianprops=medianprops)

colors = ['pink', 'lightblue', 'lightgreen', 'yellow', 'grey']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:  
        ax.plot([i + 1] * len(outlier), outlier, "x")

ax.yaxis.grid(True)
ax.set_title('Recovery Time Distribution for Various Diseases (2023)')
ax.set_ylabel('Days')

# rotate label if too long
plt.xticks(rotation=30)
plt.tight_layout()

save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/231_202312310058.png'
plt.savefig(save_path)
plt.clf()
