import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import io

# Transforming data
raw_data = """Crop,Water Usage (Million Cubic Meters),Carbon Footprint (Thousand Tonnes),Revenue (Billion $),Employment Rate (%)
Barley,800,200,15,6
Oats,600,190,12,6.5
Rye,570,185,10,7
Millet,530,180,8,8
Sorghum,500,170,7,9
Quinoa,400,160,6,10"""
data_df = pd.read_csv(io.StringIO(raw_data))
data_labels = data_df.columns[1:]
line_labels = data_df['Crop'] + ' ' + data_df[data_labels[2]].map(str)
data = data_df[data_labels].values

# Normalize color and size data to range 0-1
norm = Normalize(data[:, 3].min(), data[:, 3].max())
colors = get_cmap('viridis')(norm(data[:, 3]))
sizes = Normalize(data[:, 2].min(), data[:, 2].max())
sizes = sizes(data[:, 2]) * (5000 - 600) + 600

# Create figure and plot data
fig, ax = plt.subplots(figsize=(12, 8))
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=[colors[i]], label=None, alpha=0.6)
    ax.scatter([], [], c='k', alpha=0.6, s=20, label=line_labels[i])
ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='viridis'), ax=ax, label=data_labels[3])
ax.grid(True)

# Setting labels and title
ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1], wrap=True)
plt.title('Resource Consumption and Outcomes in Cereal Crop Production', wrap=True)

# Formatting and saving figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/196_202312310045.png')
plt.clf()
