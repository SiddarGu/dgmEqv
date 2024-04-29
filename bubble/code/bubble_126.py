import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data = np.array([[300, 15, 65, 80], [250, 20, 70, 85], [200, 12, 75, 80], [220, 18, 72, 82], [150, 10, 70, 75], [180, 16, 77, 90], [210, 14, 80, 85]])
data_labels = ["Research Funding (Million $)", "Number of Scholars (Thousands)", "Global Influence (Score)", "Social Impact (Score)"]
line_labels = ["Anthropology", "Sociology", "Philosophy", "History", "Linguistics", "Performance Art", "Literature"]

fig, ax = plt.subplots(figsize=(14, 10))
cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
s = (data[:, 2] - min(data[:, 2]))/(max(data[:, 2]) - min(data[:, 2]))*4400 + 600

for i in range(len(data)):
    line_label = f"{line_labels[i]} {data[i, 2]}"
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], color=color, s=s[i])
    ax.scatter([], [], c=color, alpha=0.6, s=20, label=line_label)

plt.title('Research Status in Social Sciences and Humanities Fields')
plt.xlabel(data_labels[0], wrap=True)
plt.ylabel(data_labels[1], wrap=True)
ax.legend(title=data_labels[2], loc='upper left')

sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/287_202312310045.png")
plt.clf()
