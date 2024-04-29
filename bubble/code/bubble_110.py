import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm

# given data
data_in = ["Organization,Annual Revenue (Million $),Volunteer Workforce (Thousands),Beneficiaries Served (Millions),Impact (Score)",
           "Red Cross,680,40,10,90", "UNICEF,5200,300,90,80", 
           "Save the Children,760,60,15,85", "Oxfam,970,100,25,83", 
           "World Vision,2600,150,50,90","Habitat for Humanity,1600,90,30,88"]

# Prepare the data
data_labels = data_in[0].split(',')[1:]
line_labels = [i.split(',')[0] + ' ' + i.split(',')[2] for i in data_in[1:]]
data = np.array([i.split(',')[1:] for i in data_in[1:]], dtype=float)

# Initialize figure and add subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Normalize colors and sizes for scatter plot
norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
colors = cm.viridis(norm(data[:, 3]))
sizes = 600 + (data[:, 2] / data[:, 2].max()) * 4000

# Plot scatter plot with normalized colors and sizes
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], color=colors[i], s=sizes[i], alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], color=colors[i], s=20, label=line_labels[i])

# Plot legend and its title
ax.legend(title=data_labels[2], loc='upper left')

# Plot color bar
sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=norm)
plt.colorbar(sm, label=data_labels[3])

# Add labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Comparison of Impact and Revenue among Notable Charities and Nonprofit Organizations')

# Adjust the wrape of text label
plt.xticks(rotation=45, ha='right')

# Adjust the size of image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/89_202312301731.png')
plt.clf()
