import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Parse data
raw_data = '''Sociology,180,400,2.5,-2,80
Philosophy,120,350,3.0,0,75
History,160,500,3.2,1,85
Psychology,220,600,3.5,4,90
Literature,140,300,2.7,-3,80
Linguistics,80,200,2.0,-1,70
Anthropology,100,250,2.3,0,76'''

data_labels = ['Number of Students (Thousands)', 'Number of Journals Published', 
               'Impact Factor', '% of change in popularity from last year', 'Employability Rate (%)']

rows = [r.split(',') for r in raw_data.split('\n')]
line_labels = [r[0] for r in rows]
data = np.array([list(map(float, r[1:])) for r in rows])

# Plot data
fig, ax = plt.subplots(figsize=(12, 8))
cmap = cm.get_cmap('viridis')

for i, line_label in enumerate(line_labels):
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())
    size = 600 + size * 5000
    color = (data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())
    ax.scatter(data[i, 0], data[i, 1], label=None, c=cmap(color), s=size, alpha=0.6, edgecolors='w')
    ax.scatter([], [], label=line_label+' '+str(data[i, 2]), c=cmap(color), s=20)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(min(data[:, 3]), max(data[:, 3])))
sm._A = []
plt.colorbar(sm, label=data_labels[3])

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.title('Popularity, Impact, and Employability in Social Sciences and Humanities fields 2023')
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/192_202312310045.png')
plt.clf()
