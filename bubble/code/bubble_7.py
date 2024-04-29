
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors
import numpy as np

data_labels = ["Price (Million $)", "Number of Houses", "Area (Million Square Meters)", "Market Performance (Score)"]
data = np.array([[2.5, 50, 3, 7],
                 [1.5, 60, 2, 8],
                 [1.3, 40, 2.5, 6],
                 [1.2, 30, 1.5, 9],
                 [3, 20, 4, 7]])

line_labels = ["Single Family Homes", "Apartments", "Townhouses", "Condos", "Vacation Homes"]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
cm = plt.cm.get_cmap('RdYlBu')

# normalize the color value
norm = mpl.colors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

# normalize the bubble size
s_m = mpl.cm.ScalarMappable(cmap=cm, norm=norm)
s_m.set_array([])

# plot the bubble chart
for i in range(data.shape[0]):
    # plot the bubble
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*1000+60, c=cm(norm(data[i, 3])), label=None)
    # plot an empty point with the same color
    ax.scatter([], [], c=cm(norm(data[i, 3])), label=line_labels[i] + f' {data[i, 2]}')

# legend
ax.legend(title=data_labels[2])
# color bar
fig.colorbar(s_m, ax=ax, label=data_labels[3])

# other settings
ax.set_title("Housing Market Performance by Property Type in 2021")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/42_2023122270050.png')

plt.cla()