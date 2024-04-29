import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# the given data
data = [
    ['Smartphones', 3000, 480, 5000, 200],
    ['Personal Computers', 1500, 300, 4000, 150],
    ['Smart Home Devices', 700, 150, 1000, 120],
    ['Cloud Services', 2000, 260, 3000, 180],
    ['eCommerce Platforms', 2500, 350, 2000, 200],
    ['Social Networks', 3200, 400, 5000, 250],
    ['Video Streaming Services', 2300, 220, 1500, 170],
    ['Online Education Platforms', 800, 100, 500, 150]
]

# Convert the data into DataFrame for easier manipulation
df = pd.DataFrame(data, columns=["Product", "Users (Millions)", "Revenue (Billion $)", "Security Threats (Thousand)", "Development Costs (Million $)"])

data_labels = list(df.columns[1:])
data = df[df.columns[1:]].values
line_labels = df["Product"].values + [" "] + data[:, 2].astype(str)

# Create figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot()

# Bubble size normalization
norm = Normalize(data[:, 2].min(), data[:, 2].max())
s = norm(data[:, 2]) * 4400 + 600

# Color normalization
norm = Normalize(data[:, 3].min(), data[:, 3].max())
cmap = get_cmap("viridis")
c = cmap(norm(data[:, 3]))

# Scatter the data
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], label=None, s=s[i], c=np.array([c[i]]), alpha=0.6)
    ax.scatter([], [], label=line_labels[i], s=20, c=np.array([c[i]]))

# Legend
ax.legend(title=data_labels[2], loc='upper left')

# Color bar
sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation="vertical", label=data_labels[3])

# Set the xlabel/ylabel
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

# Set the title
plt.title("Comparing Revenue, Users, and Costs Across Technology Products in 2023")

# Auto size
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/245_202312310045.png")

# Clear figure
plt.clf()
