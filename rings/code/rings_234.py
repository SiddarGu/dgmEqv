
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Road', 'Rail', 'Air', 'Sea', 'Intermodal']
line_labels = ['Mode']
data = np.array([[36, 15, 19, 13, 17]])

fig, ax = plt.subplots(figsize=(9, 9))

ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False)
c = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(c)
ax.legend(data_labels,loc='lower right')
ax.set_title('Transportation and Logistics Overview - 2023', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_1.png', dpi=200)
plt.clf()