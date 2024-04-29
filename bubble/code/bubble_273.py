import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib import ticker
import numpy as np

data_raw = [
    ["State Grid Corporation of China", 330, 1288, 400, 0.8],
    ["Duke Energy", 22.75, 9.2, 220, 1.1],
    ["EDF Energy", 71, 37.5, 550, 0.9],
    ["Exelon Corporation", 33.5, 10.9, 215, 1],
    ["PG&E", 16.76, 5.6, 150, 0.7],
    ["Enel", 80.32, 62.93, 260, 1.4],
    ["Georgia Power", 8.8, 2.6, 141, 0.6],
    ["Florida Power & Light", 16.55, 5.1, 162, 0.5]
]

data_labels = ["Annual Revenue (Billion $)", "Customers Service (Millions)", "Energy Production (Million MWH)", "Emission Rate (Metric Tonnes CO2e/MWh)"]
data = np.array(data_raw)[:, 1:].astype(float)
line_labels = [(name + " " + str(cust)) for name, cust in zip(np.array(data_raw)[:, 0], data[:, 2])]

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.grid(True, linewidth=0.5, linestyle="--", color='black')
plt.title('Comparative Analysis of Major Utility Companies - Energy & Utilities 2023')

ax.get_xaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax.get_yaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/69_202312301731.png", dpi=300)
plt.clf()

