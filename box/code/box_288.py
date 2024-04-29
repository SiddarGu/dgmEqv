
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Restructure the data into two 2D lists
data = [[1.5,3.0,6.0,9.0,12.0],[2.0,4.0,7.5,11.0,14.0],[1.0,2.0,4.5,7.0,10.0],[1.5,3.5,6.0,8.5,11.0],[2.0,4.5,7.0,9.5,12.0]]
outliers = [[],[24],[40,50],[13],[20]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i+1] * len(outlier)
        y = outlier
        ax.plot(x, y, 'ro', markersize=10)

# Drawing techniques such as background grids
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# Label the axes
ax.set_ylabel('Duration (Hours)', fontsize=14)
ax.set_xlabel('Art Form', fontsize=14)
ax.set_xticklabels(['Theatre', 'Dance', 'Music', 'Photography', 'Visual Arts'], rotation=30, fontsize=14, wrap=True)

# Set the legend for different colors
red_patch = mpatches.Patch(color='red', label='Outliers')
ax.legend(handles=[red_patch], fontsize=14)

# Set the title of the figure
ax.set_title('Creative Activity Duration Distribution in Arts and Culture (2020)', fontsize=16)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/18_202312270030.png')

# Clear the current image state
plt.clf()