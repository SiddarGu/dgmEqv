import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib import colors

# Given data
data_str = ["Coca-Cola,37,16,85,400","PepsiCo,65,30,80,500","Nestle,92,42,90,600",
            "Starbucks,26,12,88,250","McDonald's,21,10,75,100","KFC,15,8,70,80",
            "Pizza Hut,12,7,69,60","Burger King,10,5,75,50","Subway,11,5,72,45",
            "Dairy Queen,8,4,70,40"]

data_labels=['Company','Revenue (Billion $)','Market Share (%)','Customer Satisfaction (Score)','Products Offered (Count)']

data = []
line_labels = []
for var in data_str:
    values = var.split(',')
    line_labels.append(values[0] + " (" + str(values[2]) +"%)")
    data.append([float(values[1]), float(values[2]), float(values[3]), float(values[4])])

# Convert to numpy for easier handling
data = np.array(data)

# Create the chart
norm = plt.Normalize(data[:,3].min(), data[:,3].max())
cmap = cm.ScalarMappable(norm=norm, cmap='viridis')
cmap.set_array([])

fig, ax = plt.subplots(figsize=(10,6))
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], color=cmap.to_rgba(data[i, 3]), 
               s=(data[i, 2] - np.min(data[:, 2]))/(np.max(data[:,2])-np.min(data[:,2]))*4000 + 600, label=None)
    ax.scatter([], [], color=cmap.to_rgba(data[i, 3]), label=line_labels[i])
ax.legend(title="Company (Market Share%)")
ax.set_xlabel("Revenue (Billion $)")
ax.set_ylabel("Market Share (%)")
ax.grid(True)

cb = fig.colorbar(cmap)
cb.set_label(label=data_labels[3], size='large', weight='bold')
plt.title("Performance of Leading Companies in the Food and Beverage Industry 2023", fontsize=15)

fig.tight_layout()

# Save the plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/267_202312310045.png')

# Clear the current image state
plt.clf()
