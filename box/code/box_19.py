
import matplotlib.pyplot as plt 
import numpy as np 

# Restructure the data into two 2D lists. 
data = [[1000, 2000, 3000, 4000, 5000], 
        [1200, 2500, 3500, 4500, 5500], 
        [1400, 2700, 3700, 4700, 5700],
        [1100, 2400, 3400, 4400, 5400], 
        [1300, 2600, 3600, 4600, 5600]]
outliers = [[], [6000], [100, 6500], [6000, 7000], [6000]]
line_labels = ['Wheat', 'Rice', 'Maize', 'Soybean', 'Barley']

# Plot the data with the type of box plot. 
fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(data, whis=1.5)

# Outliers are plotted manually using ax.plot for each category.
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', c='red')

# Drawing techniques such as background grids can be used.
ax.grid()

# The title of y-axis should be given with its unit.
ax.set_xticklabels(line_labels)
ax.set_ylabel('Yield (kg/ha)')

# The title of the figure should be  Crop Yield Distribution in Agriculture and Food Production (2021).
ax.set_title('Crop Yield Distribution in Agriculture and Food Production (2021)')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/34_202312251608.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/34_202312251608.png')

# Clear the current image state at the end of the code.
plt.clf()