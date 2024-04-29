import matplotlib.pyplot as plt

# Structured data
categories = ['Movie', 'TV Show', 'Music', 'Theatre', 'Video Game']
box_data = [[2, 4, 5, 7, 8], [2, 4, 6, 7, 9], [1, 3, 4, 6, 8], [3, 4, 5, 7, 9], [1, 2, 4, 6, 8]]
outliers = [[1, 10], [1,10], [], [2,10], [0,9]]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Box plot
bp = ax.boxplot(box_data, notch=0, sym='', vert=1, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='o')

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro', ms=6)

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('Ratings Distribution in Different Entertainment Categories (2022)')
ax.set_xlabel('Entertainment Category')
ax.set_ylabel('Rating')

# Add x-tick labels
plt.setp(ax, xticks=[y + 1 for y in range(len(box_data))],
         xticklabels=categories)

# If text is long, rotate it
plt.xticks(rotation=30)

# To prevent content from being cut off
fig.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/177_202312310058.png', bbox_inches='tight')

# Clear the current figure
plt.clf()

