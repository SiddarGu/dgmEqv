import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# data
data_str = "Pablo Picasso,900,200,90,95/Vincent Van Gogh,700,180,85,90/Banksy,600,160,80,85/Yayoi Kusama,500,140,75,80/Damien Hirst,400,120,70,75/Ai Weiwei,300,100,65,70"
data_labels = ['Artist', 'Artwork Sales (Million $)', 'Museum Exhibitions', 'International Recognition (Score)', 'Cultural Impact (Score)']
data_rows = [row.split(',') for row in data_str.split('/')] # Splitting data lines
data = np.array([[float(x) for x in row[1:]] for row in data_rows]) # Converting to a NumPy array
line_labels = [f"{row[0]} {data[i, 2]}" for i, row in enumerate(data_rows)]

fig, ax = plt.subplots(figsize=(10, 8)) # Figure Creation
# Normalizing color and size data ranges
sizes = 600 + 4400 * (data[:, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")

for i in range(data.shape[0]): # Iterative plotting
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], color=color, s=sizes[i], label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], color=color, s=20, label=line_labels[i])

ax.legend(title=data_labels[2]) # Legend plotting
ax.grid(True)

plt.xlabel(data_labels[1]) # Axis labels
plt.ylabel(data_labels[2])

sm = cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())) # Color bar
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])

plt.title('Influence of Artists in Arts and Culture') # Title
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/98_202312301731.png') # Savefig
plt.clf() # Clear the current figure
