import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib import cm

# data preprocessing
raw_data = '''Sports,Revenue (Billion $),Popularity (Score),Global Audience (Billions),Cultural Impact (Score)
Soccer,48,90,4,85
Basketball,40,80,3,80
Tennis,25,70,2,75
Cricket,20,60,2.5,70
American Football,15,75,1,65
Baseball,10,65,1.5,60
Golf,7,50,1.25,55'''
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [x.split(',')[0] for x in lines[1:]]
data = np.array([x.split(',')[1:] for x in lines[1:]], dtype=float)

# normalization
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

fig, ax = plt.subplots(figsize=(10, 6))

# scatter plot
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], label=None,
               c=np.array([cmap(norm(data[i, 3]))]), 
	       s=bubble_sizes[i])
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_labels[i] + ' ' + str(data[i, 2]))
ax.legend(title=data_labels[2])
plt.grid(True)

# color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm.set_array([])

cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Evaluation of Various Sports - Factors of Revenues and Popularity in Entertainment Industry 2023')

fig.tight_layout()      
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/224_202312310045.png')
plt.clf()
