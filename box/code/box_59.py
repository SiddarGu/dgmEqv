import matplotlib.pyplot as plt

# data preparation
crops = ['Wheat', 'Barley', 'Corn', 'Rice', 'Soybean']
data = [[2, 4, 6, 8, 10], 
        [1.5, 3.5, 5.7, 7.5, 10.5], 
        [3, 6, 8, 11, 15], 
        [2.5, 5, 7, 10, 13], 
        [1.2, 2.6, 3.5, 5, 7]]
outliers = [[], [13,15], [], [1, 18], [10, 12]]

# plot settings
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5, vert = False, patch_artist = True, 
           notch = True, medianprops = {'linewidth' : 2, 'color' : 'purple'})

# handling the outliers and showing them on the plot
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# adding a grid
ax.yaxis.grid(True)
ax.set_yticklabels(crops)
# mirror the yaxes
ax.yaxis.tick_left()
ax.yaxis.set_ticks_position('both')

# adding title and labels
plt.title('Crop Yield Distribution in Agriculture (2021)')
plt.xlabel('Yield (Tonnes)')

# save the figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/56_202312270030.png')

plt.clf()
