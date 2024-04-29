import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Given data
data_info = ['Company,Revenue (Billion $),No. of Employed (Millions),Fleet Size (Unit),Green Commitment (Score)',
' DHL,62.3,0.55,84000,8', ' FedEx,83.1,0.4,70000,7', ' UPS,104.2,0.4,119000,6', ' Maersk,59.2,0.08,342,9', ' MSC,28.2,0.02,560,7', ' COSCO,14.5,0.13,478,6', 'CMA CGM,30.8,0.11,494,8' ]

data_labels = data_info[0].split(',')
data_labels = [item.strip() for item in data_labels]

data = []
line_labels = []
for line in data_info[1:]:
    items = line.split(',')
    items = [item.strip() for item in items]
    line_labels.append(items[0] + ' ' + str(items[2]))
    data.append([float(item) for item in items[1:]])

data = np.array(data)

# Bubble chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

for i in range(len(data)):
    # Normalizing color
    color = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())(data[i, 3])
    # Normalizing size
    size = np.interp(data[i, 2], (data.min(), data.max()), (600, 5000))
    ax.scatter(data[i, 0], data[i, 1], c=plt.cm.viridis(color), s=size, alpha=0.6, edgecolors="w", linewidth=2, label=None)
    ax.scatter([], [], c=plt.cm.viridis(color), label=line_labels[i])
    
# Legend
ax.legend(title=data_labels[2], loc='upper left')

# More settings
plt.grid(True)
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[2])
plt.title('Revenue vs Environmental Commitment in Top Transportation and Logistics companies', fontsize=14, fontweight='bold')

# Color bar
cax = fig.add_axes([0.92, 0.1, 0.03, 0.8])
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
fig.colorbar(sm, cax=cax)
cax.set_title(data_labels[3])

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/258_202312310045.png')
plt.clf()
