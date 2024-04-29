
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Case Volume (Thousand)", "Sentencing Rate (%)", "Jury Rate (%)", "Appeal Rate (%)"]
data = np.array([[80, 90, 10, 5],
                [200, 85, 12, 7],
                [300, 80, 15, 10],
                [400, 75, 20, 15],
                [500, 70, 25, 20]])
line_labels = ["Supreme Court_10", "District Court_12", "Magistrate Court_15", "County Court_20", "Municipal Court_25"]

# Create figure before plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)

# Plot the data with the type of bubble chart
sizes = (data[:, 2]/data[:, 2].max())*5000 + 600
colors = data[:, 3]

for i, line_label in enumerate(line_labels):
    cmap = ScalarMappable(Normalize(min(colors), max(colors)), plt.cm.plasma)
    ax.scatter(data[i, 0], data[i, 1], label=None,
               s=sizes[i], color=cmap.to_rgba(colors[i]))
    ax.scatter([], [], label=line_label,
               s=20, color=cmap.to_rgba(colors[i]))

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
cbar = fig.colorbar(cmap, ax=ax)
cbar.set_label(data_labels[3])

# Show the labels of two axes
ax.set_xlabel("Case Volume (Thousand)")
ax.set_ylabel("Sentencing Rate (%)")

# The title of the figure
ax.set_title("Legal Process Rates by Court Type in Law and Legal Affairs")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/12.png")

# Clear the current image state at the end of the code
plt.clf()