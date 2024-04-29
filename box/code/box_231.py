

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[2, 4, 6, 8, 10], 
        [7, 12, 17, 22, 27],
        [4, 10, 16, 22, 28],
        [6, 13, 20, 27, 34],
        [8, 15, 22, 29, 36]]
outliers = [[], [30], [2, 35], [2, 40], [38]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.full(len(outlier), i+1), outlier, 'ro', alpha=0.5)

# Adjust the plotting
ax.set_xticklabels(['Bonds', 'Stocks', 'Mutual Funds', 'Hedge Funds', 'Options'])
ax.set_ylabel('Return (%)')
ax.set_title('Investment Return Distribution in Business and Finance (2020)')
ax.grid(True)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/10_202312251608.png')

# Clear the current image state
plt.clf()