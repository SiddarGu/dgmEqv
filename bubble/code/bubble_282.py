import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

data="""Subject,Number of Students (Thousand),Funding (Million $),Publication (Number),Impact on Society (Score)
Sociology,150,500,4000,75
Psychology,200,450,4500,70
History,90,400,3000,80
Philosophy,50,380,2000,90
Literature,80,420,2500,85
Anthropology,60,400,2800,75
Archeology,30,380,1500,70"""

data = data.split('\n')
data_labels = data[0].split(',')[1:]

line_labels = []
category = [x.split(',')[0] for x in data[1:]]
data = [x.split(',')[1:] for x in data[1:]]
for i in range(len(data)):
    line_labels.append(category[i]+' '+data[i][2])
    data[i] = [float(x) for x in data[i]]

data = np.array(data)

fig, ax = plt.subplots(figsize=(12, 8))
color_map = mcolors.LinearSegmentedColormap.from_list("mycmap", ['blue', 'green', 'yellow', 'red'])
norm = mcolors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
sm = cm.ScalarMappable(norm=norm, cmap = color_map)

for i in range(len(data[:, 0])):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]-(np.min(data[:, 2])))/(np.max(data[:, 2])-np.min(data[:, 2]))*5000+600, 
               c=color_map(norm(data[i, 3])), alpha=0.5, label=None)
    ax.scatter([], [], label=line_labels[i], color=color_map(norm(data[i, 3])), s=20)
    
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2])
plt.grid(True)
cb = plt.colorbar(sm)
cb.set_label(data_labels[3])
plt.title('Impact and Popularity of Social Sciences and Humanities Subjects')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/68_202312301731.png')
plt.clf()
