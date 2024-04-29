

import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Renewable", "Fossil Fuel", "Natural Gas", "Nuclear", "Hydroelectric", "Solar", "Wind", "Biomass"]
data = [90, 70, 60, 50, 40, 30, 20, 10]
line_labels = ["Electric Supply"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

ax.legend(data_labels, bbox_to_anchor=(1.2, 0.5))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90, wrap=True)

ax.set_title("2020 Energy Supply by Source")

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_30.png")
plt.clf()