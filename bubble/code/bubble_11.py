

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Transform the given data into three variables
data_labels = ['Production Volume (Million Tonnes)', 'Land Used (Million Hectares)', 'Profit Margin (%)']
data = [[730, 220, 20],
        [1150, 180, 25],
        [490, 160, 15],
        [350, 120, 30],
        [220, 90, 18],
        [200,80,19],
        [120,70,17],
        [100,60,16],
        [90,50,12],
        [80,40,14]]
line_labels = ['Wheat 20', 'Corn 25', 'Rice 15', 'Soybeans 30', 'Bananas 18', 'Tomatoes 19', 'Apples 17', 'Grapes 16', 'Strawberries 12', 'Peaches 14']

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

# Set range for bubble size and color
norm = cm.colors.Normalize(vmin=15, vmax=30)
s_mapping = np.linspace(600, 5000, len(data))

# Plot each line and add a empty point
for i, d in enumerate(data):
    ax.scatter(d[0], d[1], s=s_mapping[i], c=cm.jet(norm(d[2])), label=None)
    ax.scatter([], [], c=cm.jet(norm(d[2])), label=line_labels[i], s=20)

# Plot the legend
ax.legend(title=data_labels[2], loc='upper left', bbox_to_anchor=(1, 1))

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=cm.jet, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, orientation='horizontal', fraction=0.05)
cbar.set_label(data_labels[2], labelpad=10)

# Drawing techniques such as background grids can be used
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set the title
plt.title('Profitability of Different Crop Production and Land Use - Agriculture 2023')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/8.png')

# Clear the current image state
plt.clf()