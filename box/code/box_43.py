
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[3,6,8,9,10],[2,4,7,8,9],[1,4,5,7,8],[2,3,5,7,9],[4,6,7,8,9]]
outliers = [[],[1,10],[9,10],[1,10],[10]]
line_labels = ['Covid-19', 'Influenza', 'Measles', 'Mumps', 'Tuberculosis']

# Plot the data with the type of box plot
fig, ax = plt.subplots()
ax.boxplot(data, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier) != 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro')

# Set the title of y-axis
ax.set_xticklabels(line_labels)
ax.set_ylabel('Severity (Scale 1-10)')

# Drawing techniques such as background grids
ax.yaxis.grid(True)

# Set the title of the figure
ax.set_title('Severity Scale of Common Diseases in Healthcare (2020)')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/36_202312251608.png')

# Clear the current image state
plt.clf()