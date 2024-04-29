import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data_string = """
Country,Defense Budget (Billion $),Education Budget (Billion $),Healthcare Budget (Billion $),Social Welfare Score
USA,650,70,1200,75
China,250,200,800,70
Russia,48,80,200,63
India,66,83,130,67
UK,55,102,250,78
Germany,45,100,360,81
Brazil,27,50,180,68
"""

data_lines = data_string.strip().split("\n")
data_labels = data_lines[0].split(",")[1:]
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)
line_labels = ["{} - {}".format(line.split(",")[0], line.split(",")[3]) for line in data_lines[1:]]

fig, ax = plt.subplots(figsize=(10, 10))
norm_colors = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
norm_sizes = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())

mappable = ScalarMappable(norm=norm_colors)
colorbar = plt.colorbar(mappable)
colorbar.set_label(data_labels[3])

for i in range(len(line_labels)):
    ax.scatter(data[:, 0][i], data[:, 1][i], s=600 + 5000 * norm_sizes(data[i, 2]), c=mappable.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], color=mappable.to_rgba(data[i, 3]), label=line_labels[i])
    
ax.legend(title=data_labels[2])
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Comparison of Policy Expenditure by Country - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/150_202312301731.png')
plt.close(fig)
