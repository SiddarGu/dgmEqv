import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cm

# Given data
data_string = '''Artist,Artwork Value (Million $),Public Viewings (Thousands),Cultural Impact (Score),Year of Creation
 Picasso,70,250,9,1937
 Van Gogh,55,200,7,1888
 Monet,50,180,8,1890
 Dali,45,150,8,1931
 Klimt,65,225,10,1907
 Matisse,60,140,7,1905
 Pollock,75,240,10,1948
 Warhol,80,300,9,1962'''

# Parsing data_string
data_rows = data_string.split("\n")
data_labels = data_rows[0].split(",")[1:]
data = np.array([row.split(",")[1:] for row in data_rows[1:]], dtype=float)
line_labels = [f'{row.split(",")[0]} {int(data[i, 3])}' for i, row in enumerate(data_rows[1:])]

# Normalizing, color mapping
norm = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
mapper = cm.ScalarMappable(norm=norm, cmap=cm.viridis)

# Creating figure, adjust figsize accordingly.
fig, ax = plt.subplots(figsize=(12, 8))
ax.grid(True)

for i in range(len(data)):
    ax.scatter(data[i,0], data[i,1], c=[mapper.to_rgba(data[i, 3])], s=600 + 4400*(data[i, 2]/data[:,2].max()), label=None, alpha=0.7)
    ax.scatter([], [], c=[mapper.to_rgba(data[i, 3])], s=20, label=line_labels[i], alpha=0.7)

# Add legend and labels
ax.legend(title=data_labels[2], borderaxespad=0.)
plt.colorbar(mapper, ax=ax)
ax.set_title('Impact and Value of Prominent Artists and Their Works - A Culture Perspective\n')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/254_202312310045.png')
plt.close(fig)
