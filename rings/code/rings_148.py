
import matplotlib.pyplot as plt 
import numpy as np
data_labels = ['Road Safety','Delivery Times','Fuel Efficiency','Customer Service','Vehicle Maintenance']
data = np.array([30,20,25,15,10])
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(15,8))

ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False)

centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.legend(data_labels, fontsize=12, loc="best")
ax.set_title('Transportation and Logistics Performance - 2023', fontsize=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_11.png')
plt.show()
plt.clf()