import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from pandas import DataFrame

data = DataFrame({
    'Product': ['Bread', 'Milk', 'Soda', 'Snacks', 'Water', 'Juice'],
    'Revenue (Million $)': [500, 700, 400, 300, 600, 450],
    'Market Share (%)': [15, 20, 12, 8, 18, 10],
    'Profit Margin (%)': [10, 15, 20, 18, 12, 17],
    'Customer Satisfaction (/100)': [85, 90, 80, 85, 95, 88]
})

data_labels = list(data.columns[1:])
line_labels = list(data['Product'])
data_values = data.values[:,1:].astype(float)

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

colors = list(mcolors.TABLEAU_COLORS.keys())
bubble_sizes = np.interp(data_values[:,2], (data_values[:,2].min(), data_values[:,2].max()), (600, 5000))

# Normalize color value to range of cmap values
norm = plt.Normalize(data_values[:,3].min(), data_values[:,3].max())
cmap = plt.get_cmap("YlOrRd")

for i in range(len(data_values)):
    ax.scatter(data_values[i, 0], data_values[i, 1],
                 s=bubble_sizes[i], color=cmap(norm(data_values[i, 3])),
                 label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], label=f"{line_labels[i]} ({data_values[i, 2]:.0f}%)", color=cmap(norm(data_values[i, 3])))

ax.legend(title=data_labels[2], title_fontsize=12, borderpad=1, frameon=True, framealpha=0.9, facecolor='white')

sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

cbar = plt.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3], fontsize=12)

ax.set_xlabel(data_labels[0], fontsize=14)
ax.set_ylabel(data_labels[1], fontsize=14)
ax.set_title("Performance of Food and Beverage Products", fontsize=16)

ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
ax.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/381_202312311429.png")
plt.clf()
