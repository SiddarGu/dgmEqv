import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib import cm

# Preparing data
rows = ["Children's Aid Society,500,2.5,15,90", "American Red Cross,4000,50,20,80", 
        "Doctors Without Borders,1000,10,30,95", "Habitat for Humanity,1500,8,20,85", 
        "UNICEF,5000,80,15,90", "World Wildlife Fund,750,3,25,88", "Salvation Army,3000,25,20,82"]
data_labels = ["Annual Income (Million $)", "Beneficiaries (Millions)", 
               "Operations Cost (%)", "Donor Satisfaction (%)"]
data = []
line_labels = []
for row in rows:
    tokens = row.split(',')
    line_labels.append(tokens[0] + ' ' + tokens[2])
    data.append([float(v) for v in tokens[1:]])

# convert list into numpy array
data = np.array(data)

# Create a size and color data from the third and fourth column of data
size = (data[:,2]/np.max(data[:,2])) * 5000 + 600
color = data[:,3]

# Create a color map
cmp = plt.get_cmap("viridis")
data_labels_sizes = mcolors.Normalize(vmin=color.min(), vmax=color.max(),
                                  )
scalar_map = cm.ScalarMappable(norm=data_labels_sizes, cmap=cmp)

# Create a figure and add sub-plots
fig, ax = plt.subplots(figsize=(16,8))
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, 
               s=size[i], c=scalar_map.to_rgba(color[i]))
    ax.scatter([], [], c=scalar_map.to_rgba(color[i]), 
               label=line_label)
    
# Plot legend and color bar
ax.legend(title=data_labels[2])
plt.colorbar(scalar_map, label=data_labels[3], pad=0)

# Set plot and axis titles
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Performance and Impact of Notable Charity Organizations')
plt.grid(True)

# Save the plot to a file
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/223_202312310045.png')

# Clear the current axes
plt.clf()
