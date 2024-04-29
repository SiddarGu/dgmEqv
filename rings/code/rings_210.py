
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy', 'Fossil Fuel', 'Nuclear Energy', 'Energy Efficiency', 'Grid Reliability']
data = np.array([30, 20, 10, 35, 5])
line_labels = ['Category', 'ratio']

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(data, startangle=90, counterclock=False, labels=data_labels, wedgeprops={'linewidth': 2, 'edgecolor': 'black'})
center_circle = plt.Circle((0,0), 0.6, color='white')
ax.add_artist(center_circle)

ax.legend(data_labels, loc='best', fontsize='large')
ax.set_title('Global Energy Trends - 2023')
ax.axis('equal')
fig.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_63.png')
plt.clf()