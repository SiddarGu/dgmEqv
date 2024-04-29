import matplotlib.pyplot as plt

# data as 2D lists
stats = [[17, 42, 62, 85, 110], [27, 53, 75, 90, 122], [12, 36, 60, 78, 110], [15, 47, 70, 83, 110], [20, 45, 70, 95, 120]]
outliers = [[], [3, 140], [2, 125], [1, 150], []]
labels = ['Sociology', 'Linguistics', 'Philosophy', 'Literature', 'Anthropology']

# create figure before plotting
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

# box plot each category
bplot = ax.boxplot(stats, vert=True, patch_artist=True, labels=labels, notch=True, bootstrap=5000,
                   boxprops=dict(facecolor=(0.75, 0.75, 0.75), linewidth=1.5),
                   medianprops=dict(color='red', linewidth=2.0),
                   whiskerprops=dict(linestyle='-', linewidth=1.5),
                   capprops=dict(linestyle='-', linewidth=1.5),
                   flierprops=dict(marker='o', markerfacecolor='green', markersize=6),
                   whis=1.5)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "rx")

# drawing grid and mirroring axes
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)

# Set labels
ax.set_xlabel('Area of Study')
ax.set_ylabel('Attendees (Persons)')
plt.title('Attendance Distribution in Social Sciences and Humanities Lectures (2021)')
plt.xticks(rotation=45, ha='right')

# Saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/243_202312310058.png', dpi=300)

# Clear the current figure's content
plt.clf()
