import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import pandas as pd

# Prepare data
data_str = 'Category,Train,Truck,Ship,Airplane\n Delivery Speed,75,70,65,95\n Fuel Efficiency,65,60,55,80\n Carrying Capacity,80,90,100,70\n Maintenance Cost,50,60,45,80\n Safety Rating,85,80,90,90'
data_file = StringIO(data_str)
data_df = pd.read_csv(data_file, sep =",")
data_labels = data_df.columns[1:]
line_labels = data_df['Category']
data = data_df[data_labels].values

# Create figure, set polar axis and size
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)

# Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i, row in enumerate(data):
    # Append the first item to the end for loop closure
    data_row = np.append(row, row[0])
    ax.plot(angles, data_row, colors[i % len(colors)], label=line_labels[i])
    ax.fill(angles, data_row, colors[i % len(colors)], alpha=0.25)
    radius = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, radius, color='gray', linestyle='dashed')

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)

# Adjust the radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set figure title
plt.title('Transportation and Logistics Performance Comparison', size=20, color='blue', y=1.1)

# Tighten layout and save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/73_2023122292141.png')

# Clear figure
plt.clf()
