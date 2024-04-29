
import matplotlib.pyplot as plt
import numpy as np
data_labels=['Quality Control', 'Efficiency', 'Safety', 'Production Speed', 'Delivery Time']
data=np.array([30,15,10,20,25])
line_labels=['Variable', 'Ratio']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%', pctdistance=0.8, textprops={'fontsize': 14})

cir=plt.Circle((0,0), 0.7, color='white')
ax.add_artist(cir)
ax.legend(data_labels, loc="center right", bbox_to_anchor=(1.3, 0.5),fontsize=14)
ax.set_title('Manufacturing and Production Performance - 2023', fontsize=16)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_149.png')

plt.cla()