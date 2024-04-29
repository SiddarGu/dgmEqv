import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Parsing data
raw_data = """Policy,Number of Beneficiaries (Millions),Government Spending (Billion $),Effectiveness (Score),Public Satisfaction (Score)
Universal Healthcare,330,1000,85,78
Social Security,60,750,90,80
Public Education,75,500,70,75
Infrastructure Investment,100,700,75,70
Environmental Protection,200,600,80,76
Defense Spending,150,800,88,72
Digitalisation,250,400,73,80"""

raw_data = raw_data.split('\n')
data_labels = raw_data[0].split(',')[1:]
raw_values = [row.split(',') for row in raw_data[1:]]

# Transform data to required format
line_labels = [f'{row[0]} - {row[2]}' for row in raw_values]
data = np.array([[float(val) for val in row[1:]] for row in raw_values])

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Normalize size and color data
norm_size = Normalize(vmin=np.min(data[:, 2]), vmax=np.max(data[:, 2]))
norm_color = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))

# Plotting data
colors = plt.cm.viridis(norm_color(data[:, 3]))
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], label=None, s=norm_size(data[i, 2]) * 5000 + 600, c=colors[i])
    ax.scatter([], [], c=colors[i], label=line_labels[i], s=20)


ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)
ax.legend(title=data_labels[2], loc='upper left')

sm = ScalarMappable(cmap='viridis', norm=norm_color)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])

plt.tight_layout()
plt.title("Evaluation of Various Government Policies", fontsize=15)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/166_202312310045.png')
plt.clf()
