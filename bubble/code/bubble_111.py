import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Parse the data
data_text = "Company,Market Cap (Billion $),Revenue (Billion $),Employee Count (Thousands),Dividend Yield (%)\n Apple,2000,260,137,1.2\n Amazon,1600,280,798,0\n Microsoft,1400,125,163,0.9\n Google,900,160,135,0\n Tesla,600,25,71,0\n Facebook,800,70,45,0"
data_rows = data_text.split("\n")
data_labels = data_rows[0].split(",")
data = np.array([row.split(",")[1:] for row in data_rows[1:]], dtype=float)
line_labels = [row.split(",")[0] + " " + str(data[i, 2]) for i, row in enumerate(data_rows[1:])]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 8))
cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])

# Plot bubbles
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], color=cmap(norm(data[i, 3])), s=np.interp(data[i, 2], [min(data[:, 2]), max(data[:, 2])], [600, 5000]), label=None)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), label=line_labels[i], s=20)

ax.set_title("Company Performance in Business and Finance Sector")
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.grid(True)

# Add a legend and a colorbar
plt.legend(title=data_labels[2], loc='upper left')
fig.colorbar(sm, ax=ax, orientation='vertical', label=data_labels[3])

# Finalize and save image
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/84_202312301731.png")
plt.cla()
plt.clf()
plt.close('all')
