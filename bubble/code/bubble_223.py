
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ['Average Home Price (Million $)', 'Housing Availability (Score)', 'Population (Millions)', 'Rent to Buy Ratio']
line_labels = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Dallas']
data = np.array([[1.2, 7, 8.5, 3.2],
                 [1.5, 5, 3.8, 3.8],
                 [0.8, 8, 2.7, 4],
                 [0.9, 7, 2.3, 3.4],
                 [0.7, 8, 1.6, 4.2],
                 [0.8, 8, 1.3, 3.5]])

original_data = data.copy()
# normalize data
data[:, 2] = (data[:, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) * (5000 - 600) + 600
data[:, 3] = (data[:, 3] - np.min(data[:, 3])) / (np.max(data[:, 3]) - np.min(data[:, 3]))

# plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# plot bubble
for i in range(len(data)):
    cmap = cm.get_cmap('RdYlBu')
    color = cmap(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2], c=color, label=None)
    
    # add empty point for legend
    ax.scatter([], [], c=color, label=line_labels[i] + ": " + str(original_data[i, 2]), s=20)

# plot legend
ax.legend(title=data_labels[2])

# plot colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=np.min(original_data[:, 3]), vmax=np.max(original_data[:, 3])))
sm.set_array([])
plt.colorbar(sm, label=data_labels[3], shrink=0.7, aspect=20)

# set background grid
ax.grid(linestyle='-', linewidth=0.2, color='#cccccc')

# axis label
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# set figure title
ax.set_title('Real Estate Prices and Housing Market - US Cities 2023')

# adjust the figure
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/9_2023122261440.png')

# clear current figure
plt.clf()