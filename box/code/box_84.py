import matplotlib.pyplot as plt

# Restructure the data
data = [["ISP A", 50, 100, 150, 200, 300], ["ISP B", 40, 80, 140, 180, 240], ["ISP C", 70, 120, 160, 210, 280], ["ISP D", 80, 140, 200, 260, 330], ["ISP E", 60, 110, 150, 200, 250]]
outliers = [[], [35, 450], [50], [400, 450], [500]]

data_labels, data_min, data_q1, data_median, data_q3, data_max = zip(*data) 

# Merge the min, q1, median, q3, and max data into a 2D list
merged_data = [list(a) for a in zip(data_min, data_q1, data_median, data_q3, data_max)]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Box plot
bplot = ax.boxplot(merged_data, vert=True, patch_artist=True, labels=data_labels, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgray']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax.yaxis.grid(True)
ax.set_title('Internet Speed Distribution in Various Internet Service Providers (2022)')
ax.set_ylabel('Speed (Mbps)')

# Manually add the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko", ms=3)

plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/59_202312270030.png')

plt.clf()
