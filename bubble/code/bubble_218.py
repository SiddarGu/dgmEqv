import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.cm import ScalarMappable

# Process the data
raw_data = '''Department,Employee Count,Average Age,Average Salary ($),Employee Satisfaction (Score)
HR,120,35,65000,8
Finance,150,40,75000,7
Sales,200,32,70000,9
IT,180,38,80000,8 
Marketing,100,32,72000,9 
Operations,300,37,67000,8'''

lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in lines[1:]], dtype=float)
line_labels = [line.split(',')[0]+str(data[i, 2]) for i, line in enumerate(lines[1:])]

# Normalize the values for colors and sizes
sizes = 600 + (data[:, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * (5000 - 600)
colors = (data[:, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())

# Create a new figure
fig = plt.figure(figsize=(16,10))

# Bubble plot
ax = fig.add_subplot()
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], color=mcolors.rgb2hex(plt.get_cmap('viridis')(colors[i])), label=None, edgecolors='w')
    ax.scatter([], [], label=line_labels[i], color=mcolors.rgb2hex(plt.get_cmap('viridis')(colors[i])), s=20)

# Legend
ax.legend(title=data_labels[2])

# Colorbar
sm = ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical', label=data_labels[3])

# Labels, title and grids
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Employee Management: Salary and Satisfaction across Various Departments')
ax.grid(True)

# Save the figure
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/218_202312310045.png')
fig.clear()
plt.close(fig)
