
import matplotlib.pyplot as plt 
import numpy as np
data_labels = ['Production', 'Supply Chain', 'Distribution', 'Marketing', 'Sales']
data = np.array([25, 17, 20, 15, 23])
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(111)
ring_color = ['#f9b8a0','#eeddcc','#d3b2a3','#b18975','#8e6048']
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=ring_color)
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)

ax.set_title('Food and Beverage Industry Outlook - 2023')
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.05))

plt.grid(linestyle='--')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_77.png')
plt.clf()