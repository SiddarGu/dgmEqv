import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

data_raw = '''Policy,Public Support (%),Implementation Cost (Billion $),Effectiveness (Score),Public Awareness (Score)
Healthcare Reform,65,500,90,80
Environmental Policies,75,300,70,75
Education Reform,80,600,95,90
Tax Regulation,60,400,85,55
Immigration Policies,70,200,80,60
Defence Strategies,50,700,75,50'''

data_lines = data_raw.split("\n")
data_labels = data_lines[0].split(",")[1:]
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)
line_labels = [line.split(",")[0] + " " + str(data[i, 2]) for i, line in enumerate(data_lines[1:])]

fig, ax = plt.subplots(figsize=(14, 10))

colors = data[:, 3]
norm = mcolors.Normalize(vmin=colors.min() - 10, vmax=colors.max())
cmap = plt.get_cmap("YlOrRd")

bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], label=None,
               c=cmap(norm(data[i, 3])),
               s=bubble_sizes[i],
               alpha=0.6, edgecolors="w")
    ax.scatter([], [], label=line_labels[i], s=20, c=cmap(norm(data[i, 3])))

ax.legend(title=data_labels[2], loc="lower left", fancybox=True)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, pad=0.02, aspect=50).set_label(data_labels[3])
ax.grid(True)

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.title('Public Perception and Impact of Various Government Policies')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/154_202312310045.png')
plt.clf()
