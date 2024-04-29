
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Transform the data
legend_title = 'Employees (Millions)'
data_labels = ['Revenue (Billion $)', 'Net Profit (Billion $)', 'Employees (Millions)', 'Growth (%)']
data = np.array([[200, 20, 3, 3],
                 [140, 14, 1.6, 5],
                 [110, 11, 1.2, 4],
                 [90, 9, 0.9, 7],
                 [80, 8, 1.1, 6],
                 [50, 5, 0.6, 2]])
line_labels = ['Fast Food', 'Bakery', 'Dairy', 'Fruit & Vegetable', 'Meat', 'Seafood']

# Plot the data with type of bubble chart
fig = plt.figure()
ax = fig.add_subplot()

# Normalize the color value to the range of cmap values
norm = cm.colors.Normalize(vmin=data[:, -1].min(), vmax=data[:, -1].max())
mappable = cm.ScalarMappable(norm=norm, cmap=cm.get_cmap('tab20'))

# Plot a bubble chart
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=500*data[i, 2]+60, c=mappable.to_rgba(data[i, -1]), label=None)
    ax.scatter([], [], c=mappable.to_rgba(data[i, -1]), label=line_labels[i] + ' ' + str(data[i, 2]))

# Create legend
ax.legend(title=legend_title)

# Add color bar
cb = plt.colorbar(mappable, ax=ax)
cb.set_label(data_labels[-1])

# Set figure parameters
ax.set_title('Financial Performance of the Food and Beverage Industry in 2020')
ax.grid()
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/21.png')

# Clear the current image state
plt.clf()