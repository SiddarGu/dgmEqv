import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Correctly parsing the data
data_source = """
Product,Sales Volume (Million Units),Customer Ratings (Avg Score),Profit Margin (%),Return Rates (%)
Electronics,85,4.5,15,10
Fashion,95,4.6,25,8
Sports and Fitness,50,4.7,20,6
Beauty and Personal Care,70,4.8,30,4
Home and Kitchen,80,4.9,18,12
Toys and Games,60,4.5,22,9
Books,90,4.7,28,5
Automotive,40,4.6,20,7
"""
data = np.array([row.split(",")[1:] for row in data_source.strip().split("\n")[1:]], dtype=float)
labels = [row.split(",")[0] for row in data_source.strip().split("\n")[1:]]

# Normalize color based on Return Rates (%)
norm = Normalize(data[:, -1].min(), data[:, -1].max())
colors = [get_cmap("viridis")(norm(value)) for value in data[:, -1]]

# Normalize size based on Profit Margin (%)
sizes = Normalize(data[:, -2].min(), data[:, -2].max())

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot with customized sizes and colors
for i, (x, y, c, s) in enumerate(zip(data[:, 0], data[:, 1], colors, data[:, -2])):
    ax.scatter(x, y, label=None, c=[c], edgecolors='w', s=sizes(s) * 5000)
    scatter = ax.scatter([], [], color=get_cmap("viridis")(norm(data[i, 3])), label=labels[i] + f' {data[i, 2]}')

# Legend and color bar for Return Rates (%)
ax.legend(title="Product Category")
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])
fig.colorbar(sm, label="Return Rates (%)")

# Grid and labels
ax.grid(color='white', linestyle='-', linewidth=0.2)
ax.set_xlabel("Sales Volume (Million Units)")
ax.set_ylabel("Customer Ratings (Avg Score)")
plt.title('Sales and Profit Margins in Different E-commerce Categories')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/201_202312310045.png')
plt.clf()
