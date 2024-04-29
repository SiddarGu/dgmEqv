
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cm

data_labels = ["Revenue (Billion $)", "Employees", "Market Share (%)", "Investment (Billion $)"]
line_labels = ["Google", "Amazon", "Apple", "Microsoft", "Tesla"]
data = np.array([[150, 128000, 45, 10],
                 [250, 450000, 30, 20],
                 [300, 130000, 35, 15],
                 [200, 150000, 20, 25],
                 [50, 40000, 10, 5]])

# plot the data with the type of bubble chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# normalize the data
norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = cm.viridis
m = cm.ScalarMappable(norm=norm, cmap=cmap)

# plot the scatter points
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*20, c=m.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], c=m.to_rgba(data[i, 3]), label=line_labels[i]+" "+str(data[i, 3]))

# plot legend and colorbar
ax.legend(title=data_labels[2])
cb = fig.colorbar(m, ax=ax)
cb.set_label(data_labels[3])

# set the title, labels and other parameters
plt.title("Financial Performance of the Top Tech Companies in 2023")
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid()

# adjust the figure
plt.tight_layout()

# save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/8_2023122261440.png")

# clear the current image state
plt.clf()