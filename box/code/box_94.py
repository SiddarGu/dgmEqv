import matplotlib.pyplot as plt

# Data
subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
data = [[30, 48, 56, 70, 85], [40, 52, 59, 73, 90], [42, 55, 60, 70, 80], [38, 47, 55, 66, 78], [46, 52, 60, 68, 80]]
outliers = [[20, 90], [100], [96], [98], [88, 95]]

# Create Figure and Axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Boxplot
bp = ax.boxplot(data, whis=1.5)

# Outliers
for i, outlier in enumerate(outliers):
    if outlier:  # there are outliers for this category
        x = [i + 1] * len(outlier)  # x-coordinate of the outliers
        ax.plot(x, outlier, 'rx')  # plot outliers

# Grid, labels, title
ax.set_title('Student Score Distribution in Different Subjects (Academic Year 2022)')
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.7)
ax.set_axisbelow(True)
ax.set_xlabel('Subjects')
ax.set_ylabel('Scores')
ax.set_xticklabels(subjects, rotation=15)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/170_202312310058.png')

# Clear the figure
plt.clf()

