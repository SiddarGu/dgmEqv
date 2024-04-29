
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Transform data into three variables
data_labels = ['Carbon Dioxide (Million Tonnes)', 'Methane (Million Tonnes)', 'Nitrous Oxide (Million Tonnes)', 'Environmental Impact (Score)']
line_labels = ['Transportation', 'Energy Production', 'Agriculture', 'Manufacturing', 'Households']
data = np.array([[1000, 25, 60, 400],
                 [1500, 50, 80, 600],
                 [700, 30, 40, 300],
                 [500, 20, 30, 200],
                 [200, 10, 20, 100]])

# Create figure and plot data
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Normalize data
cmap = cm.get_cmap('RdYlBu_r')
norm = plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
sizes = np.linspace(600, 5000, data.shape[0])

# Scatter plot of data
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=line_labels[i] + ' (' + str(data[i, 2]) + ')', s=20)

# Legend
ax.legend(title=data_labels[2])

# Color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, ticks=np.linspace(min(data[:, 3]), max(data[:, 3]), 5)).set_label(data_labels[3], rotation=90)

# Set parameters
ax.grid(True, linestyle='-.')
ax.set_xlabel('Emission')
ax.set_ylabel('Methane (Million Tonnes)')
# Save image
fig.suptitle('Global Emission and Environmental Impact by Source')
fig.tight_layout()

fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/6.png')

# Clear figure
plt.clf()