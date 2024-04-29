import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_raw = [['Health Reform', 70, 85, 200, 500],
            ['Immigration Reform', 60, 80, 100, 700],
            ['Education Reform', 80, 90, 150, 600],
            ['Climate Change Policies', 75, 80, 130, 400],
            ['Welfare Services', 85, 90, 250, 300],
            ['Defense Spending', 70, 75, 80, 700]]
            
data_labels = ["Approval Rate (%)", "Efficiency (Score)", "Affected Population (Millions)", "Bureaucratic Complexity (Score)"]
data = np.array([item[1:] for item in data_raw])
line_labels = [f"{item[0]} {item[3]}" for item in data_raw]

# Normalize color and size
norm_color = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
norm_size = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
cmap = cm.get_cmap('viridis')

for i, line_label in enumerate(line_labels):
    color = cmap(norm_color(data[i, 3]))
    size = norm_size(data[i, 2]) * (5000 - 600) + 600
    ax.scatter(data[i, 0], data[i, 1], s=size, c=[color], label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], c=[color], s=20, label=line_label)

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

legend_title = data_labels[2]
ax.legend(title=legend_title, loc="upper left")

sm = cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
sm.set_array([])
fig.colorbar(sm, alpha=0.6, label=data_labels[3])

plt.grid(True)
plt.title("Efficiency and Impact of Various Government Policies")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/249_202312310045.png")

plt.clf()
