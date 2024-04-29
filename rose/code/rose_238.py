
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Education", "Immigration", "Foreign Affairs", "Infrastructure", "Social Welfare", "National Security", "Economic Development", "Environment", "Health", "Technology"]
data = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
line_labels = ["Policy Area", "Number of Policy Initiatives"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

sector_angle = (2 * np.pi) / len(data_labels)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '#FFFF00', '#FF00FF']

for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, rotation=45, wrap=True)

ax.legend(bbox_to_anchor=(1.25,0.5))

ax.set_title('Government Policy Initiatives in 2021')

fig.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_78.png')
plt.close(fig)