import matplotlib.pyplot as plt

# Data for the plot
styles = ['Classical', 'Modern', 'Abstract', 'Expressionism', 'Surrealism']
data = [[8, 12, 16, 20, 24], [5, 10, 13, 16, 22], [9, 13, 17, 21, 26], [6, 9, 15, 20, 23], [4, 8, 12, 18, 22]]
outliers = [[], [3, 30], [33], [4, 5, 29], [2, 27]]

# Create the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot data
bp = ax.boxplot(data, whis=1.5)

# Iterate through outliers list and plot them
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "r*", markersize=8)

# Set grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey')
ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey')

# Mirror axes
ax.xaxis.tick_top()
ax.yaxis.tick_left()
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 

# Set labels and title
plt.xticks([i + 1 for i, _ in enumerate(styles)], styles, rotation=45)
ax.set_xlabel("Artistic Style")
ax.set_ylabel("Creation Time (Hours)")
plt.title("Creation Time Distribution in Different Artistic Styles (2021)")

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/195_202312310058.png')

# clear figure
plt.clf()
