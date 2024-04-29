
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[0.5,3.2,6.0,9.2,15.0],
        [2.0,4.5,7.1,10.9,13.4],
        [1.0,2.7,4.9,7.4,10.3],
        [1.5,3.1,5.5,8.2,12.1],
        [0.8,3.0,5.3,8.0,11.9]]

outliers = [[],
            [14.6,20.0],
            [0.1,14.2,19.1],
            [13.7,17.8],
            [16.2]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.boxplot(data, whis =1.5)

# Outliers are plotted manually using ax.plot for each category
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.full(len(outlier), i+1), outlier, "r^")

# Drawing techniques such as background grids
ax.yaxis.grid(True)
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(["City A", "City B", "City C", "City D", "City E"])
ax.set_ylabel("Greenhouse Gas Emission (Ton)")
ax.set_title("Greenhouse Gas Emission Distribution in Cities (2021)")
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/15_202312270030.png')

# Clear the current image state
plt.clf()