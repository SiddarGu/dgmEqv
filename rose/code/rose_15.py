
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Cereals', 'Fruits', 'Vegetables', 'Dairy', 'Livestock', 'Poultry', 'Fisheries', 'Forestry']
data = [98, 80, 95, 88, 60, 78, 50, 30]
line_labels = ['Production Rate']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection='polar')

sector_angle = (2 * np.pi) / len(data_labels)

for i, datum in enumerate(data):
    ax.bar(sector_angle * i, datum, width=sector_angle, alpha=0.6, label=data_labels[i], color=plt.cm.Set1(i))

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=90, wrap=True)
ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0.0)
ax.set_title("Global Production of Agricultural Products in 2021")

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_22.png')

plt.clf()