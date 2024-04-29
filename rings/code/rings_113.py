
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Air', 'Rail', 'Road', 'Sea', 'Other']
data = [20, 15, 45, 20, 0]
line_labels = ['Mode', 'ratio']

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111)

explode = (0, 0, 0.1, 0, 0)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, explode=explode)
inner_circle = plt.Circle((0,0),0.70,fc='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, loc="lower right")
ax.axis('equal')
ax.grid(linestyle = '--')
plt.title('Transport and Logistics Network - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_64.png')
plt.close()