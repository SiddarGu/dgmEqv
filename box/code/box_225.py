import matplotlib.pyplot as plt

# Data
departments = ['Defense', 'Education', 'Health', 'Agriculture', 'Transport']
funding = [[100, 150, 200, 260, 330], [80, 130, 175, 240, 300], [90, 140, 185, 250, 310], [70, 120, 160, 210, 280], [95, 140, 185, 250, 305]]
outliers = [[], [350], [370,400], [1,340], [1,360]]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111)

# Create boxplot
boxplot_dict = ax.boxplot(funding, vert=False, patch_artist=True, whis=1.5)

# Set colors
colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(boxplot_dict['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "x")

# Highlight median with horizontal lines
for line in boxplot_dict['medians']:
    x, y = line.get_xydata()[1] 
    ax.annotate(y, xy=(x, y), textcoords='data', ha='right')

# Set grid and labels
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(departments, rotation=45, ha='right')
ax.set_xlabel('Government Department')
ax.set_ylabel('Funding (Million)')
plt.title('Government Funding Distribution in Various Departments for Fiscal Year 2020')

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/117_202312270030.png')
plt.clf()
