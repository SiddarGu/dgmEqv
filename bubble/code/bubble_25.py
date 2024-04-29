
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np 

data_labels = ['Sentence (Years)', 'Recidivism Rate (%)', 'Victim Impact (Score)', 'Law Enforcement Impact (Score)']
line_labels = ['Robbery', 'Burglary', 'Assault', 'Drug Trafficking', 'Money Laundering']
data = np.array([[8, 13, 85, 100], [4, 8, 90, 90], [3, 15, 95, 80], [20, 17, 75, 95], [10, 5, 80, 100]])

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot()

# Normalize the color values
norm = Normalize(vmin=min(data[:, 3]) - 10, vmax=max(data[:, 3]))

# Normalize the bubble size
size_norm = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
size_mapper = cm.ScalarMappable(norm=size_norm, cmap=cm.Blues)

# Plot the data
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=size_norm(data[i, 2]) * 5000 + 600, c=cm.Blues(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cm.Blues(norm(data[i, 3])), label=f'{line_labels[i]} {data[i, 2]}')

# Plot the legend
ax.legend(title=data_labels[2])

# Color bar
sm = cm.ScalarMappable(cmap=cm.Blues, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation='vertical', pad=0.01)
cbar.set_label(data_labels[3])

# Other settings
ax.set_title('Impact of Laws and Sentencing on Crime and Its Victims')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=.3)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/40_2023122261326.png')
plt.close()