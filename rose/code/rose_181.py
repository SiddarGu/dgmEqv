
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Recycling", "Reforestation", "Reduction of Waste", "Energy Efficiency", "Renewable Energy", "Carbon Capture", "Water Conservation", "Air Pollution Control"]
data = [70, 25, 65, 45, 38, 20, 50, 30]
line_labels = ["Activity", "Number"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i/num_categories))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90)
ax.legend(bbox_to_anchor=(1.1, 0.9))

plt.title("Number of Environmental and Sustainability Activities in 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_15.png")
plt.clf()