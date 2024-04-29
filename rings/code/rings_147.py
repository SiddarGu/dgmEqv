
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Quality Control', 'Cost Control', 'Supply Chain', 'Production Efficiency']
data = [0.32, 0.18, 0.2, 0.3]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Manufacturing and Production - 2023')
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, wedgeprops=dict(width=0.3, edgecolor='w'))
c = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(c)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1.0))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_109.png', bbox_inches='tight')
plt.cla()