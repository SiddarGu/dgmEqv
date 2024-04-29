

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Transform data into three variables: data_labels, data, line_labels.
data_labels = ["Attendance (Millions)", "Revenue (Billion $)", 
               "Sponsorship (Million $)", "Broadcast Audience (Millions)"]
data = np.array([[100, 7.5, 750, 150], [75, 5, 500, 120], 
                 [500, 10, 1000, 300], [400, 8, 750, 250], 
                 [50, 3, 400, 90]])
line_labels = ["Super Bowl", "NBA Finals", "World Cup", 
               "Summer Olympics", "March Madness"]

# Create figure before plotting
plt.figure(figsize=(12, 10))
ax = plt.subplot()

# Plot the data with the type of bubble chart
for i in range(len(data)):
    # Normalize color
    color = cm.get_cmap("RdBu")(data[i, 3] / data[:, 3].max())
    # Normalize bubble size
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * (5000 - 600) + 600

    # Plot each line
    ax.scatter(data[i, 0], data[i, 1], c=color, s=size, label=None)
    # Scatter an empty point
    ax.scatter([], [], c=color, s=20, label=line_labels[i] + f' {data[i, 2]}')

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar
sm = plt.cm.ScalarMappable(cmap="RdBu", norm=plt.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm._A = []
plt.colorbar(sm, ax=ax, fraction=0.02, label=data_labels[3])

# Adjusting techniques
ax.grid(True)
ax.set_title("Sports and Entertainment Events by Audience and Revenue")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/34_2023122261326.png")

# Clear the current image state
plt.clf()