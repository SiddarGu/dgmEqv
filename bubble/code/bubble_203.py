
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data = np.array([['Location', 'Home Prices (Thousand $)', 'Rent Prices (Thousand $)', 'Mortgage Rates (%)', 'Affordability Index (Score)'],
                 ['New York', 1300, 800, 3.2, 7],
                 ['San Francisco', 1200, 700, 3.6, 6],
                 ['Los Angeles', 1000, 650, 3.8, 5],
                 ['Chicago', 850, 500, 3.4, 7],
                 ['Houston', 750, 400, 3.1, 8],
                 ['Miami', 900, 550, 3.5, 6]])
data_labels = data[0, 1:]
line_labels = data[1:, 0]

data = data[1:, 1:].astype(float)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

cmap = cm.get_cmap('RdYlGn_r')

bmin, bmax = np.min(data[:, 3]), np.max(data[:, 3])
smin, smax = 3, 4
norm = plt.Normalize(vmin = smin, vmax = smax)
norm_c = plt.Normalize(vmin = bmin, vmax = bmax)
bc = cmap(norm_c(data[:, 3]))
sc = norm(data[:, 2]) * 5000 + 600

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s = smin + (smax-smin)*sc[i], c = bc[i], label = None)
    ax.scatter([], [], c = bc[i], label = line_labels[i] + f' {data[i, 2]}')

ax.legend(title=data_labels[2], loc='lower right')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm._A = []
plt.colorbar(sm, ax=ax, orientation='horizontal', fraction=0.04, pad=0.08).set_label(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Location-wise Analysis of Real Estate and Housing Market Prices and Rates', fontsize=12, wrap=True, rotation=0)
plt.grid(ls='--')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/29_2023122270050.png')

plt.clf()