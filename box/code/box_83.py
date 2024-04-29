import matplotlib.pyplot as plt

# Data
region_data = [['Westside', 200000, 300000, 350000, 400000, 500000, [550000, 600000]],
               ['Eastside', 220000, 320000, 370000, 420000, 510000, [560000]],
               ['Northside', 210000, 310000, 360000, 410000, 510000, []],
               ['Southside', 230000, 330000, 375000, 425000, 515000, [570000]],
               ['Downtown', 240000, 340000, 380000, 430000, 520000, [580000,600000]]]

# Construct box plot data and outlier data
box_data = [data[1:6] for data in region_data]
outliers = [data[6] for data in region_data]

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Box plot
bplot = ax.boxplot(box_data, vert=False, patch_artist=True, whis = 1.5)

# Styling and labels
regions = [data[0] for data in region_data]
ax.set_yticklabels(regions)
plt.xticks(rotation=30)
plt.grid(True, linestyle="--", which="major", color="grey", alpha=.25)
ax.set_ylabel('Housing Market Price Distribution in Different Regions in 2022')
plt.title('Housing Market Price Distribution in Different Regions in 2022')

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Adjust layout and save plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/57_202312270030.png')

# Clear the current figure
plt.clf()
