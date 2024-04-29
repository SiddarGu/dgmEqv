import matplotlib.pyplot as plt

# restructure your data
subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
box_data = [[40, 60, 70, 85, 99], [45, 65, 75, 80, 100], [30, 55, 67, 80, 95], [35,57,68,82,98], [25,52,64,77,93]] 
outliers = [[], [110], [20,120], [130], [140]]

fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot()

# boxplot
bplot=ax.boxplot(box_data, vert=0, patch_artist=True, widths=0.6, whis=1.5)

# plot outliers
for i, outlier in enumerate(outliers):
  if outlier:  
    ax.plot(outlier, [i + 1] * len(outlier), "ro")

ax.set_yticks(range(1, len(subjects) + 1))
ax.set_yticklabels(subjects)
plt.title("Students' Score Distribution Across Different Subjects (2021)")
plt.xlabel('Score')
plt.ylabel('Subjects')
plt.grid(True)
plt.tight_layout()

path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/71_202312270030.png'
plt.savefig(path)
plt.clf()
