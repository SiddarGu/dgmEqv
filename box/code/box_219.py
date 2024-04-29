
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[20, 50, 100, 150, 200], [40, 90, 140, 190, 300], [25, 60, 110, 160, 220], [30, 70, 120, 170, 250], [50, 100, 150, 200, 300]]
outliers = [[], [400], [0.5], [400, 500], [750]]
line_labels = ['Solar Panels', 'Wind Turbines', 'Batteries', 'Geothermal Energy', 'Nuclear Reactors']
# Plot the data with the type of box plot
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)
ax.boxplot(data, whis=1.5)

# Outliers are plotted manually using ax.plot for each category
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', color='#000000')

# Drawing techniques such as background grids can be used
ax.yaxis.grid(True)
ax.set_xticklabels(line_labels)

# The title of y-axis should be given with its unit
ax.set_ylabel('Performance (Watts)')

# The title of the figure should be  Energy Performance Distribution in Science and Engineering Technologies (2025)
ax.set_title('Energy Performance Distribution in Science and Engineering Technologies (2025)')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5_202312251608.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5_202312251608.png')

# Clear the current image state at the end of the code
plt.clf()