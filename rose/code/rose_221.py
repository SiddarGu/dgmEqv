
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Renewable","Fossil Fuels","Nuclear","Hydroelectric","Solar","Wind"]
data = [150, 250, 100, 50, 60, 70]
line_labels = ["Type of Energy","Amount of Energy"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
colors = ['b','r','g','m','y','c']
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True)
ax.legend(bbox_to_anchor=(1, 0.5), loc="center left")
plt.title("Global Energy Consumption by Source in 2021")
fig.set_size_inches(12, 12)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_36.png")
plt.clf()