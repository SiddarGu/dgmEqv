import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data = '''Lawsuit Type,Number of Lawsuits (Thousands),Average Resolutions Time (Days),Winning Percentage (%),Economic Impact (Million $)
Personal Injury,300,200,40,300
Product Liability,250,180,35,250
Medical Malpractice,200,300,30,800
Employment Discrimination,400,150,50,400
Patent Infringement,100,400,25,600
Copyright Infringement,150,200,45,500'''

# Transform raw data into numpy array
data = np.array([x.split(',') for x in data.split('\n')][1:], dtype=object)
data[:, 1:5] = data[:, 1:5].astype(float)

data_labels = ['Number of Lawsuits (Thousands)', 'Average Resolutions Time (Days)', 'Winning Percentage (%)', 'Economic Impact (Million $)']
line_labels = [f'{x[0]} {x[3]}' for x in data]
data = data[:, 1:].astype(float)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

ax.set_title('Economic Performance of Various Lawsuit Types in 2023')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

# Add a color bar
sm = ScalarMappable(norm=norm, cmap='viridis')
fig.colorbar(sm, ax=ax, label=data_labels[3])

ax.legend(title=data_labels[2], loc='upper left')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/324_202312310045.png")
plt.show()
plt.clf()
