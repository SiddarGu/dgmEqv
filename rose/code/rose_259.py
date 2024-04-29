
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Fossil Fuels', 'Nuclear Power', 'Renewable Energy', 'Hydroelectric Power', 'Solar Power', 'Wind Power', 'Biomass']
line_labels = ['Energy Source', 'Number of Plants']
data = [[90,30,100,50,70,60,40]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('Number of Energy Plants in 2021 by Source')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i], color=f'C{i}')
ax.legend(data_labels, bbox_to_anchor=(1.3,0.5), loc="center right")
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_34.png')
plt.clf()