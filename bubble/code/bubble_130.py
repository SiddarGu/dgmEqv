import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cmx

# Preprocessing the data
data_str = "Artist,Artworks Sold (Number),Total Revenue (Million $),International Recognition (Score),Influence (Score)\n Pablo Picasso,20000,900,10,9\n Leonardo da Vinci,15,860,10,10\n Vincent van Gogh,900,600,9,9\n Claude Monet,2500,500,9,7\n Andy Warhol,9000,600,8,10\n Salvador Dali,6500,400,8,9\n Frida Kahlo,150,300,7,8"
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
data_values = [line.split(',')[1:] for line in lines[1:]]
data_values = np.array(data_values, dtype=float)
line_labels = [line.split(',')[0] + ' ' + str(int(line.split(',')[2])) for line in lines[1:]]

# Creating a figure and plotting data
plt.figure(figsize=(12, 8))
ax=plt.subplot()
cm = plt.get_cmap('RdYlBu')
cNorm = mcolors.Normalize(vmin=data_values[:, 3].min(), vmax=data_values[:, 3].max())
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)

# Scatter plot
for i in range(len(line_labels)):
    color_val = scalarMap.to_rgba(data_values[i, 3])
    ax.scatter(data_values[i, 0], data_values[i, 1], alpha=0.5, s=np.interp(data_values[i, 2], [data_values[:, 2].min(), data_values[:, 2].max()], [600, 5000]), c=color_val, edgecolors='black', label=None)
    ax.scatter([], [], c=color_val, alpha=0.5, s=20, label=line_labels[i])

# Legend
ax.legend(title=data_labels[2], loc='upper left')

# Colorbar
cbar = plt.colorbar(scalarMap)
cbar.set_label(data_labels[3])

# Labels
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Title and other settings
plt.title('Influence and Commercial Success of Artists in the World of Arts and Culture')
plt.grid(True)


# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/121_202312301731.png')
plt.clf()
