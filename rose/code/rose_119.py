
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Single Family Home", "Condominium", "Townhouse", "Multi-Family Home", "Apartment", "Vacant Land"]
data = [500000, 425000, 350000, 280000, 200000, 175000]
line_labels = ["Price"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

sector_angle = (2 * np.pi) / len(data_labels)

colors = ["darkblue", "dodgerblue", "mediumturquoise", "royalblue", "skyblue", "slategray"]

for i in range(len(data_labels)):
    ax.bar(x=i * sector_angle, height=data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=12)
ax.legend(bbox_to_anchor=(1.2, 1.0))
ax.set_title("Average Price of Different Types of Real Estate in 2023", fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_117.png')
plt.clf()