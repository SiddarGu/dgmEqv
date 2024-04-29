import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import numpy as np

# Data
data_str = "Company,Revenue (Billion $),User Base (Millions),Number of Employees,Innovation Score (Out of 10)/n Microsoft,153,100,163000,9/n Google,160,120,140000,10/n Amazon,386,200,1200000,8/n Apple,274,90,137000,9/n Facebook,86,70,52534,8/n Twitter,3.46,40,4500,7/n Netflix,25,210,9500,9/n eBay,10.27,30,25000,7"
data_str = data_str.split("/n")
data_labels = data_str[0].split(",")[1:]
data = np.array([item.split(",")[1:] for item in data_str[1:]]).astype(float)
line_labels = [item.split(",")[0] + " " + str(item.split(",")[3]) for item in data_str[1:]]

# Figure
fig, ax = plt.subplots(figsize=(10,8))

# Colors
cmap = get_cmap('viridis')
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

# Bubble size normalization
sizes = np.array(data[:, 2]) / max(np.array(data[:, 2])) * 5000

# Scatter plot
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], color=cmap(norm(data[i, 3])), s=sizes[i], label=None)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), s=20, label=line_labels[i])

# Legends and labels
ax.legend(title=data_labels[2], loc='center left')
ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1], wrap=True)
plt.title('Technology and Internet Companies: Revenue, User Base, Employees and Innovation Score 2023')

# Color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, orientation="vertical", label=data_labels[3])

# Save and show figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/169_202312310045.png')
plt.clf()
