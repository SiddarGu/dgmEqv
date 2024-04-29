

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Transform data
data_labels = ["Student Enrollment (Thousands)", "Graduate Rate (%)", "Research Funding (Million $)", "Rating (Score)"]
data = np.array([[25,90,500,100], [20,85,400,90], [15,95,320,95], [10,92,250,80], [8,87,200,85], [7,94,180,90]])
line_labels = ["Harvard University", "Stanford University", "Massachusetts Institute of Technology", "University of California, Berkeley", "Cornell University", "Princeton University"]

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Normalize color
cmap = plt.get_cmap("tab20")
norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))

# Scatter each line
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) * (5000 - 600) + 600, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i, 3])), label=line_labels[i] + f' {data[i, 2]}')

# Configure legend
ax.legend(title=data_labels[2], loc="upper right")

# Color bar
sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cb = fig.colorbar(sm, ax=ax)
cb.set_label(data_labels[3])

# Configure axes
ax.set_title("Education Performance Across Major Institutions in the US")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Other settings
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/5.png")
plt.close()