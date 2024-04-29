import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable

# Parsing data
raw_data = """Medicine,230,60,200,8.5
Engineering,400,50,150,8.7
Humanities,320,40,100,9.0
Business,600,40,130,8.0
Fine Arts,150,30,80,9.4
Computer Science,500,45,160,8.8
Social Sciences,350,35,90,9.1"""
lines = raw_data.split("\n")

# Transform data
data_labels = ['Number of Graduates (thousands)', 'Average Tuition (thousands $)',
               'Average Salary after Graduation (thousands $)', 'Satisfaction Score (out of 10)']
line_labels = [f"{line.split(',')[0]} {line.split(',')[2]}" for line in lines]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines])

# Create figure
fig, ax = plt.subplots(figsize=(10, 10))

# Normalize bubble size and color
colors = (data[:,3]-data[:,3].min())/(data[:,3].max()-data[:,3].min())
sizes = 600 + 4400*((data[:,2]-data[:,2].min())/(data[:,2].max()-data[:,2].min()))

for i in range(len(data)):
    # Plot each data point
    ax.scatter(data[i, 0], data[i, 1], c=plt.cm.jet(colors[i]), s=sizes[i], label=None)
    # Scatter an empty point
    ax.scatter([], [], c=plt.cm.jet(colors[i]), s=20, label=line_labels[i])

# Legend
ax.legend(title=data_labels[2], bbox_to_anchor=(1.05, 1), loc='upper right')

# Color bar
sm = ScalarMappable(cmap=plt.cm.jet, norm=plt.Normalize(vmin=0, vmax=10))
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Labels and grid
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Graduates Jobs Satisfaction and Earnings Based on Field of Study")
fig.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/59_202312301731.png")

# Clear figure
plt.clf()
