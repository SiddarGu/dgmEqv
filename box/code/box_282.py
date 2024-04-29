import matplotlib.pyplot as plt

# Restructured data
data = [["Cosmetics", [100, 500, 800, 1200, 1500]],
        ["Electronics", [200, 800, 1300, 1800, 2300]],
        ["Fashion", [150, 600, 1050, 1500, 1950]],
        ["Books", [50, 400, 750, 1100, 1450]],
        ["Household Essentials", [120, 700, 1300, 1900, 2500]]]
outliers = [[3000], [4000], [500, 100, 3500], [], [100, 5000]]

# Create the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot data
bp = ax.boxplot([item[1] for item in data], vert=False, patch_artist=True, notch=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'orange']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "x", color="black")

# Set axes' labels
ax.set_xlabel('Sales (Q)')
ax.set_ylabel('Product Category')
ax.set_yticklabels([item[0] for item in data])

# Set title
plt.title('Quarterly Sales Distribution in Retail and E-commerce Categories (2020)')

# Show grid
ax.grid(True)

# Mirroring the y-axis
ax.set_ylim(ax.get_ylim()[::-1])

# Save to file
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/116_202312270030.png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.clf()
