
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Wheat", "Rice", "Maize", "Millet", "Barley", "Sorghum", "Soybean"]
data = [98, 100, 80, 50, 30, 20, 10]
line_labels = ["Category", "Number"]

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection="polar")

ax.set_title("Global Production of Grains in 2021")

colors = ["#FF0000", "#FFA500", "#FFFF00", "#7FFF00", "#00FF00", "#00FFFF", "#0000FF"]

sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(
        sector_angle * i,
        data[i],
        width=sector_angle,
        color=colors[i],
        label=data_labels[i],
    )
    
ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, rotation=40, ha="right")

ax.grid(linestyle="--", color="gray")

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_30.png")
plt.clf()