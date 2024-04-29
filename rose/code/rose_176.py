

import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ["Wheat", "Rice", "Soybean", "Corn", "Potato", "Onion", 
               "Tomato", "Carrot", "Garlic", "Beetroot"]
data = [10500, 9000, 8500, 7500, 6000, 5000, 4000, 3000, 2000, 1000]
line_labels = ["Crop Type", "Volume of Production"]

# Create figure and modify axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Create rose chart with loop and legend
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.jet(1.*i/len(data_labels)), label=data_labels[i])
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, wrap=True)
ax.legend(bbox_to_anchor=(1, 0.5))

# Set parameters
ax.set_title('Volume of Agricultural Products Harvested in 2021', fontsize=20)
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_91.png')

# Clear the current image state
plt.clf()