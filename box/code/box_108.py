import matplotlib.pyplot as plt

# define data
isp = ['ISP A', 'ISP B', 'ISP C', 'ISP D', 'ISP E']
min_ping_time = [[12,20,30,40,50],[18,25,35,45,55],[15,23,33,43,53],[10,22,32,42,52],[20,28,38,48,58]]
outlier_ping_time = [[60,70],[10,65],[8,75],[7,80],[85]]

# create figure
fig, ax = plt.subplots(figsize=(10,8))

# create box plot
bp = ax.boxplot(min_ping_time, whis=1.5, patch_artist=True)

# Colors for each boxplot
colors = ['lightblue', 'lightgreen', 'lightyellow', 'pink', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# plot outliers
for i, outlier in enumerate(outlier_ping_time):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "rx")

# make the grid
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# title and labels
plt.title('Ping Time Distribution among Internet Service Providers (2022)')
plt.ylabel('Ping Time (ms)')
plt.xticks(range(1, len(isp) + 1), isp, rotation=30, ha='right')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/201_202312310058.png')

# Clear the current figure
plt.clf()
