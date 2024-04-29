
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

data_labels = ["Graduation Rate(%)","Dropout Rate(%)","Student Retention(%)","Overall Score(out of 10)"]
line_labels = ["Harvard University","Stanford University","Massachusetts Institute of Technology",
               "University of California, Berkeley","University of Cambridge"]
data = np.array([[95,2,90,9.5],
                 [90,3,85,9.0],
                 [87,4,82,8.5],
                 [85,5,80,8.0],
                 [83,6,78,7.5]])

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Plot data
for i in range(data.shape[0]):
    # Normalize color
    color = (data[i, 3] - data[:, 3].min()) / (data[:, 3].max()-data[:, 3].min())

    # Normalize bubble size
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max()-data[:, 2].min()) * (3000-600) + 600

    # Plot data
    ax.scatter(data[i, 0], data[i, 1], c=cm.RdYlGn(color), s=size, label=None)
    ax.scatter([], [], c=cm.RdYlGn(color), s=20, label=line_labels[i] + ' ' + data_labels[2] + ': ' + str(data[i, 2]))

# Plot legend
ax.legend(title=data_labels[2])

# Plot colorbar
sm = cm.ScalarMappable(cmap=cm.RdYlGn, norm=plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, fraction=0.03)
cbar.set_label(data_labels[3], rotation=90)

# Adjust parameters
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
fig.suptitle('Academic Performance of Elite Institutions in Education')
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/2_2023122261440.png')

# Clear figure
plt.close(fig)