import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase
from matplotlib.cm import get_cmap

# transform given data into three variables
data_labels = ['Healthcare Spending (Billion $)', 'Education Spending (Billion $)', 'Military Spending (Billion $)', 'Citizen Satisfaction (Score)', 'Environmental Conservation (Score)']
line_labels = ['USA', 'China', 'Germany', 'UK', 'Japan', 'Australia', 'Brazil', 'India']
data = np.array(
    [
        [3600, 900, 750, 70, 60],
        [650, 200, 250, 65, 55],
        [450, 150, 45, 75, 70],
        [200, 50, 55, 80, 75],
        [350, 105, 45, 80, 65],
        [100, 35, 25, 85, 75],
        [75, 20, 35, 60, 55],
        [50, 25, 55, 55, 50]
    ]
)

# normalize color and size data to cmap and size ranges
color = (data[:, 3]-data[:, 3].min())/(data[:, 3].max()-data[:, 3].min())
size = 600 + (data[:, 2]-data[:, 2].min())*(5000-600)/(data[:, 2].max()-data[:, 2].min())

# create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# scatter plot
scatter = ax.scatter(data[:, 0], data[:, 1], c=color, s=size, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=1, label=None)
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], color=get_cmap("viridis")(color[i]), label=line_label+'\n'+str(data[i, 2]))

# more settings
ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)
plt.xlabel(data_labels[0], wrap=True)
plt.ylabel(data_labels[1], wrap=True)
plt.title("Public Policy Investment and Performance Across Countries")

# color bar
cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cb = ColorbarBase(cax, cmap='viridis', norm=norm, orientation='vertical')
cb.set_label(data_labels[3])

# save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/178_202312310045.png', bbox_inches='tight')
plt.clf()
