
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables
data_labels = ["Engagement (Score)", "Popularity (Score)", "Reach (Score)", "Longevity (Score)"]
data = np.array([[800,900,1000,750],[650,700,950,900],[900,800,850,950],[750,700,950,800],[800,600,750,900],[850,700,950,800]])
line_labels = ["Psychology", "Philosophy", "Literature", "History", "Sociology", "Political Science"]

# Create figure
fig, ax = plt.subplots(figsize=(15,10))
cmap = plt.cm.hot
norm = Normalize(vmin=700, vmax=1000)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
# Plot the data with the type of bubble chart
for i in range(data.shape[0]):
    # Normalize color to the range of cmap values
    c = cmap(norm(data[i, 3]))
    # Normalize bubble size from 60 to 500
    s = 600 + (data[i, 2]-750)/(1000-750)*(5000-600)
    ax.scatter(data[i, 0], data[i, 1], c=c, s=s, label=None)
    # During each iteration of plotting, you must also scatter an empty point
    ax.scatter([], [], c=c, s=20, label=line_labels[i] + f' {data[i, 2]}')

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
cbar = fig.colorbar(sm, ax=ax, fraction=0.0363, pad=0.03)
cbar.set_label(data_labels[3], fontsize=18)

# Show the labels of two axes
ax.set_xlabel(data_labels[0], fontsize=18)
ax.set_ylabel(data_labels[1], fontsize=18)

# The title of the figure
plt.title('Perception of Different Social Sciences and Humanities over Time', fontsize=30)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/10_2023122261326.png')

# Clear the current image state
plt.clf()