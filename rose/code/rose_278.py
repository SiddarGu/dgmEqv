
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Residential Usage', 'Commercial Usage', 'Industrial Usage', 'Utility Usage']
data = [4200, 3200, 1200, 800]
line_labels = ['Usage', 'Number']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

sector_angle = (2 * np.pi) / len(data_labels)
colors = ['darkred', 'darkgreen', 'darkblue', 'yellow']

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=16, rotation=45, ha='right')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=16)
ax.set_title('Energy and Utilities Consumption in 2021', fontsize=20)

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_74.png")

plt.clf()