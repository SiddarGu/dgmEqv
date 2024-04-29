import matplotlib.pyplot as plt

# Defining the data 
transport_modes = ['Air Freight', 'Sea Freight', 'Rail Freight', 'Road Freight', 'Truck Delivery']
stats = [[1,2,3,4,5], [10,12,16,20,24], [5,6,8,12,15], [3,4,6,7,9], [2,3,4,5,6]]
outliers = [[], [8,30], [1,18], [2,13], [1,8]]

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Plotting the box plots
bplot = ax.boxplot(stats, vert=True, patch_artist=True, notch=True, whis=1.5)

# Styling the plot
colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'plum']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Manually add outliers
for i, outlier in enumerate(outliers):
    if outlier: # Check for outliers
        ax.plot([i + 1] * len(outlier), outlier, "ko", markersize=3)

ax.set_xticklabels(transport_modes, rotation=45) # Setting the x-tick labels with rotation
ax.yaxis.grid(True) # Adding a horizontal grid
ax.set_ylabel("Delivery Time (Days)", labelpad=15) # Setting the y label
ax.set_title("Delivery Time Distribution in Different Modes of Transportation (2022)") # Setting the title

# Increase space between ticks and x-axis to prevent overlapping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/206_202312310058.png')

# Clear the figure
plt.clf()
