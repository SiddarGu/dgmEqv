import matplotlib.pyplot as plt

# Restructure the data
data = [
    ['Steel', 350, 400, 500, 600, 800, []],
    ['Aluminium', 70, 150, 200, 250, 300, [30, 400]],
    ['Titanium', 440, 600, 780, 900, 1000, [300, 1100]],
    ['Carbon Fiber', 550, 650, 700, 750, 800, [500, 900]],
    ['Copper', 100, 200, 250, 300, 350, [50, 400]]
]

box_data, outliers = [], []
for item in data:
    box_data.append(item[1:6])
    outliers.append(item[6])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Box plot 
box = ax.boxplot(box_data, widths=0.4, vert=False, sym='', whis=1.5)

# Add a horizontal grid to the plot
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Add labels for x and y axis
ax.set_xlabel("Strength (MPa)")
ax.set_ylabel("Material")

# Set title
ax.set_title("Material Strength Distribution in Science and Engineering Materials")

# Set the y-tick labels to correlate to the given categories
ax.set_yticklabels([item[0] for item in data])

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:  # check if the outlier list is not empty
        ax.plot(outlier, [i + 1] * len(outlier), 'ro', alpha=0.5)

# Save the figure with tight layout
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/86_202312270030.png")

# Clear the current image state
plt.clf()
