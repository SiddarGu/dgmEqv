
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Oil', 'Coal', 'Natural Gas', 'Solar', 'Wind', 'Hydroelectricity', 'Nuclear', 'Biomass']
data = [130, 90, 200, 170, 120, 80, 50, 30]
line_labels = ['Energy Source', 'Number of Users']

fig = plt.figure()
ax = fig.add_subplot(polar=True)

sector_angle = (2 * np.pi) / len(data)

colors = ['#ff0000', '#006600', '#0000cc', '#660099', '#cc3399', '#33cc33', '#cccc00', '#cc00cc']

for i, angle in enumerate(np.arange(0, 2 * np.pi, sector_angle)):
    ax.bar(angle, data[i], width=sector_angle, color=colors[i])
    ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
    ax.set_xticklabels(data_labels, rotation=90, wrap=True)

ax.legend(data_labels, bbox_to_anchor=(1.2, 1.05))
ax.set_title('Number of Consumers Using Different Energy Sources in 2021')
fig.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_12.png')
plt.clf()