import numpy as np
import matplotlib.pyplot as plt

# Convert the raw data into the specific format
raw_data = [
    "Psychology,1500,8000,120",
    "Sociology,1300,7500,150",
    "Philosophy,1000,5000,60",
    "Historical Studies,800,3000,40",
    "Linguistics,1800,8500,200"
]

y_values = ["Number of Research Papers", "Number of Citations", "Number of Patents Awarded"]
x_values = []
data = []

for line in raw_data:
    parts = line.split(',')
    x_values.append(parts[0])
    data.append([np.float32(value) for value in parts[1:]])

data = np.array(data)

# Plot the 3D bar chart
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(projection='3d')

bar_width = 0.4
bar_depth = 0.5
colors = ['r', 'g', 'b']

for i in range(len(y_values)):    
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              bar_width, bar_depth, data[:, i], color=colors[i%len(colors)], alpha=0.7)

ax.set_title('Contribution and Impact in Social Sciences and Humanities Research Fields')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30, horizontalalignment='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.view_init(elev=20., azim=-35)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/170_202312302235.png', bbox_inches='tight')
plt.clf()
