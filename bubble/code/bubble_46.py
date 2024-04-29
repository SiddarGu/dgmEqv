
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Transform the data into three variables
data=np.array([[300,90,20,200],[400,80,30,400],[350,85,25,350],[250,70,35,400],[200,75,15,250],[150,65,10,150]])
data_labels=['Productivity (Units/Hour)','Quality (Score)','Employee Numbers (Thousands)','Cost of Production (Million $)']
line_labels=['ABC Inc.','XYZ Corp.','UVW Ltd.','RST Co.','DEF Group','GHI Pty.']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max()) # Normalize color
sm = ScalarMappable(cmap="Reds", norm=norm) # Set cmap
sm.set_array([])

# Scatter the data
for i in range(data.shape[0]):
    ax.scatter(data[i,0], data[i,1], s=600 + 5000*((data[i,3]-data[:,3].min())/(data[:,3].max()-data[:,3].min())), c=sm.to_rgba(data[i,3]), label=None) # Bubble size and color
    ax.scatter([], [], s=20, c=sm.to_rgba(data[i,3]), label=line_labels[i] + f' {data[i, 2]}') # Add empty points

# Plot the legend
ax.legend(title=data_labels[2])

# Add color bar
cbar=fig.colorbar(sm, orientation='vertical') # Add color bar
cbar.set_label(data_labels[3]) # Set color bar title

# Adjust the figure
plt.title('Manufacturing and Production - Performance and Cost Compariso') # Set title
ax.set_xlabel(data_labels[0]) # Set x-axis label
ax.set_ylabel(data_labels[1]) # Set y-axis label
plt.tight_layout() # Automatically resize the image

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/47_2023122261326.png')

# Clear the current image state
plt.clf()