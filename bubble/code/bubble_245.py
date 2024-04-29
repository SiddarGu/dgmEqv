import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from sklearn.preprocessing import MinMaxScaler

# Processing raw data
raw_data = """
Policy Area,Operating Cost (Billion $),Societal Impact (Score),Public Opinion (% Approval),Policy Robustness (Score)
Health,500,95,90,100
Education,300,90,85,90
Defense,800,85,65,100
Infrastructure,400,80,78,95
Environment,200,92,98,85
Social Protection,350,80,80,80
Economic Affairs,450,88,87,90
"""

# Extracting and scaling data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in lines[1:]], dtype=float)
line_labels = [line.split(',')[0] for line in lines[1:]]

# Scaling the color and size
colors = MinMaxScaler().fit_transform(data[:, 3].reshape(-1, 1)).ravel()
sizes = MinMaxScaler((200, 2000)).fit_transform(data[:, 2].reshape(-1, 1)).ravel()
cmap = mpl.cm.get_cmap('viridis')

# Creating the scatter plot
fig, ax = plt.subplots(figsize=(16, 8))
scatter = ax.scatter(data[:, 0], data[:, 1], c=colors, cmap=cmap, s=sizes, label=None)

# Adding legend
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], label=f"{line_label} ({int(data[i, 2])}%)", color=cmap(colors[i]), s=100)
ax.legend(title="Public Opinion (% Approval)")

# Labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Government and Public Policy: Impact and Cost across Different Areas')

# Colorbar for societal impact
norm = mpl.colors.Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
cbar = plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
cbar.set_label(data_labels[3])

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/207_202312310045.png')
plt.clf()
