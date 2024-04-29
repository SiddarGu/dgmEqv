import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Prepare data
data_raw = '''Product,Annual Sales (Million $),Customer Ratings,Stock (Millions),Discount Rate (%)
Electronics,1500,4.5,50,10
Apparel,1200,4.2,80,15
Home Decor,900,4.3,60,20
Books,800,4.4,70,5
Sports Equipment,700,4.0,75,12
Cosmetics,600,4.4,65,20
Furniture,500,3.8,85,30'''

lines = data_raw.split('\n')
data_labels = lines[0].split(',')[1:]
data_values = [line.split(',')[1:] for line in lines[1:]]
data = np.array(data_values, dtype=float)
line_labels = [f'{line.split(",")[0]} {data[i, 2]}' for i, line in enumerate(lines[1:])]

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")

figure = plt.figure(figsize=(12, 8))
ax = figure.add_subplot()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

plt.colorbar(plt.cm.ScalarMappable(norm=plt.Normalize(np.min(data[:, 3]), np.max(data[:, 3])), cmap='viridis'), ax=ax).set_label(data_labels[3])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2], loc='lower right')
plt.grid(True)
plt.title('Annual Sales and Customer Satisfaction in Retail and E-commerce sector')
plt.tight_layout()

# Save plot to file
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/240_202312310045.png')
plt.close()
