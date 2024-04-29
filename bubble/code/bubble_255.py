import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Transform original data
raw_data = """Product,Production Quantity (Million Units),Cost per Unit ($),Revenue (Billion $),Quality Index (Out of 5)
Cars,65,20000,1300,4.5
Smartphones,500,800,400,4
Laptops,200,1000,200,4.3
TV sets,150,500,75,4.2
Watches,300,300,90,4.7
Bicycles,250,100,25,4.6"""

# Splitting data
rows = raw_data.split("\n")
data_labels = rows[0].split(",")
line_labels = [row.split(",")[0] + " " + row.split(",")[2] for row in rows[1:]]
data = np.array([row.split(",")[1:] for row in rows[1:]], dtype=float)

colors = plt.cm.viridis(np.linspace(0,1,len(data)))

# Create a new figure
fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)

# Normalizing
bubble_sizes = 600 + 4400 * (data[:, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2]))
colors = (data[:, 3] - np.min(data[:, 3])) / (np.max(data[:, 3]) - np.min(data[:, 3]))

# Draw data
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=matplotlib.cm.viridis(colors[i]), label=None)
    ax.scatter([], [], c=matplotlib.cm.viridis(colors[i]), label=line_labels[i], s=20)

# Set labels
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# Draw legend
lgd = ax.legend(title=data_labels[2], loc='upper left')

# Draw colorbar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(min(data[:, 3]), max(data[:, 3])))
plt.colorbar(sm, label=data_labels[3])
ax.grid(True)

# Set title and save figure
plt.title('Revenue, Cost and Quality Index for Different Manufactured Products')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/273_202312310045.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.cla()
