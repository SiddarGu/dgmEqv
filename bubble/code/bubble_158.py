import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import numpy as np

# Transform the data
data_str = 'Harvard,22,4,40,90 Stanford,16,3,27,85 Oxford,24,5,6,88 Cambridge,19,4,7,89 MIT,11,3,16,92 Yale,13,2,30,87 Princeton,8,1,26,86 Chicago,15,2,8,84'
data_list = [item.split(',') for item in data_str.split()]
data = np.array([[float(val) for val in sublist[1:]] for sublist in data_list])
data_labels = ['Enrollment (Thousands)', 'Faculty (Thousands)', 'Endowment (Billion $)', 'Research Output (Score)']
line_labels = [item[0] + ' ' + str(item[1][2]) for item in zip([sublist[0] for sublist in data_list], data)]

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define color map
cmap = plt.get_cmap("tab10")

# Normalize data for color mapping
norm = mplc.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

for i, line_label in enumerate(line_labels):
    # Plot data with plt.scatter
    ax.scatter(data[i, 0], data[i, 1], 
              s=600 + 4400 * (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()), 
              c=cmap(norm(data[i, 3])), 
              alpha=0.6, 
              edgecolors='w', 
              linewidth=2, 
              label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), alpha=0.6, s=20, label=line_label)

# Add a colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

# Legend
ax.legend(loc='upper left', title=data_labels[2])

# Labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Comparison of Top Universities in terms of Enrollment, Faculty, Endowment, and Research Output')

# Grid
ax.grid(True)
fig.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/176_202312310045.png')

# Clear the current image state
plt.clf()
