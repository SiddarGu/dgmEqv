import matplotlib.pyplot as plt

categories_data = [['Theatre', [10,20,30,40,50]], ['Classical Music', [8,18,28,38,48]], ['Modern Art', [12,22,32,42,52]], ['Literature', [14,24,34,44,54]], ['Dance', [16,26,36,46,56]]]
outlier_data = [[], [65], [], [75, 80], [92, 96]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# set these so that the box width will be changed automatically
min_ylim, max_ylim = plt.ylim()
box_width = (max_ylim - min_ylim) / (len(categories_data) * 2)

# create box plots
bplot = ax.boxplot([x[1] for x in categories_data], vert=False, patch_artist=True, whis=1.5)

for i, outlier in enumerate(outlier_data):
  if outlier:
    ax.plot(outlier, [i + 1] * len(outlier), "ko")

ax.set_yticklabels([x[0] for x in categories_data])
ax.set_xlabel('Attendance (Thousand)')
ax.set_title('Audience Attendance Distribution in Various Art Genres (2020)', fontsize=14)
plt.grid(True, which='both', axis='x', linestyle='--', linewidth=0.6)
plt.gca().xaxis.grid(True,linestyle='--')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/130_202312270030.png', dpi=300)
plt.clf()
