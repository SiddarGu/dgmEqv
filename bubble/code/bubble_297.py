import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Data parsing
data_string = "Facebook,2690,4.5,86,6/YouTube,2000,3.8,20,7/WhatsApp,2000,3.5,5,8/Twitter,330,2,3.5,7/Instagram,1200,3.2,20,7/Linkedin,310,1.5,2,9"
data_rows = data_string.split("/")
data = np.array([row.split(",")[1:] for row in data_rows], dtype=float)
line_labels = [row.split(",")[0] for row in data_rows]

# Plot configuration
fig, ax = plt.subplots(figsize=(10, 8))
colors = Normalize(min(data[:, 3]), max(data[:, 3]))(data[:, 3])
sizes = (data[:, 2] / max(data[:, 2])) * 5000 + 600 # Normalize sizes
scatter = ax.scatter(data[:, 0], data[:, 1], c=colors, cmap='viridis', s=sizes, edgecolors='w')

# Legend and labels
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], color=get_cmap("viridis")(colors[i]), alpha=0.3, s=100, label=line_label + f' {data[i, 2]}')
ax.legend(loc='upper left', title="Platforms")
plt.xlabel('Monthly Active Users (Millions)')
plt.ylabel('Ad Revenue (Billion $)')
plt.title('Comparison of Popular Social Media Platforms by User Engagement and Revenue 2023')

# Colorbar for Data Privacy Score
sm = ScalarMappable(cmap='viridis', norm=Normalize(min(data[:, 3]), max(data[:, 3])))
plt.colorbar(sm, label='Data Privacy Score (out of 10)')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/215_202312310045.png')
plt.clf()
