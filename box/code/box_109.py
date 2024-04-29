import matplotlib.pyplot as plt

# Restructure your data
categories = ['Civil Engineering', 'Mechanical Engineering', 'Electrical Engineering', 'Chemical Engineering', 'Aerospace Engineering']
data = [[3, 6, 12, 18, 24], [4, 7, 13, 19, 26], [5, 10, 15, 20, 25], [6, 11, 16, 21, 27], [7, 8, 14, 17, 23]]
outliers = [[], [30,31], [1,2], [28,29,30], [5,6,24,25]]

# Create a figure before plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Create box plots for each category
bp = ax.boxplot(data, vert=False, patch_artist=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:  # check if outlier list is not empty
        ax.plot(outlier, [i + 1] * len(outlier), 'x', color='k')

ax.set_yticklabels(categories, fontsize=8)

# Add grid lines
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# Add title and labels
plt.title('Project Duration Distribution in Engineering Disciplines (2015-2020)')
plt.xlabel('Project Duration (Months)')
plt.ylabel('Engineering Discipline')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/84_202312270030.png')

# Clear figure
plt.clf()
