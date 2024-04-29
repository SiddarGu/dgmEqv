import matplotlib.pyplot as plt

# Data
hotel_brand = ['Luxury Suites', 'Family Inn', 'Beachfront Deluxe', 'City Central', 'Mountain Retreat']
box_plot_data = [[5,12,18,25,30], [7,15,20,28,35], [6,14,19,26,33], [8,16,22,28,34], [10,18,24,30,36]]
outliers_data = [[], [2, 40], [50], [5, 45], [55]]

# Create figure and subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Box plot
bplot = ax.boxplot(box_plot_data, patch_artist=True, notch=True, vert=1, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'purple', 'lightyellow']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers manually
for i, outliers in enumerate(outliers_data):
    if outliers:
        ax.plot([i + 1] * len(outliers), outliers, "x")

# Configure the chart
ax.set_xticklabels(hotel_brand, rotation = 30)
ax.set_ylim([0,60])
plt.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
plt.title('Check-in Time Distribution in Hotel Brands (in minutes) in 2022', size=15)
plt.ylabel('Time (minutes)')

# Save figure and clear image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/181_202312310058.png')
plt.clf()
