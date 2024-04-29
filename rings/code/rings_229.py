
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Labor Cost', 'Equipment Investment', 'Quality Control', 'Raw Materials', 'Production Efficiency']
line_labels = ['Category', 'ratio']
data = np.array([[19, 14, 12, 27, 28]])

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

ax.pie(data[0], startangle=90, counterclock=False, colors=plt.cm.Set2.colors)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc='center', bbox_to_anchor=(1, 0.5))
ax.set_title('Manufacturing and Production Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_91.png')
plt.clf()