import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

raw_data = '''Department,Number of Employees,Average Job Satisfaction (Scale 1-10),Annual Turnover Rate (%),Recruitment Budget (in thousands $)
Human Resources,200,7.5,15,300
Marketing,600,8,12,500
Sales,1000,8.5,10,600
IT,300,7,20,450
Operations,1200,8.3,8,700
Finance,400,7.2,18,350
Research and Development,500,8.7,7,400'''

# Data processing
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] + ' ' + line.split(',')[3] for line in lines[1:]]
raw_values = [list(map(float, line.split(',')[1:])) for line in lines[1:]]
data = np.array(raw_values)

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Normalize color and size
size_scale = mcolors.Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
color_scale = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

# Scatter plotting
for i in range(len(data)):
    line_label = line_labels[i]
    size = 600 + 4400*size_scale(data[i,2])
    color = plt.cm.viridis(color_scale(data[i,3]))
    ax.scatter(data[i,0], data[i,1], s=size, c=[color], label=None)
    ax.scatter([], [], c=[color], label=line_label)

# Legend
ax.legend(title=data_labels[2])

# Color bar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max()))
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

plt.title('Employee Management Analysis in Different Departments')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/90_202312301731.png')
plt.clf()
