import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

csv_data = '''Super Bowl,100,400,9,8,4
Olympics,500,1000,10,9,5
World Cup,200,600,8,9,3
NBA Finals,50,200,7,7,2
Wimbledon,30,100,6,8,1'''

data_labels = ['Event', 'Attendance (Thousands)','Revenue (Million $)', 
               'Media Coverage (Score)', 'Player Performance (Score)', 'Team Value (Billion $)']

lines = csv_data.split('\n')
line_labels = [line.split(',')[0] for line in lines]
raw_data = [list(map(float, line.split(',')[1:])) for line in lines]
data = np.array(raw_data)

fig, ax = plt.subplots(figsize=(10, 6))
colors = Normalize(data[:, 3].min(), data[:, 3].max())(data[:, 3])
plt.scatter(data[:, 0], data[:, 1], c=colors, s=data[:,2]*1000, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=1, label=None)
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label= f"{line_label} "+ str(data[i, 2]))
plt.legend(title=data_labels[2])
ax.grid(True)

cbar = plt.colorbar(cm.ScalarMappable(norm=Normalize(data[:, 3].min(), data[:, 3].max()), cmap='viridis'))
cbar.set_label(data_labels[3])
plt.title('Analysis of Sports and Entertainment Events')
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[2])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/361_202312311429.png')
plt.clf()
