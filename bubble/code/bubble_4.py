
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables
data_labels = ["Number of Users (Millions)", "Average Time Spent (Hours/Day)", "Engagement (Score)", "Ad Revenue (Billion $)"]
data = np.array([[2, 2, 90, 25], [1.5, 1.4, 80, 10], [0.5, 0.6, 70, 3], [0.4, 0.4, 60, 1], [0.3, 0.2, 50, 0.5], [0.2, 0.2, 40, 0.2]])
line_labels = ["YouTube", "Instagram", "Twitter", "Reddit", "LinkedIn", "WhatsApp"]

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()

# For the plotting using plt.scatter
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
cmap = cm.get_cmap("RdYlGn")

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2] * 50 + 600, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i,3])), label=line_labels[i]+" "+str(data[i,3]))

# Plot the legend with the title
leg = ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
sm = cm.ScalarMappable(norm, cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Adjust the figure view better
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set the title of the figure
plt.title("Social Media Usage and Engagement Statistics - 2021")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/25_2023122261326.png")

# Clear the current image state
plt.clf()