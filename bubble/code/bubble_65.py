import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Initialize the data
data_labels = ['Global Cases (Millions)', 'Death Rate (%)', 'Treatment Cost (Billion $)', 'Research Funding (Billion $)']
data = np.array([[14, 26, 500, 200],
                 [422, 15, 250, 150],
                 [17.9, 31, 300, 180],
                 [1000, 39, 200, 100],
                 [38, 48, 150, 90],
                 [50, 28, 290, 120]])
line_labels = ['Cancer', 'Diabetes', 'Heart Disease', 'Respiratory Diseases', 'HIV/AIDS', 'Dementia']

# Normalize values for colors and sizes
colors = Normalize(min(data[:,3]), max(data[:,3]))(data[:,3])
sizes = Normalize(min(data[:,2]), max(data[:,2]), clip=True)(data[:,2]) * (5000 - 600) + 600

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")

# Plot data
for i, line_label in enumerate(line_labels):
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], color=color, alpha=0.6, edgecolors='w', linewidth=2, label=None)
    ax.scatter([], [], color=color, s=20, label=line_label + ': {}'.format(data[i, 2]))

# Add color bar
sm = ScalarMappable(Normalize(min(data[:,3]), max(data[:,3])), cmap='viridis')
sm.set_array([])
fig.colorbar(sm, label=data_labels[3], pad=0.1)

# Set legend and labels
ax.legend(title=data_labels[2], loc='lower right')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set grid and title
ax.grid(True)
plt.title('Global Impact of Major Diseases on Healthcare Costs and Research Funding', pad=20)

# Adjust layout and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/155_202312310045.png', bbox_inches='tight')

# Clear the figure
plt.clf()
