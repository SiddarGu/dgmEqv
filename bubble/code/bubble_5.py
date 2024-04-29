
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

data_labels = ["Research Investment (Billion $)", "Patent Applications (Thousands)", "Innovations (Score)", "Engineering Graduates (Thousands)"]
data = [[25, 500, 8.5, 3.2], [20, 400, 7.6, 2.4], [15, 300, 7.2, 2.6], [10, 200, 6.9, 1.8], [5, 100, 6.4, 1.2]]
line_labels = ["Machine Learning", "Artificial Intelligence", "Robotics", "Quantum Computing", "Biometrics"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

for i in range(len(data)):
    cNorm = colors.Normalize(vmin=min([item[3] for item in data]), vmax=max([item[3] for item in data]))
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cm.get_cmap("Greens"))
    ax.scatter(data[i][0], data[i][1], c=scalarMap.to_rgba(data[i][3]), s=data[i][2]/max([item[2] for item in data])*1000+600, label=None)
    ax.scatter([], [], c=scalarMap.to_rgba(data[i][3]), s=20, label=line_labels[i]+" "+data_labels[2]+str(data[i][2]))

ax.legend(title=data_labels[2], loc="upper left")
scalarMap.set_array(data)
cbar = fig.colorbar(scalarMap, ax=ax)
cbar.ax.set_title(data_labels[3])

ax.set_title("Advances in Science and Engineering - The Impact of Research Investment")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.grid()
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/2_2023122270050.png")
plt.clf()