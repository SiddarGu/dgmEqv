import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Transforming given data into required variables
data_labels = ["Quantity (Thousands)", "Production Cost ($)", "Profit Margin (%)", "Market Share (%)"]
data = np.array([[500, 100000, 10, 30],
                 [800, 80000, 15, 20],
                 [400, 50000, 12, 25],
                 [600, 60000, 8, 15],
                 [300, 70000, 10, 10],
                 [200, 90000, 5, 5]])
line_labels = ["Cars" + str(data[0, 2]),
               "Electronics" + str(data[1, 2]),
               "Furniture" + str(data[2, 2]),
               "Textiles" + str(data[3, 2]),
               "Appliances" + str(data[4, 2]),
               "Machinery" + str(data[5, 2])]

# Create the figure
fig, ax = plt.subplots(figsize=(12, 6)) 

cmap = plt.get_cmap("tab20")
colors = cmap(np.arange(len(data)) / len(data))
for i, color in enumerate(colors):
    ax.scatter(data[i, 0], data[i, 1], label=None, color=color, s=(data[i, 2] * 60), alpha=0.5)
    ax.scatter([], [], color=color, label=line_labels[i], alpha=0.5)

plt.legend(title=data_labels[2])
plt.title('Analysis of Manufacturing and Production in Different Industries')

# Add a color bar
from matplotlib.cm import ScalarMappable
sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=100))
sm.set_array([])
plt.colorbar(sm, label="Market Share (%)", orientation='vertical')

# Show axes labels
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/368_202312311429.png')
plt.clf()

