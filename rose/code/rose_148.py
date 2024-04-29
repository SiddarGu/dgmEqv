

import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Coal", "Natural Gas", "Nuclear", "Hydroelectric", "Solar", "Wind", "Biomass"]
data = [200, 150, 100, 50, 30, 20, 10]
line_labels = ["Energy Source", "Amount of Usage"]

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, projection='polar')

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.jet(i/num_categories))

ax.set_theta_zero_location("N")
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)
ax.set_title("Usage of Different Energy Sources in 2021", fontsize=20)
ax.legend(bbox_to_anchor=(1.1, 1.05), fontsize=15)

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_29.png")
plt.clf()