import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.ticker import MaxNLocator

# Parse data
data_raw = '''Government Agency,Budget Allocation (Billion $),Policy Impact (Score),Number of Employees,Public Satisfaction (Score)
Department of Defense,700,90,2.8,70
Department of Health & Human Services,1100,85,1.0,80
Department of Education,65,80,0.4,90
Department of Transportation,100,70,0.6,80
Department of Treasury,550,75,1.2,70
Department of Agriculture,150,60,1.5,75
Department of Commerce,60,65,0.5,85'''

# Convert data to matrix format
data_raw_lines = data_raw.split("\n")
data_labels = data_raw_lines[0].split(",")
data_values = [line.split(",") for line in data_raw_lines[1:]]
data = np.array(data_values)[:, 1:].astype(float)
line_labels = [data_values[i][0] for i in range(len(data_values))]
line_labels = [f"{name} ({impact})" for name, impact in zip(line_labels, data[:, 2])]

# Initialize plot and color map
fig, ax = plt.subplots(figsize=(12, 8))
my_cmap = plt.get_cmap("viridis")

# Create scatter plot
scatter = ax.scatter(data[:, 0], data[:, 1], s=600 + 4400 * (data[:, 2] - min(data[:, 2])) / (max(data[:, 2]) - min(data[:, 2])),
                     c=data[:, 3], cmap=my_cmap, edgecolors='black', linewidths=1, alpha=0.75)

# Create legend
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=my_cmap(Normalize(min(data[:, 3]), max(data[:, 3]))(data[i, 3])),
               s=20, label=line_label, alpha=0.75)

ax.legend(title=data_labels[2], loc='upper left')

# Create color bar
cbar = plt.colorbar(ScalarMappable(norm=Normalize(min(data[:, 3]), max(data[:, 3])), cmap=my_cmap), ax=ax)
cbar.set_label(data_labels[3])

# Set axes labels
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.grid(True)

# Set title
plt.title('Budget Allocation and Public Satisfaction - Government Agencies 2023')

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/107_202312301731.png')
plt.clf()
