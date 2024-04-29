import matplotlib.pyplot as plt
import numpy as np

# Process data
raw_data = """Policy Area,Q1,Q2,Q3,Q4
Public Health,80,82,84,86
Education,85,87,89,91
Infrastructure,75,77,79,81
Security,90,92,94,96
Economic Policy,70,72,74,76"""
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [l.split(',')[0] for l in lines[1:]]
data = np.array([list(map(int, l.split(',')[1:])) for l in lines[1:]])

# Prepate figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Normalize to adjust chart
normalize = lambda data: np.concatenate((data, [data[0]]))
max_data = np.max(data)
num_vars = len(data_labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)
data = np.apply_along_axis(normalize, 1, data)

# Iterate over each "line" or set of values
for i, row in enumerate(data):
    color = plt.cm.viridis(i / len(data))  
    ax.plot(angles, row, color=color, linewidth=2, label=line_labels[i])  
    ax.fill(angles, row, color=color, alpha=0.25)  

# Verbatim application of your pseudocode handles the plotting of gridlines
for i, _ in enumerate(data):
    radius = np.full_like(angles, (i+1) * max_data / len(data))
    ax.plot(angles, radius, color='silver', alpha=0.6)

ax.set_thetagrids(np.degrees(angles[:-1]), data_labels, wrap=True)
ax.set_ylim(0, max_data)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.legend(*ax.get_legend_handles_labels(), loc='upper right')

plt.title('Government Policy Performance Review', size=20, pad=30)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/96_2023122292141.png', dpi=300)
plt.clf()
