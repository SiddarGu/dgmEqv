
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Climate Change', 'Renewable Energy', 'Waste Management', 'Sustainable Agriculture',
               'Air Quality', 'Water Management', 'Conservation', 'Ecological Restoration']
data = [90, 70, 60, 50, 40, 30, 20, 10]
line_labels = ['Category', 'Number']

# Plot data
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=f'C{i}')

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=45, ha='right', wrap=True)
ax.set_title('Number of Environmental and Sustainability Projects in 2021')
ax.legend(bbox_to_anchor=(1.1, 1.05))

fig.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_37.png')
plt.clf()