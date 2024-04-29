
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Fossil Fuel","Renewable Energy","Nuclear Energy","Natural Gas","Electricity","Water"]
data = [500, 350, 200, 150, 100, 50]
line_labels = ["Component", "Amount"]

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
ax.set_title("Energy and Utilities Resources in 2021")

colors = ['b', 'g', 'r', 'c', 'm', 'y']

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])
ax.legend(bbox_to_anchor=(1.2, 1.0))

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=45, wrap=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_94.png')
plt.clf()