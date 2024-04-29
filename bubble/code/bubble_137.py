import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data_string = """
Destination,Number of Tourists (Millions),Tourism Revenue (Billion $),Hotel Occupancy Rate (%),Sustainability (Score)
Paris,19,68,75,7
Tokyo,16,61,70,8
New York,13,59,78,6
London,21,70,68,7
Dubai,12,44,82,5
Singapore,15,45,72,7
Sydney,11,39,70,9
"""

# Parse the string to usable data and labels
data_string = data_string.strip().split("\n")
data_labels = data_string[0].split(",")[1:]
data = np.array([row.split(",")[1:] for row in data_string[1:]], dtype=float)
line_labels = [f"{row.split(',')[0]} {data[i, 2]}" for i, row in enumerate(data_string[1:])]

fig, ax = plt.subplots(figsize=(10,10))

# Create color map
cmap = plt.get_cmap('viridis')
c_norm = Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3]))

for i in range(len(data)):
    # Scatter the bubbles
    scatter = ax.scatter(data[i, 0], data[i, 1], alpha=0.6, 
                         s=600 + (data[i, 2] - np.min(data[:,2]))/(np.max(data[:,2]) - np.min(data[:,2])) * (5000 - 600), 
                         c=[data[i, 3]], cmap=cmap, norm=c_norm, edgecolors='w', label=None)
    # Add an empty point for legend
    ax.scatter([], [], alpha=0.6, s=20, color=cmap(c_norm(data[i, 3])), edgecolors='w', label=line_labels[i])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Create legend & title
legend_title = data_labels[2]
plt.title('Analysis of Tourist Numbers, Revenue, and Sustainability in Popular Destinations')
ax.legend(title=legend_title, loc='upper left')

# Add a colorbar
sm = ScalarMappable(cmap=cmap, norm=Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3])))
fig.colorbar(sm, ax=ax, orientation='vertical', label=data_labels[3])

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/129_202312301731.png')
plt.clf()
