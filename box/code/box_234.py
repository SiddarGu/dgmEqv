import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

data = [
    ['Electronic Devices', 10, 40, 80, 120, 200, []],
    ['Appliances', 15, 60, 100, 200, 300, [10,400]],
    ['Furniture', 20, 80, 150, 250, 400, [25,500]],
    ['Toys', 5, 30, 70, 110, 150, [300]],
    ['Vehicles', 25, 75, 150, 225, 300, [400]],
    ['Food and Beverage', 20, 40, 90, 140, 190, [275,390]]
]

# Split data into labels, box_plot_data and outliers
labels = [item[0] for item in data]
box_plot_data = [item[1:6] for item in data]
outliers = [item[6] for item in data]

# Creating figure
fig = plt.figure(figsize =(10, 7))

# Creating axes instance
ax = fig.add_subplot(111)

ax.boxplot(box_plot_data, whis=1.5, patch_artist=True)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:  # check if outlier list is not empty
        ax.plot([i + 1] * len(outlier), outlier, "x")
        
# Adding title
plt.title("2022 Production Time Distribution in Various Manufacturing Sectors")

# Adding y label
plt.ylabel("Production Time (Hours)")

# Adding x label
plt.xlabel("Product Type")

plt.xticks([1, 2, 3, 4, 5, 6], labels, rotation='vertical')

# Removing top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
        
plt.grid(True)

# Saving the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/122_202312270030.png', bbox_inches="tight")

# Clear the current figure
plt.clf()
