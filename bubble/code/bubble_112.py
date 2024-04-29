import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Parsing data
raw_data = 'University,Number of Students (Thousands),Courses Offered,Graduation Rate (%),Research Funding (Million $)\n\
Harvard,20,4000,98,680\n\
Stanford,16,3800,95,560\n\
Oxford,23,4200,96,690\n\
Cambridge,18,3900,97,660\n\
Yale,12,3700,96,580\n\
MIT,11,4000,94,700\n\
University of Chicago,14,3500,95,520\n\
Princeton,8,3300,97,600'
lines = raw_data.split('\n')

data_labels = lines[0].split(',')
rows = [line.split(',') for line in lines[1:]]
line_labels = [row[0] + " " + str(row[3]) for row in rows]
data = np.array([[int(value) for value in row[1:]] for row in rows])

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title('Comparative Analysis of Top Universities across Key Academic Parameters')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

ax.legend(title=data_labels[2], loc='lower right')

# Colorbar
colorbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='viridis'), ax=ax)
colorbar.set_label(data_labels[3])

# Axis labels
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# Adjust display
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/239_202312310045.png')
plt.clf()
