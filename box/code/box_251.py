import matplotlib.pyplot as plt

# Define data
categories = ['Mathematics', 'English', 'Physics', 'Chemistry', 'Biology']
values = [[50,65,75,85,95], [55,70,80,90,100], [62,77,85,93,99], [59,68,77,86,96], [53,67,74,81,90]]
outliers = [[], [45,120], [], [105], [48,98]]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Box plot
ax.boxplot(values, whis=1.5, labels=categories, notch=True, vert=True, patch_artist=True, showfliers=False)

# Iterate through outliers list
for i, outlier in enumerate(outliers):
    if outlier:  # plot only if there are outliers
        ax.plot([i + 1] * len(outlier), outlier, "ro", markersize = 4)

ax.set_title("Students' Score Distribution in Major Subjects (2021)")
ax.set_ylabel('Score')
ax.yaxis.grid(True)

# Adjust layout and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/164_202312310058.png')

# Clear current figure
plt.clf()
