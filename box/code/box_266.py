import matplotlib.pyplot as plt
company_data = [["Company A", 3, 6, 8, 12, 15, []],
                ["Company B", 4, 7, 10, 14, 18, [22]],
                ["Company C", 5, 7, 11, 15, 19, [2, 23]],
                ["Company D", 6, 9, 13, 17, 21, [1, 24]],
                ["Company E", 7, 10, 14, 18, 22, [25]]]

#split the box plot data and outliers
box_plot_data = [x[1:-1] for x in company_data]
outliers = [x[-1] for x in company_data]

#setup the figure and axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.set_title('Transit Time Distribution for Shipping Companies in 2025')
ax.set_ylabel('Transit Time (Days)')
ax.grid(True)

#create box plots
bp = ax.boxplot(box_plot_data, vert=False, patch_artist=True, notch=True, bootstrap=5000, whiskerprops=dict(linestyle="--"), whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

#plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro", markersize=5)

#set xticks labels
ax.set_yticklabels([x[0] for x in company_data])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/105_202312270030.png')
plt.clf()
