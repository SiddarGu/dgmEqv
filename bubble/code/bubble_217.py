import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Transformed data
data_labels = ["Annual Sales (Billion $)", "Employment Rate (%)", "Customer Satisfaction (Score)", "Environmental Impact (Score)"]
data = np.array([[300, 15, 80, 40],
                 [500, 20, 85, 50],
                 [200, 10, 90, 60],
                 [700, 25, 70, 35],
                 [600, 18, 95, 55],
                 [100, 8, 87, 65]])
line_labels = ["Soda", "Beer", "Wine", "Fast food", "Coffee", "Fruit Juice"]

# Create figure
fig, ax = plt.subplots(figsize=(10,10))

# Plot data
colors = cm.viridis(Normalize()(data[:, 3]))
sizes = Normalize()(data[:, 2])*4400 + 600
for (i, (x, y)) in enumerate(zip(data[:, 0], data[:, 1])):
    ax.scatter(x, y, label=None, color=colors[i], s=sizes[i])
    # Scatter an empty point for each line_label
    ax.scatter([], [], label=line_labels[i] + f' {data[i, 2]}', s=20, color=colors[i])
  
# Plot legend
ax.legend(title=data_labels[2], loc='upper left')

# Add color bar
sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
plt.colorbar(sm, label=data_labels[3])

# Further adjust
ax.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Market Analysis of the Food and Beverage Industry 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/83_202312301731.png')

# Clear the current image state
plt.clf()
